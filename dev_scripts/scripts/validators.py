import json
from typing import Dict, List

import toml
from pydantic import BaseModel

from scripts.cli.cli_functions import console


class MatchCasesModel(BaseModel):
    cases: List[str]


class TomlSchema(BaseModel):
    numeric: MatchCasesModel
    legal: MatchCasesModel
    important: MatchCasesModel
    voyage_related: MatchCasesModel
    counterparts: MatchCasesModel
    other: MatchCasesModel


# Lang json schema


class Capture(BaseModel):
    name: str


class Pattern(BaseModel):
    name: str
    match: str
    captures: Dict[str, Capture]


class LangJsonSchema(BaseModel):
    name: str
    scopeName: str
    patterns: List[Pattern]


def validate_match_cases_toml(path: str) -> None:
    try:
        toml_file = toml.load(path)
        TomlSchema.model_validate(toml_file)
        console.print(
            f"[green]✔ [/green][yellow]'{path}'[/yellow][green] toml stucture ok."
        )
    except Exception as e:
        raise ValueError(f"Invalid structure of {path} file: {e}")


def validate_lang_json(path: str) -> None:
    try:
        with open(path, "r") as f:
            lang_json = json.load(f)
        LangJsonSchema.model_validate(lang_json)
        console.print(
            f"[green]✔ [/green][yellow]'{path}'[/yellow][green] json stucture ok."
        )
    except Exception as e:
        raise ValueError(f"Invalid structure of {path} file: {e}")
