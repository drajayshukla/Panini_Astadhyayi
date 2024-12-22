def remove_last_characters(word, characters_to_remove=None):
    """
    Remove specific characters from the end of a word.

    :param word: The input word as a string
    :param characters_to_remove: A list of characters to remove from the end of the word. 
                                  Defaults to Sanskrit vowels ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ'].
    :return: The word with the specified characters removed from the end.
    """
    if characters_to_remove is None:
        # Default to removing common Sanskrit vowels
        characters_to_remove = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ']
    
    while word.endswith(tuple(characters_to_remove)):
        word = word[:-1]
    return word

# Example usage
if __name__ == "__main__":
    example_word = "पाठअ"
    print("Original Word:", example_word)
    cleaned_word = remove_last_characters(example_word)
    print("Cleaned Word:", cleaned_word)
