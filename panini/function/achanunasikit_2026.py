def replace_anunasik_with_respective_it(word):
    anunasik_akshar = ['अँ', 'आँ', 'इँ', 'ईँ', 'उँ', 'ऊँ', 'ऋँ', 'ॠँ', 'ऌँ', 'ॡँ', 'एँ', 'ओँ', 'ऐँ', 'औँ']
    replacement_it = ['{अदित्}', '{आदित्}', '{इदित्}', '{ईदित्}', '{उदित्}', '{ऊदित्}', '{ऋदित्}', '{ॠदित्}', '{ऌदित्}',
                      '{ॡदित्}', '{एदित्}', '{ओदित्}', '{ऐदित्}', '{औदित्}']

    for akshar, it in zip(anunasik_akshar, replacement_it):
        word = word.replace(akshar, it)
    return word


def replace_anunasik_with_respective_it_in_list(word_list):
    modified_list = []
    for word in word_list:
        modified_word = replace_anunasik_with_respective_it(word)
        modified_list.append(modified_word)
    return modified_list
