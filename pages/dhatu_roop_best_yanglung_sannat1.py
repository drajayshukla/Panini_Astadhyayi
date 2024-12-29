import streamlit as st
import json
import pandas as pd

# File paths
DATA_FILE_PATH = 'data/dhatupath/dhatupath reference/dhatupath_roop/merged_krut.json'
NOTES_FILE_PATH = 'notes.json'

# Load data from JSON
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Save notes to a JSON file
def save_notes_to_file(notes, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

# Load notes from a JSON file
def load_notes_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Initialize notes
if "notes" not in st.session_state:
    st.session_state.notes = load_notes_from_file(NOTES_FILE_PATH)

DATA = load_data(DATA_FILE_PATH)

# Mapping for display names
LAKAR_MAP = {
    "plat": "कर्तरि लट्लकारः (परस्मैपदम्) - वर्तमान",
    "plit": "कर्तरि लिट्लकारः (परस्मैपदम्) - परोक्ष -अनध्यतन भूतकाल =आज से पहले",
    "plut": "कर्तरि लुट्लकारः (परस्मैपदम्) - अनध्यतन भविष्य =आज के बाद",
    "plrut": "कर्तरि लृट्लकारः (परस्मैपदम्) - भविष्य",
    "plot": "कर्तरि लोट्लकारः (परस्मैपदम्) - आज्ञा अनुमति प्रशंसा प्रार्थना आशीर्वाद निमंत्रण",
    "plang": "कर्तरि लङ्लकारः (परस्मैपदम्) - अनध्यतन भूतकाल =आज से पहले",
    "pvidhiling": "कर्तरि विधिलिङ्लकारः (परस्मैपदम्) - आज्ञा अनुमति प्रशंसा प्रार्थना निमंत्रण",
    "pashirling": "कर्तरि आशीर्लिङ्लकारः (परस्मैपदम्) - आशीर्वाद",
    "plung": "कर्तरि लुङ्लकारः (परस्मैपदम्)",
    "plrung": "कर्तरि लृङ्लकारः (परस्मैपदम्) - यदि ये होता भूतकाल",
    "alat": "कर्तरि लट्लकारः (आत्मनेपदम्) - वर्तमान",
    "alit": "कर्तरि लिट्लकारः (आत्मनेपदम्) - परोक्ष -अनध्यतन भूतकाल =आज से पहले",
    "alut": "कर्तरि लुट्लकारः (आत्मनेपदम्) - अनध्यतन भविष्य =आज के बाद",
    "alrut": "कर्तरि लृट्लकारः (आत्मनेपदम्) - भविष्य",
    "alot": "कर्तरि लोट्लकारः (आत्मनेपदम्) - आज्ञा अनुमति प्रशंसा प्रार्थना आशीर्वाद निमंत्रण",
    "alang": "कर्तरि लङ्लकारः (आत्मनेपदम्) - अनध्यतन भूतकाल =आज से पहले",
    "avidhiling": "कर्तरि विधिलिङ्लकारः (आत्मनेपदम्) - आज्ञा अनुमति प्रशंसा प्रार्थना निमंत्रण",
    "aashirling": "कर्तरि आशीर्लिङ्लकारः (आत्मनेपदम्) - आशीर्वाद",
    "alung": "कर्तरि लुङ्लकारः (आत्मनेपदम्)",
    "alrung": "कर्तरि लृङ्लकारः (आत्मनेपदम्) - यदि ये होता भूतकाल"
}

# Function to create tables with editable notes
def create_table_with_notes(forms, dhatu_code, lakar):
    forms_list = forms.split(";")
    rows = [forms_list[i:i+3] for i in range(0, len(forms_list), 3)]
    df = pd.DataFrame(rows, columns=["1st", "2nd", "3rd"])

    for index, row in df.iterrows():
        for col in df.columns:
            word = row[col]
            if word not in st.session_state.notes:
                st.session_state.notes[word] = ""  # Initialize with empty notes
            notes_input = st.text_input(f"Note for {word} ({dhatu_code} - {lakar})", value=st.session_state.notes[word], key=f"{dhatu_code}-{lakar}-{word}")
            st.session_state.notes[word] = notes_input  # Update the note

    return df

# Function to display Dhatu details
def display_dhatu(dhatu_code, dhatu_data):
    st.write(f"### {dhatu_code} (कौमुदीधातुः)")
    parasmaipadam = {key: value for key, value in dhatu_data.items() if key.startswith('pl')}
    atmanepadam = {key: value for key, value in dhatu_data.items() if key.startswith('al')}

    if parasmaipadam:
        st.write("## परस्मैपदम्")
        for lakar, forms in parasmaipadam.items():
            if lakar in LAKAR_MAP:
                st.write(f"#### {LAKAR_MAP[lakar]}")
                table = create_table_with_notes(forms, dhatu_code, lakar)
                st.table(table)

    if atmanepadam:
        st.write("## आत्मनेपदम्")
        for lakar, forms in atmanepadam.items():
            if lakar in LAKAR_MAP:
                st.write(f"#### {LAKAR_MAP[lakar]}")
                table = create_table_with_notes(forms, dhatu_code, lakar)
                st.table(table)

# Main Streamlit UI
st.title("धातुरूप प्रदर्शनी")

if st.button("Save Notes"):
    save_notes_to_file(st.session_state.notes, NOTES_FILE_PATH)
    st.success("Notes saved successfully!")

search_query = st.text_input("धातु कोड या रूप खोजें:")
if search_query:
    for set_name, dhatus in DATA.items():
        if search_query in dhatus:
            display_dhatu(search_query, dhatus[search_query])
else:
    for set_name, dhatus in DATA.items():
        st.write(f"## {set_name}")
        for dhatu_code in dhatus:
            display_dhatu(dhatu_code, dhatus[dhatu_code])
