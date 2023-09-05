import toml

def find_duplicates(lst):
    seen = set()
    duplicates = []
    for index, item in enumerate(lst):
        if item in seen:
            duplicates.append((item, index))
        else:
            seen.add(item)
    return duplicates

def combine_match_cases():
    # Load the match cases from the TOML file
    with open('dictionary/matchCases.toml', 'r') as f:
        match_cases = toml.load(f)

    all_items = {}
    
    # Find duplicates and sort
    inside_duplicates = 0
    for key, value in match_cases.items():
        # Find duplicates within the same list
        duplicates = find_duplicates(value['cases'])
        if duplicates:
            inside_duplicates += 1
            print(f"Found duplicates in {key}:")
            for item, index in duplicates:
                print(f"  - Duplicate: {item}, at index: {index}")

        # Sort the list
        value['cases'].sort()

        # Collect all items for finding duplicates across lists
        for item in value['cases']:
            if item in all_items:
                all_items[item].append(key)
            else:
                all_items[item] = [key]

    # Find duplicates across different lists
    across_dulicates = 0
    for item, keys in all_items.items():
        if len(keys) > 1:
            across_dulicates += 1
            print(f"Item {item} found in multiple lists: {', '.join(keys)}")
    
    
    if inside_duplicates == 0 and across_dulicates == 0:
        print(f"No duplicates found")
    
    print("Lists sorted alphabetically")

    # Save the sorted lists back to the TOML file
    with open('dictionary/matchCases.toml', 'w') as f:
        toml.dump(match_cases, f)

if __name__ == "__main__":
    combine_match_cases()