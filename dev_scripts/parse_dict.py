import json
import toml

def combine_match_cases():
    # Load the match cases from the TOML file
    with open('dictionary/matchCases.toml', 'r') as f:
        match_cases = toml.load(f)

    # Load the language file template
    with open('scripts/language_file_template.json', 'r') as f:
        language_data = json.load(f)

    # Mapping between TOML keys and JSON names
    mapping = {
        "numeric": "constant.numeric",
        "legal": "string.quoted",
        "important": "variable.parameter",
        "voyage_related": "variable.other.readwrite",
        "counterparts": "storage",
        "other": "entity.name.type.class"
    }

    for pattern in language_data['patterns']:
        name = pattern.get('name')
        toml_key = [key for key, value in mapping.items() if value == name][0]
        if toml_key in match_cases:
            joined_match = "|".join(match_cases[toml_key]['cases'])
            pattern['match'] = f"(?i)\\b({joined_match})\\b"

    # Save the updated language data back to the JSON file
    with open('syntaxes/recap.tmLanguage.json', 'w') as f:
        json.dump(language_data, f,indent=2)

if __name__ == "__main__":
    combine_match_cases()
