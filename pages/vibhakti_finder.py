import streamlit as st
import json

# Function to load the .txt file
@st.cache_data
def load_data(uploaded_file):
    # Read the uploaded file as a string
    file_content = uploaded_file.read().decode("utf-8")
    data = json.loads(file_content)
    return data["data"]

# Function to search and filter the data
def search_data(data, query, filter_by=None):
    if not query:
        return data
    result = []
    for entry in data:
        if filter_by:
            if filter_by in entry and query.lower() in str(entry[filter_by]).lower():
                result.append(entry)
        else:
            if any(query.lower() in str(value).lower() for value in entry.values()):
                result.append(entry)
    return result

# Main Streamlit app
def main():
    st.title("Sanskrit Shabd Roop Vibhakti Finder")
    st.sidebar.header("Upload and Search")

    # File upload
    uploaded_file = st.sidebar.file_uploader("Upload the .txt file", type=["txt"])
    #shabdpath_2.txt
    if uploaded_file:
        data = load_data(uploaded_file)
        st.success("Data loaded successfully!")

        # Search query
        st.sidebar.header("Search Options")
        query = st.sidebar.text_input("Search Query", "")
        filter_by = st.sidebar.selectbox("Filter By", options=[None, "word", "linga", "grp", "end"], index=0)

        # Search results
        results = search_data(data, query, filter_by)

        if results:
            st.write(f"Found {len(results)} result(s):")
            for result in results:
                st.subheader(result.get("word", "Unknown Word"))
                st.write(f"Meaning: {result.get('artha', 'N/A')} ({result.get('artha_eng', 'N/A')})")
                st.write(
                    f"Linga: {result.get('linga', 'N/A')}, Group: {result.get('grp', 'N/A')}, Ending: {result.get('end', 'N/A')}")
                st.write(f"Forms: {result.get('forms', 'N/A')}")
                st.write(f"Tags: {result.get('tags', 'N/A')}")
                st.write(f"Amara Reference: {result.get('amara', 'N/A')}")
                st.write("---")
        else:
            st.warning("No results found.")
    else:
        st.info("Please upload a .txt file to start.")

if __name__ == "__main__":
    main()
