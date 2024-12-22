def remove_anunasik_akshar(word):
    anunasik_akshar = ['अँ', 'आँ', 'इँ', 'ईँ', 'उँ', 'ऊँ', 'ऋँ', 'ॠँ', 'ऌँ', 'ॡँ', 'एँ', 'ओँ', 'ऐँ', 'औँ']
    for akshar in anunasik_akshar:
        word = word.replace(akshar, '')
    return word

def remove_anunasik_akshar_from_list(word_list):
    modified_list = []
    for word in word_list:
        modified_word = remove_anunasik_akshar(word)
        modified_list.append(modified_word)
    return modified_list

# Example usage
#input_list = ['ज्इ', 'अ', 'ल्अँ']
#output_list = remove_anunasik_akshar_from_list(input_list)
#print("Input:", input_list)
#print("Output:", output_list)
