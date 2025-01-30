import json
import re

# Function to process the description
def process_description(description):
    parts = description.split(',', maxsplit=2)  # Split into three parts
    if len(parts) > 2:
        # Replace spaces with commas in the second part
        parts[1] = ','.join(parts[1].split())
        return ','.join(parts)
    return description  # If the description doesn't match, return as is

# Read input JSON
with open('/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/panini_function/dhatu_gan.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

# Process each item in the data
for item in data:
    item['description'] = process_description(item['description'])

# Write output JSON
with open('output1111.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print("Processing complete. Check 'output.json' for results.")
