import streamlit as st

# Define Vowels (स्वर)
vowels = ["अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ॠ", "ऌ", "ॡ", "ए", "ऐ", "ओ", "औ", "अं", "अः"]

# Define Consonants (व्यंजन)
consonants = [
    "क", "ख", "ग", "घ", "ङ",
    "च", "छ", "ज", "झ", "ञ",
    "ट", "ठ", "ड", "ढ", "ण",
    "त", "थ", "द", "ध", "न",
    "प", "फ", "ब", "भ", "म",
    "य", "र", "ल", "व",
    "श", "ष", "स", "ह",
    "क्ष", "त्र", "ज्ञ"
]

# Define Matras (मात्राएँ)
matras = ["", "ा", "ि", "ी", "ु", "ू", "ृ", "ॄ", "ॢ", "ॣ", "े", "ै", "ो", "ौ", "ं", "ः"]

# Generate Full Devanagari Index
full_index = vowels[:]
for consonant in consonants:
    for matra in matras:
        full_index.append(consonant + matra)

# Add standalone consonants for completion
full_index += consonants

# Load the data
def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()

# Filter data by Devanagari index
def filter_by_devanagari(data, letter):
    return [line for line in data if line.startswith(letter)]

# Filter data by index range
def filter_by_index_range(data, start, end):
    return data[start:end]

# Main Streamlit app
def main():
    st.title("Sanskrit Word Search with Full Devanagari Index")
    st.subheader("Search and filter words using Devanagari index and word range.")

    # Load data
    uploaded_file = st.file_uploader("Upload Sanskrit Text File", type="txt")
    if uploaded_file:
        data = load_data(uploaded_file)

        # Select Devanagari index
        st.sidebar.header("Filters")
        st.sidebar.subheader("Filter by Devanagari Index")
        selected_letter = st.sidebar.selectbox(
            "Choose a Devanagari Letter or Combination",
            ["All"] + full_index
        )

        # Filter by index range
        st.sidebar.subheader("Filter by Word Index Range")
        start_index = st.sidebar.number_input("Start Index", min_value=0, max_value=len(data) - 1, value=0)
        end_index = st.sidebar.number_input("End Index", min_value=0, max_value=len(data), value=len(data))

        # Apply filters
        filtered_data = data
        if selected_letter != "All":
            filtered_data = filter_by_devanagari(filtered_data, selected_letter)
        filtered_data = filter_by_index_range(filtered_data, start_index, end_index)

        # Display results
        st.subheader("Filtered Results")
        if filtered_data:
            for idx, line in enumerate(filtered_data, start=start_index):
                st.text(f"{idx}: {line.strip()}")
        else:
            st.warning("No words found for the selected filters.")

        # Option to show full text
        if st.checkbox("Show Full Text"):
            st.text_area("Uploaded Text Content", "\n".join(data), height=300)

    else:
        st.info("Please upload a Sanskrit text file to get started.")

if __name__ == "__main__":
    main()
