def modify_cleaned_strings(cleaned_strings):
    last_char = cleaned_strings[0][-1]
    first_char = cleaned_strings[1][0]

    if last_char in ['ए', 'ओ', 'ऐ', 'औ'] and first_char in ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ॠ', 'ऌ', 'ए', 'ऐ', 'ओ',
                                                            'औ']:
        if last_char == 'ए':
            cleaned_strings[0] = cleaned_strings[0][:-1] + 'अय्'
        elif last_char == 'ओ':
            cleaned_strings[0] = cleaned_strings[0][:-1] + 'अव्'
        elif last_char == 'ऐ':
            cleaned_strings[0] = cleaned_strings[0][:-1] + 'आय्'
        elif last_char == 'औ':
            cleaned_strings[0] = cleaned_strings[0][:-1] + 'आव्'

        #cleaned_strings[1] = cleaned_strings[1][1:]

    return cleaned_strings


#cleaned_strings = ['भ्ओ', 'इ', 'त्ऋ']
#modified_cleaned_strings = modify_cleaned_strings(cleaned_strings)
#print("Modified Cleaned Strings:", modified_cleaned_strings)
