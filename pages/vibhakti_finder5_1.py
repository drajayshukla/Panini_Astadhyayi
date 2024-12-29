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
    updated_forms = []
    for form in forms:
        updated_forms.append(form.replace(common_substring, ""))

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

# Function to calculate unique patterns at each position for all endings
def calculate_unique_patterns(data):
    ending_types = list(set(entry.get("end", "") for entry in data))
    results = {}

    for ending in ending_types:
        ending_data = [entry for entry in data if entry.get("end") == ending]

        patterns = {f"{i+1}": set() for i in range(24)}  # 24 positions for vibhakti-vachan

        for entry in ending_data:
            separated_forms = entry.get("separated_forms", [])
            for i, form in enumerate(separated_forms):
                patterns[f"{i+1}"].add(form)

        results[ending] = {key: len(value) for key, value in patterns.items()}

    return results

# Function to parse vibhakti forms into a structured table
def parse_forms(forms):
    forms_list = forms.split(";")

    reordered_forms = [
        forms_list[0], forms_list[1], forms_list[2],
        forms_list[3], forms_list[4], forms_list[5],
        forms_list[6], forms_list[7], forms_list[8],
        forms_list[9], forms_list[10], forms_list[11],
        forms_list[12], forms_list[13], forms_list[14],
        forms_list[15], forms_list[16], forms_list[17],
        forms_list[18], forms_list[19], forms_list[20],
        forms_list[21], forms_list[22], forms_list[23]
    ]

    vibhakti_names = [
        "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी",
        "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधन"
    ]

    ekavachanam = reordered_forms[0::3]
    dvivachanam = reordered_forms[1::3]
    bahuvachanam = reordered_forms[2::3]

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
    ekavachanam.extend(["" for _ in range(max_length - len(ekavachanam))])
    dvivachanam.extend(["" for _ in range(max_length - len(dvivachanam))])
    bahuvachanam.extend(["" for _ in range(max_length - len(bahuvachanam))])

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

    # Trim all arrays to the length of `vibhakti_names`
    ekavachanam = ekavachanam[:len(vibhakti_names)]
    dvivachanam = dvivachanam[:len(vibhakti_names)]
    bahuvachanam = bahuvachanam[:len(vibhakti_names)]

    # Ensure all arrays have the same length
    max_length = len(vibhakti_names)
    ekavachanam.extend(["" for _ in range(max_length - len(ekavachanam))])
    dvivachanam.extend(["" for _ in range(max_length - len(dvivachanam))])
    bahuvachanam.extend(["" for _ in range(max_length - len(bahuvachanam))])

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

        # Display Suffix Only Table
        st.header("Suffix Only")
        suffix_only_table = create_suffix_only_table(selected_entry["suffix_only"])
        st.table(suffix_only_table)

        # Calculate unique patterns for all ending types
        st.header("Unique Patterns by Ending Type")
        unique_patterns = calculate_unique_patterns(data)
        for ending, counts in unique_patterns.items():
            st.subheader(f"Ending Type: {ending}")
            st.json(counts)

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
