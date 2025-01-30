def at_upadhaya(input_data):
    """
    Replaces specified characters marked by double asterisks:
    - '**अ**' with 'आ'
    - '**ई**' with 'ऐ'
    - '**उ**' with 'औ'

    Args:
        input_data (str or list): A word (str) or list of words to process.

    Returns:
        str or list: The modified word or list of words.
    """
    replacements = {'[अ]': 'आ', '[ई]': 'ऐ', '[उ]': 'औ'}

    def replace_characters(word):
        for old, new in replacements.items():
            word = word.replace(old, new)
        return word

    if isinstance(input_data, str):
        return replace_characters(input_data)
    elif isinstance(input_data, list):
        return [replace_characters(word) for word in input_data]
    else:
        raise TypeError("Input must be a string or a list of strings.")


