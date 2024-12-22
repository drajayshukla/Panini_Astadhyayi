import os
import json

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
        if any(filename.endswith(ext) for ext in extensions) and "_xyz" in filename:
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
            # Highlight the keyword in the line
            highlighted_line = line.replace(
                keyword, f"***{keyword}***"
            ).replace(
                keyword.lower(), f"***{keyword.lower()}***"
            ).replace(
                keyword.upper(), f"***{keyword.upper()}***"
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


# Directory and extensions
current_directory = os.getcwd()
file_extensions = [".txt", ".json"]

# Input the keyword to search
keyword_to_search = input("Enter the word or phrase to search: ")

# Search in files
results = search_keyword_in_files(current_directory, keyword_to_search, file_extensions)

# Display results
if results:
    for file, matches in results.items():
        print(f"\nFile: {file}")
        for match in matches:
            print(f"Line Number: {match['line_number']}")
            print("Context:")
            for line in match["context"]:
                print(line.strip())
            print("-" * 50)
else:
    print("No matches found.")
