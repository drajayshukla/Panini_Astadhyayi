import streamlit as st
import json
from io import BytesIO

def load_file(file):
    """Load the file content."""
    content = file.read().decode('utf-8')
    return content

def convert_to_json(content):
    """Convert JSON-like text content to a valid JSON object."""
    try:
        # Convert the JSON-like string into a Python dictionary
        data = json.loads(content)
        return data
    except json.JSONDecodeError as e:
        st.error(f"Error decoding JSON: {e}")
        return None

def download_json(json_data):
    """Prepare JSON data for download."""
    return BytesIO(json.dumps(json_data, indent=4).encode('utf-8'))

# Streamlit app
st.title("JSON Converter with Download Option")

uploaded_file = st.file_uploader("Upload a .txt file with JSON-like structure", type="txt")

if uploaded_file:
    # Read and display the raw file content
    st.subheader("Raw File Content")
    raw_content = load_file(uploaded_file)
    st.text(raw_content)

    # Attempt to convert to JSON
    st.subheader("Converted JSON")
    json_data = convert_to_json(raw_content)

    if json_data:
        # Display the JSON as formatted text
        st.json(json_data)

        # Create a download link for the JSON file
        st.subheader("Download JSON File")
        json_file = download_json(json_data)
        st.download_button(
            label="Download JSON",
            data=json_file,
            file_name="converted.json",
            mime="application/json"
        )
