def remove_anunasik_akshar(word):
    """
    Removes anunāsika characters from a single word and replaces them with 'इत्'.

    Parameters:
        word (str): The input word to process.

    Returns:
        str: The word with anunāsika characters replaced by 'इत्'.
    """
    anunasik_akshar = ['अँ', 'आँ', 'इँ', 'ईँ', 'उँ', 'ऊँ', 'ऋँ', 'ॠँ', 'ऌँ', 'ॡँ', 'एँ', 'ओँ', 'ऐँ', 'औँ']
    for akshar in anunasik_akshar:
        word = word.replace(akshar, 'इत्')
    return word


def categorize_dhatu(dhatu_list):
    """
    Categorizes a list of dhatus by identifying their unique features and patterns.

    Parameters:
        dhatu_list (list): A list of dhatu words.

    Returns:
        dict: A dictionary categorizing dhatus into processed and anunasik-containing categories.
    """
    anunasik_dhatu = []
    processed_dhatu = []

    for dhatu in dhatu_list:
        if any(char in dhatu for char in ['ँ', 'ं', 'ः']):  # Check for anunāsika markers
            anunasik_dhatu.append(dhatu)
        processed_dhatu.append(remove_anunasik_akshar(dhatu))

    return {
        "Anunāsika_Dhatus": anunasik_dhatu,
        "Processed_Dhatus": processed_dhatu
    }


def process_word_list(word_list):
    """
    Processes a list of words, replacing all anunāsika characters with 'इत्'.

    Parameters:
        word_list (list): A list of words to process.

    Returns:
        list: A list with processed words containing 'इत्' replacements.
    """
    return [remove_anunasik_akshar(word) for word in word_list]


# Example Input
dhatu_upadesh = ['भू', 'एधँ', 'स्पर्धँ', 'गाधृँ', 'बाधृँ', 'नाधृँ', 'नाथृँ', 'दधँ', 'स्कुदिँ', 'श्विदिँ']

# Step 1: Categorize and Process Dhatus
categorized_dhatus = categorize_dhatu(dhatu_upadesh)

# Step 2: Display Categorized Results
for category, words in categorized_dhatus.items():
    print(f"{category}: {', '.join(words)}")

# Additional Operations
processed_dhatus = process_word_list(dhatu_upadesh)
print("Processed Dhatus (Replacements Applied):")
print(processed_dhatus)
