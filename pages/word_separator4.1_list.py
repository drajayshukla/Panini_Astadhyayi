import streamlit as st


# Streamlit app
def main():
    st.title("Prefix Removal App")
    st.write("This app removes a specified prefix from a list of strings.")

    # Input for prefix to remove
    prefix = st.text_input("Enter the prefix to remove (e.g., 'श्अम्भ्'):", value="श्अम्भ्")

    # Input for the list of strings
    st.write("Enter the list of strings (separated by commas):")
    original_list_input = st.text_area("List of strings:", value="श्अम्भ्अव्ः, श्अम्भ्उम्, श्अम्भ्ऊ")

    # Process the input into a list
    original_list = [item.strip() for item in original_list_input.split(",") if item.strip()]

    if original_list and prefix:
        st.write("### Original List")
        st.write(original_list)

        # Remove prefix and create a dictionary
        modified_dict = {i: value.replace(prefix, "") for i, value in enumerate(original_list)}

        st.write("### Modified Dictionary")
        st.json(modified_dict)
    else:
        st.warning("Please enter both a prefix and a list of strings.")


# Run the app
if __name__ == "__main__":
    main()
