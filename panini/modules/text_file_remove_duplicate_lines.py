from collections import Counter


def extract_unique_lines_with_counts(input_file, output_file):
    """
    Extracts unique lines within square brackets [] from a .txt file,
    counts their occurrences, and saves the unique lines with their counts
    in an output file.

    Args:
        input_file (str): Path to the input .txt file.
        output_file (str): Path to save the output .txt file.
    """
    try:
        # List to store all lines within brackets
        bracket_lines = []

        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                # Find lines enclosed in square brackets
                start_index = line.find('Modified List:')
                end_index = line.rfind(']')
                if start_index != -1 and end_index != -1 and start_index < end_index:
                    bracket_lines.append(line[start_index:end_index + 1].strip())

        # Count occurrences of each unique line
        line_counts = Counter(bracket_lines)

        # Write the unique lines with their counts to the output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line, count in line_counts.items():
                outfile.write(f"{line} - {count} times\n")

        print(f"Unique lines with counts have been saved to: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Input and output file paths
input_file_path = "processed_output.txt"  # Replace with the path to your input file
output_file_path = "output_unique1.txt"  # Replace with the desired path for the output file

# Run the function
extract_unique_lines_with_counts(input_file_path, output_file_path)
