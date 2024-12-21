def modify_cleaned_strings(cleaned_strings):
    if cleaned_strings:
        first_word = cleaned_strings[0]

        # Check and replace the last character if needed
        if first_word.endswith("इ"):
            first_word = first_word[:-1] + "ए"
        elif first_word.endswith("ई"):
            first_word = first_word[:-1] + "ए"
        elif first_word.endswith("उ"):
            first_word = first_word[:-1] + "ओ"
        elif first_word.endswith("ऊ"):
            first_word = first_word[:-1] + "ओ"
        elif first_word.endswith("ऋ"):
            first_word = first_word[:-1] + "अर्"
        elif first_word.endswith("ॠ"):
            first_word = first_word[:-1] + "अर्"

        # Modify the cleaned strings list
        cleaned_strings[0] = first_word

'''modify_cleaned_strings(cleaned_strings)
print('7:1:84=सार्वधातुक-आर्धधातुकयोः=सार्वधातुके आर्धधातुके च प्रत्यये परे इगन्तस्य अङ्गस्य गुणादेशः भवति ')
print("Modified Cleaned Strings:", cleaned_strings)'''

