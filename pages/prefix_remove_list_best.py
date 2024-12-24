import streamlit as st


def generate_mapping():
    mapping = {}
    base_consonants = [
        'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ',
        'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
        'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श',
        'ष', 'स', 'ह'
    ]
    matras = {
        '': 'अ', 'ा': 'आ', 'ि': 'इ', 'ी': 'ई', 'ु': 'उ', 'ू': 'ऊ',
        'े': 'ए', 'ै': 'ऐ', 'ो': 'ओ', 'ौ': 'औ', 'ं': 'ं',
        'ः': 'ः', 'ृ': 'ऋ', 'ॄ': 'ॠ', 'ॢ': 'ऌ', 'ॣ': 'ॡ',
    }
    for consonant in base_consonants:
        for matra, vowel in matras.items():
            key = consonant + matra
            value = consonant + '्' + vowel
            mapping[key] = value
    special_combinations = {'क्ष': 'क्' + 'ष', 'त्र': 'त्' + 'र', 'ज्ञ': 'ज्' + 'ञ'}
    mapping.update(special_combinations)
    for consonant in base_consonants:
        mapping[consonant + '्'] = consonant + '्'
    return mapping


def separate_characters_and_map(input_string, mapping):
    output = ''
    i = 0
    while i < len(input_string):
        if i + 2 <= len(input_string) and input_string[i:i + 2] in mapping:
            output += mapping[input_string[i:i + 2]]
            i += 2
        elif input_string[i] in mapping:
            output += mapping[input_string[i]]
            i += 1
        else:
            output += input_string[i]
            i += 1
    return output


def prefix_removal(strings, prefix):
    return {i: value.replace(prefix, "") for i, value in enumerate(strings)}


def main():
    st.title("Integrated Devanagari Word Processor")

    # Generate mapping
    mapping = generate_mapping()

    # First Step: Devanagari Word Processing
    st.header("Step 1: Devanagari Word Mapping")
    input_text = st.text_area("Enter Devanagari words (comma-separated):", "शम्भुः, शम्भू, शम्भवः")
    delimiter = st.radio("Select delimiter:", ["comma", "semicolon"], index=0)
    word_list = input_text.split(",") if delimiter == "comma" else input_text.split(";")

    word_list = [word.strip() for word in word_list if word.strip()]

    if st.button("Process Words"):
        if word_list:
            processed_words = [separate_characters_and_map(word, mapping) for word in word_list]
            st.subheader("Processed Words")
            st.write(processed_words)
            st.session_state["processed_words"] = processed_words
        else:
            st.error("Please enter words to process.")

    # Second Step: Prefix Removal
    if "processed_words" in st.session_state:
        st.header("Step 2: Remove Prefix")
        prefix = st.text_input("Enter prefix to remove:", "श्अम्भ्")
        processed_words = st.session_state["processed_words"]


        if st.button("Remove Prefix"):
            # Call the function to remove prefixes
            modified_dict = prefix_removal(processed_words, prefix)

            # Display output as a dictionary (JSON format)
            st.subheader("Modified Dictionary")
            st.json(modified_dict)

            # Convert the dictionary values to a Python list
            modified_list = list(modified_dict.values())

            # Display output as a Python list
            st.subheader("Modified Python List")
            st.text(modified_list)


if __name__ == "__main__":
    main()
