from filepaths import PATH_LANG_FILE, PATH_LANG_FILE_TEMPLATE, PATH_TOML_FILE
from scripts.lang_file_updater import LangFileUpdater
from scripts.match_toml_housekeeping import do_toml_housekeeping


def main() -> None:
    do_toml_housekeeping(PATH_TOML_FILE)
    LangFileUpdater(
        PATH_TOML_FILE, PATH_LANG_FILE_TEMPLATE, PATH_LANG_FILE
    ).update_language_file()


if __name__ == "__main__":
    main()
