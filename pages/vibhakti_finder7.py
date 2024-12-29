import streamlit as st
import json
import os

# Function to load JSON data from the 'data' folder
@st.cache_data
def load_json_data():
    file_path = os.path.join("data", "shabdpath", "updated_data.json")  # Correct file path
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

# Function to extract forms for a specific vibhakti-vachan combination
def extract_forms(data, vibhakti_index, vachan_index):
    forms = []
    for entry in data:
        forms_list = entry["forms"].split(";")
        index = vibhakti_index * 3 + vachan_index
        if index < len(forms_list):
            forms.append(forms_list[index])
    return forms

# Main Streamlit app
def main():
    st.title("Sanskrit Shabd Roop Analyzer")

    # Load JSON data
    data = load_json_data()
    st.success("Data loaded successfully!")

    # Sidebar filters
    grp_values = list(set(entry.get("grp", "") for entry in data))
    end_values = list(set(entry.get("end", "") for entry in data))
    linga_values = list(set(entry.get("linga", "") for entry in data))

    selected_grp = st.sidebar.selectbox("Filter by Group (grp)", ["All"] + grp_values)
    selected_end = st.sidebar.selectbox("Filter by Ending Type (end)", ["All"] + end_values)
    selected_linga = st.sidebar.selectbox("Filter by Linga (Gender)", ["All"] + linga_values)

    # Filter data based on selections
    filtered_data = [
        entry for entry in data
        if (selected_grp == "All" or entry.get("grp") == selected_grp) and
           (selected_end == "All" or entry.get("end") == selected_end) and
           (selected_linga == "All" or entry.get("linga") == selected_linga)
    ]

    # Vibhakti and Vachan options
    vibhakti_names = [
        "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी",
        "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधन"
    ]
    vachana_names = ["एकवचनम्", "द्विवचनम्", "बहुवचनम्"]

    selected_vibhakti = st.sidebar.selectbox("Select Vibhakti (Case)", vibhakti_names)
    selected_vachan = st.sidebar.selectbox("Select Vachan (Number)", vachana_names)

    # Determine indices for vibhakti and vachan
    vibhakti_index = vibhakti_names.index(selected_vibhakti)
    vachan_index = vachana_names.index(selected_vachan)

    # Extract forms for the selected combination
    extracted_forms = extract_forms(filtered_data, vibhakti_index, vachan_index)

    # Display the result
    st.header(f"All {selected_vibhakti} - {selected_vachan} Forms")
    st.text(", ".join(extracted_forms))

if __name__ == "__main__":
    main()
