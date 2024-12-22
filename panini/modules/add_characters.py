def append_characters(input_string, characters_to_add):
    """
    Append specified characters to an input string and process tagging.

    :param input_string: The base string to which characters will be appended.
    :param characters_to_add: A list of characters with optional tags or ranges.
    :return: A processed string with appended characters.
    """
    output_string = ""

    for character in characters_to_add:
        if "=" in character:
            # Handle tagged characters (e.g., 'ए13=sarva')
            char, tag = character.split("=")
            output_string += f"{input_string}{char} ({tag}), "
        elif "-" in character:
            # Handle range-based characters (e.g., 'अम्11-21=gyan')
            char_range, tag = character.split("=")
            char_start, char_end = char_range.split("-")
            output_string += f"{input_string}{char_start} to {char_end} ({tag}), "
        else:
            # Simple character addition
            output_string += f"{input_string}{character}, "

    # Remove the trailing comma and space
    return output_string.rstrip(", ")

# Example usage
if __name__ == "__main__":
    input_string = "पठ"
    characters_to_add = [
        'अ:11', 'औ12', 'आ:13', 'अम्21', 'औ22', 'आन्23', 
        'एण्अ31', 'आभ्य्आम्32', 'ऐ:33', 'आय्अ41', 'आभ्य्आम्42',
        'एभ्य्अ:43', 'आत्51', 'आभ्य्आम्52', 'एभ्य्अ:53', 
        'अस्य्अ61', 'अय्ओ:62', 'आण्आम्63', 'ए71', 'अय्ओ:72', 
        'एष्उ73', 'ए13=sarva', 'अस्मै41=sarva', 'अस्मात्51=sarva',
        'एषाम्63=sarva', 'अस्मिन्71=sarva', 'अम्11-21=gyan',
        'ए12-22=gyan', 'आनि13-23=gyan', 'एन31=gyan'
    ]
    output = append_characters(input_string, characters_to_add)
    print(output)
