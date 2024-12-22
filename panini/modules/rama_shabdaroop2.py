import streamlit as st
import re
from sanskrit.mapping_akshar_separator1 import generate_mapping, separate_characters_and_map


def remove_last_characters(word, characters_to_remove):
    """Removes specified characters from the end of a word."""
    while word.endswith(tuple(characters_to_remove)):
        word = word[:-1]
    return word


def merge_characters(word):
    """Merges specific Devanagari characters in the word."""
    merged_word = word.replace("्ओ", "ो").replace("्औ", "ौ").replace(":", ":").replace("्आ", "ा").replace("्अ",
                                                                                                          "").replace(
        'शइ', 'शि').replace('कउ', 'कु').replace(':', ':').replace('म्औ', 'मौ').replace('म्', 'म्').replace('न्',
                                                                                                           'न्').replace(
        'म्ऐ', 'मै').replace('म्ए', 'मे').replace('त्', 'त्').replace('ष्उ', 'षु').replace('व्ए', 'वे') \
        .replace('व्ऐ', 'वै').replace('प्ऊ', 'पू').replace('त्ए', 'ते').replace('त्ऐ', 'तै').replace('न्इ', 'नि').replace('र्ई', 'री')
    merged_word = re.sub(r'([इईउऊएऐऔअंअ:])्', r'\1', merged_word)
    return merged_word


def main():
    st.title("Devanagari Akshar Separator and Processor")

    # Generate the mapping
    mapping = generate_mapping()

    # Input string
    input_string = st.text_area("Enter the Devanagari text:", "रमा")

    # Dropdown menu for characters to remove
    characters = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ']
    characters_to_remove = st.multiselect(
        "Select characters to remove from the end of the word:",
        options=characters,
        default=['आ']
    )

    if st.button("Process"):
        # Step 1: Map Characters
        mapped_output = separate_characters_and_map(input_string, mapping)
        st.subheader("Mapped Characters:")
        st.text(mapped_output)

        # Step 2: Remove Last Characters
        processed_string = remove_last_characters(mapped_output, characters_to_remove)
        st.subheader(f"After Removing Selected Characters ({', '.join(characters_to_remove)}):")
        st.text(processed_string)

        # Step 3: Add Characters
        if characters_to_remove == ['आ']:
            characters_to_add = [
                'आ11', 'ए12', 'आ:13', 'आम्21', 'ए22', 'आ:23', 'अया31', 'आभ्य्आम्32', 'आभि:33',
                'आयै41', 'आभ्य्आम्42', 'आभ्य्अ:43', 'आया:51', 'आभ्य्आम्52', 'आभ्य्अ:53', 'आया:61',
                'अय्ओ:62', 'आन्आम्63', 'आयाम्71', 'अय्ओ:72', 'आनु73', 'ए13=sarva', 'अस्मै41=sarva',
                'अस्मात्51=sarva', 'एषाम्63=sarva', 'अस्मिन्71=sarva', 'अम्11-21=gyan',
                'ए12-22=gyan', 'आनि13-23=gyan', 'एन31=gyan'
            ]
        elif characters_to_remove == ['अ']:
            characters_to_add = [
                'अ:11', 'औ12', 'आ:13', 'अम्21', 'औ22', 'आन्23', 'एण्अ31', 'आभ्य्आम्32', 'ऐ:33',
                'आय्अ41', 'आभ्य्आम्42', 'एभ्य्अ:43', 'आत्51', 'आभ्य्आम्52', 'एभ्य्अ:53',
                'अस्य्अ61', 'अय्ओ:62', 'आण्आम्63', 'ए71', 'अय्ओ:72', 'एष्उ73', 'ए13=sarva',
                'अस्मै41=sarva', 'अस्मात्51=sarva', 'एषाम्63=sarva', 'अस्मिन्71=sarva',
                'अम्11-21=gyan', 'ए12-22=gyan', 'आनि13-23=gyan', 'एन31=gyan'
            ]
        elif characters_to_remove == ['ई']:
            characters_to_add = [
                'ई11', 'यौ12', 'यः13', 'ईम्21', 'यौ22', 'ईः23',
                'या31', 'ईभ्याम्32', 'ईभिः33', 'यै41', 'ईभ्याम्42', 'ईभ्यः43',
                'याः51', 'ईभ्याम्52', 'ईभ्यः53', 'याः61', 'योः62', 'ईणाम्63',
                'याम्71', 'योः72', 'ईषु73'
            ]
        else:
            characters_to_add = []

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
