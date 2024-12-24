import streamlit as st

def remove_anunasik_akshar(word):
    """
    Removes anunāsika characters from a single word and replaces them with 'इत्'.
    """
    anunasik_akshar = ['अँ', 'आँ', 'इँ', 'ईँ', 'उँ', 'ऊँ', 'ऋँ', 'ॠँ', 'ऌँ', 'ॡँ', 'एँ', 'ओँ', 'ऐँ', 'औँ']
    for akshar in anunasik_akshar:
        word = word.replace(akshar, 'इत्')
    return word

def process_text(text):
    """
    Processes the text, replacing all anunāsika characters with 'इत्'.
    """
    words = text.split()
    processed_words = [remove_anunasik_akshar(word) for word in words]
    return " ".join(processed_words)

# Streamlit App
st.title("Anunasik Akshar Processor")
st.write("Upload a .txt file or enter text to process and replace anunāsika characters with 'इत्'.")

# Option to upload a .txt file
uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
input_text = st.text_area("Or enter text manually:")

# Process the text if either input is provided
if uploaded_file is not None or input_text:
    if uploaded_file is not None:
        # Read the uploaded file
        text = uploaded_file.read().decode("utf-8")
    else:
        text = input_text

    # Process the text
    processed_text = process_text(text)
    st.subheader("Processed Text:")
    st.text(processed_text)

    # Provide download option for processed text
    st.download_button(
        label="Download Processed Text",
        data=processed_text,
        file_name="processed_text.txt",
        mime="text/plain",
    )
