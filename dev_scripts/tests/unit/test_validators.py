from unittest.mock import mock_open, patch

import pytest
import toml

from scripts.validators import validate_match_cases_toml


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
            validate_match_cases_toml("fake_path")
