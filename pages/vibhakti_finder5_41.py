import streamlit as st
import json
import pandas as pd
import os
from collections import Counter

# Function to load data from uploaded file
@st.cache_data
def load_json_data(uploaded_file):
    file_content = uploaded_file.read().decode("utf-8")
    data = json.loads(file_content)
    return data

# Function to find and remove all common substrings in forms, ignoring entries starting with 'ह्ए'
def remove_all_common_units(forms):
    # Filter out entries starting with 'ह्ए'
    filtered_forms = [form for form in forms if not form.startswith("ह्ए")]
    if not filtered_forms:
        return forms  # If no forms remain after filtering, return original

    # Find the longest common substring among filtered forms
    common_substring = os.path.commonprefix(filtered_forms)

    # Remove the common substring from all forms
    updated_forms = [form.replace(common_substring, "") for form in forms]

    return updated_forms

# Function to filter out forms starting with 'ह्ए' in the final suffix_only list
def filter_suffix_only(suffix_only):
    return [form for form in suffix_only if not form.startswith("ह्ए")]

# Function to add new entry with suffix-only data
def add_suffix_only_entry(data):
    updated_data = []
    for entry in data:
        separated_forms = entry.get("separated_forms", [])
        if separated_forms:
            suffix_only = remove_all_common_units(separated_forms)
            suffix_only = filter_suffix_only(suffix_only)  # Remove entries starting with 'ह्ए'
            entry["suffix_only"] = suffix_only
        updated_data.append(entry)
    return updated_data

# Function to parse vibhakti forms into a structured table
def parse_forms(forms):
    forms_list = forms.split(";")

    vibhakti_names = [
        "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी",
        "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधन"
    ]

    ekavachanam = forms_list[0::3]
    dvivachanam = forms_list[1::3]
    bahuvachanam = forms_list[2::3]

    table_data = {
        "": vibhakti_names,
        "एकवचनम्": ekavachanam,
        "द्विवचनम्": dvivachanam,
        "बहुवचनम्": bahuvachanam,
    }
    return pd.DataFrame(table_data)

# Function to create tables for separated forms
def create_separated_forms_table(separated_forms):
    vibhakti_names = [
        "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी",
        "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधन"
    ]
    ekavachanam = separated_forms[0::3]
    dvivachanam = separated_forms[1::3]
    bahuvachanam = separated_forms[2::3]

    # Ensure all arrays have the same length
    max_length = max(len(ekavachanam), len(dvivachanam), len(bahuvachanam))
    ekavachanam.extend([""] * (max_length - len(ekavachanam)))
    dvivachanam.extend([""] * (max_length - len(dvivachanam)))
    bahuvachanam.extend([""] * (max_length - len(bahuvachanam)))

    table_data = {
        "": vibhakti_names,
        "एकवचनम्": ekavachanam,
        "द्विवचनम्": dvivachanam,
        "बहुवचनम्": bahuvachanam,
    }
    return pd.DataFrame(table_data)

# Function to create tables for suffix-only forms
def create_suffix_only_table(suffix_only):
    vibhakti_names = [
        "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी",
        "पञ्चमी", "षष्ठी", "सप्तमी"
    ]  # Removed "सम्बोधन" since suffix_only has one less row

    ekavachanam = suffix_only[0::3]
    dvivachanam = suffix_only[1::3]
    bahuvachanam = suffix_only[2::3]

    # Ensure all arrays have the same length
    max_length = len(vibhakti_names)
    ekavachanam.extend([""] * (max_length - len(ekavachanam)))
    dvivachanam.extend([""] * (max_length - len(dvivachanam)))
    bahuvachanam.extend([""] * (max_length - len(bahuvachanam)))

    table_data = {
        "": vibhakti_names,
        "एकवचनम्": ekavachanam,
        "द्विवचनम्": dvivachanam,
        "बहुवचनम्": bahuvachanam,
    }
    return pd.DataFrame(table_data)

# Main Streamlit app
def main():
    st.title("Sanskrit Shabd Roop Analyzer")
    st.sidebar.header("Upload JSON File")

    # File upload
    uploaded_file = st.sidebar.file_uploader("Upload the .json file", type=["json"])
    if uploaded_file:
        # Load JSON data
        data = load_json_data(uploaded_file)
        st.success("Data loaded successfully!")

        # Add `suffix_only` entries
        data = add_suffix_only_entry(data)

        # Add filters
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

        # Select a word to display
        words = [entry["word"] for entry in filtered_data]
        selected_word = st.sidebar.selectbox("Select a Word", words)
        selected_entry = next(entry for entry in filtered_data if entry["word"] == selected_word)

        # Display Forms Table
        st.header(f"Forms for {selected_word}")
        forms_table = parse_forms(selected_entry["forms"])
        st.table(forms_table)

        # Display Separated Forms Table
        st.header("Separated Forms")
        separated_forms_table = create_separated_forms_table(selected_entry["separated_forms"])
        st.table(separated_forms_table)

        # Display Suffix Only Table (with a safeguard for missing 'suffix_only')
        st.header("Suffix Only")
        if "suffix_only" in selected_entry:
            suffix_only_table = create_suffix_only_table(selected_entry["suffix_only"])
            st.table(suffix_only_table)
        else:
            st.warning(f"No 'suffix_only' data available for the word: {selected_word}")

        # Downloadable JSON file
        st.download_button(
            label="Download Updated JSON",
            data=json.dumps(data, ensure_ascii=False, indent=4),
            file_name="filtered_data.json",
            mime="application/json"
        )
    else:
        st.info("Please upload a .json file to start.")

if __name__ == "__main__":
    main()