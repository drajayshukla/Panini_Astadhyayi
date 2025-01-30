def replace_anunasik_with_it(word):
    anunasik_akshar = ['अँ', 'आँ', 'इँ', 'ईँ', 'उँ', 'ऊँ', 'ऋँ', 'ॠँ', 'ऌँ', 'ॡँ', 'एँ', 'ओँ', 'ऐँ', 'औँ']
    for akshar in anunasik_akshar:
        word = word.replace(akshar, '"इत्"')
    return word

def replace_anunasik_with_it_in_list(word_list):
    modified_list = []
    for word in word_list:
        modified_word = replace_anunasik_with_it(word)
        modified_list.append(modified_word)
    return modified_list
