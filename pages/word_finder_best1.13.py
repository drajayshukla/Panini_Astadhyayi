import os
import json
import streamlit as st
from urllib.parse import quote


def search_keyword_in_files(directory, keyword, extensions, words_before=1, words_after=2):
    """
    Searches for all instances of a keyword in files with specific extensions, extracts context, and provides references.

    Parameters:
        directory (str): Path to the directory where files are located.
        keyword (str): The word or phrase to search for.
        extensions (list): List of file extensions to target (e.g., ['.txt', '.json']).
        words_before (int): Number of words before the keyword to include in the context.
        words_after (int): Number of words after the keyword to include in the context.

    Returns:
        dict: A dictionary with file names as keys and a list of matched contexts as values.
    """
    results = {}

    for filename in os.listdir(directory):
        if any(filename.endswith(ext) for ext in extensions):
            file_path = os.path.join(directory, filename)
            if filename.endswith(".txt"):
                # Process text files
                with open(file_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                    matches = find_keyword_in_lines(lines, keyword, file_path, words_before, words_after)
                    if matches:
                        results[filename] = matches
            elif filename.endswith(".json"):
                # Process JSON files
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    if isinstance(data, str):
                        lines = data.split("\n")
                    elif isinstance(data, list):
                        lines = [str(line) for line in data]
                    elif isinstance(data, dict):
                        lines = json.dumps(data, indent=2).split("\n")
                    else:
                        lines = []
                    matches = find_keyword_in_lines(lines, keyword, file_path, words_before, words_after)
                    if matches:
                        results[filename] = matches

    return results


def find_keyword_in_lines(lines, keyword, file_path, words_before=1, words_after=2):
    """
    Searches for all instances of a keyword in a list of lines and extracts surrounding words.

    Parameters:
        lines (list): List of lines to search in.
        keyword (str): The word or phrase to search for.
        file_path (str): Path to the file being processed.
        words_before (int): Number of words before the keyword to include in the context.
        words_after (int): Number of words after the keyword to include in the context.

    Returns:
        list: A list of matched contexts with highlighted keywords.
    """
    matches = []
    keyword_lower = keyword.lower()
    for i, line in enumerate(lines):
        if keyword_lower in line.lower():
            # Split line into words
            words = line.split()
            for j, word in enumerate(words):
                if keyword_lower in word.lower():
                    # Extract surrounding words
                    start_index = max(0, j - words_before)
                    end_index = min(len(words), j + words_after + 1)
                    context_words = words[start_index:end_index]

                    # Highlight the keyword
                    context_words = [
                        f"<mark>{w}</mark>" if keyword_lower in w.lower() else w
                        for w in context_words
                    ]

                    # Combine context words into a string
                    context = " ".join(context_words)

                    # Encode file path and line number as a clickable link
                    file_link = f"file://{quote(file_path)}"
                    match_entry = {
                        "line_number": i + 1,  # Line numbers start at 1
                        "context": context,
                        "file_link": file_link
                    }
                    matches.append(match_entry)
    return matches


# Streamlit App
st.title("Keyword Search in Data Files")
st.write("Search for all instances of a keyword in `.txt` and `.json` files within the `data` folder.")

# Default directory inside the current working directory
current_directory = os.getcwd()
default_directory = os.path.join(current_directory, "../data")
directory = st.text_input("Enter the directory path:", default_directory)
keyword = st.text_input("Enter the keyword to search:")
extensions = st.multiselect("Select file extensions:", [".txt", ".json"], default=[".txt", ".json"])

# Additional user inputs for word context range
words_before = st.number_input("Number of words before the keyword:", min_value=0, max_value=50, value=1)
words_after = st.number_input("Number of words after the keyword:", min_value=0, max_value=50, value=2)

# Search button
if st.button("Search"):
    if not keyword:
        st.error("Please enter a keyword to search.")
    elif not os.path.isdir(directory):
        st.error("Invalid directory path.")
    else:
        # Perform the search
        with st.spinner("Searching..."):
            results = search_keyword_in_files(directory, keyword, extensions, words_before, words_after)

        # Display results
        if results:
            st.success(f"Found matches in {len(results)} file(s):")
            for file, matches in results.items():
                st.subheader(f"File: {file}")
                for match in matches:
                    st.write(f"**Line Number:** {match['line_number']}")
                    st.markdown(
                        f"[Open File at Line {match['line_number']}]({match['file_link']})",
                        unsafe_allow_html=True
                    )
                    # Render the context with highlighted keyword
                    st.markdown(match["context"], unsafe_allow_html=True)
                    st.markdown("<hr>", unsafe_allow_html=True)
        else:
            st.warning("No matches found.")
