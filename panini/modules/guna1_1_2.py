# Define गुण characters
guna_vowels = ['अ', 'ए', 'ओ']

# Define a mapping for गुण transformations
guna_mapping = {
    'अ': 'अ',  # ऋ transforms to अ
    'इ': 'ए',  # इ transforms to ए
    'उ': 'ओ',
    'ऋ':'अर्'# उ transforms to ओ
}

def get_guna_vowels():
    """
    Retrieve all vowels that qualify as गुण.
    :return: List of गुण vowels
    """
    return guna_vowels

def is_guna(char):
    """
    Check if the given character is a गुण character.
    :param char: A single character (str)
    :return: True if the character is गुण, False otherwise
    """
    return char in guna_vowels

def identify_guna_vowels(word):
    """
    Identify गुण characters in the given word.
    :param word: Input Sanskrit word (str)
    :return: List of गुण vowels found in the word
    """
    return [char for char in word if is_guna(char)]

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

def explain_guna():
    """
    Provide an explanation of the concept of गुण in Sanskrit grammar.
    :return: Explanation string
    """
    explanation = """
    ### Guna (गुण)
    In Sanskrit grammar, certain vowels are classified as 'Guna'. 
    According to the rule `अत्-एङ् गुणः`, the vowels अ, ए, and ओ are designated as 'Guna'.

    #### Examples:
    1. ऋtoङिसर्वनामस्थानयोः (7.3.110):
       - Input: पितृ + औ (Prathama-Dvivachana suffix)
       - Transformation:
           - पितर् + औ (ऋ transforms to अ as per Guna rule)
       - Output: पितरौ

    2. Guna transformations are also applied to ऋ, इ, and उ as per the rules of Panini's grammar.
    """
    return explanation

# Example usage
if __name__ == "__main__":
    # Example input
    word = "पितृ"

    print("Input Word:", word)

    # Get गुण vowels
    print("गुण Vowels:", get_guna_vowels())

    # Identify गुण characters
    guna_characters = identify_guna_vowels(word)
    print("Identified गुण Characters:", guna_characters)

    # Apply गुण transformation
    transformed_word = apply_guna_transformation(word, guna_mapping)
    print("Transformed Word:", transformed_word)

    # Explanation of गुण
    print(explain_guna())
