import json

# Function to process the description
def add_comma_after_next_word(description):
    # Split into parts up to the second comma
    parts = description.split(',', maxsplit=2)
    if len(parts) > 2:
        # Break the third part into the first word and the rest
        third_part = parts[2].strip()
        if third_part:  # Ensure third_part is not empty
            words = third_part.split(maxsplit=1)
            if len(words) > 1:
                # Insert a comma after the first word
                modified_third_part = f"{words[0]}, {words[1]}"
            else:
                # If there's only one word, add a comma at the end of it
                modified_third_part = f"{words[0]},"
            # Reconstruct the description
            return f"{parts[0]},{parts[1]},{modified_third_part}"
    # Return original description if it doesn't match the expected structure
    return description

# Read input JSON
try:
    with open('/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/panini/function/output.json', 'r', encoding='utf-8') as infile:
        data = json.load(infile)
except FileNotFoundError:
    print("Error: 'input.json' file not found.")
    exit()

# Process each item in the data
for item in data:
    if 'description' in item and isinstance(item['description'], str):
        item['description'] = add_comma_after_next_word(item['description'])

# Write output JSON
with open('output21.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print("Processing complete. Check 'output.json' for results.")
