import streamlit as st
import json
import pandas as pd
import os

# Function to load JSON data from the 'data' folder
@st.cache_data
def load_json_data():
    file_path = os.path.join("data", "shabdpath", "updated_data.json")  # Correct file path
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

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

    # Load JSON data from the 'data' folder
    data = load_json_data()
    st.success("Data loaded successfully!")

    # Add filters
    grp_values = list(set(entry.get("grp", "") for entry in data))
    end_values = list(set(entry.get("end", "") for entry in data))
    linga_values = list(set(entry.get("linga", "") for entry in data))

    selected_grp = st.sidebar.selectbox("Filter by Group (grp)", ["All"] + grp_values)
    selected_end = st.sidebar.selectbox("Filter by Ending Type (end)", ["All"] + end_values)
    selected_linga = st.sidebar.selectbox("Filter by Linga (Gender)", ["All"] + linga_values)

    # Add filters for Ekavachanam, Dvivachanam, Bahuvachanam
    selected_vachan = st.sidebar.multiselect(
        "Filter by Vachanam",
        ["एकवचनम्", "द्विवचनम्", "बहुवचनम्"],
        default=["एकवचनम्", "द्विवचनम्", "बहुवचनम्"]
    )

    # Filter data based on selections
    filtered_data = [
        entry for entry in data
        if (selected_grp == "All" or entry.get("grp") == selected_grp) and
           (selected_end == "All" or entry.get("end") == selected_end) and
           (selected_linga == "All" or entry.get("linga") == selected_linga)
    ]

    # Select multiple words
    words = [entry["word"] for entry in filtered_data]
    selected_words = st.sidebar.multiselect("Select Words", words)

    # Display tables for each selected word
    for selected_word in selected_words:
        selected_entry = next(entry for entry in filtered_data if entry["word"] == selected_word)

        # Parse forms and filter based on selected Vachanam
        forms_table = parse_forms(selected_entry["forms"])
        if selected_vachan:
            forms_table = forms_table[[""] + selected_vachan]  # Filter columns based on selected Vachanam

        # Display Forms Table
        st.header(f"Forms for {selected_word}")
        st.table(forms_table)

        # Display Separated Forms Table
        st.header(f"Separated Forms for {selected_word}")
        separated_forms_table = create_separated_forms_table(selected_entry["separated_forms"])
        if selected_vachan:
            separated_forms_table = separated_forms_table[[""] + selected_vachan]  # Filter columns
        st.table(separated_forms_table)

        # Display Suffix Only Table
        st.header(f"Suffix Only for {selected_word}")
        suffix_only_table = create_suffix_only_table(selected_entry["suffix_only"])
        if selected_vachan:
            suffix_only_table = suffix_only_table[[""] + selected_vachan]  # Filter columns
        st.table(suffix_only_table)

    # Downloadable JSON file
    st.download_button(
        label="Download Updated JSON",
        data=json.dumps(data, ensure_ascii=False, indent=4),
        file_name="filtered_data.json",
        mime="application/json"
    )

if __name__ == "__main__":
    main()