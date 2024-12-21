def remove_last_characters(strings):
    characters_to_remove = ['ह्', 'य्', 'व्', 'र्', 'ल्', 'ञ्', 'म्', 'ङ्', 'न्', 'ण्', 'झ्', 'भ्', 'घ्', 'ढ्',
                            'ध्', 'ज्', 'ब्', 'ग्', 'ड्', 'द्', 'ख्', 'फ्', 'छ्', 'ठ्', 'थ्', 'च्', 'ट्', 'त्',
                            'क्', 'प्', 'श्', 'ष्', 'स्']
    cleaned_strings = []
    for string in strings:
        if string.endswith(tuple(characters_to_remove)):
            string = string[:-2]
        cleaned_strings.append(string)
    return cleaned_strings
