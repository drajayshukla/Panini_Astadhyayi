def replace_characters(words):
    """
    Apply Ayadi Sandhi rules to combine two words based on specified replacement characters.

    :param words: A string containing two Sanskrit words separated by a space.
    :return: The combined word after applying Ayadi Sandhi rules.
    """
    try:
        first_word, second_word = words.split()
    except ValueError:
        raise ValueError("Input must contain two words separated by a space.")

    # Characters to replace based on Ayadi Sandhi rules
    characters_to_replace = ['ए', 'ओ', 'ऐ', 'औ']
    replacement_characters = ['अय्', 'अव्', 'आय्', 'आव्']

    # Check if the last character of the first word matches the list
    # and if the first character of the second word is a valid vowel
    if (
        first_word[-1] in characters_to_replace
        and second_word[0] in ['अ', 'आ', 'ई', 'इ', 'उ', 'ऊ', 'ऋ', 'ॠ', 'लृ', 'ॡ', 'ए', 'ओ', 'ऐ', 'औ']
    ):
        # Find the index of the character to replace
        index = characters_to_replace.index(first_word[-1])
        replaced_character = replacement_characters[index]
        
        # Replace the last character of the first word with the mapped replacement
        new_first_word = first_word[:-1] + replaced_character
        
        # Combine the transformed first word with the second word
        result = new_first_word + second_word
        return result

    # If no replacement rules match, return the original input
    return words


# Example usage
if __name__ == "__main__":
    input_words = "ए आक्ऋत्इः"  # Example input
    result = replace_characters(input_words)
    print("Result:", result)
def modify_cleaned_strings(cleaned_strings):
    """
    Apply Ayadi Sandhi rules to a list of words based on their last and first characters.

    :param cleaned_strings: List of words to modify based on Ayadi Sandhi rules.
    :return: Modified list of words after applying Ayadi Sandhi rules.
    """
    if len(cleaned_strings) < 2:
        raise ValueError("The list must contain at least two words for Ayadi Sandhi to apply.")

    last_char = cleaned_strings[0][-1]  # Last character of the first word
    first_char = cleaned_strings[1][0]  # First character of the second word

    # Characters to transform based on Ayadi Sandhi
    ayadi_map = {
        'ए': 'अय्',
        'ओ': 'अव्',
        'ऐ': 'आय्',
        'औ': 'आव्'
    }

    # Check if the last character and first character meet the transformation criteria
    if last_char in ayadi_map and first_char in ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ॠ', 'ऌ', 'ए', 'ऐ', 'ओ', 'औ']:
        # Transform the last character of the first word
        cleaned_strings[0] = cleaned_strings[0][:-1] + ayadi_map[last_char]

    return cleaned_strings


# Example usage
if __name__ == "__main__":
    # Example list of cleaned strings
    cleaned_strings = ["ओ", "आचार्यः"]

    print("Original Strings:", cleaned_strings)

    # Apply Ayadi Sandhi transformation
    modified_strings = modify_cleaned_strings(cleaned_strings)
    print("Modified Strings:", modified_strings)
