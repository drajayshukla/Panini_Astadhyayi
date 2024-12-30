import json
import streamlit as st

# Load merged JSON file
#MERGED_JSON_PATH = '/Users/dr.ajayshukla/PycharmProjects/Panini_Astadhyayi/switchoff/python_codes/merged_krut.json'
MERGED_JSON_PATH ='data/dhatupath/dhatupath reference/dhatupath_roop/merged_krut.json'

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

DATA = load_data(MERGED_JSON_PATH)

# Function to display pratyayas for a given dhatu or its combinations
def display_pratyayas(dhatu_code, pratyayas):
    st.subheader(f"Dhatu Code: {dhatu_code}")
    for pratyaya, forms in pratyayas.items():
        st.write(f"- **{pratyaya}:** {', '.join(forms)}")

# Main Streamlit app
st.title("Dhatu-Pratyaya Viewer")

menu_option = st.sidebar.selectbox(
    "Choose an Option:",
    ["View All Dhatu-Pratyaya Combinations", "Search by Dhatu Code", "Search by Pratyaya"]
)

if menu_option == "View All Dhatu-Pratyaya Combinations":
    for file_name, dhatus in DATA.items():
        st.header(f"File: {file_name}")
        for dhatu_code, pratyayas in dhatus.items():
            display_pratyayas(dhatu_code, pratyayas)

elif menu_option == "Search by Dhatu Code":
    dhatu_code = st.text_input("Enter Dhatu Code:")
    if dhatu_code:
        found = False
        for file_name, dhatus in DATA.items():
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
        for file_name, dhatus in DATA.items():
            for dhatu_code, pratyayas in dhatus.items():
                if pratyaya in pratyayas:
                    st.header(f"File: {file_name}")
                    st.subheader(f"Dhatu Code: {dhatu_code}")
                    st.write(f"- **{pratyaya}:** {', '.join(pratyayas[pratyaya])}")
                    found = True
        if not found:
            st.error("No matching Pratyaya found.")
