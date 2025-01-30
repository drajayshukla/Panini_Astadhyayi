import re

def modify_word_based_on_txt(word_list, txt_file_path):
    """
    Modify the second last logical character of words in the list if the word is present in anga.txt.

    Args:
        word_list (list): List of words to process.
        txt_file_path (str): Path to the anga.txt file.

    Returns:
        list: Modified word list.
    """
    # Read contents of anga.txt
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            anga_words = {line.strip() for line in file}
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {txt_file_path} does not exist.")

    def split_halant_sequence(word):
        """
        Treat halant (\u094d) sequences as a single character unit.
        """
        pattern = r'\w\u094d?'
        return re.findall(pattern, word)

    # Process each word in the list
    modified_words = []
    for word in word_list:
        if word in anga_words:
            logical_chars = split_halant_sequence(word)
            if len(logical_chars) > 1:  # Ensure there are enough characters to modify
                # Insert ** around the second last logical character
                logical_chars[-2] = f'[{logical_chars[-2]}]'
                modified_word = ''.join(logical_chars)
                modified_words.append(modified_word)
            else:
                modified_words.append(word)  # No modification if the word is too short
        else:
            modified_words.append(word)  # No modification if the word is not in anga.txt

    return modified_words

# Example Usage

