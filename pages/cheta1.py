import streamlit as st
from panini.modules.separate_characters import separate_characters_and_map
from panini.modules.halantayam_list import remove_last_characters
from panini.modules.adengaguna import modify_cleaned_strings
from panini.modules.upadha_deergh import apply_last_character_rules
from panini.modules.merging_in_list import merge_characters
from panini.modules.nalop_pratipadak import remove_last_character_if_needed

# Function to replace the last occurrence of a substring
def replace_last_occurrence(word, old_char, new_chars):
    reversed_word = word[::-1]
    reversed_new_chars = new_chars[::-1]
    replaced_word = reversed_word.replace(old_char[::-1], reversed_new_chars, 1)
    return replaced_word[::-1]

def run():
    st.title("Cheta: Character and Rule Processing")
    st.write("Explore Pāṇini's grammatical rules step-by-step.")

    # Input Section
    st.header("Input Section")
    input_string = st.text_input("Enter a string (e.g., 'चिञ् तृच्')", "चिञ् तृच्")

    if input_string:
        st.subheader("Input String")
        st.write(input_string)

        # Step 1: Character Separation
        output_string = separate_characters_and_map(input_string)
        st.subheader("Step 1: Character Separation")
        st.write(output_string)

        # Step 2: Halantayam Processing
        input_strings = output_string.split(" ")
        cleaned_strings = remove_last_characters(input_strings)
        st.subheader("Step 2: Halantayam Processing")
        st.write(cleaned_strings)

        # Step 3: Modify Cleaned Strings
        modify_cleaned_strings(cleaned_strings)
        st.subheader("Step 3: Modify Cleaned Strings")
        st.write(cleaned_strings)

        # Step 4: Add 'स्' and Replace 'ऋ' with 'अन्'
        cleaned_strings.append("स्")
        second_word = cleaned_strings[1]
        if 'ऋ' in second_word:
            modified_second_word = replace_last_occurrence(second_word, 'ऋ', 'अन्')
            cleaned_strings[1] = modified_second_word
        st.subheader("Step 4: Add 'स्' and Replace 'ऋ'")
        st.write(cleaned_strings)

        # Step 5: Apply Upadha Deergh Rules
        cleaned_strings[1] = apply_last_character_rules(cleaned_strings[1])
        st.subheader("Step 5: Apply Upadha Deergh Rules")
        st.write(cleaned_strings)

        # Step 6: Remove 'सुँ'
        cleaned_strings = cleaned_strings[:-1]
        st.subheader("Step 6: Remove 'सुँ'")
        st.write(cleaned_strings)

        # Step 7: Merge Characters
        merged_word = merge_characters(''.join(cleaned_strings))
        st.subheader("Step 7: Merge Characters")
        st.write(merged_word)

        # Step 8: Apply Nalop Rules
        output = remove_last_character_if_needed(merged_word)
        st.subheader("Step 8: Apply Nalop Rules")
        st.write(output)

        # Final Output
        st.header("Final Output")
        st.write(output)

if __name__ == "__main__":
    run()
