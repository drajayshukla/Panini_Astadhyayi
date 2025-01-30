def load_pratyaya(file_path):
    """Load pratyayas from a text file into a list."""
    with open(file_path, 'r', encoding='utf-8') as file:
        pratyayas = [
            line.strip() for line in file
            if line.strip() and not line.startswith('#')  # Skip comments
        ]
    return pratyayas


def replace_starting_characters(word, pratyaya_file):
    """Replace specific starting characters with '"इत्"' for words in the pratyaya file."""
    # Load pratyayas
    pratyayas = load_pratyaya(pratyaya_file)

    # Patterns to replace
    patterns_to_replace = ['क्', 'ख्', 'ग्', 'घ्', 'ङ्', 'ल्', 'श्']

    # Check if the word is in the pratyaya file
    if word in pratyayas:
        for pattern in patterns_to_replace:
            if word.startswith(pattern):
                # Replace the starting pattern with '"इत्"'
                word = '"इत्"' + word[len(pattern):]
                break
    return word


def process_words(input_list, pratyaya_file):
    """Process a list of words to replace starting characters with '"इत्"' if they match the pratyaya file."""
    return [replace_starting_characters(word, pratyaya_file) for word in input_list]


# Example Usage
#pratyaya_file_path = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/panini/function/taddhati_bhin_pratyaya.txt'  # Path to your .txt file

# Input list
#input_list = ['क्यच्', 'खिष्णुच्', 'ल्युट्', 'अन्य']

# Process the words
#output_list = process_words(input_list, pratyaya_file_path)

# Print results
#print('Final Output:', output_list)
