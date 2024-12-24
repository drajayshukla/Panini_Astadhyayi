import streamlit as st

def generate_mapping():
    """
    Generates the complete mapping of Devanagari base consonants with their matras.
    Returns:
        dict: A dictionary containing mappings for Devanagari characters.
    """
    mapping = {}

    # Define base consonants (without implicit 'अ')
    base_consonants = [
        'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ',
        'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
        'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श',
        'ष', 'स', 'ह'
    ]

    # Define matras (vowel signs)
    matras = {
        '': 'अ',  # Implicit vowel
        'ा': 'आ',
        'ि': 'इ',
        'ी': 'ई',
        'ु': 'उ',
        'ू': 'ऊ',
        'े': 'ए',
        'ै': 'ऐ',
        'ो': 'ओ',
        'ौ': 'औ',
        'ं': 'ं',
        'ः': 'ः',
        'ृ': 'ऋ',
        'ॄ': 'ॠ',
        'ॢ': 'ऌ',
        'ॣ': 'ॡ',
    }

    # Generate mapping for consonants + matras
    for consonant in base_consonants:
        for matra, vowel in matras.items():
            key = consonant + matra
            value = consonant + '्' + vowel
            mapping[key] = value

    # Add special combinations
    special_combinations = {
        'क्ष': 'क्' + 'ष',
        'त्र': 'त्' + 'र',
        'ज्ञ': 'ज्' + 'ञ'
    }
    mapping.update(special_combinations)

    # Add halant consonants (standalone without vowels)
    for consonant in base_consonants:
        mapping[consonant + '्'] = consonant + '्'

    return mapping


def separate_characters_and_map(input_string, mapping):
    """
    Separates characters in the input string and maps them using the provided mapping.

    Args:
        input_string (str): The string to process.
        mapping (dict): The mapping dictionary.

    Returns:
        str: The processed string with characters separated and mapped.
    """
    output = ''
    i = 0
    while i < len(input_string):
        # Check for two-character matches in the mapping
        if i + 2 <= len(input_string) and input_string[i:i + 2] in mapping:
            output += mapping[input_string[i:i + 2]]
            i += 2
        # Check for single-character matches in the mapping
        elif input_string[i] in mapping:
            output += mapping[input_string[i]]
            i += 1
        # Handle unmatched characters (pass through as is)
        else:
            output += input_string[i]
            i += 1
    return output


def main():
    """
    Streamlit app to process a user-provided list of Devanagari words.
    """
    st.title("Devanagari Word List Processor")

    # Generate the mapping
    mapping = generate_mapping()

    # User input for a list of words
    input_text = st.text_area(
        "Enter a list of Devanagari words (separated by newline, comma, or space):",
        "शम्भुः, शम्भू, शम्भवः"
    )

    # Input processing: split into a list of words
    delimiter = st.radio("Select the delimiter for your input:", options=["newline", "comma", "space"], index=1)
    if delimiter == "newline":
        word_list = input_text.split("\n")
    elif delimiter == "comma":
        word_list = input_text.split(",")
    elif delimiter == "space":
        word_list = input_text.split()

    # Clean up any extra spaces in the input
    word_list = [word.strip() for word in word_list if word.strip()]

    if st.button("Process"):
        if word_list:
            st.subheader("Original Word List:")
            st.write(word_list)

            # Process each word in the list
            processed_words = [separate_characters_and_map(word, mapping) for word in word_list]

            st.subheader("Processed Word List:")
            st.write(processed_words)

            # Optional: Display side-by-side comparison
            st.subheader("Comparison of Original and Processed Words:")
            for original, processed in zip(word_list, processed_words):
                st.write(f"**Original:** {original} → **Processed:** {processed}")
        else:
            st.error("Please enter at least one word to process.")


if __name__ == "__main__":
    main()
