import re


def prevent_halant_splitting(word):
    """
    Prevent halant (\u094d) splitting in a word by treating halant sequences
    as single character units.

    Args:
        word (str): The Sanskrit word to process.

    Returns:
        list: A list of character units where halant sequences are kept intact.
    """
    pattern = r'\w\u094d?'
    return re.findall(pattern, word)


# Example usage:
word = "भ्आज्"
print(prevent_halant_splitting(word))  # Output: ['भ', '्', 'आ', 'ज्']
