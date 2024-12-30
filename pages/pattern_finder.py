import streamlit as st

# Mapping for character separation
mapping = {
    'क': 'क्' + 'अ', 'का': 'क्' + 'आ', 'कि': 'क्' + 'इ', 'की': 'क्' + 'ई',
    'कु': 'क्' + 'उ', 'कू': 'क्' + 'ऊ', 'के': 'क्' + 'ए', 'कै': 'क्' + 'ऐ',
    'को': 'क्' + 'ओ', 'कौ': 'क्' + 'औ', 'कं': 'क्' + 'ं', 'कः': 'क्' + 'ः',
    # Include all mappings here as per your list...
    'ह्': 'ह्'
}


# Function to separate characters and map them
def separate_characters_and_map(input_list):
    output_list = []
    for item in input_list:
        output = ''
        i = 0
        while i < len(item):
            if i + 2 <= len(item) and item[i:i + 2] in mapping:
                output += mapping[item[i:i + 2]]
                i += 2
            elif item[i] in mapping:
                output += mapping[item[i]]
                i += 1
            else:
                output += item[i]
                i += 1
        output_list.append(output)
    return output_list


# Function to classify words by their ending characters
def classify_words_by_endings(words):
    classified_words = {}
    for word in words:
        separated_characters = separate_characters_and_map([word])[0]
        if separated_characters:
            end_char = separated_characters[-1]
            if end_char not in classified_words:
                classified_words[end_char] = []
            classified_words[end_char].append(word)
    return classified_words


# Streamlit App
st.title("Devanagari Word Classifier")
st.write("Enter comma-separated Devanagari words to classify them by their ending characters.")

# Input for user
input_text = st.text_area("Enter words (comma-separated):", placeholder="e.g., पुलाकाद-पुलाकात, पुलिनाद-पुलिनात")

if st.button("Classify"):
    if input_text.strip():
        # Split the input text into words
        words = [word.strip() for word in input_text.split(",") if word.strip()]

        # Classify words by their ending characters
        classified_words = classify_words_by_endings(words)

        # Display results
        st.subheader("Classification Results")
        for end_char, word_list in classified_words.items():
            st.write(f"**Ending Character '{end_char}':** {', '.join(word_list)}")
    else:
        st.warning("Please enter some words to classify.")
