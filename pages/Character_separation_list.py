import streamlit as st
from panini.modules.separate_characters import separate_characters_and_map


# Streamlit Header
st.title("Character Separation Tool")
st.markdown('''
Upload a Python list containing words, and this app will process the list to separate characters based on the rules in your custom `separate_characters_and_map` function.
''')

# File Upload for Python List
uploaded_file = st.file_uploader("Upload a Python list file (.txt)", type="txt")

if uploaded_file is not None:
    # Read the uploaded file
    try:
        content = uploaded_file.read().decode("utf-8")
        # Convert the uploaded content into a Python list
        input_list = eval(content.strip())  # Ensure the input is a valid Python list
        if not isinstance(input_list, list):
            st.error("The uploaded file does not contain a valid Python list.")
        else:
            st.success("Python list successfully loaded!")
            st.write("Uploaded List:", input_list)

            # Process the list using the separate_characters_and_map function
            output_list = separate_characters_and_map(input_list)
            st.write("Characters Separation Result:", output_list)
    except Exception as e:
        st.error(f"Error processing the uploaded file: {e}")
else:
    st.info("Please upload a Python list file to begin.")

# Note for the user
st.markdown("""
### Instructions:
1. Create a `.txt` file containing a Python list, e.g., `['word1', 'word2', 'word3']`.
2. Upload the file using the button above.
3. The app will process the list and display the results.
""")
