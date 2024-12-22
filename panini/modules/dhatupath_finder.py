def search_dhatu(file_path, search_term):
    """
        Searches for the specified term in the given file and prints lines containing the term.

        :param file_path: Path to the .txt file containing Panini Dhatu Path information.
        :param search_term: The word to search for.
        """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            matched_lines = [line.strip() for line in lines if search_term in line]

        if matched_lines:
            print(f"Found {len(matched_lines)} matching line(s):\n")
            for line in matched_lines:
                print(line)
        else:
            print(f"No matches found for '{search_term}'.")

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main execution
if __name__ == "__main__":
    # Specify the path to your .txt file
    file_path = "dhatupath.txt"  # Replace with the actual file path

    # Enter the term to search
    search_term = input("Enter the term to search: ").strip()

    # Call the search function
    search_dhatu(file_path, search_term)
