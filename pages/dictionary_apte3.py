import json
import os
from typing import List, Dict

# Path to the data file
DATA_FOLDER = './data'
DATA_FILE = os.path.join(DATA_FOLDER, 'apte_dhatu_pratyaya_arth_testin.json')


# Load data from JSON file
def load_dictionary(file_path: str) -> Dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


# Create a simplified dictionary
def create_sanskrit_hindi_dict(data: Dict) -> Dict[str, str]:
    words = data['data']['words']
    text = data['data']['text']
    return {word: text[meaning.split(",")[0]] for word, meaning in words.items()}


# Search for a Sanskrit word
def search_sanskrit_word(dictionary: Dict[str, str], word: str) -> str:
    return dictionary.get(word, "Word not found.")


# Reverse lookup: Search by Hindi meaning
def search_hindi_meaning(dictionary: Dict[str, str], phrase: str) -> List[str]:
    return [word for word, meaning in dictionary.items() if phrase in meaning]


# Partial match for Sanskrit words
def partial_match_sanskrit(dictionary: Dict[str, str], substring: str) -> List[str]:
    return [word for word in dictionary.keys() if substring in word]


# Save dictionary in different formats
def save_dictionary(dictionary: Dict[str, str], format: str = 'json'):
    output_file = os.path.join(DATA_FOLDER, f'sanskrit_hindi_dict.{format}')
    if format == 'json':
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, ensure_ascii=False, indent=4)
    elif format == 'csv':
        import csv
        with open(output_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Sanskrit Word', 'Hindi Meaning'])
            writer.writerows(dictionary.items())
    print(f"Dictionary saved as {output_file}")


# Main execution
if __name__ == "__main__":
    data = load_dictionary(DATA_FILE)
    sanskrit_hindi_dict = create_sanskrit_hindi_dict(data)

    # Example Usage
    print(search_sanskrit_word(sanskrit_hindi_dict, "अंशः"))
    print(search_hindi_meaning(sanskrit_hindi_dict, "भाग"))
    print(partial_match_sanskrit(sanskrit_hindi_dict, "अंश"))

    # Save dictionary in JSON and CSV formats
    save_dictionary(sanskrit_hindi_dict, 'json')
    save_dictionary(sanskrit_hindi_dict, 'csv')
