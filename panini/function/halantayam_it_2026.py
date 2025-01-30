def replace_last_hal_with_respective_it(strings):
    import os

    # List of characters to replace and their respective replacements
    characters_to_replace = ['ह्', 'य्', 'व्', 'र्', 'ल्', 'ञ्', 'म्', 'ङ्', 'न्', 'ण्', 'झ्', 'भ्', 'घ्', 'ढ्',
                             'ध्', 'ज्', 'ब्', 'ग्', 'ड्', 'द्', 'ख्', 'फ्', 'छ्', 'ठ्', 'थ्', 'च्', 'ट्', 'त्',
                             'क्', 'प्', 'श्', 'ष्', 'स्']
    replacement_it = ['{हित्}', '{यित्}', '{वित्}', '{रित्}', '{लित्}', '{ञित्}', '{मित्}', '{ङित्}', '{नित्}',
                      '{णित्}', '{झित्}', '{भित्}', '{घित्}', '{ढित्}', '{धित्}', '{जित्}', '{बित्}', '{गित्}',
                      '{डित्}', '{दित्}', '{खित्}', '{फित्}', '{छित्}', '{ठित्}', '{थित्}', '{चित्}', '{टित्}',
                      '{तित्}', '{कित्}', '{पित्}', '{शित्}', '{षित्}', '{सित्}']

    # Create a mapping for easy lookup
    char_to_replacement = dict(zip(characters_to_replace, replacement_it))

    # Load words from vibhakti_tusma.txt
    exception_words = set()
    file_path = "../../data/panini_function/vibhakti_tusma.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            exception_words = {line.strip() for line in file}

    modified_strings = []
    for string in strings:
        # Skip words present in the exception list
        if string in exception_words:
            modified_strings.append(string)
            continue

        # Replace the last hal character with its corresponding replacement
        for char in characters_to_replace:
            if string.endswith(char):
                string = string[:-len(char)] + char_to_replacement[char]
                break
        modified_strings.append(string)

    return modified_strings

# Example usage
# input_list = ['भ्ऊ', 'इट्', 'त्ऋच्', 'क्यह्', 'श्चथ्']
# modified_list = replace_last_hal_with_respective_it(input_list)
# print("Modified List:", modified_list)
