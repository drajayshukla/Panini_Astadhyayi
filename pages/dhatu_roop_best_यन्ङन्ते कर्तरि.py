import streamlit as st
import json
import pandas as pd

# Load JSON data from file
DATA_FILE_PATH = 'data/dhatupath/dhatupath reference/dhatupath_roop/dhatupath_best_yangkartari.json'

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

DATA = load_data(DATA_FILE_PATH)

# Mapping for display names
LAKAR_MAP = {
    "plat": "यन्ङन्ते कर्तरि लट्लकारः (परस्मैपदम्) - वर्तमान",
    "plit": "यन्ङन्ते कर्तरि लिट्लकारः (परस्मैपदम्) - परोक्ष -अनध्यतन भूतकाल =आज से पहले",
    "plut": "यन्ङन्ते कर्तरि लुट्लकारः (परस्मैपदम्) - अनध्यतन भविष्य =आज के बाद",
    "plrut": "यन्ङन्ते कर्तरि लृट्लकारः (परस्मैपदम्) - भविष्य",
    "plot": "यन्ङन्ते कर्तरि लोट्लकारः (परस्मैपदम्) - आज्ञा अनुमति प्रशंसा प्रार्थना आशीर्वाद निमंत्रण",
    "plang": "यन्ङन्ते कर्तरि लङ्लकारः (परस्मैपदम्) - अनध्यतन भूतकाल =आज से पहले",
    "pvidhiling": "यन्ङन्ते कर्तरि विधिलिङ्लकारः (परस्मैपदम्) - आज्ञा अनुमति प्रशंसा प्रार्थना निमंत्रण",
    "pashirling": "यन्ङन्ते कर्तरि आशीर्लिङ्लकारः (परस्मैपदम्) - आशीर्वाद",
    "plung": "यन्ङन्ते कर्तरि लुङ्लकारः (परस्मैपदम्)",
    "plrung": "यन्ङन्ते कर्तरि लृङ्लकारः (परस्मैपदम्) - यदि ये होता भूतकाल",
    "alat": "यन्ङन्ते कर्तरि लट्लकारः (आत्मनेपदम्) - वर्तमान",
    "alit": "यन्ङन्ते कर्तरि लिट्लकारः (आत्मनेपदम्) - परोक्ष -अनध्यतन भूतकाल =आज से पहले",
    "alut": "यन्ङन्ते कर्तरि लुट्लकारः (आत्मनेपदम्) - अनध्यतन भविष्य =आज के बाद",
    "alrut": "यन्ङन्ते कर्तरि लृट्लकारः (आत्मनेपदम्) - भविष्य",
    "alot": "यन्ङन्ते कर्तरि लोट्लकारः (आत्मनेपदम्) - आज्ञा अनुमति प्रशंसा प्रार्थना आशीर्वाद निमंत्रण",
    "alang": "यन्ङन्ते कर्तरि लङ्लकारः (आत्मनेपदम्) - अनध्यतन भूतकाल =आज से पहले",
    "avidhiling": "यन्ङन्ते कर्तरि विधिलिङ्लकारः (आत्मनेपदम्) - आज्ञा अनुमति प्रशंसा प्रार्थना निमंत्रण",
    "aashirling": "यन्ङन्ते कर्तरि आशीर्लिङ्लकारः (आत्मनेपदम्) - आशीर्वाद",
    "alung": "यन्ङन्ते कर्तरि लुङ्लकारः (आत्मनेपदम्)",
    "alrung": "यन्ङन्ते कर्तरि लृङ्लकारः (आत्मनेपदम्) - यदि ये होता भूतकाल"
}

def create_table(forms):
    forms_list = forms.split(";")
    rows = [forms_list[i:i+3] for i in range(0, len(forms_list), 3)]
    return pd.DataFrame(rows, columns=["1st", "2nd", "3rd"])

def display_dhatu(dhatu_code, dhatu_data):
    st.write(f"### {dhatu_code} (कौमुदीधातुः)")
    parasmaipadam = {key: value for key, value in dhatu_data.items() if key.startswith('pl')}
    atmanepadam = {key: value for key, value in dhatu_data.items() if key.startswith('al')}

    # Dynamically display all tables
    def display_tables(data, title):
        st.write(f"## {title}")
        for lakar, forms in data.items():
            if lakar in LAKAR_MAP:
                st.write(f"#### {LAKAR_MAP[lakar]}")
                table = create_table(forms)
                st.table(table)

    if parasmaipadam:
        display_tables(parasmaipadam, "परस्मैपदम्")

    if atmanepadam:
        display_tables(atmanepadam, "आत्मनेपदम्")

def search_dhatu(query, data):
    result = {key: value for key, value in data.items() if query in key}
    return result

def search_form(query, data):
    matching_dhatus = {}
    for dhatu_code, dhatu_data in data.items():
        for lakar, forms in dhatu_data.items():
            if query in forms:
                if dhatu_code not in matching_dhatus:
                    matching_dhatus[dhatu_code] = {}
                matching_dhatus[dhatu_code][lakar] = forms
    return matching_dhatus

# Streamlit UI
st.title("धातुरूप प्रदर्शनी")

dhatu_codes = list(DATA.keys())
search_query = st.text_input("धातु कोड या रूप खोजें:")
if search_query:
    search_results = search_dhatu(search_query, DATA)
    form_results = search_form(search_query, DATA)

    if search_results:
        st.write("### कोड के लिए खोज परिणाम:")
        for code, details in search_results.items():
            display_dhatu(code, details)

    if form_results:
        st.write("### रूप के लिए खोज परिणाम:")
        for code, details in form_results.items():
            st.write(f"#### धातु कोड: {code}")
            for lakar, forms in details.items():
                if lakar in LAKAR_MAP:
                    st.write(f"##### {LAKAR_MAP[lakar]}")
                    table = create_table(forms)
                    st.table(table)

    if not search_results and not form_results:
        st.write("### कोई परिणाम नहीं मिला।")
else:
    selected_dhatu = st.selectbox("धातु कोड चुनें:", dhatu_codes)
    display_dhatu(selected_dhatu, DATA[selected_dhatu])
