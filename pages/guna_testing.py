import streamlit as st
from panini.modules.guna1_1_2 import get_guna_vowels, identify_guna_vowels, explain_guna
from panini.modules.separate_characters import separate_characters_and_map
from panini.modules.halant_handling import group_sanskrit_characters
from panini.modules.merging_in_list import merge_characters

# Guna mapping for vowels
guna_mapping = {
    'अ': 'अ',
    'इ': 'ए',
    'उ': 'ओ',
    'ऋ': 'अर्',
    'ए': 'ए',
    'ओ': 'ओ'
}


def apply_guna(char, guna_mapping):
    """Replace the given character with its Guna equivalent."""
    return guna_mapping.get(char, char)


# App title
st.title("Sanskrit Guna Transformation: Pāṇini's Grammar")

# Section 1: Retrieve Guna Vowels
st.header("Retrieve Guna Vowels")
guna_vowels = get_guna_vowels()
st.write("Guna Vowels:", guna_vowels)

# Section 2: Identify and Apply Guna to a Sanskrit String
st.header("Identify and Apply Guna to a Sanskrit String")
input_string = st.text_input("Enter a Sanskrit string (e.g., 'पितृ औ')", "पितृ औ")

if input_string:
    # Step 1: Separate characters
    separated_characters_raw = separate_characters_and_map(input_string)
    separated_characters = group_sanskrit_characters(separated_characters_raw)
    st.write("Separated Characters:", separated_characters)

    # Step 2: Display characters with indices
    st.subheader("Characters with Indices")
    for i, char in enumerate(separated_characters, start=1):
        st.write(f"{i}: {char}")

    # Step 3: User selects a character for Guna
    selected_index = st.number_input(
        "Select the index of the character to apply Guna:",
        min_value=1,
        max_value=len(separated_characters),
        step=1
    )

    # Step 4: Apply Guna transformation
    if st.button("Apply Guna"):
        selected_char = separated_characters[selected_index - 1]
        transformed_char = apply_guna(selected_char, guna_mapping)

        # Update the selected character
        separated_characters[selected_index - 1] = transformed_char

        # Display transformed characters
        st.write("Transformed Characters:", ''.join(separated_characters))

        # Step 5: Merge characters for final output
        merged_word = merge_characters(''.join(separated_characters))
        st.subheader("Final Merged Word")
        st.write(merged_word)

# Explanation of Guna
st.header("Explanation of Guna")
explanation = explain_guna()
st.write(explanation)

# Markdown Notes at the End
st.markdown("""
### Examples of Guna Application

#### Example 1: ऋतो ङिसर्वनामस्थानयोः (7.3.110)
- **Input**: पितृ + औ [प्रथमाद्विवचनस्य 'औ' प्रत्ययः]
- **Steps**:
    - पितृ + औ → पितर् + औ [ऋतो ङिसर्वनामस्थानयोः 7.3.110 इत्यनेन ऋकारस्य गुणः अकारः। उरण् रपरः 1.1.51 इति सः रपरः]
    - **Output**: पितरौ

#### Example 2: Other Transformations
- Use the app to experiment with other Guna transformations!
""")
