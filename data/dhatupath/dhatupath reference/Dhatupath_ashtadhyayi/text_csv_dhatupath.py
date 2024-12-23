import csv
import re

def txt_to_csv(input_file, output_file):
    # Open and read the input .txt file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Process each line
    processed_lines = []
    for line in lines:
        # Remove leading/trailing whitespaces
        line = line.strip()
        # Split using brackets while preserving the brackets as separate columns
        parts = re.split(r'(\([^\)]+\))', line)
        # Further split non-bracketed parts by tab or whitespace
        split_parts = []
        for part in parts:
            if part.startswith('(') and part.endswith(')'):
                split_parts.append(part.strip())
            else:
                split_parts.extend(part.split())
        processed_lines.append(split_parts)

    # Write to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(processed_lines)

# Example usage
input_txt_file = 'dhatu_path.txt'  # Replace with your .txt file path
output_csv_file = 'output.csv'  # Replace with your desired .csv file path
txt_to_csv(input_txt_file, output_csv_file)

print(f"Conversion complete! CSV saved to {output_csv_file}")
