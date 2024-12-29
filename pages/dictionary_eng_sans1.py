import streamlit as st
import json
import random


# Load JSON Data
def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# Generate three-letter prefixes
def generate_three_letter_combinations(words):
    combinations = set(word[:3].lower() for word in words if len(word) >= 3)
    return sorted(combinations)


# Filter words by prefix (case-insensitive and partial match)
def filter_words_by_prefix(words, prefix):
    prefix = prefix.lower()
    return {word: words[word] for word in words if word.lower().startswith(prefix)}


#dd
def main():
    st.title("English to Sanskrit Dictionary")
    st.sidebar.title("Navigation")
    options = ["Dictionary Lookup", "Index (Up to 3 Letters)", "Quiz Game", "About"]
    choice = st.sidebar.radio("Go to", options)

    # Load data
    data = load_data("data/kosh/eng_san/converted_file.json")
    words_data = data["data"]["words"]
    text_data = data["data"]["text"]

    if choice == "Dictionary Lookup":
        st.subheader("Search for English Words")
        search_word = st.text_input("Enter an English word (partial matches allowed):")

        if search_word:
            search_word = search_word.lower()
            matching_words = {word: words_data[word] for word in words_data if search_word in word.lower()}

            if matching_words:
                st.write(f"### Results for '{search_word}':")
                for word, word_id in matching_words.items():
                    definition = text_data.get(word_id, "Definition not available.")
                    st.write(f"**{word.capitalize()}**: {definition}", unsafe_allow_html=True)
            else:
                st.error("No matching words found.")

    elif choice == "Index (Up to 3 Letters)":
        st.subheader("Browse Words by Letter Combinations")

        # Generate three-letter prefixes
        three_letter_combinations = generate_three_letter_combinations(words_data.keys())

        # Dropdown to select three-letter prefix
        selected_prefix = st.selectbox("Select a Three-Letter Prefix", three_letter_combinations)

        # Filter words based on the selected prefix
        if selected_prefix:
            filtered_words = filter_words_by_prefix(words_data, selected_prefix)

            if filtered_words:
                st.write(f"### Words Starting with '{selected_prefix}':")
                for word, word_id in sorted(filtered_words.items()):
                    definition = text_data.get(word_id, "Definition not available.")
                    st.write(f"**{word.capitalize()}**: {definition}", unsafe_allow_html=True)
            else:
                st.write(f"No words found starting with '{selected_prefix}'.")

    elif choice == "Quiz Game":
        st.subheader("Quiz Game: Translate English to Sanskrit")
        all_words = list(words_data.keys())
        word_to_guess = random.choice(all_words)
        correct_answer = words_data[word_to_guess]

        st.write(f"Translate the word: **{word_to_guess}**")
        user_answer = st.text_input("Your Answer (Enter Sanskrit meaning):")

        if st.button("Submit"):
            if user_answer.strip() == correct_answer:
                st.success("Correct!")
            else:
                st.error(f"Wrong! The correct answer is: {correct_answer}")

    elif choice == "About":
        st.subheader("About the App")
        st.write("""
            This app serves as a comprehensive English-to-Sanskrit dictionary.
            Features include:
            - Word lookup (with partial match and case-insensitive search)
            - Navigation by three-letter prefixes
            - Quiz games to test your vocabulary
        """)


if __name__ == "__main__":
    main()
