# Open the file for reading
'''with open('panini_sutra.txt', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    lines = file.readlines()

# Filter the lines and remove the lines starting with "•" and ending with "।"
lines = [line for line in lines if not (line.startswith("•") and line.rstrip().endswith("।"))]

# Open the file in write mode to overwrite the contents
with open('panini_sutra.txt', 'w', encoding='utf-8') as file:
    # Write the filtered lines back to the file
    file.writelines(lines)'''
import re

# Open the file for reading
with open('panini_sutra.txt', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    text = file.read()

# Define the Devanagari number mapping
devanagari_digits = {
    '०': '',
    '१': '',
    '२': '',
    '३': '',
    '४': '',
    '५': '',
    '६': '',
    '७': '',
    '८': '',
    '९': ''
}

# Remove the numbers using regular expressions
pattern = '[' + ''.join(devanagari_digits.keys()) + ']'
text_without_numbers = re.sub(pattern, '', text)

# Open the file in write mode to overwrite the contents
with open('panini_sutra.txt', 'w', encoding='utf-8') as file:
    # Write the text without numbers back to the file
    file.write(text_without_numbers)

