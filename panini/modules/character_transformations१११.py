# Base mapping for consonants with inherent 'अ'
base_consonants = [
    ('क', 'क्'), ('ख', 'ख्'), ('ग', 'ग्'), ('घ', 'घ्'), ('ङ', 'ङ्'),
    ('च', 'च्'), ('छ', 'छ्'), ('ज', 'ज्'), ('झ', 'झ्'), ('ञ', 'ञ्'),
    ('ट', 'ट्'), ('ठ', 'ठ्'), ('ड', 'ड्'), ('ढ', 'ढ्'), ('ण', 'ण्'),
    ('त', 'त्'), ('थ', 'थ्'), ('द', 'द्'), ('ध', 'ध्'), ('न', 'न्'),
    ('प', 'प्'), ('फ', 'फ्'), ('ब', 'ब्'), ('भ', 'भ्'), ('म', 'म्'),
    ('य', 'य्'), ('र', 'र्'), ('ल', 'ल्'), ('व', 'व्'), ('श', 'श्'),
    ('ष', 'ष्'), ('स', 'स्'), ('ह', 'ह्')
]

# Vowel diacritics mapping
vowel_diacritics = {
    'अ': '', 'ा': 'ा', 'ि': 'ि', 'ी': 'ी', 'ु': 'ु', 'ू': 'ू',
    'े': 'े', 'ै': 'ै', 'ो': 'ो', 'ौ': 'ौ', 'ं': 'ं', 'ः': 'ः',
    'ृ': 'ृ', 'ॄ': 'ॄ', 'ॢ': 'ॢ'
}

# Generate the mapping dynamically
mapping = {}
for consonant, half_consonant in base_consonants:
    for vowel, diacritic in vowel_diacritics.items():
        if vowel == 'अ':
            # Map consonant without diacritic when vowel is 'अ'
            mapping[consonant] = half_consonant + 'अ'
        else:
            # Map consonant with diacritic for other vowels
            mapping[consonant + vowel] = half_consonant + diacritic

# Add special consonant clusters
special_clusters = {
    'क्ष': 'क्' + 'ष', 'त्र': 'त्' + 'र', 'ज्ञ': 'ज्' + 'ञ'
}
mapping.update(special_clusters)

def transform_text(input_text):
    transformed_word = ""
    i = 0
    while i < len(input_text):
        char = input_text[i]
        # Check for special consonant cluster
        if i < len(input_text) - 1 and (char + input_text[i + 1]) in mapping:
            transformed_word += mapping[char + input_text[i + 1]]
            i += 2
        # Check for vowel diacritic after consonant
        elif char in mapping and i < len(input_text) - 1 and input_text[i + 1] in vowel_diacritics:
            transformed_word += mapping[char + input_text[i + 1]]
            i += 2
        # Handle single consonants or non-matching characters
        elif char in mapping:
            transformed_word += mapping[char]
            i += 1
        else:
            transformed_word += char
            i += 1
    return transformed_word

# Main loop
while True:
    user_input = input("Enter characters (or ';;' to exit): ")
    if user_input == ";;":
        break

    result = transform_text(user_input)
    print("Transformed word:", result)
