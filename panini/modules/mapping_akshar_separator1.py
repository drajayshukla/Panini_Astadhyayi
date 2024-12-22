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
    Streamlit app to generate the mapping and process user input.
    """
    st.title("Devanagari Character Mapping")

    # Generate the mapping
    mapping = generate_mapping()

    # User input
    input_string = st.text_area("Enter the Devanagari text to process:", "")

    # Process and display output if input is provided
    if input_string:
        output_string = separate_characters_and_map(input_string, mapping)
        st.subheader("Mapped Output:")
        st.text(output_string)


# Run the Streamlit app
if __name__ == "__main__":
    main()
