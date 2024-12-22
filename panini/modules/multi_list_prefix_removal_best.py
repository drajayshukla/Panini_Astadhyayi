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

def main():
    st.title("Multi-list Prefix Processor")

    # Input: Multiple lists separated by newlines
    input_text = st.text_area(
        "Enter multiple semicolon-delimited lists (one per line):",
        "[देवः;देवौ;देवाः;देवम्;देवौ;देवान्;देवेन;देवाभ्याम्;देवैः;देवाय;देवाभ्याम्;देवेभ्यः;देवात्-देवाद्;देवाभ्याम्;देवेभ्यः;देवस्य;देवयोः;देवानाम्;देवे;देवयोः;देवेषु]\n"
        "[रामः;रामौ;रामाः;रामम्;रामौ;रामान्;रामेण;रामाभ्याम्;रामैः;रामाय;रामाभ्याम्;रामेभ्यः;रामात्-रामाद्;रामाभ्याम्;रामेभ्यः;रामस्य;रामयोः;रामाणाम्;रामे;रामयोः;रामेषु]\n"
        "[सर्वः;सर्वौ;सर्वे;सर्वम्;सर्वौ;सर्वान्;सर्वेण;सर्वाभ्याम्;सर्वैः;सर्वस्मै;सर्वाभ्याम्;सर्वेभ्यः;सर्वस्मात्-सर्वस्माद्;सर्वाभ्याम्;सर्वेभ्यः;सर्वस्य;सर्वयोः;सर्वेषाम्;सर्वस्मिन्;सर्वयोः;सर्वेषु]\n"
        "[विश्वः;विश्वौ;विश्वे;विश्वम्;विश्वौ;विश्वान्;विश्वेन;विश्वाभ्याम्;विश्वैः;विश्वस्मै;विश्वाभ्याम्;विश्वेभ्यः;विश्वस्मात्-विश्वस्माद्;विश्वाभ्याम्;विश्वेभ्यः;विश्वस्य;विश्वयोः;विश्वेषाम्;विश्वस्मिन्;विश्वयोः;विश्वेषु]"
    )

    if st.button("Process Lists"):
        # Split the input text into separate lists
        raw_lists = [line.strip("[]").strip() for line in input_text.split("\n") if line.strip()]
        results = process_multiple_lists(raw_lists)

        for i, result in enumerate(results, start=1):
            st.subheader(f"List {i}")
            st.write(f"**Original List**: {result['original_list']}")
            st.write(f"**Common Prefix**: {result['common_prefix']}")
            st.write(f"**Modified List**: {', '.join(result['modified_list'])}")

if __name__ == "__main__":
    main()
