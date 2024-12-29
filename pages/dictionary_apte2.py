import streamlit as st
import json
import os

# Load JSON Data
def load_json_from_url(url):
    import requests
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def load_json_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Search for a specific word
def search_word(data, word):
    return data.get(word, "Word not found in the dictionary.")

# Find words matching a pattern
def find_matching_words(data, pattern):
    return {key: value for key, value in data.items() if pattern in key}

# Main Streamlit app
def main():
    st.title("Sanskrit Dictionary Query")
    st.subheader("Explore the dictionary with advanced search and filtering options.")

    # Select data source
    data_source = st.sidebar.radio(
        "Choose data source",
        ["Load from URL", "Load from data/ folder"]
    )

    if data_source == "Load from URL":
        url = st.text_input("Enter the URL of the JSON file", "https://raw.githubusercontent.com/sanskrit-lexicon/csl-json/main/ashtadhyayi.com/skd.json")
        if st.button("Load JSON from URL"):
            try:
                json_data = load_json_from_url(url)
                words_data = json_data["data"]["words"]
                text_data = json_data["data"]["text"]
                st.success("Data successfully loaded from URL.")
            except Exception as e:
                st.error(f"Error loading JSON data from URL: {e}")
                return
    elif data_source == "Load from data/ folder":
        folder_path = "data/"
        available_files = [f for f in os.listdir(folder_path) if f.endswith(".json")]
        selected_file = st.selectbox("Select a JSON file", available_files)
        if st.button("Load JSON from file"):
            try:
                json_data = load_json_from_file(os.path.join(folder_path, selected_file))
                words_data = json_data["data"]["words"]
                text_data = json_data["data"]["text"]
                st.success("Data successfully loaded from file.")
            except Exception as e:
                st.error(f"Error loading JSON data from file: {e}")
                return

    # Ensure data is loaded before proceeding
    if 'words_data' not in locals() or 'text_data' not in locals():
        st.info("Please load data to proceed.")
        return

    # Select operation
    operation = st.sidebar.selectbox(
        "Choose an operation",
        ["Word Finder", "Matching Finder", "Dictionary Browser"]
    )

    if operation == "Word Finder":
        st.subheader("Word Finder")
        word = st.text_input("Enter a word to search")
        if word:
            result = search_word(words_data, word)
            st.write(f"**Word:** {word}")
            st.write(f"**Occurrences:** {result}")
            if isinstance(result, str) and result != "Word not found in the dictionary.":
                st.write(f"**Details:**")
                for occurrence in result.split(","):
                    if occurrence.strip() in text_data:
                        st.text_area(
                            f"Details for occurrence {occurrence.strip()}",
                            "\n".join(text_data[occurrence.strip()]),
                            height=200
                        )

    elif operation == "Matching Finder":
        st.subheader("Matching Finder")
        pattern = st.text_input("Enter a substring or pattern")
        if pattern:
            matches = find_matching_words(words_data, pattern)
            st.write(f"Found {len(matches)} matching words:")
            for key, value in matches.items():
                st.write(f"**Word:** {key} | **Occurrences:** {value}")

    elif operation == "Dictionary Browser":
        st.subheader("Dictionary Browser")
        st.write("Browse all words in the dictionary.")
        all_words = list(words_data.keys())
        start_index = st.number_input(
            "Start Index", min_value=0, max_value=len(all_words)-1, value=0
        )
        end_index = st.number_input(
            "End Index", min_value=0, max_value=len(all_words), value=min(len(all_words), 100)
        )
        for word in all_words[start_index:end_index]:
            st.write(f"**Word:** {word} | **Occurrences:** {words_data[word]}")

if __name__ == "__main__":
    main()
