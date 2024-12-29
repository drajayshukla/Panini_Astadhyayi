import streamlit as st


def find_common_prefix(words):
    """
    Finds the common prefix (word unit) among a list of words.
    """
    if not words:
        return ""
    # Start with the first word as the base prefix
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def process_text(input_text, delimiter=";"):
    """
    Processes the input text, splits by delimiter, and finds the common prefix.
    """
    words = [word.strip() for word in input_text.split(delimiter) if word.strip()]
    common_prefix = find_common_prefix(words)
    return common_prefix


def main():
    st.title("Common Word Unit Finder")

    # Input text
    input_text = st.text_area(
        "Enter the text separated by a delimiter (e.g., ';')",
        "स्अख्ईः;स्अख्य्औ;स्अख्य्ः;स्अख्य्अम्;स्अख्य्औ;स्अख्य्ः;स्अख्य्आ;स्अख्ईभ्य्आम्;स्अख्ईभ्इः;स्अख्य्ए;"
        "स्अख्ईभ्य्आम्;स्अख्ईभ्य्ः;स्अख्य्उः;स्अख्ईभ्य्आम्;स्अख्ईभ्य्ः;स्अख्य्उः;स्अख्य्ओः;स्अख्य्आम्;"
        "स्अख्य्इ;स्अख्य्ओः;स्अख्ईष्उ"
    )

    delimiter = st.text_input("Enter the delimiter used in the text:", ";")

    if st.button("Find Common Word Unit"):
        common_word_unit = process_text(input_text, delimiter)
        if common_word_unit:
            st.success(f"The common word unit is: {common_word_unit}")
        else:
            st.warning("No common word unit found!")


if __name__ == "__main__":
    main()
