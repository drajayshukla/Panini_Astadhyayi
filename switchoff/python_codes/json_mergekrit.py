import os
import json

# Directory containing the JSON files
directory ='/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/dhatupath/dhatupath reference/dhatupath_roop/krut'

# Output file name
output_file = 'merged_krut.json'

# Initialize an empty dictionary to store the merged data
merged_data = {}

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)

        # Read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # Tag the data with the filename (excluding extension)
            tag = os.path.splitext(filename)[0]

            # Add the tagged data to the merged data
            merged_data[tag] = data

# Write the merged data to the output JSON file
with open(output_file, 'w', encoding='utf-8') as output:
    json.dump(merged_data, output, ensure_ascii=False, indent=4)

print(f"All JSON files have been merged into {output_file}.")
