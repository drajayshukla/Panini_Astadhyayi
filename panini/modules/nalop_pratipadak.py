def remove_last_character_if_needed(input_string):
    if input_string.endswith("न्"):
        output_string = input_string[:-2]  # Remove the last character
    else:
        output_string = input_string

    return output_string
