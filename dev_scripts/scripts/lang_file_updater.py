import json
from dataclasses import dataclass, field
from typing import Any

import toml

from scripts.cli.cli_functions import console

PATH_LANG_FILE_TEMPLATE = "./data/language_file_template.json"
PATH_TOML_FILE = "../matchCases.toml"
PATH_LANG_FILE = "../syntaxes/recap.tmLanguage.json"
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
    path_lang_json: str = PATH_LANG_FILE
    path_json_template: str = PATH_LANG_FILE_TEMPLATE
    toml_json_mapping: dict[str, str] = field(default_factory=lambda: TOML_JSON_MAPPING)

    def update_language_file(self) -> None:
        with open(self.path_lang_json, "w") as f:
            json.dump(self._combine_match_cases(), f, indent=2)
            console.print("[green]Language file updated.")

    def _combine_match_cases(self) -> dict[str, Any]:
        return self._pattern_matcher(
            self.kwd_toml, self.json_template, self.toml_json_mapping
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

    @property
    def kwd_toml(self) -> dict[str, Any]:
        with open(self.path_kwd_toml, "r") as f:
            return toml.load(f)

    @property
    def lang_json(self) -> dict[str, Any]:
        with open(self.path_lang_json, "r") as f:
            return json.load(f)

    @property
    def json_template(self) -> dict[str, Any]:
        with open(self.path_json_template, "r") as f:
            return json.load(f)


if __name__ == "__main__":
    LangFileUpdater().update_language_file()
