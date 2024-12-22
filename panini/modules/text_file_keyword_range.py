def extract_modified_lists(input_file, output_file):
    """
    Extracts all text between 'Modified List:' and ']' from the input file
    and writes it into a new file, ensuring each line is enclosed in square brackets.

    Args:
        input_file (str): Path to the input .txt file.
        output_file (str): Path to save the output .txt file.
    """
    try:
        extracted_lists = []

        # Open the input file for reading
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

            # Extract relevant text
            for line in lines:
                if 'Modified List:' in line:
                    start_index = line.find('Modified List:') + len('Modified List:')
                    end_index = line.rfind(']')
                    if start_index < end_index:
                        modified_text = line[start_index:end_index + 1].strip()
                        extracted_lists.append(modified_text)

        # Write the extracted lists to the output file, enclosing each in []
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for extracted in extracted_lists:
                outfile.write(f"[{extracted}]\n")

        print(f"Extracted lists have been saved to: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


input_file_path = "processed_output.txt"  # Replace with the path to your input file
output_file_path = "output_keywords.txt"  # Replace with the desired path for the output file

# Run the function
extract_modified_lists(input_file_path, output_file_path)

# Input and output file paths

