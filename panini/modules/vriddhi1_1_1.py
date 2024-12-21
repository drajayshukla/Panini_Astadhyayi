# vriddhi.py

def get_vriddhi_vowels():
    """
    Returns the list of Vriddhi vowels: आ, ऐ, औ.
    """
    return ['आ', 'ऐ', 'औ']

def identify_vriddhi_vowels(input_string):
    """
    Identifies Vriddhi vowels in the given string.
    Args:
        input_string (str): The input string to search.
    Returns:
        list: Vriddhi vowels found in the input string.
    """
    vriddhi_vowels = get_vriddhi_vowels()
    return [char for char in input_string if char in vriddhi_vowels]

def explain_vriddhi():
    """
    Explains the concept of Vriddhi vowels in Pāṇini's grammar.
    """
    explanation = (
        "Vriddhi vowels are the extended or strengthened vowels "
        "in Sanskrit grammar. According to Pāṇini's Aṣṭādhyāyī, "
        "आ, ऐ, and औ are classified as Vriddhi vowels."
    )
    return explanation
