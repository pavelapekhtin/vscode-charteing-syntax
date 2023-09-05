import json
from unittest.mock import mock_open, patch

import toml

from scripts.file_loaders import load_lang_json, load_match_cases


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
