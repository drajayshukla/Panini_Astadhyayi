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
