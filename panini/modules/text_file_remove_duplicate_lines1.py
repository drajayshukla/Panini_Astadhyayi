from collections import Counter


def extract_unique_lines_with_prefix(input_file, output_file):
    """
    Extracts unique 'Modified List:' lines with counts and appends corresponding 'Common Prefix:' lines.

    Args:
        input_file (str): Path to the input .txt file.
        output_file (str): Path to save the output .txt file.
    """
    try:
        # Dictionaries to store bracket lines and their corresponding prefixes
        modified_lines = []
        prefix_map = {}

        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
            current_prefix = None

            for line in lines:
                # Capture 'Common Prefix:' lines
                if line.startswith("Common Prefix:"):
                    current_prefix = line.strip()

                # Capture 'Modified List:' lines
                if 'Modified List:' in line:
                    start_index = line.find('Modified List:') + len('Modified List:')
                    end_index = line.rfind(']')
                    if start_index < end_index:
                        modified_text = line[start_index:end_index + 1].strip()
                        modified_lines.append(modified_text)

                        # Map the modified text to its corresponding prefix
                        if modified_text not in prefix_map:
                            prefix_map[modified_text] = []
                        if current_prefix:
                            prefix_map[modified_text].append(current_prefix)

        # Count occurrences of each unique 'Modified List:'
        line_counts = Counter(modified_lines)

        # Write the results to the output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line, count in line_counts.items():
                prefixes = " ".join(prefix_map[line])  # Combine prefixes in {}
                outfile.write(f"{line} - {count} times {{ {prefixes} }}\n")

        print(f"Unique lines with counts and prefixes have been saved to: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Input and output file paths
input_file_path = "processed_output.txt"  # Replace with the path to your input file
output_file_path = "output_unique_with_prefix11.txt"  # Replace with the desired path for the output file

# Run the function
extract_unique_lines_with_prefix(input_file_path, output_file_path)
