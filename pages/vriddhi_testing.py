import streamlit as st
from panini.modules.vriddhi1_1_1 import get_vriddhi_vowels, identify_vriddhi_vowels, explain_vriddhi
from panini.modules.separate_characters import separate_characters_and_map
from panini.modules.halant_handling import group_sanskrit_characters
from panini.modules.merging_in_list import merge_characters
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
        merged_word = merge_characters(''.join(separated_characters))
        st.subheader("Step 7: Merge Characters")
        st.write(merged_word)


# Add Markdown Notes at the End
st.markdown("""
### Examples of Vriddhi Application

#### Example 1: अत उपधायाः (7.2.116)
- **Input**: पठ् + घञ् [कृत्संज्ञकः घञ्-प्रत्ययः]
- **Steps**:
    - पठ् + अ [इत्संज्ञालोपः]
    - पाठ् + अ [अत उपधायाः 7.2.116 इत्यनेन पकारोत्तरस्य अकारस्य वृद्धिः आकारः]
    - **Output**: पाठ ।

#### Example 2: अचो ञ्णिति (7.2.115)
- **Input**: नी + णिच् [स्वार्थिकः णिच्-प्रत्ययः]
- **Steps**:
    - नी + इ [इत्संज्ञालोपः]
    - नै + इ [अचो ञ्णिति 7.2.115 इत्यनेन नकारोत्तरस्य ईकारस्य वृद्धिः ऐकारः]
    - नाय् + इ [एचोऽयवायावः 6.1.78 इति आयादेशः]
    - **Output**: नायि [सनाद्यन्ता धातवः 3.1.32 इति धातुसंज्ञा]

#### Example 3: तद्धितेष्वचामादेः (7.2.117)
- **Input**: उपगु + अण् [तद्धितसंज्ञकः अण्-प्रत्ययः]
- **Steps**:
    - उपगु + अ [इत्संज्ञालोपः]
    - औपगु + अ [तद्धितेष्वचामादेः 7.2.117 इत्यनेन आदिस्थस्य उकारस्य वृद्धिः भवति। अनेन उकारस्य स्थाने वृद्धिसंज्ञकः औकारः विधीयते]
    - औपगो + अ [ओर्गुणः 6.4.146 इति उकारस्य गुणः ओकारः]
    - औपगव् + अ [एचोऽयवायावः 6.1.78 इति अवादेशः]
    - **Output**: औपगव्
""")
