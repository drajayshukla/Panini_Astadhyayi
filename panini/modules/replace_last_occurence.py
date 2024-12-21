def replace_last_occurrence(word, old_char, new_chars):
    """
    Replaces the last occurrence of `old_char` in `word` with `new_chars`.

    Args:
        word (str): The original string.
        old_char (str): The character to be replaced.
        new_chars (str): The replacement characters.

    Returns:
        str: The modified string with the last occurrence replaced.
    """
    reversed_word = word[::-1]
    reversed_new_chars = new_chars[::-1]
    replaced_word = reversed_word.replace(old_char[::-1], reversed_new_chars, 1)
    return replaced_word[::-1]