import streamlit as st


# Load file content
@st.cache_data
def load_file(uploaded_file):
    return uploaded_file.read().decode("utf-8")


def find_context(raw_text, search_term, before=10, after=50):
    """
    Search for a term in the raw text and extract context.
    Returns a list of matches with 10 words before and 50 words after the search term.
    """
    words = raw_text.split()
    results = []

    # Find indices of matches
    for i, word in enumerate(words):
        if search_term in word:
            before_text = " ".join(words[max(0, i - before):i])
            after_text = " ".join(words[i + 1:min(len(words), i + after + 1)])
            context = f"{before_text} {search_term} {after_text}"
            results.append(context)
    return results


# Streamlit app
def main():
    st.title("Keyword Search in Text")
    st.write(
        "Upload any file, and search for a keyword or phrase. The app will show 10 words before and 50 words after the searched term.")

    # Upload file
    uploaded_file = st.file_uploader("Upload a text file", type=["txt", "json"])

    if uploaded_file:
        # Load file content
        raw_text = load_file(uploaded_file)

        # Search term input
        search_term = st.text_input("Enter a keyword or phrase to search:")

        # Button to search
        if st.button("Search"):
            if search_term.strip():
                results = find_context(raw_text, search_term)
                if results:
                    st.write(f"Found {len(results)} match(es):")
                    for i, result in enumerate(results, 1):
                        st.markdown(f"**Match {i}:** {result}")
                else:
                    st.write("No matches found.")
            else:
                st.write("Please enter a valid keyword or phrase.")


if __name__ == "__main__":
    main()
