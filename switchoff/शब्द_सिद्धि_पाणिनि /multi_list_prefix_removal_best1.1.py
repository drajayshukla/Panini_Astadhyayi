import streamlit as st


def find_common_prefix(words):
    """
    Finds the common prefix among a list of words.
    """
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def prefix_removal(strings, prefix):
    """
    Removes the prefix from each string in the list.
    """
    return [value.replace(prefix, "") for value in strings]


def process_multiple_lists(lists):
    """
    Processes multiple lists of semicolon-delimited text:
    - Finds the common prefix for each list.
    - Removes the prefix from the list elements.
    Returns the results in a structured format.
    """
    results = []
    for lst in lists:
        words = [word.strip() for word in lst.split(";") if word.strip()]
        common_prefix = find_common_prefix(words)
        modified_list = prefix_removal(words, common_prefix)
        results.append({
            "original_list": lst,
            "common_prefix": common_prefix,
            "modified_list": modified_list
        })
    return results


def process_file(uploaded_file):
    """
    Reads the uploaded .txt file and processes each line.
    """
    # Read lines from the uploaded file
    lines = uploaded_file.readlines()
    raw_lists = [line.decode("utf-8").strip("[]").strip() for line in lines if line.strip()]
    results = process_multiple_lists(raw_lists)

    # Prepare the output
    output_lines = []
    for i, result in enumerate(results, start=1):
        output_lines.append(f"List {i}:")
        output_lines.append(f"Original List: {result['original_list']}")
        output_lines.append(f"Common Prefix: {result['common_prefix']}")
        output_lines.append(f"Modified List: {', '.join(result['modified_list'])}")
        output_lines.append("")  # Add a blank line for readability
    return "\n".join(output_lines)


def main():
    st.title("Multi-list Prefix Processor from File")

    # File upload
    uploaded_file = st.file_uploader("Upload a .txt file containing semicolon-delimited lists:", type="txt")

    if uploaded_file is not None:
        # Process the file
        processed_output = process_file(uploaded_file)

        # Display the processed output
        st.subheader("Processed Output")
        st.text_area("Output:", processed_output, height=400)

        # Provide a download option for the processed file
        st.download_button(
            label="Download Processed File",
            data=processed_output,
            file_name="processed_output.txt",
            mime="text/plain",
        )


if __name__ == "__main__":
    main()
