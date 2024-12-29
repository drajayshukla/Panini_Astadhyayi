import os
import json
import streamlit as st

def search_keyword_in_files(directory, keyword, extensions):
    """
    Searches for a keyword in files with specific extensions, extracts context, and provides references.

    Parameters:
        directory (str): Path to the directory where files are located.
        keyword (str): The word or phrase to search for.
        extensions (list): List of file extensions to target (e.g., ['.txt', '.json']).

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
                    matches = find_keyword_in_lines(lines, keyword)
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
                    matches = find_keyword_in_lines(lines, keyword)
                    if matches:
                        results[filename] = matches

    return results


def find_keyword_in_lines(lines, keyword):
    """
    Searches for a keyword in a list of lines and extracts one line before and two lines after each occurrence.

    Parameters:
        lines (list): List of lines to search in.
        keyword (str): The word or phrase to search for.

    Returns:
        list: A list of matched contexts with one line before and two lines after.
    """
    matches = []
    keyword_lower = keyword.lower()
    for i, line in enumerate(lines):
        if keyword_lower in line.lower():
            # Highlight the keyword in the line using HTML
            highlighted_line = line.replace(
                keyword, f"<mark>{keyword}</mark>"
            ).replace(
                keyword.lower(), f"<mark>{keyword.lower()}</mark>"
            ).replace(
                keyword.upper(), f"<mark>{keyword.upper()}</mark>"
            )
            # Extract one line before and two lines after
            context = lines[max(0, i-1):min(len(lines), i+3)]
            # Replace the original line with the highlighted one
            context[i - max(0, i-1)] = highlighted_line
            matches.append({
                "line_number": i + 1,  # Line numbers start at 1
                "context": context
            })
    return matches

# Streamlit App
st.title("Keyword Search in Data Files")
st.write("Search for a keyword in `.txt` and `.json` files within the `data` folder.")

# Default directory inside the current working directory
current_directory = os.getcwd()
default_directory = os.path.join(current_directory, "../data")
directory = st.text_input("Enter the directory path:", default_directory)
keyword = st.text_input("Enter the keyword to search:")
extensions = st.multiselect("Select file extensions:", [".txt", ".json"], default=[".txt", ".json"])

# Search button
if st.button("Search"):
    if not keyword:
        st.error("Please enter a keyword to search.")
    elif not os.path.isdir(directory):
        st.error("Invalid directory path.")
    else:
        # Perform the search
        with st.spinner("Searching..."):
            results = search_keyword_in_files(directory, keyword, extensions)

        # Display results
        if results:
            st.success(f"Found matches in {len(results)} file(s):")
            for file, matches in results.items():
                st.subheader(f"File: {file}")
                for match in matches:
                    st.write(f"**Line Number:** {match['line_number']}")
                    for context_line in match["context"]:
                        # Render each line with highlighted keyword
                        st.markdown(context_line, unsafe_allow_html=True)
                    st.markdown("<hr>", unsafe_allow_html=True)
        else:
            st.warning("No matches found.")
