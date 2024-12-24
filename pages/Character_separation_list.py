import streamlit as st
from panini.modules.separate_characters_list import separate_characters_and_map
import ast  # Safer alternative to eval for parsing Python objects

# App Title
st.title("Python List Character Separation Tool")

# App Description
st.markdown("""
Upload a `.txt` file containing a Python list (e.g., `['word1', 'word2', 'word3']`), 
or directly input the list, and this app will process the list using the `separate_characters_and_map` function.
""")

# Option to choose input method
input_option = st.radio("Choose input method:", ("Upload File", "Enter Text"))

input_list = None

if input_option == "Upload File":
    # File Upload Section
    uploaded_file = st.file_uploader("Upload a Python List File (.txt)", type="txt")

    if uploaded_file is not None:
        try:
            # Read the uploaded file content
            file_content = uploaded_file.read().decode("utf-8").strip()

            # Safely parse the file content into a Python object
            parsed_content = ast.literal_eval(file_content)

            # Validate if the parsed content is a list
            if isinstance(parsed_content, list):
                input_list = parsed_content
                st.success("Python list successfully uploaded!")
                st.write("Uploaded List:", input_list)
            else:
                st.error("The uploaded file does not contain a valid Python list.")
        except SyntaxError:
            st.error("The file contains invalid Python syntax. Please ensure it contains a valid Python list.")
        except Exception as e:
            st.error(f"Error processing the file: {e}")

elif input_option == "Enter Text":
    # Text Input Section
    text_input = st.text_area("Enter a Python List (e.g., ['word1', 'word2', 'word3']):")

    if text_input:
        try:
            # Safely parse the text input into a Python object
            parsed_content = ast.literal_eval(text_input)

            # Validate if the parsed content is a list
            if isinstance(parsed_content, list):
                input_list = parsed_content
                st.success("Python list successfully entered!")
                st.write("Entered List:", input_list)
            else:
                st.error("The entered text does not contain a valid Python list.")
        except SyntaxError:
            st.error("The input contains invalid Python syntax. Please ensure it contains a valid Python list.")
        except Exception as e:
            st.error(f"Error processing the input: {e}")

# Processing and Output
if input_list is not None:
    # Process the list using the custom function
    output_list = separate_characters_and_map(input_list)
    st.write("Character Separation Result:", output_list)

    # Provide a download button for the result
    output_str = str(output_list)
    st.download_button(
        label="Download Result as .txt",
        data=output_str,
        file_name="processed_list.txt",
        mime="text/plain"
    )

# Instructions Section
st.markdown("""
### Instructions:
1. Create a `.txt` file with a valid Python list, e.g., `['word1', 'word2', 'word3']`, or directly enter it in the text box.
2. Upload the file or enter the text above.
3. View the processed result and download it as a `.txt` file.
""")
