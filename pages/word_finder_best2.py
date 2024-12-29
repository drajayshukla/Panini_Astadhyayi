import os
import json
import streamlit as st
import os

# Define the path to the data directory relative to this script
data_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/data")

print(f"Searching in directory: {os.path.abspath(data_directory)}")

def search_keyword_in_files(directory, keyword, match_limit):
    """
    Searches for up to `match_limit` instances of a keyword in files ending with `.txt` and `.json`.

    Parameters:
        directory (str): Path to the directory where files are located.
        keyword (str): The word or phrase to search for.
        match_limit (int): Maximum number of matches to find.

    Returns:
        tuple: A tuple containing:
            - list of all file names searched.
            - dictionary with file names as keys and a list of matched contexts as values.
    """
    extensions = [".txt", ".json"]
    all_files = []
    results = {}
    total_matches = 0  # To track the total matches found

    for filename in os.listdir(directory):
        if total_matches >= match_limit:
            break  # Stop searching once match limit is reached

        if any(filename.endswith(ext) for ext in extensions):
            all_files.append(filename)  # Add file to the searched list
            file_path = os.path.join(directory, filename)
            if filename.endswith(".txt"):
                # Process text files
                with open(file_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                    matches = find_keyword_in_lines(lines, keyword, match_limit - total_matches)
                    if matches:
                        results[filename] = matches
                        total_matches += len(matches)
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
                    matches = find_keyword_in_lines(lines, keyword, match_limit - total_matches)
                    if matches:
                        results[filename] = matches
                        total_matches += len(matches)

    return all_files, results


def find_keyword_in_lines(lines, keyword, match_limit):
    """
    Searches for up to `match_limit` instances of a keyword in a list of lines and highlights them.

    Parameters:
        lines (list): List of lines to search in.
        keyword (str): The word or phrase to search for.
        match_limit (int): Maximum number of matches to find in the lines.

    Returns:
        list: A list of matched contexts with one line before and two lines after.
    """
    matches = []
    keyword_lower = keyword.lower()
    for i, line in enumerate(lines):
        if len(matches) >= match_limit:
            break  # Stop searching once match limit is reached

        if keyword_lower in line.lower():
            # Highlight all instances of the keyword in the line
            highlighted_line = line
            for word in [keyword, keyword.lower(), keyword.upper()]:
                highlighted_line = highlighted_line.replace(word, f"<mark>{word}</mark>")

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
st.write("Search for up to 50 instances of a keyword in files ending with `.txt` and `.json` in the `data` folder.")

# Default directory inside the app's structure
data_directory = os.path.join(os.getcwd(), "../data")

# Input for keyword
keyword = st.text_input("Enter the keyword to search:")
match_limit = 50  # Maximum number of matches to display

# Search button
if st.button("Search"):
    if not keyword:
        st.error("Please enter a keyword to search.")
    elif not os.path.isdir(data_directory):
        st.error("The `/data` directory does not exist.")
    else:
        # Perform the search
        with st.spinner("Searching..."):
            all_files, results = search_keyword_in_files(data_directory, keyword, match_limit)

        # Display searched file names
        st.subheader("Searched Files")
        if all_files:
            st.write(f"Total files searched: {len(all_files)}")
            st.write(", ".join(all_files))
        else:
            st.warning("No files ending with `.txt` or `.json` found.")

        # Display results
        if results:
            total_found = sum(len(matches) for matches in results.values())
            st.success(f"Found {total_found} matches (stopped at {match_limit}):")
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
