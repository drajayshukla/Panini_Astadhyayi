# guna1_1_2.py

# Define गुण characters
guna_vowels = ['अ', 'ए', 'ओ']

# Define a mapping for गुण transformations
guna_mapping = {
    'ऋ': 'अ',  # ऋ transforms to अ
    # Add other transformations as needed based on further rules
}

def is_guna(char):
    """
    Check if the given character is a गुण character.
    :param char: A single character (str)
    :return: True if the character is गुण, False otherwise
    """
    return char in guna_vowels

def apply_guna_transformation(word, guna_mapping):
    """
    Apply गुण transformation to the input word based on the mapping.
    :param word: Input Sanskrit word (str)
    :param guna_mapping: Dictionary containing transformations for गुण characters
    :return: Transformed word (str)
    """
    transformed_word = ""
    for char in word:
        transformed_word += guna_mapping.get(char, char)
    return transformed_word

def identify_guna_in_context(word):
    """
    Identify गुण characters in the context of a Sanskrit word.
    :param word: Input Sanskrit word (str)
    :return: List of tuples with index and गुण characters
    """
    guna_indices = [(i, char) for i, char in enumerate(word) if is_guna(char)]
    return guna_indices

# Example usage
if __name__ == "__main__":
    # Example input
    word = "पितृ"

    print("Input Word:", word)

    # Identify गुण characters
    guna_characters = identify_guna_in_context(word)
    print("गुण Characters with Indices:", guna_characters)

    # Apply गुण transformation
    transformed_word = apply_guna_transformation(word, guna_mapping)
    print("Transformed Word:", transformed_word)
