def load_pratyaya(file_path):
    """Load pratyayas from a text file into a list."""
    with open(file_path, 'r', encoding='utf-8') as file:
        pratyayas = [
            line.strip() for line in file
            if line.strip() and not line.startswith('#')  # Skip comments
        ]
    return pratyayas


def replace_starting_characters(word, pratyaya_file):
    """Replace specific starting characters with respective replacements for words in the pratyaya file."""
    # Load pratyayas
    pratyayas = load_pratyaya(pratyaya_file)

    # Patterns and their replacements
    patterns_to_replace = ['क्', 'ख्', 'ग्', 'घ्', 'ङ्', 'ल्', 'श्']
    replacements = ['{कित्}', '{खित्}', '{गित्}', '{घित्}', '{ङित्}', '{लित्}', '{शित्}']

    # Check if the word is in the pratyaya file
    if word in pratyayas:
        for pattern, replacement in zip(patterns_to_replace, replacements):
            if word.startswith(pattern):
                # Replace only the matched starting pattern and keep the rest of the word
                word = replacement + word[len(pattern):]
                break
    return word


def process_words(input_list, pratyaya_file):
    """Process a list of words to replace starting characters with respective replacements if they match the pratyaya file."""
    return [replace_starting_characters(word, pratyaya_file) for word in input_list]


# Example Usage
#pratyaya_file_path = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/panini/function/taddhati_bhin_pratyaya.txt'  # Path to your .txt file

# Input list
#input_list = ['क्यच्', 'खिष्णुच्', 'ल्युट्', 'अन्य']

# Process the words
#output_list = process_words(input_list, pratyaya_file_path)

# Print results
#print('Final Output:', output_list)
