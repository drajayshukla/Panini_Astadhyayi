import json
import pandas as pd

# Load merged JSON file
MERGED_JSON_PATH = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/data/dhatupath/dhatupath reference/dhatupath_roop/merged_krut.json'

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

DATA = load_data(MERGED_JSON_PATH)

# Function to display pratyayas for a given dhatu or its combinations
def display_pratyayas(dhatu_code, pratyayas):
    print(f"### Dhatu Code: {dhatu_code}")
    for pratyaya, forms in pratyayas.items():
        print(f"{pratyaya}: {forms}")

# Main menu for selection
def main_menu(data):
    print("Welcome to Dhatu-Pratyaya Viewer")
    print("Select an option:")
    print("1. View all Dhatu-Pratyaya combinations")
    print("2. Search by Dhatu Code")
    print("3. Search by Pratyaya")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        for file_name, dhatus in data.items():
            print(f"## File: {file_name}")
            for dhatu_code, pratyayas in dhatus.items():
                display_pratyayas(dhatu_code, pratyayas)
    elif choice == '2':
        search_dhatu(data)
    elif choice == '3':
        search_pratyaya(data)
    elif choice == '4':
        print("Exiting the viewer. Goodbye!")
        exit()
    else:
        print("Invalid choice. Try again.")

# Search by Dhatu Code
def search_dhatu(data):
    dhatu_code = input("Enter Dhatu Code: ")
    found = False
    for file_name, dhatus in data.items():
        if dhatu_code in dhatus:
            print(f"## File: {file_name}")
            display_pratyayas(dhatu_code, dhatus[dhatu_code])
            found = True
    if not found:
        print("No matching Dhatu Code found.")

# Search by Pratyaya
def search_pratyaya(data):
    pratyaya = input("Enter Pratyaya: ")
    found = False
    for file_name, dhatus in data.items():
        print(f"## File: {file_name}")
        for dhatu_code, pratyayas in dhatus.items():
            if pratyaya in pratyayas:
                print(f"### Dhatu Code: {dhatu_code}")
                print(f"{pratyaya}: {pratyayas[pratyaya]}")
                found = True
    if not found:
        print("No matching Pratyaya found.")

if __name__ == "__main__":
    while True:
        main_menu(DATA)
