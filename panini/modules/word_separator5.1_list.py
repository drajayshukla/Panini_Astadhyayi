import streamlit as st
import re
from sanskrit.mapping_akshar_separator1 import generate_mapping, separate_characters_and_map


def remove_last_characters(word):
    characters_to_remove = ['आ']
    while word.endswith(tuple(characters_to_remove)):
        word = word[:-1]
    return word


def merge_characters(word):
    merged_word = word.replace("्ओ", "ो").replace("्औ", "ौ").replace(":", ":").replace("्आ", "ा").replace("्अ",
                                                                                                          "").replace(
        'शइ', 'शि').replace('कउ', 'कु').replace(':', ':').replace('म्औ', 'मौ').replace('म्', 'म्').replace('न्',
                                                                                                           'न्').replace(
        'म्ऐ', 'मै').replace('म्ए', 'मे').replace('त्', 'त्').replace('ष्उ', 'षु').replace('व्ए', 'वे') \
        .replace('व्ऐ', 'वै').replace('प्ऊ', 'पू').replace('त्ए', 'ते').replace('त्ऐ', 'तै').replace('न्इ', 'नि')
    merged_word = re.sub(r'([इईउऊएऐऔअंअ:])्', r'\1', merged_word)
    return merged_word


def main():
    st.title("Devanagari Akshar Separator and Processor")

    # Generate the mapping
    mapping = generate_mapping()

    # Input string
    input_string = st.text_area("Enter the Devanagari text:", "रमा")

    if st.button("Process"):
        # Step 1: Map Characters
        mapped_output = separate_characters_and_map(input_string, mapping)
        st.subheader("Mapped Characters:")
        st.text(mapped_output)

        # Step 2: Remove Last Characters
        processed_string = remove_last_characters(mapped_output)
        st.subheader("After Removing Last Characters (आ):")
        st.text(processed_string)

        # Step 3: Characters to Add (User Input)
        user_input = st.text_area("Enter characters to add (comma-separated):",
                                  "आ11, ए12, आ:13, आम्21, ए22, आ:23")
        characters_to_add = [char.strip() for char in user_input.split(",")]

        output_string = ", ".join([processed_string + char for char in characters_to_add])
        st.subheader("Characters Added:")
        st.text(output_string)

        # Step 4: Merge Characters
        words = re.split(r',\s*', output_string)
        words = [re.sub(r'^\W+|\W+$', '', word) for word in words]
        merged_outputs = " , ".join([merge_characters(word) for word in words])
        st.subheader("Final Merged Output:")
        st.text(merged_outputs)


if __name__ == "__main__":
    main()
