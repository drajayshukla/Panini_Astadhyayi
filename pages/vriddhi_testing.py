import streamlit as st
from panini.modules.vriddhi1_1_1 import get_vriddhi_vowels, identify_vriddhi_vowels, explain_vriddhi
from panini.modules.separate_characters import separate_characters_and_map
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

# Vriddhi mapping for vowels
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

# Separate characters
if input_string:
    separated_chars = separate_characters_and_map(input_string)
    # Ensure separated_chars is a list
    separated_chars = list(separated_chars)

    indexed_chars = [(i, char) for i, char in enumerate(separated_chars, start=1)]
    st.write("Separated Characters with Indices:")
    for index, char in indexed_chars:
        st.write(f"{index}: {char}")

    # Character index selection
    selected_index = st.number_input(
        "Enter the index of the character to apply Vriddhi (e.g., 2):",
        min_value=1,
        max_value=len(separated_chars),
        step=1
    )

    # Get the character based on index
    if selected_index:
        char_to_vriddhi = separated_chars[selected_index - 1]
        st.write(f"Selected Character: '{char_to_vriddhi}'")

        # Check if the character can have Vriddhi
        if char_to_vriddhi in vriddhi_mapping:
            transformed_char = apply_vriddhi(char_to_vriddhi, vriddhi_mapping)
            st.write(f"The character '{char_to_vriddhi}' is replaced with its Vriddhi equivalent: '{transformed_char}'")

            # Modify the list of characters
            transformed_chars = separated_chars[:]  # Create a copy of the list
            transformed_chars[selected_index - 1] = transformed_char
            transformed_string = ''.join(transformed_chars)
            st.write("Transformed String:", transformed_string)
        else:
            st.write(f"The character '{char_to_vriddhi}' does not have a Vriddhi equivalent.")
