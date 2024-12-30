

import json
import streamlit as st

# Load merged JSON file
MERGED_JSON_PATH ='data/dhatupath/dhatupath reference/dhatupath_roop/merged_krut.json'

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Lazy loading of JSON data to reduce memory usage
data_cache = {}
def get_data():
    if not data_cache:
        data_cache.update(load_data(MERGED_JSON_PATH))
    return data_cache

# Function to display pratyayas for a given dhatu or its combinations
def display_pratyayas(dhatu_code, pratyayas):
    st.subheader(f"Dhatu Code: {dhatu_code}")
    for pratyaya, forms in pratyayas.items():
        forms_list = forms.split(",")  # Avoid unnecessary separation of characters
        forms_cleaned = [form.strip() for form in forms_list if form.strip()]  # Clean empty or unnecessary spaces
        st.write(f"- **{pratyaya}:** {' '.join(forms_cleaned)}")

# Function to filter JSON data by dhatu prefix or pratyaya

def filter_data_by_dhatu(data, dhatu_prefix):
    filtered = {}
    for file_name, dhatus in data.items():
        for dhatu_code, pratyayas in dhatus.items():
            if dhatu_code.startswith(dhatu_prefix):
                if file_name not in filtered:
                    filtered[file_name] = {}
                filtered[file_name][dhatu_code] = pratyayas
    return filtered

def filter_data_by_pratyaya(data, pratyaya_key):
    filtered = {}
    for file_name, dhatus in data.items():
        for dhatu_code, pratyayas in dhatus.items():
            if pratyaya_key in pratyayas:
                if file_name not in filtered:
                    filtered[file_name] = {}
                filtered[file_name][dhatu_code] = {pratyaya_key: pratyayas[pratyaya_key]}
    return filtered

# Main Streamlit app
st.title("Dhatu-Pratyaya Viewer")

menu_option = st.sidebar.selectbox(
    "Choose an Option:",
    ["Search by Dhatu Code", "Search by Pratyaya", "Filter by Dhatu Prefix", "Filter by Pratyaya"]
)

data = get_data()

if menu_option == "Search by Dhatu Code":
    dhatu_code = st.text_input("Enter Dhatu Code:")
    if dhatu_code:
        found = False
        for file_name, dhatus in data.items():
            if dhatu_code in dhatus:
                st.header(f"File: {file_name}")
                display_pratyayas(dhatu_code, dhatus[dhatu_code])
                found = True
        if not found:
            st.error("No matching Dhatu Code found.")

elif menu_option == "Search by Pratyaya":
    pratyaya = st.text_input("Enter Pratyaya:")
    if pratyaya:
        found = False
        for file_name, dhatus in data.items():
            for dhatu_code, pratyayas in dhatus.items():
                if pratyaya in pratyayas:
                    st.header(f"File: {file_name}")
                    st.subheader(f"Dhatu Code: {dhatu_code}")
                    display_pratyayas(dhatu_code, {pratyaya: pratyayas[pratyaya]})
                    found = True
        if not found:
            st.error("No matching Pratyaya found.")

elif menu_option == "Filter by Dhatu Prefix":
    dhatu_prefix = st.text_input("Enter Dhatu Prefix:")
    if dhatu_prefix:
        filtered_data = filter_data_by_dhatu(data, dhatu_prefix)
        if filtered_data:
            for file_name, dhatus in filtered_data.items():
                st.header(f"File: {file_name}")
                for dhatu_code, pratyayas in dhatus.items():
                    display_pratyayas(dhatu_code, pratyayas)
        else:
            st.error("No matching Dhatus found with the given prefix.")

elif menu_option == "Filter by Pratyaya":
    pratyaya_key = st.text_input("Enter Pratyaya Key:")
    if pratyaya_key:
        filtered_data = filter_data_by_pratyaya(data, pratyaya_key)
        if filtered_data:
            for file_name, dhatus in filtered_data.items():
                st.header(f"File: {file_name}")
                for dhatu_code, pratyayas in dhatus.items():
                    display_pratyayas(dhatu_code, pratyayas)
        else:
            st.error("No matching Pratyayas found with the given key.")
