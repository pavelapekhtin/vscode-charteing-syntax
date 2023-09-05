from typing import Any

fixture = Any


def test_pattern_matcher(lang_file_updater_inst_e2e: fixture) -> None:
    match_cases = {
        "numeric": {"cases": ["one", "two"]},
        "legal": {"cases": ["law", "order"]},
    }
    language_data = {
        "patterns": [
            {"name": "constant.numeric"},
            {"name": "string.quoted"},
        ]
    }
    mapping = {
        "numeric": "constant.numeric",
        "legal": "string.quoted",
    }

    parser = lang_file_updater_inst_e2e

    result = parser._pattern_matcher(match_cases, language_data, mapping)  # type: ignore

    assert result["patterns"][0]["match"] == "(?i)\\b(one|two)\\b"
    assert result["patterns"][1]["match"] == "(?i)\\b(law|order)\\b"
