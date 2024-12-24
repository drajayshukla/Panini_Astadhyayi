import streamlit as st

def generate_mapping():
    """
    Generates the complete mapping of Devanagari base consonants with their matras.
    """
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
    """
    Separates characters and maps them using the provided mapping.
    """
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

def find_common_prefix(words):
    """
    Finds the common prefix among a list of words.
    """
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

def prefix_removal(strings, prefix):
    """
    Removes the prefix from each string in the list.
    """
    return {i: value.replace(prefix, "") for i, value in enumerate(strings)}

def main():
    st.title("Integrated Devanagari Word Processor")

    # Generate the mapping
    mapping = generate_mapping()

    # Step 1: Devanagari Word Mapping
    st.header("Step 1: Devanagari Word Mapping")
    input_text = st.text_area(
        "Enter Devanagari words separated by a delimiter (e.g., ';')",
        "परमक्रीः;परमक्र्यौ;परमक्र्यः;परमक्र्यम्;परमक्र्यौ;परमक्र्यः;परमक्र्या;परमक्रीभ्याम्;परमक्रीभिः;परमक्र्ये;परमक्रीभ्याम्;परमक्रीभ्यः;परमक्र्यः;परमक्रीभ्याम्;परमक्रीभ्यः;परमक्र्यः"
    )
    delimiter = st.radio("Select delimiter:", [";", ","], index=0)

    if st.button("Process Words"):
        word_list = [word.strip() for word in input_text.split(delimiter) if word.strip()]
        if word_list:
            processed_words = [separate_characters_and_map(word, mapping) for word in word_list]
            st.subheader("Mapped Output")
            st.text_area("Output:", ";".join(processed_words), height=200)
            st.session_state["processed_words"] = processed_words
        else:
            st.error("Please enter valid words.")

    # Step 2: Common Word Unit Finder
    if "processed_words" in st.session_state:
        st.header("Step 2: Common Word Unit Finder")
        output_text = ";".join(st.session_state["processed_words"])
        st.text_area("Mapped Output from Step 1:", output_text, height=200)
        delimiter = st.text_input("Enter the delimiter used in the text:", ";")
        if st.button("Find Common Word Unit"):
            words = [word.strip() for word in output_text.split(delimiter) if word.strip()]
            common_prefix = find_common_prefix(words)
            if common_prefix:
                st.success(f"The common word unit is: {common_prefix}")
                st.session_state["common_prefix"] = common_prefix
            else:
                st.warning("No common word unit found!")

    # Step 3: Remove Prefix
    if "common_prefix" in st.session_state:
        st.header("Step 3: Remove Prefix")
        prefix = st.text_input("Enter prefix to remove:", st.session_state["common_prefix"])
        processed_words = st.session_state.get("processed_words", [])
        if st.button("Remove Prefix"):
            modified_dict = prefix_removal(processed_words, prefix)
            st.subheader("Modified Dictionary")
            st.json(modified_dict)
            st.subheader("Modified Python List")
            st.text(list(modified_dict.values()))

if __name__ == "__main__":
    main()
