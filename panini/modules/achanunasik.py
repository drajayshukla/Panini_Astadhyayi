def remove_anunasik_akshar(word):
    """
    Remove all anunasik akshar (nasalized vowels) from a Sanskrit word.

    :param word: A string containing Sanskrit text.
    :return: The modified string with anunasik akshar removed.
    """
    anunasik_akshar = ['अँ', 'आँ', 'इँ', 'ईँ', 'उँ', 'ऊँ', 'ऋँ', 'ॠँ', 'ऌँ', 'ॡँ', 'एँ', 'ऐँ', 'ओँ', 'औँ']
    for akshar in anunasik_akshar:
        word = word.replace(akshar, '')
    return word


def remove_anunasik_akshar_from_list(word_list):
    """
    Remove all anunasik akshar (nasalized vowels) from a list of Sanskrit words.

    :param word_list: A list of strings containing Sanskrit text.
    :return: A list of strings with anunasik akshar removed.
    """
    modified_list = []
    for word in word_list:
        modified_word = remove_anunasik_akshar(word)
        modified_list.append(modified_word)
    return modified_list




import re

def remove_anunasik_akshar1(word1):
    """
    Remove all anunasik akshar (nasalized vowels) from a Sanskrit word.

    :param word: A string containing Sanskrit text.
    :return: The modified string with anunasik akshar removed.
    """
    # Regular expression for nasalized vowels
    pattern = r'[अआइईउऊऋॠऌॡएऐओऔ]ँ'
    return re.sub(pattern, '', word1)

def remove_anunasik_akshar_from_list1(word1_list):
    """
    Remove all anunasik akshar (nasalized vowels) from a list of Sanskrit words.

    :param word_list: A list of strings containing Sanskrit text.
    :return: A list of strings with anunasik akshar removed.
    """
    return [remove_anunasik_akshar1(word) for word1 in word1_list]

# Example usage
if __name__ == "__main__":
    # Single word example
    word = "अँआँइँईँउँऊँऋँ"
    print("Original Word:", word)
    print("Modified Word:", remove_anunasik_akshar(word))

    # List of words example
    word_list = ["अँआँ", "इँईँ", "उँऊँऋँ"]
    print("Original Word List:", word_list)
    print("Modified Word List:", remove_anunasik_akshar_from_list(word_list))
