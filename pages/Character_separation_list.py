import streamlit as st
from panini.modules.separate_characters_list import separate_characters_and_map
import ast  # Safer alternative to eval for parsing Python objects

# App Title
st.title("Python List Character Separation Tool")

# App Description
st.markdown("""
Upload a `.txt` file containing a Python list (e.g., `['word1', 'word2', 'word3']`), 
and this app will process the list using the `separate_characters_and_map` function.
""")

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
        else:
            st.error("The uploaded file does not contain a valid Python list.")
    except SyntaxError:
        st.error("The file contains invalid Python syntax. Please ensure it contains a valid Python list.")
    except Exception as e:
        st.error(f"Error processing the file: {e}")
else:
    st.info("Please upload a `.txt` file containing a valid Python list.")

# Instructions Section
st.markdown("""
### Instructions:
1. Create a `.txt` file with a valid Python list, e.g.:2. Upload the file using the uploader above.
3. View the processed result and download it as a `.txt` file.
""")

