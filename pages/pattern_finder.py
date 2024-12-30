import streamlit as st
import re
from panini.modules.mapping_akshar_separator1 import generate_mapping, separate_characters_and_map

def classify_by_end_character(words):
    """Classifies words based on their ending characters."""
    classification = {}

    for word in words:
        separated_word = separate_characters_and_map(word)
        end_characters = separated_word[-1] if separated_word else ""

        if end_characters not in classification:
            classification[end_characters] = []

        classification[end_characters].append(word)

    return classification

# Streamlit app
def main():
    st.title("Devanagari Word Separator and Classifier")
    st.write("Enter Devanagari words as comma-separated input.")

    # Input text box
    user_input = st.text_area("Enter words:", value="पुलाकाद्-पुलाकात्, पुलिनाद्-पुलिनात्, पुलिन्दाद्-पुलिन्दात्, पुलोमजायाः, पुंश्चल्याः, पुष्कराद्-पुष्करात्, पुष्कराह्वाद्-पुष्कराह्वात्, पुष्करिण्याः")

    if st.button("Classify"):
        # Split input into words
        words = [word.strip() for word in user_input.split(',') if word.strip()]

        if not words:
            st.warning("Please enter some valid words.")
            return

        # Classify words
        classification = classify_by_end_character(words)

        # Display results
        st.subheader("Classification by Ending Characters")
        for end_character, classified_words in classification.items():
            st.write(f"**Ending Character(s): {end_character}**")
            st.write(", ".join(classified_words))

if __name__ == "__main__":
    main()
