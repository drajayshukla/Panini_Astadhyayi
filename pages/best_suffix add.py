import streamlit as st
import re
from panini.modules.mapping_akshar_separator1 import generate_mapping, separate_characters_and_map


def remove_last_character(word):
    """Removes the last character from a word."""
    return word[:-1]


def merge_characters(word):
    """Merges specific Devanagari characters in the word."""
    merged_word = word.replace("्ओ", "ो").replace("्औ", "ौ").replace(":", ":").replace("्आ", "ा").replace("्अ",
                                                                                                          "").replace(
        'शइ', 'शि').replace('कउ', 'कु').replace(':', ':').replace('म्औ', 'मौ').replace('म्', 'म्').replace('न्',
                                                                                                           'न्').replace(
        'म्ऐ', 'मै').replace('म्ए', 'मे').replace('त्', 'त्').replace('ष्उ', 'षु').replace('व्ए', 'वे') \
        .replace('व्ऐ', 'वै').replace('प्ऊ', 'पू').replace('त्ए', 'ते').replace('त्ऐ', 'तै').replace('न्इ',
                                                                                                     'नि').replace(
        'र्ई', 'री')
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

        # Step 2: Remove Last Character
        processed_string = remove_last_character(mapped_output)
        st.subheader("After Removing the Last Character:")
        st.text(processed_string)

        # Step 3: Add Suffixes
        suffix_lists = [
            ['आ11', 'ए12', 'आ:13'],
            ['अया31', 'आभ्य्आम्32', 'आभि:33'],
            ['आयै41', 'आभ्य्आम्42', 'आभ्य्अ:43'],
            ['ईः_11', 'य्औ_12', 'य्ः_13', 'य्अम्_21', 'य्औ_22', 'य्ः_23', 'य्आ_31', 'ईभ्य्आम्_32', 'ईभ्इः_33', 'य्ए_41',
             'ईभ्य्आम्_42', 'ईभ्य्ः_43', 'य्उः_51', 'ईभ्य्आम्_52', 'ईभ्य्ः_53', 'य्उः_61', 'य्ओः_62', 'य्आम्_63',
             'य्इ_71',
             'य्ओः_72', 'ईष्उ_73'],['ईः_11', 'य्औ_12', 'य्ः_13', 'य्अम्_21', 'य्औ_22', 'य्ः_23', 'य्आ_31', 'ईभ्य्आम्_32', 'ईभ्इः_33', 'य्ए_41', 'ईभ्य्आम्_42', 'ईभ्य्ः_43', 'य्उः_51', 'ईभ्य्आम्_52', 'ईभ्य्ः_53', 'य्उः_61', 'य्ओः_62', 'य्आम्_63', 'य्इ_71', 'य्ओः_72', 'ईष्उ_73']
        ]

        # Flatten the list of suffixes
        all_suffixes = [suffix for suffix_list in suffix_lists for suffix in suffix_list]

        # Append suffixes to the processed string
        output_string = ", ".join([processed_string + suffix for suffix in all_suffixes])

        st.subheader("After Adding Suffixes:")
        st.text(output_string)

        # Step 4: Merge Characters
        words = re.split(r',\s*', output_string)
        words = [re.sub(r'^\W+|\W+$', '', word) for word in words]
        merged_outputs = " , ".join([merge_characters(word) for word in words])
        st.subheader("Final Merged Output:")
        st.text(merged_outputs)


if __name__ == "__main__":
    main()
