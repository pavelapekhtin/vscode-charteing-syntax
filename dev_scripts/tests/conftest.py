from typing import Any

import pytest

fixture = Any


@pytest.fixture
def lang_file_updater_inst_e2e():
    from scripts.lang_file_updater import LangFileUpdater

    return LangFileUpdater()


@pytest.fixture
def list_with_str_duplicates():
    return ["a", "b", "c", "a", "d", "e", "b", "f", "g"]


@pytest.fixture
def list_without_str_duplicates():
    return ["a", "b", "c", "d", "e", "f", "g"]


@pytest.fixture
def sample_toml_content():
    return {
        "legal": {"cases": ["law", "order", "law"]},
        "numeric": {"cases": ["one", "two"]},
        "other": {"cases": ["apple", "banana"]},
    }


@pytest.fixture
def sample_all_items():
    return {
        "law": ["legal", "legal"],
        "order": ["legal"],
        "one": ["numeric"],
        "two": ["numeric"],
        "apple": ["other"],
        "banana": ["other"],
    }
