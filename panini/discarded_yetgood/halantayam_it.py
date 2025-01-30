def replace_last_hal_with_it(strings):
    characters_to_replace = ['ह्', 'य्', 'व्', 'र्', 'ल्', 'ञ्', 'म्', 'ङ्', 'न्', 'ण्', 'झ्', 'भ्', 'घ्', 'ढ्',
                             'ध्', 'ज्', 'ब्', 'ग्', 'ड्', 'द्', 'ख्', 'फ्', 'छ्', 'ठ्', 'थ्', 'च्', 'ट्', 'त्',
                             'क्', 'प्', 'श्', 'ष्', 'स्']
    modified_strings = []
    for string in strings:
        if string.endswith(tuple(characters_to_replace)):
            for char in characters_to_replace:
                if string.endswith(char):
                    string = string[:-len(char)] + '"इत्"'
                    break
        modified_strings.append(string)
    return modified_strings

# Example usage
#input_list = ['भ्ऊ', 'इट्', 'त्ऋच्']
##print("Modified List:", modified_list)
