import streamlit as st
import re
from panini.modules.separate_characters_list import separate_characters_and_map

def classify_by_end_characters(word_list):
    """
    Classifies words by their ending character(s).

    Parameters:
    word_list (list): List of words.

    Returns:
    dict: Classification of words based on their ending characters.
    """
    classification = {}
    for word in word_list:
        separated_word = separate_characters_and_map(word)
        if separated_word:
            end_char = separated_word[-1]  # Take the last character
            if end_char not in classification:
                classification[end_char] = []
            classification[end_char].append(word)
    return classification

def main():
    st.title("Devanagari Word Classifier")
    st.write("Enter Devanagari words separated by commas, and the app will classify them based on their ending character(s).")

    # Input area for words
    user_input = st.text_area("Enter words:", placeholder="पुलाकाद्-पुलाकात्, पुलिनाद्-पुलिनात्, ...")

    if st.button("Classify Words"):
        if user_input.strip():
            # Preprocess input
            words = [word.strip() for word in re.split(r',\s*', user_input) if word.strip()]

            # Classify words by ending character
            classification = classify_by_end_characters(words)

            if classification:
                st.subheader("Classification Results")
                for end_char, grouped_words in classification.items():
                    st.write(f"### Ending Character: {end_char}")
                    st.write(", ".join(grouped_words))
            else:
                st.write("No valid words found for classification.")
        else:
            st.write("Please enter some words to classify.")

if __name__ == "__main__":
    main()