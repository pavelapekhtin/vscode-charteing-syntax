import os
import toml
import json
from unittest.mock import mock_open, patch
from src.parse_dict import combine_match_cases

def test_combine_match_cases(mock_files):
    m = mock_open()
    m.side_effect = [
        mock_open(read_data=mock_files["toml"]).return_value,
        mock_open(read_data=mock_files["json"]).return_value,
        mock_open().return_value
    ]

    with patch('builtins.open', m):
        with patch('json.load', side_effect=json.loads):
            with patch('toml.load', side_effect=toml.loads):
                combine_match_cases("fake_path_template", "fake_path_lang_json", "fake_path_match_cases")

    written_json = json.loads(m().write.call_args.args[0])
    assert written_json["patterns"][0]["match"] == r"(?i)\b(one|two)\b"
    assert written_json["patterns"][1]["match"] == r"(?i)\b(law|order)\b"
    assert "match" not in written_json["patterns"][2]

print(os.getcwd())