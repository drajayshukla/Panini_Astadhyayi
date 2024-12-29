import streamlit as st


def add_suffixes(input_text, delimiter):
    """
    Add specific suffixes to input text based on the delimiter.
    """
    suffixes = [
        "_11", "_12", "_13", "_21", "_22", "_23", "_31", "_32", "_33",
        "_41", "_42", "_43", "_51", "_52", "_53", "_61", "_62", "_63",
        "_71", "_72", "_73"
    ]
    # Split input text based on the selected delimiter
    words = input_text.split(",") if delimiter == "comma" else input_text.split(";")
    # Add suffixes to the words
    modified_words = [f"{word.strip()}{suffix}" for word, suffix in zip(words, suffixes)]
    return modified_words


def main():
    st.title("Add Suffixes to Input Text")

    # Input text area
    input_text = st.text_area(
        "Enter the text (separated by comma or semicolon):",
        "सखीः;सख्यौ;सख्यः;सख्यम्;सख्यौ;सख्यः;सख्या;सखीभ्याम्;सखीभिः;सख्ये;सखीभ्याम्;सखीभ्यः;सख्युः;सखीभ्याम्;सखीभ्यः;सख्युः;सख्योः;सख्याम्;सख्यि;सख्योः;सखीषु"
    )

    # Select delimiter
    delimiter = st.radio("Select delimiter:", ["comma", "semicolon"], index=1)

    # Add suffixes when the button is clicked
    if st.button("Add Suffixes"):
        modified_words = add_suffixes(input_text, delimiter)
        st.subheader("Modified Text:")
        st.text("; ".join(modified_words) if delimiter == "semicolon" else ", ".join(modified_words))


if __name__ == "__main__":
    main()
