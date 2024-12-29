import os
import re  # Import the `re` module
import streamlit as st

# Define the folder to save uploaded files
DATA_FOLDER = "./data"

# Ensure the folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# Streamlit App
st.title("Text File Uploader, Viewer, and Finder")

# File uploader
uploaded_files = st.file_uploader("Upload .txt files", type=["txt"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Save each uploaded file to the /data folder
        save_path = os.path.join(DATA_FOLDER, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"Uploaded: {uploaded_file.name}")

# Get a list of all .txt files in the /data folder
txt_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".txt")]

if txt_files:
    # Dropdown to select a file or "All Files"
    selected_file = st.selectbox("Select a file to view", ["All Files"] + txt_files)

    # Word or Phrase Finder
    search_term = st.text_input("Enter a word or phrase to search for:")

    if selected_file == "All Files":
        st.subheader("All Files Content:")
        for file_name in txt_files:
            st.write(f"### {file_name}")
            file_path = os.path.join(DATA_FOLDER, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if search_term:
                    occurrences = len(re.findall(re.escape(search_term), content, flags=re.IGNORECASE))
                    st.markdown(f"**Occurrences of '{search_term}':** {occurrences}")
                    highlighted_content = re.sub(
                        re.escape(search_term),
                        f"**:blue[`{search_term}`]**",
                        content,
                        flags=re.IGNORECASE,
                    )
                else:
                    highlighted_content = content
                st.text_area(f"Content of {file_name}", highlighted_content, height=300)
    else:
        st.subheader(f"Content of {selected_file}:")
        file_path = os.path.join(DATA_FOLDER, selected_file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            if search_term:
                occurrences = len(re.findall(re.escape(search_term), content, flags=re.IGNORECASE))
                st.markdown(f"**Occurrences of '{search_term}':** {occurrences}")
                highlighted_content = re.sub(
                    re.escape(search_term),
                    f"**:blue[`{search_term}`]**",
                    content,
                    flags=re.IGNORECASE,
                )
            else:
                highlighted_content = content
            st.text_area("File Content", highlighted_content, height=300)
else:
    st.info("No .txt files found in the /data folder. Please upload files to view.")
