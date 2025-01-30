def word_to_list(input_text=None):
    """
    Converts a single word or space-separated string into a Python list.
    If no input is provided, it prompts the user to enter the text interactively.
    """
    if input_text is None:
        input_text = input("Enter word(s): ")
    return input_text.split()
