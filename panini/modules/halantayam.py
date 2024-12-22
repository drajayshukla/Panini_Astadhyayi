def remove_last_characters(word):
    characters_to_remove = ['ह्', 'य्', 'व्', 'र्', 'ल्', 'ञ्', 'ङ्', 'ण्', 'झ्', 'भ्', 'घ्', 'ढ्'
        , 'ज्', 'ब्', 'ग्', 'ड्', 'ख्', 'फ्', 'छ्', 'ठ्', 'च्', 'ट्',
                            'क्', 'प्', 'श्', 'ष्']
    if word[-2:] in characters_to_remove:
        word = word[:-2]
    return word
