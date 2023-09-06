from typing import Dict, List, Tuple

import toml

from scripts.cli.cli_functions import console
from scripts.file_loaders import TomlDict, load_match_cases
from scripts.lang_file_updater import PATH_TOML_FILE


def find_list_duplicates(kwd_list: List[str]) -> List[Tuple[str, int]]:
    seen: set[str] = set()
    duplicates: List[Tuple[str, int]] = []
    for index, item in enumerate(kwd_list):
        if item in seen:
            duplicates.append((item, index))
        else:
            seen.add(item)
    return duplicates


def find_and_report_duplicates_within_lists(toml_content: TomlDict) -> int:
    inside_duplicates = 0
    for list_name, case in toml_content.items():
        duplicates = find_list_duplicates(case["cases"])
        if duplicates:
            inside_duplicates += 1
            console.print(
                f"[red]⚠ Duplicates! [/red]in [yellow]'{list_name}'[/yellow]:"
            )
            for item, index in duplicates:
                print(f"  - Duplicate: {item}, at index: {index}")
    return inside_duplicates


def find_and_report_duplicates_across_lists(
    all_items: Dict[str, set[str]]
) -> int:  # Changed from List to set
    across_duplicates = 0
    for item, keys in all_items.items():
        if len(keys) > 1:
            across_duplicates += 1
            console.print(
                f"[red]⚠ Duplicates! [/red]\nItem {item} found in multiple lists: {', '.join(keys)}"
            )  # join works on sets too
    return across_duplicates


def sort_lists(toml_content: TomlDict) -> None:
    for case in toml_content.values():
        case["cases"].sort()


def combine_match_cases(toml_dict: TomlDict) -> None:
    toml_content = toml_dict.copy()
    all_items: Dict[str, set[str]] = {}  # Changed from List to set

    # Step 1: Find duplicates within each list and report them
    inside_duplicates = find_and_report_duplicates_within_lists(toml_content)

    # Step 2: Collect all items for finding duplicates across lists
    for list_name, case in toml_content.items():
        for item in case["cases"]:
            if item in all_items:
                all_items[item].add(list_name)  # Using set's add method
            else:
                all_items[item] = {
                    list_name
                }  # Initialize with a set containing list_name

    # Step 3: Find and report duplicates across different lists
    across_duplicates = find_and_report_duplicates_across_lists(all_items)

    # Step 4: Sort the lists
    sort_lists(toml_content)

    # Summary and save
    if inside_duplicates == 0 and across_duplicates == 0:
        console.print("[green]✔ No duplicates found")
    console.print("[green]✔ Lists sorted alphabetically")

    # Save the sorted lists back to the TOML file
    # with open("dictionary/matchCases.toml", "w") as f:
    #     toml.dump(toml_content, f)


def do_toml_housekeeping(filepath: str) -> None:
    toml_dict = load_match_cases(filepath)
    combine_match_cases(toml_dict)
    with open(filepath, "w") as f:
        toml.dump(toml_dict, f)
    console.print(f"[green]✔ [/green]File updated: [yellow]'{filepath}'[/yellow]")


if __name__ == "__main__":
    do_toml_housekeeping(PATH_TOML_FILE)
