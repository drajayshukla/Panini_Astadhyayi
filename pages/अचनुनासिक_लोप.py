import streamlit as st
import re

# Function to remove anunasik akshar from a single word
def remove_anunasik_akshar(word):
    anunasik_akshar = ['अँ', 'आँ', 'इँ', 'ईँ', 'उँ', 'ऊँ', 'ऋँ', 'ॠँ', 'ऌँ', 'ॡँ', 'एँ', 'ऐँ', 'ओँ', 'औँ']
    for akshar in anunasik_akshar:
        word = word.replace(akshar, '')
    return word

# Function to remove anunasik akshar from a list of words
def remove_anunasik_akshar_from_list(word_list):
    return [remove_anunasik_akshar(word) for word in word_list]

# Streamlit App
st.title("Anunasik Akshar Removal Tool")

st.markdown("""
This app removes **anunasik akshar** (nasalized vowels) from Sanskrit words. You can input a single word, a list of words, or upload a `.txt` file containing a Python list.
""")

# Single word input
st.header("Single Word Processing")
single_word = st.text_input(
    "Enter a Sanskrit word with anunasik akshar:",
    value="एध्अँ"  # Example placeholder
)

if single_word:
    result_single = remove_anunasik_akshar(single_word)
    st.write("Modified Word:", result_single)

# List of words input
st.header("List of Words Processing")
upload_option = st.radio(
    "Choose input method:",
    options=["Enter text directly", "Upload a .txt file"]
)

if upload_option == "Enter text directly":
    word_list_input = st.text_area(
        "Enter a list of Sanskrit words (comma-separated):",
        value="'एध्अँ', 'स्प्अर्ध्अँ', 'ग्आध्ऋँ', 'ब्आध्ऋँ', 'न्आध्ऋँ'"  # Example placeholder
    )
    if word_list_input:
        try:
            # Parse the input and remove whitespace
            word_list = [word.strip().strip("'") for word in word_list_input.split(',')]
            result_list = remove_anunasik_akshar_from_list(word_list)
            st.write("Original List:", word_list)
            st.write("Modified List:", result_list)

            # Download button for modified list
            result_str = ", ".join(result_list)
            st.download_button(
                label="Download Modified List",
                data=result_str,
                file_name="modified_word_list.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"Error processing the list: {e}")

elif upload_option == "Upload a .txt file":
    uploaded_file = st.file_uploader("Upload a .txt file with a Python list structure", type=["txt"])
    if uploaded_file:
        try:
            # Read and parse the file content
            content = uploaded_file.read().decode("utf-8")
            word_list = eval(content)  # Assuming the file contains a Python list
            if isinstance(word_list, list):
                result_list = remove_anunasik_akshar_from_list(word_list)
                st.write("Original List:", word_list)
                st.write("Modified List:", result_list)

                # Download button for modified list
                result_str = ", ".join(result_list)
                st.download_button(
                    label="Download Modified List",
                    data=result_str,
                    file_name="modified_word_list.txt",
                    mime="text/plain"
                )
            else:
                st.error("The uploaded file does not contain a valid Python list.")
        except Exception as e:
            st.error(f"Error processing the file: {e}")

st.markdown("""
---
### Note:
- Single words can be processed in the first section.
- Lists of words should be comma-separated or uploaded as a `.txt` file containing a Python list.
""")
