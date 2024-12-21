import re

def merge_characters(word):
    """
    Merge characters in a word to form correct Sanskrit words by handling
    combinations of vowels, consonants, and special cases.

    :param word: Input word as a string
    :return: Merged word with proper character combinations
    """
    # Define specific mappings for common combinations
    mappings = {
        "्ओ": "ो",
        "्औ": "ौ",
        "्आ": "ा",
        "्अ": "",
        "शइ": "शि",
        "कउ": "कु",
        "म्औ": "मौ",
        "म्ऐ": "मै",
        "म्ए": "मे",
        "ष्उ": "षु",
        "व्ए": "वे",
        "व्ऐ": "वै",
        "प्ऊ": "पू",
        "त्ए": "ते",
        "त्ऐ": "तै",
        "न्इ": "नि",
        "च्ए": "चे",
        "न्ए": "ने",
        "व्इ": "वि",
        "र्इ": "रि",
        "त्इ": "ति",
        "ज्ए": "जे",
        "य्ए": "ये",
        "य्उ": "यु",
        "क्ऋ": "कृ",
        "प्इ": "पि",
        "ग्उ": "गु",
        "द्ए": "दे",
        "न्उ": "नु",
        "स्उ": "सु"
    }

    # Apply specific mappings first
    for key, value in mappings.items():
        word = word.replace(key, value)

    # Handle cases where a halant (्) is followed by a vowel or special symbol
    word = re.sub(r'([इईउऊएऐऔअंअ:])्', r'\1', word)

    # Handle trailing halant (e.g., "क्" to "क")
    word = re.sub(r'(.्)$', r'\1', word)

    # Additional rules can be added here if needed

    return word

# Example Usage
if __name__ == "__main__":
    example_word = "प्अठ्उ"
    merged_word = merge_characters(example_word)
    print("Merged Word:", merged_word)
