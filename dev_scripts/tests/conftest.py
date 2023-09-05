import pytest


@pytest.fixture
def lang_file_updater_inst_e2e():
    from scripts.lang_file_updater import LangFileUpdater

    return LangFileUpdater()
