from typing import Any

import pytest

from filepaths import PATH_TOML_FILE
from scripts.file_loaders import load_match_cases
from scripts.match_toml_housekeeping import (
    combine_match_cases,
    find_and_report_duplicates_across_lists,
    find_and_report_duplicates_within_lists,
    find_list_duplicates,
    sort_lists,
)
from tests.conftest import fixture


@pytest.mark.acceptance
def test_combine_match_cases_e2e(capsys: Any) -> None:
    toml_file = load_match_cases(PATH_TOML_FILE)
    combine_match_cases(toml_file)
    captured = capsys.readouterr()
    assert "⚠ Duplicates!" not in captured.out


def test_find_list_duplicates(
    list_with_str_duplicates: fixture, list_without_str_duplicates: fixture
) -> None:
    assert find_list_duplicates(list_with_str_duplicates) == [("a", 3), ("b", 6)]
    assert find_list_duplicates(list_without_str_duplicates) == []


def test_find_and_report_duplicates_within_lists(
    sample_toml_content: fixture, capsys: Any
) -> None:
    duplicates_count = find_and_report_duplicates_within_lists(sample_toml_content)
    captured = capsys.readouterr()
    assert duplicates_count == 1
    assert "⚠ Duplicates! in 'legal':" in captured.out
    assert "  - Duplicate: law, at index: 2" in captured.out


def test_find_and_report_duplicates_across_lists(
    sample_all_items: fixture, capsys: Any
) -> None:
    duplicates_count = find_and_report_duplicates_across_lists(sample_all_items)
    captured = capsys.readouterr()
    assert duplicates_count == 1
    assert "Item law found in multiple lists: legal, legal" in captured.out


def test_sort_lists(sample_toml_content: fixture) -> None:
    sort_lists(sample_toml_content)
    assert sample_toml_content["legal"]["cases"] == ["law", "law", "order"]
    assert sample_toml_content["numeric"]["cases"] == ["one", "two"]
    assert sample_toml_content["other"]["cases"] == ["apple", "banana"]
