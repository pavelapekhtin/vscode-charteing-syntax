import json
from typing import Any, Dict, List

import toml
from pydantic import BaseModel


class MatchCasesFile(BaseModel):
    cases: List[str]


class TomlKeywords(BaseModel):
    numeric: MatchCasesFile
    legal: MatchCasesFile
    important: MatchCasesFile
    voyage_related: MatchCasesFile
    counterparts: MatchCasesFile
    other: MatchCasesFile


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


TomlDict = Dict[str, Dict[str, List[str]]]


def load_match_cases(path: str) -> TomlDict:
    try:
        with open(path, "r") as f:
            toml_file = toml.load(f)
        TomlKeywords.model_validate(toml_file)
        return toml_file
    except Exception as e:
        raise ValueError(f"Invalid structure of {path} file: {e}")


def load_lang_json(path: str) -> dict[str, Any]:
    try:
        with open(path, "r") as f:
            lang_json = json.load(f)
        LangJsonSchema.model_validate(lang_json)
        return lang_json
    except Exception as e:
        raise ValueError(f"Invalid structure of {path} file: {e}")
