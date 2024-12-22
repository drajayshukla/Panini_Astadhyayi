# Sanskrit word declension generator

def decline_word(word, suffixes):
    """
    Declines the given word based on the provided suffixes for different cases and numbers.

    :param word: The base form of the Sanskrit word
    :param suffixes: A dictionary containing the suffixes for different cases and numbers
    :return: A dictionary with the declined forms
    """
    declined_forms = {}

    for case, endings in suffixes.items():
        declined_forms[case] = [word[:-1] + ending for ending in endings]

    return declined_forms

# Suffixes for different cases and numbers for a masculine noun ending in 'a'
suffixes = {
    "प्रथमा (Nominative)": ["ः", "ौ", "ाः"],
    "द्वितीया (Accusative)": ["म्", "ौ", "ान्"],
    "तृतीया (Instrumental)": ["ेन", "आभ्याम्", "ैः"],
    "चतुर्थी (Dative)": ["ाय", "आभ्याम्", "ेभ्यः"],
    "पञ्चमी (Ablative)": ["ात्", "आभ्याम्", "ेभ्यः"],
    "षष्ठी (Genitive)": ["स्य", "योः", "ानाम्"],
    "सप्तमी (Locative)": ["े", "योः", "ेषु"],
    "सम्बोधनम् (Vocative)": ["", "ौ", "ाः"]
}

# Word input (choose from the image or any other Sanskrit word ending in 'a')
word = "रा"  # Replace with any word from the image

# Generate declined forms
declined_forms = decline_word(word, suffixes)

# Print the results
for case, forms in declined_forms.items():
    print(f"{case}: {', '.join(forms)}")
