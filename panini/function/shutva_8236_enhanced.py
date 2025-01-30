import re
def shutva_8236_final(input_list):
    """
    Apply the Shutva rule (8236) while ensuring the halant (्) is not broken:
    - Convert the last "ज्", "श्", "च्छ्", or "श्च्" in the first word to "ष्".
    - If there are two words, process the second word for jhal_sounds.

    Parameters:
    input_list (list): A list of one or two elements.

    Returns:
    list: Modified list after applying the rule.
    """

    # List of applicable words
    applicable_words = ["व्रश्च्", "भ्रस्ज्", "सृज्", "मृज्", "यज्", "राज्", "भ्राज्", "म्आर्ज्"]

    # Regular expressions for handling शकारान्त / च्छकारान्त / श्चकारान्त and halant sequences
    halant_sequence_pattern = "(.*)ज्$|(.*)श्$|(.*)च्छ्$|(.*)श्च्$"

    # Modify the first word in the list
    if input_list[0] in applicable_words or re.match(halant_sequence_pattern, input_list[0]):
        input_list[0] = re.sub("(.*)ज्$", r"\1ष्", input_list[0])
        input_list[0] = re.sub("(.*)श्$", r"\1ष्", input_list[0])
        input_list[0] = re.sub("(.*)च्छ्$", r"\1ष्", input_list[0])
        input_list[0] = re.sub("(.*)श्च्$", r"\1ष्", input_list[0])

    # If there are two words, process the second word for jhal_sounds
    if len(input_list) > 1:
        # List of "झल्" sounds
        jhal_sounds = [
            "झ्", "भ्", "घ्", "ढ्", "ध्", "ज्", "ब्", "ग्", "ड्", "द्",
            "ख्", "फ्", "छ्", "ठ्", "थ्", "च्", "ट्", "त्", "क्", "प्",
            "श्", "ष्", "स्", "ह्"
        ]
        for sound in jhal_sounds:
            if input_list[1].startswith(sound):
                input_list[1] = f"{{{sound}}}" + input_list[1][len(sound):]
                break

    return input_list

# Input examples
#input_single = ['व्रश्च्']  # Single word, ending with श्च्
#input_double = ['म्आर्ज्', 'त्इ']  # Two words, first ends with श्च्

# Apply the function
#output_single = shutva_8236_final(input_single)
#output_double = shutva_8236_final(input_double)

#print(output_single, output_double)
