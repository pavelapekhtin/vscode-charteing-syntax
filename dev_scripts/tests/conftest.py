import pytest
import json
import toml


@pytest.fixture
def mock_files():
    mock_toml_data = {
        "numeric": {"cases": ["one", "two"]},
        "legal": {"cases": ["law", "order"]},
    }

    mock_json_data = {
        "patterns": [
            {"name": "constant.numeric"},
            {"name": "string.quoted"},
            {"name": "variable.parameter"}
        ]
    }

    return {
        "toml": toml.dumps(mock_toml_data),
        "json": json.dumps(mock_json_data)
    }