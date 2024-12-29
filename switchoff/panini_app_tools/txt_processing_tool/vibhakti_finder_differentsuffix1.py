import streamlit as st
import json
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

# Main Streamlit app
def main():
    st.title("JSON Suffix Removal and Update App")
    st.sidebar.header("Upload JSON File")

    # File upload
    uploaded_file = st.sidebar.file_uploader("Upload the .json file", type=["json"])
    if uploaded_file:
        # Load JSON data
        data = load_json_data(uploaded_file)
        st.success("Data loaded successfully!")

        # Add new entry with suffix-only data
        updated_data = add_suffix_only_entry(data)

        # Display sample result
        st.header("Updated JSON Sample")
        st.write(json.dumps(updated_data[:3], ensure_ascii=False, indent=4))

        # Downloadable updated JSON file
        st.download_button(
            label="Download Updated JSON",
            data=json.dumps(updated_data, ensure_ascii=False, indent=4),
            file_name="updated_data.json",
            mime="application/json"
        )
    else:
        st.info("Please upload a .json file to start.")

if __name__ == "__main__":
    main()
