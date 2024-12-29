import streamlit as st

def add_prefix_to_lists(lists, prefix):
    """
    Attaches a prefix to each word in multiple lists.

    Args:
        lists (list): A list of lists containing words.
        prefix (str): The prefix to attach.

    Returns:
        list: A list of final merged words with the prefix.
    """
    final_words = []
    for word_list in lists:
        merged_list = [f"{prefix}{word}" for word in word_list]
        final_words.extend(merged_list)  # Merge all lists into a single list
    return final_words

def main():
    st.title("Attach Prefix to Lists of Words")

    # Input: Text area for multiple lists
    input_text = st.text_area(
        "Enter lists of words (one list per line, words separated by commas):",
        "[अः, औ, आः, अम्, औ, आन्, एन, आभ्याम्, ऐः, आय, आभ्याम्, एभ्यः, आत्-आद्, आभ्याम्, एभ्यः, अस्य, अयोः, आनाम्, ए, अयोः, एषु, अ, औ, आः]\n"
        "[ः, ौ, ाः, म्, ौ, ान्, ेन, ाभ्याम्, ैः, ाय, आभ्याम्, ेभ्यः, ात्-ाद्, ाभ्याम्, ेभ्यः, स्य, योः, ानाम्, े, योः, ेषु, , ौ, ाः]\n"
        "[ः, ौ, ाः, म्, ौ, ान्, ेण, आभ्याम्, ैः, ाय, आभ्याम्, ेभ्यः, ात्-ाद्, ाभ्याम्, ेभ्यः, स्य, योः, ाणाम्, े, योः, ेषु, , ौ, ाः]"
    )

    # Input: Prefix word
    prefix = st.text_input("Enter the prefix to attach to each word:", "राम")

    if st.button("Generate Final Words"):
        try:
            # Convert input text into lists of words
            word_lists = []
            for line in input_text.strip().split("\n"):
                line = line.strip("[]")  # Remove square brackets
                words = [word.strip() for word in line.split(",") if word.strip()]  # Split by commas and strip
                word_lists.append(words)

            # Attach the prefix to all words
            final_words = add_prefix_to_lists(word_lists, prefix)

            # Display results
            st.subheader("Final Words List")
            st.text_area("Output:", ", ".join(final_words), height=200)

            # Provide download option for final words
            final_output = "\n".join(final_words)
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
