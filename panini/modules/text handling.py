def process_file(input_file_path, output_file_path):
    """
    Reads a text file, adds square brackets around each line, and saves the result.

    Args:
        input_file_path (str): Path to the input .txt file.
        output_file_path (str): Path to save the processed .txt file.
    """
    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
            for line in infile:
                stripped_line = line.strip()
                if stripped_line:  # Only process non-empty lines
                    outfile.write(f"[{stripped_line}]\n")
        print(f"Processed file saved to: {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace these paths with your actual file paths
input_file = "text handling.txt"  # Path to the input file
output_file = "../atest_it/outputtext.txt"  # Path to save the processed output file

# Run the function
process_file(input_file, output_file)
