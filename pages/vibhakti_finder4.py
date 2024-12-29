import streamlit as st
import json
import pandas as pd
from panini.modules.separate_characters import separate_characters_and_map

# Function to load data from uploaded file
@st.cache_data
def load_data(uploaded_file):
    file_content = uploaded_file.read().decode("utf-8")
    data = json.loads(file_content)
    return data["data"]

# Function to parse vibhakti forms into a structured table
def parse_forms(forms):
    forms_list = forms.split(";")

    # Map to correctly tag and order forms as per the given sequence
    reordered_forms = [
        forms_list[0], forms_list[1], forms_list[2],  # Prathama Ekavachan, Dvivachan, Bahuvachan
        forms_list[3], forms_list[4], forms_list[5],  # Dvitiya Ekavachan, Dvivachan, Bahuvachan
        forms_list[6], forms_list[7], forms_list[8],  # Tritiya Ekavachan, Dvivachan, Bahuvachan
        forms_list[9], forms_list[10], forms_list[11],  # Chaturthi Ekavachan, Dvivachan, Bahuvachan
        forms_list[12], forms_list[13], forms_list[14],  # Panchami Ekavachan, Dvivachan, Bahuvachan
        forms_list[15], forms_list[16], forms_list[17],  # Shashti Ekavachan, Dvivachan, Bahuvachan
        forms_list[18], forms_list[19], forms_list[20],  # Saptami Ekavachan, Dvivachan, Bahuvachan
        forms_list[21], forms_list[22], forms_list[23]   # Sambodhan Ekavachan, Dvivachan, Bahuvachan
    ]

    vibhakti_names = [
        "\u092a\u094d\u0930\u0925\u092e\u093e", "\u0926\u094d\u0935\u093f\u0924\u0940\u092f\u093e", "\u0924\u0943\u0924\u0940\u092f\u093e", "\u091a\u0924\u0941\u0930\u094d\u0925\u0940",
        "\u092a\u091e\u094d\u091a\u092e\u0940", "\u0937\u0937\u094d\u0920\u0940", "\u0938\u092a\u094d\u0924\u092e\u0940", "\u0938\u092e\u094d\u092c\u094b\u0927\u0928\u092e\u094d"
    ]

    ekavachanam = reordered_forms[0::3]
    dvivachanam = reordered_forms[1::3]
    bahuvachanam = reordered_forms[2::3]

    table_data = {
        "": vibhakti_names,
        "\u090f\u0915\u0935\u091a\u0928\u092e\u094d": ekavachanam,
        "\u0926\u094d\u0935\u093f\u0935\u091a\u0928\u092e\u094d": dvivachanam,
        "\u092c\u0939\u0941\u0935\u091a\u0928\u092e\u094d": bahuvachanam,
    }
    return pd.DataFrame(table_data)

# Function to generate a table of separated characters
def generate_separated_characters_table(forms):
    forms_list = forms.split(";")

    # Map to correctly tag and order forms as per the given sequence
    reordered_forms = [
        forms_list[0], forms_list[1], forms_list[2],  # Prathama Ekavachan, Dvivachan, Bahuvachan
        forms_list[3], forms_list[4], forms_list[5],  # Dvitiya Ekavachan, Dvivachan, Bahuvachan
        forms_list[6], forms_list[7], forms_list[8],  # Tritiya Ekavachan, Dvivachan, Bahuvachan
        forms_list[9], forms_list[10], forms_list[11],  # Chaturthi Ekavachan, Dvivachan, Bahuvachan
        forms_list[12], forms_list[13], forms_list[14],  # Panchami Ekavachan, Dvivachan, Bahuvachan
        forms_list[15], forms_list[16], forms_list[17],  # Shashti Ekavachan, Dvivachan, Bahuvachan
        forms_list[18], forms_list[19], forms_list[20],  # Saptami Ekavachan, Dvivachan, Bahuvachan
        forms_list[21], forms_list[22], forms_list[23]   # Sambodhan Ekavachan, Dvivachan, Bahuvachan
    ]

    vibhakti_names = [
        "\u092a\u094d\u0930\u0925\u092e\u093e", "\u0926\u094d\u0935\u093f\u0924\u0940\u092f\u093e", "\u0924\u0943\u0924\u0940\u092f\u093e", "\u091a\u0924\u0941\u0930\u094d\u0925\u0940",
        "\u092a\u091e\u094d\u091a\u092e\u0940", "\u0937\u0937\u094d\u0920\u0940", "\u0938\u092a\u094d\u0924\u092e\u0940", "\u0938\u092e\u094d\u092c\u094b\u0927\u0928\u092e\u094d"
    ]

    ekavachanam = [separate_characters_and_map(reordered_forms[i]) for i in range(0, len(reordered_forms), 3)]
    dvivachanam = [separate_characters_and_map(reordered_forms[i]) for i in range(1, len(reordered_forms), 3)]
    bahuvachanam = [separate_characters_and_map(reordered_forms[i]) for i in range(2, len(reordered_forms), 3)]

    table_data = {
        "": vibhakti_names,
        "\u090f\u0915\u0935\u091a\u0928\u092e\u094d": ekavachanam,
        "\u0926\u094d\u0935\u093f\u0935\u091a\u0928\u092e\u094d": dvivachanam,
        "\u092c\u0939\u0941\u0935\u091a\u0928\u092e\u094d": bahuvachanam,
    }
    return pd.DataFrame(table_data)

# Function to add separated characters to JSON data
def add_separated_characters_to_json(shabda_data):
    updated_data = []
    for entry in shabda_data:
        forms_list = entry["forms"].split(";")
        separated_characters = [separate_characters_and_map(form) for form in forms_list]
        entry["separated_forms"] = separated_characters
        updated_data.append(entry)
    return updated_data

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

        # Add separated characters to JSON
        updated_data = add_separated_characters_to_json(shabda_data)

        # Downloadable JSON file
        st.sidebar.download_button(
            label="Download Updated JSON",
            data=json.dumps(updated_data, ensure_ascii=False, indent=4),
            file_name="updated_shabda_data.json",
            mime="application/json"
        )

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

        # Generate and display separated characters table
        st.header("Separated Characters Table for All Vachans")
        separated_characters_table = generate_separated_characters_table(word_entry["forms"])
        st.table(separated_characters_table)
    else:
        st.info("Please upload a .txt file to start.")

if __name__ == "__main__":
    main()
