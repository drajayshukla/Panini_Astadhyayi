import json
import streamlit as st
import os

# Paths to JSON files
MERGED_JSON_PATH = 'data/dhatupath/dhatupath reference/dhatupath_roop/merged_krut.json'
DHATUPATH_JSON_PATH = 'data/dhatupath/dhatupath reference/dhatupath_roop/dhatupath.json'

# Helper function to load data from JSON file
def load_data(file_path):
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return {}
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Normalize numbers to handle Devanagari and international formats
def normalize_dhatu_code(code):
    devanagari_to_international = str.maketrans("०१२३४५६७८९", "0123456789")
    return code.translate(devanagari_to_international)

# Standardize Dhatu Code to match identifiers
def standardize_dhatu_code(code):
    normalized_code = normalize_dhatu_code(code)
    parts = normalized_code.split(".")
    if len(parts) == 2:
        return f"{int(parts[0]):02}.{int(parts[1]):04}"
    return normalized_code

# Lazy loading of merged data
data_cache = {}
def get_data():
    if not data_cache:
        data_cache.update(load_data(MERGED_JSON_PATH))
    return data_cache

# Lazy loading of Dhatu descriptions
dhatupath_data = []
def get_dhatupath_data():
    if not dhatupath_data:
        dhatupath_data.extend(load_data(DHATUPATH_JSON_PATH))
    return dhatupath_data

# Function to display Pratyayas for a given Dhatu Code
def display_pratyayas(dhatu_code, pratyayas):
    st.subheader(f"Dhatu Code: {dhatu_code}")
    for pratyaya, forms in pratyayas.items():
        forms_list = forms.split(",")
        forms_cleaned = [form.strip() for form in forms_list if form.strip()]
        st.write(f"- **{pratyaya}:** {' '.join(forms_cleaned)}")

# Function to display description for a Dhatu Code
def display_dhatu_description(dhatu_code, dhatupath_data):
    standardized_code = standardize_dhatu_code(dhatu_code)
    description_found = False
    for entry in dhatupath_data:
        if normalize_dhatu_code(entry['identifier']) == standardized_code:
            st.info(f"**Description:** {entry['description']}")
            description_found = True
            break
    if not description_found:
        st.warning(f"No description found for Dhatu Code: {dhatu_code}")

# Function to search any Dhatu derived forms in JSON
def search_derived_forms(data, query):
    results = []
    query = query.strip()
    for file_name, dhatus in data.items():
        for dhatu_code, pratyayas in dhatus.items():
            for pratyaya, forms in pratyayas.items():
                if query in forms:
                    results.append((file_name, dhatu_code, pratyaya, forms))
    return results

# Main Streamlit app
st.title("Dhatu-Pratyaya Viewer")

# Load JSON data
data = get_data()
dhatupath = get_dhatupath_data()

# Extract unique Dhatu Codes and Pratyayas
if data:
    all_dhatus = sorted({standardize_dhatu_code(dhatu_code) for dhatus in data.values() for dhatu_code in dhatus.keys()})
    all_pratyayas = sorted({pratyaya for dhatus in data.values() for pratyayas in dhatus.values() for pratyaya in pratyayas.keys()})

    # Dropdown for Dhatu Code and Pratyaya selection
    dhatu_code = st.selectbox("Select a Dhatu Code:", all_dhatus)
    pratyaya = st.selectbox("Select a Pratyaya:", all_pratyayas)

    if dhatu_code:
        # Display Dhatu description
        display_dhatu_description(dhatu_code, dhatupath)

    if dhatu_code and pratyaya:
        found = False
        for file_name, dhatus in data.items():
            if dhatu_code in dhatus and pratyaya in dhatus[dhatu_code]:
                st.header(f"File: {file_name}")
                display_pratyayas(dhatu_code, {pratyaya: dhatus[dhatu_code][pratyaya]})
                found = True
        if not found:
            st.error("No matching data found for the selected Dhatu Code and Pratyaya.")

    # Search functionality
    st.sidebar.header("Search Derived Forms")
    search_query = st.sidebar.text_input("Enter a derived form to search:")
    if search_query:
        search_results = search_derived_forms(data, search_query)
        if search_results:
            st.sidebar.subheader("Search Results:")
            for file_name, dhatu_code, pratyaya, forms in search_results:
                st.sidebar.write(f"File: {file_name}")
                st.sidebar.write(f"Dhatu Code: {dhatu_code}, Pratyaya: {pratyaya}")
                st.sidebar.write(f"Forms: {forms}")
                st.sidebar.write("---")
        else:
            st.sidebar.error("No matches found.")
else:
    st.error("Failed to load Dhatu-Pratyaya data.")
