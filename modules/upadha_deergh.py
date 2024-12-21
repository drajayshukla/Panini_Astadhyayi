def apply_last_character_rules(word):
    last_char = word[-1]
    third_last_char = word[-3]

    if last_char in  ['्']:
        if third_last_char == 'अ':
            word = word[:-3] + 'आ' + word[-2:]
        elif third_last_char == 'आ':
            word = word[:-3] + 'आ' + word[-2:]
        elif third_last_char == 'इ':
            word = word[:-3] + 'ई' + word[-2:]
        elif third_last_char == 'ई':
            word = word[:-3] + 'ई' + word[-2:]
        elif third_last_char == 'उ':
            word = word[:-3] + 'ऊ' + word[-2:]
        elif third_last_char == 'ऊ':
            word = word[:-3] + 'ऊ' + word[-2:]
        elif third_last_char == 'ऋ':
            word = word[:-3] + 'ॠ' + word[-2:]
        elif third_last_char == 'ॠ':
            word = word[:-3] + 'ॠ' + word[-2:]
        elif third_last_char == 'ऌ':
            word = word[:-3] + 'ॡ' + word[-2:]
        elif third_last_char == 'ॡ':
            word = word[:-3] + 'ॡ' + word[-2:]
        elif third_last_char == 'ए':
            word = word[:-3] + 'ऐ' + word[-2:]
        elif third_last_char == 'ऐ':
            word = word[:-3] + 'ऐ' + word[-2:]
        elif third_last_char == 'ओ':
            word = word[:-3] + 'औ' + word[-2:]
        elif third_last_char == 'औ':
            word = word[:-3] + 'औ' + word[-2:]
    elif last_char in ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ॠ', 'ऌ', 'ॡ', 'ए', 'ऐ', 'ओ', 'औ']:
        if third_last_char in ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ॠ', 'ऌ', 'ॡ', 'ए', 'ऐ', 'ओ', 'औ']:
            word = word[:-2] + 'आन्' + word[-1]

    return word


word_list = ['च्ए', 'त्अन्', 'स्']
modified_word = apply_last_character_rules(word_list[1])
print(modified_word)
