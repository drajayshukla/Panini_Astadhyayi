import json
import csv


# Function to convert JSON to CSV
def json_to_csv(json_file, csv_file):
    try:
        # Read the JSON file
        with open(json_file, 'r', encoding='utf-8') as infile:
            data = json.load(infile)

        # Ensure the data is a list of dictionaries
        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            # Get the headers from the keys of the first dictionary
            headers = data[0].keys()

            # Write to CSV
            with open(csv_file, 'w', encoding='utf-8', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
            print(f"CSV file '{csv_file}' created successfully.")
        else:
            print("Error: JSON structure is not a list of dictionaries.")
    except Exception as e:
        print(f"An error occurred: {e}")


# File paths
input_json = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/panini/function/output21.json'  # Replace with your input JSON file name
output_csv = 'output4321.csv'  # Replace with your desired output CSV file name

# Convert JSON to CSV
json_to_csv(input_json, output_csv)
