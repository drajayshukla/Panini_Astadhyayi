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

    # Option to view all vibhakti-vachan combinations or select a word
    view_all = st.sidebar.checkbox("View All Vibhakti-Vachan Combinations", value=False)

    if view_all:
        st.header("All Vibhakti-Vachan Combinations")
        for entry in filtered_data:
            st.subheader(entry["word"])
            forms_table = parse_forms(entry["forms"])
            st.table(forms_table)
    else:
        # Select a word to display
        words = [entry["word"] for entry in filtered_data]
        selected_word = st.sidebar.selectbox("Select a Word", words)
        selected_entry = next(entry for entry in filtered_data if entry["word"] == selected_word)

        # Display Forms Table
        st.header(f"Forms for {selected_word}")
        forms_table = parse_forms(selected_entry["forms"])
        st.table(forms_table)

        # Add vibhakti and vachan filter
        vibhakti_names = [
            "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी",
            "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधन"
        ]
        vachana_names = ["एकवचनम्", "द्विवचनम्", "बहुवचनम्"]

        selected_vibhakti = st.sidebar.selectbox("Select Vibhakti (Case)", ["All"] + vibhakti_names)
        selected_vachan = st.sidebar.selectbox("Select Vachan (Number)", ["All"] + vachana_names)

        if selected_vibhakti != "All" or selected_vachan != "All":
            # Display filtered forms
            st.header("Filtered Form")
            if selected_vibhakti != "All":
                vibhakti_index = vibhakti_names.index(selected_vibhakti)
                if selected_vachan == "All":
                    st.write(forms_table.iloc[vibhakti_index])
                else:
                    column_index = {"एकवचनम्": 1, "द्विवचनम्": 2, "बहुवचनम्": 3}[selected_vachan]
                    filtered_form = forms_table.iloc[vibhakti_index, column_index]
                    st.write(f"**{selected_vibhakti} - {selected_vachan}:** {filtered_form}")
            elif selected_vachan != "All":
                column_index = {"एकवचनम्": 1, "द्विवचनम्": 2, "बहुवचनम्": 3}[selected_vachan]
                filtered_forms = forms_table.iloc[:, [0, column_index]]
                st.table(filtered_forms)

if __name__ == "__main__":
    main()
