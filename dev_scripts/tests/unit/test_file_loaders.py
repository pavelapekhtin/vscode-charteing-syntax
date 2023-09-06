import json
from unittest.mock import mock_open, patch

import pytest
import toml

from filepaths import PATH_LANG_FILE, PATH_TOML_FILE
from scripts.file_loaders import load_lang_json, load_match_cases


@pytest.mark.acceptance
def test_toml_structure_e2e():
    try:
        load_match_cases(PATH_TOML_FILE)
    except Exception as e:
        pytest.fail(f"Invalid structure of {PATH_TOML_FILE} file: {e}")


@pytest.mark.acceptance
def test_lang_json_structure_e2e():
    try:
        load_lang_json(PATH_LANG_FILE)
    except Exception as e:
        pytest.fail(f"Invalid structure of {PATH_LANG_FILE} file: {e}")


@pytest.mark.unit
def test_validate_match_cases_toml():
    mock_toml_data = {
        "numeric": {"cases": ["a", "b"]},
        "legal": {"cases": ["c", "d"]},
        "important": {"cases": ["e", "f"]},
        "voyage_related": {"cases": ["g", "h"]},
        "counterparts": {"cases": ["i", "j"]},
        "other": {"cases": ["k", "l"]},
    }

    with patch("builtins.open", mock_open(read_data=toml.dumps(mock_toml_data))):
        with patch(
            "toml.load", return_value=mock_toml_data
        ):  # Mocking toml.load to return mock_toml_data directly
            load_match_cases("fake_path")


@pytest.mark.unit
def test_validate_lang_json():
    mock_lang_json = {
        "name": "Recap",
        "scopeName": "source.recap",
        "patterns": [
            {
                "name": "constant.numeric",
                "match": "(?i)\\b(one|two)\\b",
                "captures": {"1": {"name": "constant.numeric"}},
            },
            {
                "name": "string.quoted",
                "match": "(?i)\\b(law|order)\\b",
                "captures": {"1": {"name": "string.quoted"}},
            },
        ],
    }

    with patch("builtins.open", mock_open(read_data=json.dumps(mock_lang_json))):
        with patch(
            "json.load", return_value=mock_lang_json
        ):  # Mocking json.load to return mock_lang_json directly
            load_lang_json("fake_path")
