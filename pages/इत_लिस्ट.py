import streamlit as st

# Function to filter words based on suffix
def filter_by_suffix(words, suffix):
    return [word for word in words if word.endswith(suffix)]

# Function to filter words based on prefix
def filter_by_prefix(words, prefix):
    return [word for word in words if word.startswith(prefix)]

# Function to filter words containing specific anunasik characters
def filter_by_anunasik(words, anunasik_akshars):
    return [word for word in words if any(akshar in word for akshar in anunasik_akshars)]

# Streamlit App
st.title("Sanskrit Word Filter")

# Initialize words as an empty list
words = []

# User input: upload or enter list
upload_or_input = st.radio("How do you want to provide the list of words?", ("Upload File", "Enter Words Manually"))

if upload_or_input == "Upload File":
    uploaded_file = st.file_uploader("Upload a file containing words (one word per line):")
    if uploaded_file:
        words = uploaded_file.read().decode("utf-8").splitlines()
else:
    words_input = st.text_area("Enter words (separated by commas):")
    if words_input:
        words = [word.strip() for word in words_input.split(",")]

# Proceed if words are available
if words:
    # Filtering words
    ends_with_ष = filter_by_suffix(words, "ष्")
    ends_with_इर = filter_by_suffix(words, "इर्")

    starts_with_ञि = filter_by_prefix(words, "ञ्इ")
    starts_with_टु = filter_by_prefix(words, "ट्उ")
    starts_with_डु = filter_by_prefix(words, "ड्उ")

    anunasik_akshars = ["अँ", "आँ", "इँ", "ईँ", "उँ", "ऊँ", "ऋँ", "ॠँ", "ऌँ", "ॡँ", "एँ", "ओँ", "ऐँ", "औँ"]
    anunasik_words = filter_by_anunasik(words, anunasik_akshars)

    # Display results
    st.header("Filtered Words")
    st.subheader("Words ending with:")
    st.write(f"**ष्:** {ends_with_ष}")
    st.write(f"**इर्:** {ends_with_इर}")

    st.subheader("Words starting with:")
    st.write(f"**ञि:** {starts_with_ञि}")
    st.write(f"**टु:** {starts_with_टु}")
    st.write(f"**डु:** {starts_with_डु}")

    st.subheader("Words containing Anunasik Akshars:")
    st.write(anunasik_words)
else:
    st.info("Please provide a list of words to proceed.")
