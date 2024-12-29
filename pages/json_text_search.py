import streamlit as st


def search_in_file(filepath, query, max_results=50):
    """Search for a keyword in the text file, limiting results to max_results."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()  # Read the entire file as a string
    except FileNotFoundError:
        st.error("Error: File not found. Please check the file path.")
        return []

    results = []
    query_len = len(query)
    start = 0

    while len(results) < max_results:  # Stop if we reach the maximum number of results
        # Find the query in the content
        start = content.find(query, start)
        if start == -1:
            break

        # Determine the snippet bounds
        snippet_start = max(0, start - 50)
        snippet_end = min(len(content), start + query_len + 300)

        # Extract the snippet
        snippet = content[snippet_start:snippet_end]

        # Highlight the query in the snippet
        highlighted_snippet = snippet.replace(query, f"<mark>{query}</mark>")
        results.append(highlighted_snippet)

        # Move past the current match
        start += query_len

    return results


def main():
    st.title("Sanskrit Text Keyword Search Tool")
    st.write("Search for keywords in the text file. The matched text will be highlighted in yellow.")

    # Hardcoded file path
    filepath = "data/kosh/skd/skd.json"  # Replace with your file path

    # Input for keyword
    query = st.text_input("Enter the keyword to search", "")

    if query:
        results = search_in_file(filepath, query, max_results=50)
        if results:
            st.success(f"Found {len(results)} result(s). (Showing up to 50 matches)")
            for i, snippet in enumerate(results, 1):
                st.markdown(f"**Result {i}:**")
                st.markdown(f"<div style='background-color: #fdfd96; padding: 10px;'>{snippet}</div>",
                            unsafe_allow_html=True)
        else:
            st.warning("No results found. Try a different query.")


if __name__ == "__main__":
    main()
