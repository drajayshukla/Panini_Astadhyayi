import streamlit as st
from panini.modules.vriddhi1_1_1 import get_vriddhi_vowels, identify_vriddhi_vowels, explain_vriddhi

# Title of the app
st.title("Vriddhi Testing: Pāṇini's Grammar")

# Section 1: Retrieve Vriddhi Vowels
st.header("Retrieve Vriddhi Vowels")
vriddhi_vowels = get_vriddhi_vowels()
st.write("Vriddhi Vowels:", vriddhi_vowels)  # Display vowels

# Section 2: Identify Vriddhi Vowels in Input
st.header("Identify Vriddhi Vowels in a String")
input_string = st.text_input("Enter a string (e.g., 'रामः शैवः गौरवः')", "रामः शैवः गौरवः")
if input_string:
    found_vowels = identify_vriddhi_vowels(input_string)
    st.write("Found Vriddhi Vowels:", found_vowels)  # Display found vowels

# Section 3: Explanation of Vriddhi
st.header("Explanation of Vriddhi")
explanation = explain_vriddhi()
st.write(explanation)
