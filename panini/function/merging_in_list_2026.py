import re

def merge_characters(word):
    """
    Merges all possible Devanagari character combinations to ensure proper rendering.

    Args:
        word (str): A string with Devanagari text to process.

    Returns:
        str: The string with merged Devanagari characters.
    """
    # Specific replacements for vowel modifiers and combinations
    replacements = [
        ("्ओ", "ो"), ("्औ", "ौ"), ("्आ", "ा"), ("्अ", ""), ("्इ", "ि"), ("्ई", "ी"),
        ("्उ", "ु"), ("्ऊ", "ू"), ("्ऋ", "ृ"), ("्ए", "े"), ("्ऐ", "ै")
    ]

    for pattern, replacement in replacements:
        word = word.replace(pattern, replacement)

    # Handle halant and consonant clusters correctly
    word = re.sub(r'([क-ह])्([क-ह])', r'\1्\2', word)  # Preserve halant clusters
    word = re.sub(r'([क-ह])्$', r'\1्', word)  # Preserve trailing halants
    word = re.sub(r'([क-ह])्ँ', r'\1ं', word)  # Handle nasalization
    word = re.sub(r'([क-ह])्([इईउऊऋएऐओऔ])', r'\1\2', word)  # Merge consonants with vowels

    return word

# Process a list of words
#words = ['स्फ्ऊर्ज्', 'क्ऊमार', 'म्एत्र', 'ञ्इज्ञ', 'ट्उप']
#merged_words = [merge_characters(word) for word in words]
#print(merged_words)
