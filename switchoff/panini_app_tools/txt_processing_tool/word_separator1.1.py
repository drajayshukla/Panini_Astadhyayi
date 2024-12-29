import streamlit as st
import re
from panini.modules.mapping_akshar_separator1 import generate_mapping, separate_characters_and_map
#from sanskrit.mapping_akshar_separator1 import generate_mapping, separate_characters_and_map


def remove_last_characters(word, characters_to_remove):
    """Removes specified characters from the end of a word."""
    while word.endswith(tuple(characters_to_remove)):
        word = word[:-1]
    return word


def merge_characters(word):
    """Merges specific Devanagari characters in the word."""
    # Adjust character replacements for proper merging
    merged_word = word.replace("्ओ", "ो").replace("्औ", "ौ").replace("्आ", "ा").replace("्अ", "").replace(
        'शइ', 'शि').replace('कउ', 'कु').replace('म्औ', 'मौ').replace('म्ऐ', 'मै').replace('म्ए', 'मे').replace(
        'ष्उ', 'षु').replace('व्ए', 'वे').replace('व्ऐ', 'वै').replace('प्ऊ', 'पू').replace('त्ए', 'ते').replace(
        'त्ऐ', 'तै').replace('न्इ', 'नि').replace('र्ई', 'री')

    # Use regex to clean up invalid halant combinations
    merged_word = re.sub(r'([इईउऊएऐऔअं:])्', r'\1', merged_word)
    return merged_word


def main():
    st.title("Devanagari Akshar Separator and Processor")

    # Generate the mapping
    mapping = generate_mapping()

    # Input string
    input_string = st.text_area("Enter the Devanagari text:", "रमा", height=100)

    # Dropdown menu for characters to remove
    characters = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'ं', 'ः']
    characters_to_remove = st.multiselect(
        "Select characters to remove from the end of the word:",
        options=characters,
        default=['आ']
    )

    if st.button("Process"):
        # Step 1: Map Characters
        mapped_output = separate_characters_and_map(input_string, mapping)
        st.subheader("Mapped Characters:")
        st.text_area("Mapped Output:", mapped_output, height=150)

        # Step 2: Remove Last Characters
        processed_string = remove_last_characters(mapped_output, characters_to_remove)
        st.subheader(f"After Removing Selected Characters ({', '.join(characters_to_remove)}):")
        st.text_area("Processed Output:", processed_string, height=150)

        # Step 3: Merge Characters
        final_output = merge_characters(processed_string)
        st.subheader("Final Merged Output:")
        st.text_area("Final Output:", final_output, height=150)


if __name__ == "__main__":
    main()
