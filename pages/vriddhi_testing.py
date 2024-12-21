import streamlit as st
from panini.modules.vriddhi1_1_1 import get_vriddhi_vowels, identify_vriddhi_vowels, explain_vriddhi
from panini.modules.separate_characters import separate_characters_and_map
from panini.modules.halant_handling import group_sanskrit_characters

# Title of the app
st.title("Vriddhi Testing: Pāṇini's Grammar")

# Section 1: Retrieve Vriddhi Vowels
st.header("Retrieve Vriddhi Vowels")
vriddhi_vowels = get_vriddhi_vowels()
st.write("Vriddhi Vowels:", vriddhi_vowels)

# Section 2: Identify Vriddhi Vowels in Input
st.header("Identify Vriddhi Vowels in a String")
input_string = st.text_input("Enter a string (e.g., 'रामः शैवः गौरवः')", "रामः शैवः गौरवः")

if input_string:
    # Step 1: Separate characters using separate_characters_and_map
    separated_characters = separate_characters_and_map(input_string)
    st.write("Separated Characters:", separated_characters)

    # Step 2: Identify Vriddhi vowels from the separated characters
    found_vowels = [char for char in separated_characters if char in vriddhi_vowels]
    st.write("Found Vriddhi Vowels:", found_vowels)

# Section 3: Explanation of Vriddhi
st.header("Explanation of Vriddhi")
explanation = explain_vriddhi()
st.write(explanation)
#import streamlit as st
#from panini.modules.separate_characters import separate_characters_and_map


import streamlit as st

from panini.modules.separate_characters import separate_characters_and_map

# Vriddhi mapping for vowels
vriddhi_mapping = {
    'अ': 'आ',
    'इ': 'ऐ',
    'उ': 'औ',
    'ऋ': 'अर्',
    'ए': 'ऐ',
    'ओ': 'औ'
}


def apply_vriddhi(char, vriddhi_mapping):
    """Replace the given character with its Vriddhi equivalent."""
    return vriddhi_mapping.get(char, char)


# App title
st.title("Sanskrit Vriddhi Transformation")

# Input string
input_string = st.text_input("Enter a Sanskrit string (e.g., 'पठ् घञ्')", "पठ् घञ्")
if input_string:
    # Step 1: Separate characters using separate_characters_and_map
    separated_characters1 = separate_characters_and_map(input_string)
    st.write("Separated Characters:", separated_characters1)
    separated_characters=group_sanskrit_characters(separated_characters1)
    # Display the characters with their indices
    for i, char in enumerate(separated_characters, start=1):
        st.write(f"{i}: {char}")

    # Step 2: Let the user select a character index
    selected_index = st.number_input(
        "Enter the index of the character to apply Vriddhi:",
        min_value=1,
        max_value=len(separated_characters),
        step=1
    )

    # Step 3: Apply Vriddhi transformation
    if st.button("Apply Vriddhi"):
        selected_char = separated_characters[selected_index - 1]
        transformed_char = apply_vriddhi(selected_char, vriddhi_mapping)

        # Update the character in the list
        separated_characters[selected_index - 1] = transformed_char

        # Display the transformed characters
        st.write("Transformed Characters:", ''.join(separated_characters))


