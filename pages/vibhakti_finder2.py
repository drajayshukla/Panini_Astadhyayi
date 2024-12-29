import streamlit as st
import json
import pandas as pd


# Function to load data from uploaded file
@st.cache_data
def load_data(uploaded_file):
    file_content = uploaded_file.read().decode("utf-8")
    data = json.loads(file_content)
    return data["data"]


# Function to parse vibhakti forms into a structured table
def parse_forms(forms):
    vibhakti_names = [
        "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी",
        "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधनम्"
    ]
    forms_list = forms.split(";")
    ekavachanam = forms_list[0:8]
    dvivachanam = forms_list[8:16]
    bahuvachanam = forms_list[16:24]

    table_data = {
        "": vibhakti_names,
        "एकवचनम्": ekavachanam,
        "द्विवचनम्": dvivachanam,
        "बहुवचनम्": bahuvachanam,
    }
    return pd.DataFrame(table_data)


# Main Streamlit app
def main():
    st.title("Sanskrit Shabd Roop Vibhakti Finder")
    st.sidebar.header("Upload and Search")

    # File upload
    uploaded_file = st.sidebar.file_uploader("Upload the .txt file", type=["txt"])
    if uploaded_file:
        # Load data from uploaded file
        shabda_data = load_data(uploaded_file)
        st.success("Data loaded successfully!")

        # Add filters for linga and ending
        linga_values = list(set(entry.get("linga", "N/A") for entry in shabda_data))
        end_values = list(set(entry.get("end", "N/A") for entry in shabda_data))

        selected_linga = st.sidebar.selectbox("Filter by Linga (Gender)", ["All"] + linga_values)
        selected_end = st.sidebar.selectbox("Filter by Ending Type", ["All"] + end_values)

        # Filter data based on selections
        filtered_data = [
            entry for entry in shabda_data
            if (selected_linga == "All" or entry.get("linga") == selected_linga) and
               (selected_end == "All" or entry.get("end") == selected_end)
        ]

        # Select a word to display
        word_list = [entry["word"] for entry in filtered_data]
        if not word_list:
            st.warning("No words match the selected filters.")
            return
        selected_word = st.sidebar.selectbox("Select a Word", word_list)

        # Find the entry for the selected word
        word_entry = next(entry for entry in filtered_data if entry["word"] == selected_word)

        # Display metadata
        st.header(f"Forms for: {word_entry['word']}")
        st.write(f"Meaning: {word_entry.get('artha', 'N/A')} ({word_entry.get('artha_eng', 'N/A')})")
        st.write(f"Linga: {word_entry.get('linga', 'N/A')}, Ending: {word_entry.get('end', 'N/A')}")

        # Parse and display vibhakti forms in a table
        forms_table = parse_forms(word_entry["forms"])
        st.table(forms_table)
    else:
        st.info("Please upload a .txt file to start.")


if __name__ == "__main__":
    main()
