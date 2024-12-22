import json


# Function to extract "dhatu" values and return as a Python list
def extract_dhatu_as_list(file_path):
    try:
        # Read the JSON data from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Ensure the expected structure exists
        dhatu_list = []
        if "data" in data and isinstance(data["data"], list):
            for item in data["data"]:
                if "dhatu" in item:
                    dhatu_list.append(item["dhatu"])
                else:
                    dhatu_list.append(None)  # Handle missing 'dhatu' key
        else:
            print("Invalid structure: 'data' key is missing or not a list.")
            return []

        return dhatu_list

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Invalid JSON in the file: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Main entry point
if __name__ == "__main__":
    # Specify the file path to the .txt file
    input_file_path = input("Enter the path to your .txt file: ").strip()

    # Call the function and get the list of "dhatu" values
    dhatu_list = extract_dhatu_as_list(input_file_path)

    # Print the Python list
    print("Python List of 'dhatu' values:")
    print(dhatu_list)
