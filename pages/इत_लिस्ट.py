import streamlit as st
import re

# Function to filter words containing the exact anunasik character sequence
def filter_by_exact_anunasik(words, anunasik_char):
    """
    Filters words containing the exact anunasik character sequence.
    Uses regex to ensure the character is matched as a proper unit.
    """
    pattern = re.compile(rf"{anunasik_char}")
    return [word for word in words if pattern.search(word)]

# Streamlit App
st.title("Sanskrit Word Filter for Anunasik Characters")

# Initialize words as an empty list
words = []

# User input: upload or enter list
upload_or_input = st.radio("How do you want to provide the list of words?", ("Upload File", "Enter Words Manually"))

if upload_or_input == "Upload File":
    uploaded_file = st.file_uploader("Upload a file containing words (one word per line):")
    if uploaded_file:
        words = uploaded_file.read().decode("utf-8").splitlines()
else:
    words_input = st.text_area("Enter words (separated by commas):")
    if words_input:
        words = [word.strip() for word in words_input.split(",")]

# Proceed if words are available
if words:
    # List of anunasik characters
    anunasik_chars = ["अँ", "आँ", "इँ", "ईँ", "उँ", "ऊँ", "ऋँ", "ॠँ", "ऌँ", "ॡँ", "एँ", "ओँ", "ऐँ", "औँ"]
    results = {}

    # Filter words for each anunasik character
    for char in anunasik_chars:
        results[char] = filter_by_exact_anunasik(words, char)

    # Display results
    st.header("Words Containing Anunasik Characters")
    for char, words_with_char in results.items():
        st.subheader(f"Words containing '{char}':")
        if words_with_char:
            st.write(words_with_char)
        else:
            st.write(f"No words contain '{char}'.")

else:
    st.info("Please provide a list of words to proceed.")
