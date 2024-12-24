import streamlit as st
from panini.modules.separate_characters_list import separate_characters_and_map

# App Title
st.title("Text Character Separation Tool")

# App Description
st.markdown("""
Upload a `.txt` file containing any text, or directly input the text, 
and this app will process the text using the `separate_characters_and_map` function.
""")

# Option to choose input method
input_option = st.radio("Choose input method:", ("Upload File", "Enter Text"))

input_text = None

if input_option == "Upload File":
    # File Upload Section
    uploaded_file = st.file_uploader("Upload a Text File (.txt)", type="txt")

    if uploaded_file is not None:
        try:
            # Read the uploaded file content
            input_text = uploaded_file.read().decode("utf-8").strip()
            st.success("File successfully uploaded!")
            st.write("Uploaded Text:")
            st.text(input_text)
        except Exception as e:
            st.error(f"Error processing the file: {e}")

elif input_option == "Enter Text":
    # Text Input Section
    input_text = st.text_area("Enter any text below:")

    if input_text:
        st.success("Text successfully entered!")
        st.write("Entered Text:")
        st.text(input_text)

# Processing and Output
if input_text:
    # Process the text using the custom function
    output_result = separate_characters_and_map(input_text)
    st.write("Character Separation Result:", output_result)

    # Provide a download button for the result
    output_str = str(output_result)
    st.download_button(
        label="Download Result as .txt",
        data=output_str,
        file_name="processed_text.txt",
        mime="text/plain"
    )

# Instructions Section
st.markdown("""
### Instructions:
1. Upload a `.txt` file containing any text, or directly enter your text in the box.
2. View the processed result and download it as a `.txt` file.
""")
