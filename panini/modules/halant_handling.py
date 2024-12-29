def group_sanskrit_characters(input_string):
    """
    Groups Sanskrit characters logically, combining consonants with halants.

    Parameters:
    - input_string (str): Input string in Sanskrit.

    Returns:
    - grouped (list): List of logically grouped characters.
    """
    grouped = []
    temp = ""

    for char in input_string:
        if char in ['्', 'ं', 'ः']:  # Combine with the previous character
            temp += char
        else:
            if temp:  # Append the current group if exists
                grouped.append(temp)
            temp = char  # Start a new group with the current character

    if temp:  # Append the last group if any
        grouped.append(temp)

    return grouped

# Example Usage (if executed directly)
if __name__ == "__main__":
    example_input = "पठ् घञ्"
    grouped_characters = group_sanskrit_characters(example_input)
    print("Input String:", example_input)
    print("Grouped Characters:", grouped_characters)
