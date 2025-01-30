import re

def split_halant_sequence(word):
    """
    Treat halant (\u094d) sequences as a single character unit.
    """
    pattern = r'\w\u094d?'
    return re.findall(pattern, word)

def chajo(word_list):
    """
    Replaces the last character of words in the list based on specific rules:
    - If the word ends with 'ज्', replace it with 'ग्'
    - If the word ends with 'च्', replace it with 'क्'

    Args:
        word_list (list): A list of words to process.

    Returns:
        list: The modified list of words.
    """
    # Load anga.txt
    try:
        with open('../../data/panini_function/anga.txt', 'r', encoding='utf-8') as f:
            anga_words = set(f.read().splitlines())
    except FileNotFoundError:
        raise FileNotFoundError("anga.txt file not found. Please ensure it's in the same directory.")

    def process_word(word):
        split_word = split_halant_sequence(word)  # Ensure halants are treated correctly
        if ''.join(split_word) in anga_words:
            if split_word[-1] == 'ज्':
                split_word[-1] = 'ग्'
            elif split_word[-1] == 'च्':
                split_word[-1] = 'क्'
        return ''.join(split_word)  # Rejoin the sequence into a single word

    return [process_word(w) for w in word_list]

# Example usage:
#word = ['भ्आज्', 'अ']
# Assuming 'भ्आज्' is in anga.txt
#print(chajo(word))  # Output: ['भ्आग्', 'अ']
