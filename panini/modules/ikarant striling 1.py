def create_mapping():
    # List of consonants and their corresponding halant form
    consonants = {
        'क': 'क्', 'ख': 'ख्', 'ग': 'ग्', 'घ': 'घ्', 'ङ': 'ङ्',
        'च': 'च्', 'छ': 'छ्', 'ज': 'ज्', 'झ': 'झ्', 'ञ': 'ञ्',
        'ट': 'ट्', 'ठ': 'ठ्', 'ड': 'ड्', 'ढ': 'ढ्', 'ण': 'ण्',
        'त': 'त्', 'थ': 'थ्', 'द': 'द्', 'ध': 'ध्', 'न': 'न्',
        'प': 'प्', 'फ': 'फ्', 'ब': 'ब्', 'भ': 'भ्', 'म': 'म्',
        'य': 'य्', 'र': 'र्', 'ल': 'ल्', 'व': 'व्', 'श': 'श्',
        'ष': 'ष्', 'स': 'स्', 'ह': 'ह्', 'क्ष': 'क्', 'त्र': 'त्',
        'ज्ञ': 'ज्'
    }

    # List of vowels and their corresponding forms
    vowels = {
        'अ': '', 'आ': 'ा', 'इ': 'ि', 'ई': 'ी', 'उ': 'ु', 'ऊ': 'ू',
        'ए': 'े', 'ऐ': 'ै', 'ओ': 'ो', 'औ': 'ौ', 'ं': 'ं', 'ः': 'ः',
        'ऋ': 'ृ', 'ॠ': 'ॄ', 'ऌ': 'ॢ'
    }

    # Create a dictionary for mapping
    mapping = {}
    for consonant, halant in consonants.items():
        for vowel, vowel_mark in vowels.items():
            combined_char = consonant + vowel
            mapped_value = halant + vowel_mark
            mapping[combined_char] = mapped_value
        mapping[halant] = halant  # Mapping for pure consonants

    return mapping

mapping = create_mapping()

def separate_characters_and_map(input_string):
    output = ''
    i = 0
    while i < len(input_string):
        # Check for two-character matches first
        if i + 2 <= len(input_string) and input_string[i:i + 2] in mapping:
            output += mapping[input_string[i:i + 2]]
            i += 2
        elif input_string[i] in mapping:
            output += mapping[input_string[i]]
            i += 1
        else:
            output += input_string[i]
            i += 1
    return output

def remove_last_characters(word):
    characters_to_remove = ['ई']
    while word.endswith(tuple(characters_to_remove)):
        word = word[:-1]
    return word

def merge_characters(word):
    replacements = {
        "्औ": "ौ", "्ओ": "ो", "्आ": "ा", "्अ": "", "शइ": "शि", "कउ": "कु",
        "म्औ": "मौ", "म्ऐ": "मै", "म्ए": "मे", "ष्उ": "षु", "व्ए": "वे",
        "व्ऐ": "वै", "प्ऊ": "पू", "त्ए": "ते", "त्ऐ": "तै", "न्इ": "नि",
        "ग्औ": "गौ", "र्ई": "री", "इय": "य", "उय": "य"
    }
    for old, new in replacements.items():
        word = word.replace(old, new)
    return word

def main():
    input_string = input("Enter the input string: ")
    output_string = separate_characters_and_map(input_string)
    print('characters separation:', output_string)

    input_string = remove_last_characters(output_string)
    print("remove last ई :", input_string)

    characters_to_add = [
        '11', 'यौ12', 'यः13', 'ईम्21', 'यौ22', 'ईः23',
        'या31', 'ईभ्याम्32', 'ईभिः33', 'यै41', 'ईभ्याम्42', 'ईभ्यः43',
        'याः51', 'ईभ्याम्52', 'ईभ्यः53', 'याः61', 'योः62', 'ईणाम्63',
        'याम्71', 'योः72', 'ईषु73', 'हे गौरि81', 'हे गौर्यौ82', 'हे गौर्यः83'
    ]

    output_string = ", ".join(input_string + character for character in characters_to_add)
    print(output_string)

    words = [word.strip() for word in output_string.split(',')]
    merged_outputs = " , ".join(merge_characters(word) for word in words)
    print('ईकारांत =', merged_outputs)

if __name__ == "__main__":
    main()
