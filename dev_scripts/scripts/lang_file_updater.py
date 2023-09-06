import json
from dataclasses import dataclass, field
from typing import Any

from filepaths import PATH_LANG_FILE, PATH_LANG_FILE_TEMPLATE, PATH_TOML_FILE
from scripts.cli.cli_functions import console
from scripts.file_loaders import load_lang_json, load_match_cases

TOML_JSON_MAPPING = {
    "numeric": "constant.numeric",
    "legal": "string.quoted",
    "important": "variable.parameter",
    "voyage_related": "variable.other.readwrite",
    "counterparts": "storage",
    "other": "entity.name.type.class",
}


@dataclass
class LangFileUpdater:
    path_kwd_toml: str = PATH_TOML_FILE
    path_lang_json_template: str = PATH_LANG_FILE_TEMPLATE
    path_lang_json: str = PATH_LANG_FILE
    toml_json_mapping: dict[str, str] = field(default_factory=lambda: TOML_JSON_MAPPING)

    def __post_init__(self):
        self.kwd_toml: dict[str, Any] = load_match_cases(self.path_kwd_toml)
        self.lang_json_template: dict[str, Any] = load_lang_json(
            self.path_lang_json_template
        )
        console.print(
            f"[green]✔ [/green][yellow]'{self.path_kwd_toml}'[/yellow][green] toml stucture ok."
        )
        console.print(
            f"[green]✔ [/green][yellow]'{self.path_lang_json_template}'[/yellow][green] json stucture ok."
        )
        console.print(
            f"[green]✔ [/green][yellow]'{self.path_lang_json}'[/yellow][green] json stucture ok."
        )

    def update_language_file(self) -> None:
        with open(self.path_lang_json, "w") as f:
            json.dump(self._combine_match_cases(), f, indent=2)
            console.print("[green]Language file updated.")

    def _combine_match_cases(self) -> dict[str, Any]:
        return self._pattern_matcher(
            self.kwd_toml, self.lang_json_template, self.toml_json_mapping
        )

    def _pattern_matcher(
        self,
        match_cases: dict[str, Any],
        language_data: dict[str, Any],
        mapping: dict[str, str],
    ):
        lang_json = language_data.copy()
        for pattern in lang_json["patterns"]:
            name = pattern.get("name")
            toml_key = [key for key, value in mapping.items() if value == name][0]
            if toml_key in match_cases:
                joined_match = "|".join(match_cases[toml_key]["cases"])
                pattern["match"] = f"(?i)\\b({joined_match})\\b"
        return lang_json


if __name__ == "__main__":
    LangFileUpdater().update_language_file()
