import streamlit as st

# Streamlit App
st.title("Text File Viewer")

# File upload widget
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file is not None:
    try:
        # Read the content of the uploaded file
        file_content = uploaded_file.read().decode("utf-8")

        # Display the content in a text area
        st.subheader("File Content:")
        st.text_area("Text Content", file_content, height=300)
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
else:
    st.info("Please upload a .txt file to view its content.")
