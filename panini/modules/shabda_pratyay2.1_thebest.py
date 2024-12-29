import streamlit as st

def add_prefix_and_tag_to_lists(lists, prefix):
    """
    Attaches a prefix and tags the first 21 words in multiple lists.

    Args:
        lists (list): A list of lists containing words.
        prefix (str): The prefix to attach.

    Returns:
        list: A list of final merged lists with the prefix and tags.
    """
    tag_suffixes = [
        "_11", "_12", "_13", "_21", "_22", "_23", "_31", "_32", "_33",
        "_41", "_42", "_43", "_51", "_52", "_53", "_61", "_62", "_63",
        "_71", "_72", "_73"
    ]
    final_lists = []

    for word_list in lists:
        tagged_list = []
        for idx, word in enumerate(word_list):
            tagged_word = f"{prefix}{word}"  # Attach the prefix
            # Add a tag if within the first 21 words
            if idx < len(tag_suffixes):
                tagged_word += tag_suffixes[idx]
            tagged_list.append(tagged_word)
        final_lists.append(tagged_list)  # Append the processed list to final lists

    return final_lists

def process_uploaded_file(uploaded_file):
    """
    Reads the uploaded file and converts the contents into lists of words.

    Args:
        uploaded_file: The uploaded .txt file.

    Returns:
        list: A list of lists containing words.
    """
    word_lists = []
    content = uploaded_file.read().decode("utf-8").strip()
    for line in content.split("\n"):
        line = line.strip("[]")  # Remove square brackets
        words = [word.strip() for word in line.split(",") if word.strip()]  # Split by commas and strip whitespace
        word_lists.append(words)
    return word_lists

def main():
    st.title("Attach Prefix and Tag Words in Uploaded File")

    # File upload
    uploaded_file = st.file_uploader("Upload a .txt file containing word lists:", type="txt")

    # Input: Prefix word
    prefix = st.text_input("Enter the prefix to attach to each word:", "राम")

    if uploaded_file and st.button("Generate Final Words"):
        try:
            # Process the uploaded file into lists of words
            word_lists = process_uploaded_file(uploaded_file)

            # Attach the prefix and tag the first 21 words
            final_lists = add_prefix_and_tag_to_lists(word_lists, prefix)

            # Format final output as lists enclosed in []
            final_output = "\n".join(["[" + ", ".join(word_list) + "]" for word_list in final_lists])

            # Display results
            st.subheader("Final Words List")
            st.text_area("Output:", final_output, height=300)

            # Provide download option for final words
            st.download_button(
                label="Download Final Words",
                data=final_output,
                file_name="final_words.txt",
                mime="text/plain",
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
