import os
import json
import streamlit as st
from urllib.parse import quote


def search_keyword_in_files(directory, keyword, extensions, lines_before=1, lines_after=2):
    """
    Searches for all instances of a keyword in files with specific extensions, extracts context, and provides references.

    Parameters:
        directory (str): Path to the directory where files are located.
        keyword (str): The word or phrase to search for.
        extensions (list): List of file extensions to target (e.g., ['.txt', '.json']).
        lines_before (int): Number of lines before the keyword to include in the context.
        lines_after (int): Number of lines after the keyword to include in the context.

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
                    matches = find_keyword_in_lines(lines, keyword, file_path, lines_before, lines_after)
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
                    matches = find_keyword_in_lines(lines, keyword, file_path, lines_before, lines_after)
                    if matches:
                        results[filename] = matches

    return results


def find_keyword_in_lines(lines, keyword, file_path, lines_before=1, lines_after=2):
    matches = []
    keyword_lower = keyword.lower()
    for i, line in enumerate(lines):
        if keyword_lower in line.lower():
            # Highlight all instances of the keyword in the line
            highlighted_line = line
            for word in [keyword, keyword.lower(), keyword.upper()]:
                highlighted_line = highlighted_line.replace(word, f"<mark>{word}</mark>")

            # Extract the specified range of lines
            context = lines[max(0, i-lines_before):min(len(lines), i+lines_after+1)]
            # Replace the original line with the highlighted one
            context[i - max(0, i-lines_before)] = highlighted_line

            # Encode file path and line number as a clickable link
            file_link = f"file://{quote(file_path)}"
            match_entry = {
                "line_number": i + 1,
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

# Search button
# Additional user inputs for context range
lines_before = st.number_input("Number of lines before the keyword:", min_value=0, max_value=10, value=1)
lines_after = st.number_input("Number of lines after the keyword:", min_value=0, max_value=10, value=2)

# Search button
if st.button("Search"):
    if not keyword:
        st.error("Please enter a keyword to search.")
    elif not os.path.isdir(directory):
        st.error("Invalid directory path.")
    else:
        # Perform the search
        with st.spinner("Searching..."):
            results = search_keyword_in_files(directory, keyword, extensions, lines_before, lines_after)

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
                    for context_line in match["context"]:
                        st.markdown(context_line, unsafe_allow_html=True)
                    st.markdown("<hr>", unsafe_allow_html=True)
        else:
            st.warning("No matches found.")
