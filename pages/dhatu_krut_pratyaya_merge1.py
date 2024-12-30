import json
import streamlit as st

# Load merged JSON file
MERGED_JSON_PATH = 'data/dhatupath/dhatupath reference/dhatupath_roop/merged_krut.json'

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

# Main Streamlit app
st.title("Dhatu-Pratyaya Viewer")

# Load data
data = get_data()

# Extract unique Dhatu Codes and Pratyayas
all_dhatus = sorted({dhatu_code for dhatus in data.values() for dhatu_code in dhatus.keys()})
all_pratyayas = sorted({pratyaya for dhatus in data.values() for pratyayas in dhatus.values() for pratyaya in pratyayas.keys()})

# Dropdown for Dhatu Code and Pratyaya selection
dhatu_code = st.selectbox("Select a Dhatu Code:", all_dhatus)
pratyaya = st.selectbox("Select a Pratyaya:", all_pratyayas)

if dhatu_code and pratyaya:
    found = False
    for file_name, dhatus in data.items():
        if dhatu_code in dhatus and pratyaya in dhatus[dhatu_code]:
            st.header(f"File: {file_name}")
            display_pratyayas(dhatu_code, {pratyaya: dhatus[dhatu_code][pratyaya]})
            found = True
    if not found:
        st.error("No matching data found for the selected Dhatu Code and Pratyaya.")
