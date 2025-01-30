def load_pratyaya(file_path):
    """Load pratyayas from a text file into a list."""
    with open(file_path, 'r', encoding='utf-8') as file:
        pratyayas = [line.strip() for line in file if line.strip()]
    return pratyayas


def replace_starting_characters_with_it(input_data):
    """Replace starting characters in words with their respective patterns."""
    patterns_to_replace = ['ट्', 'ठ्', 'ड्', 'ढ्', 'ण्', 'च्', 'छ्', 'ज्', 'झ्', 'ञ्']
    replacements = ['{टित्}', '{ठित्}', '{डित्}', '{ढित्}', '{णित्}', '{चित्}', '{छित्}', '{जित्}', '{झित्}', '{ञित्}']


    # Handle single word input by converting to a list
    if isinstance(input_data, str):
        input_data = [input_data]

    modified_words = []
    for word in input_data:
        modified = False
        for pattern, replacement in zip(patterns_to_replace, replacements):
            if word.startswith(pattern):
                word = replacement + word[len(pattern):]
                modified = True
                break
        modified_words.append(word)

    return modified_words


def process_words(input_list, pratyaya_file):
    """Process words from the input list if they are in the pratyaya file."""
    # Load pratyayas from the file
    pratyayas = load_pratyaya(pratyaya_file)

    # Process the words
    modified_words = []
    for index, word in enumerate(input_list):
        if any(pratyaya in word for pratyaya in pratyayas):
            # Apply the replacement logic
            modified_word = replace_starting_characters_with_it([word])[0]
        else:
            # Keep the word as is if not part of the pratyaya file
            modified_word = word
        modified_words.append(modified_word)

    return modified_words


# Example Input
#pratyaya_file_path = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/panini/function/pratyaya.txt'  # Update this path to the actual file location
#input_list = ['ड्उभ्अज्अँ', 'ण्अघ्अञ्']

# Process the words
#output_list = process_words(input_list, pratyaya_file_path)

# Print the results
#print('Final Output:', output_list)
