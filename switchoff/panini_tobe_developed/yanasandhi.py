def replace_last_character(a):
    characters_to_replace = ['इ', 'उ', 'ऋ', 'लृ', 'ई', 'ऊ', 'ॠ', 'ॡ']
    replacement_characters = ['य्', 'व्', 'र्', 'ल्', 'य्', 'व्', 'र्', 'ल्']

    last_character = a[0][-1]
    index = characters_to_replace.index(last_character)
    new_last_character = replacement_characters[index]
    a[0] = a[0][:-1] + new_last_character

    return a
#a = ['स्उध्ई', 'उप्आस्य्अ']
#new_a = replace_last_character(a)
#print(new_a)
