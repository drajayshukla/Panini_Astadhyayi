import streamlit as st
from panini.modules.separate_characters import separate_characters_and_map

# Title of the app
st.title("गुण-वृद्धि Interactive Explanation")

# Header
st.header("गुण-वृद्धि (गुण and वृद्धि Substitutions)")

# Introduction
st.write("""
This app explains and demonstrates the application of `गुण` and `वृद्धि` rules as defined in Pāṇini's grammar. 
The user can explore derivations interactively.
""")

# Explanation Section
st.subheader("Theory")
st.write("""
- **गुणः (1.1.2)**: Denotes the substitution of `ए`, `ओ`, or `अय` based on the context.
- **वृद्धिः (1.1.1)**: Denotes the substitution of `ऐ`, `औ`, or `आय` based on the context.
- These substitutions apply to `इक्` letters (इ, उ, ऋ, ऌ).
- If `गुणः` or `वृद्धिः` is mentioned without specifying where the substitution occurs, it applies to `इक्` letters in their place.
""")

# Input Section for Character Mapping
st.header("Input Section")
input_string = st.text_input("Enter a string (e.g., 'चिञ् तृच्')", "चिञ् तृच्")

if input_string:
    st.subheader("Input String")
    st.write(input_string)

    # Step 1: Character Separation and Mapping
    try:
        output_string = separate_characters_and_map(input_string)
        st.subheader("Step 1: Character Separation")
        st.write(output_string)
    except Exception as e:
        st.error(f"Error in processing input string: {e}")

# Inputs for derivations
st.subheader("Derivation Input")
col1, col2 = st.columns(2)

with col1:
    first_word = st.text_input("Enter the first word:")
with col2:
    second_word = st.text_input("Enter the second word:")

# Function to apply गुण and वृद्धि
def apply_guna_vriddhi(first_word, second_word):
    if first_word.endswith("अ") and second_word.startswith("इ"):
        return first_word[:-1] + "ए" + second_word[1:], "गुणः"
    elif first_word.endswith("अ") and second_word.startswith("ई"):
        return first_word[:-1] + "ए" + second_word[1:], "गुणः"
    elif first_word.endswith("आ") and second_word.startswith("इ"):
        return first_word[:-1] + "ए" + second_word[1:], "गुणः"
    elif first_word.endswith("आ") and second_word.startswith("ई"):
        return first_word[:-1] + "ए" + second_word[1:], "गुणः"
    elif first_word.endswith("अ") and second_word.startswith("उ"):
        return first_word[:-1] + "ओ" + second_word[1:], "गुणः"
    elif first_word.endswith("अ") and second_word.startswith("ऊ"):
        return first_word[:-1] + "ओ" + second_word[1:], "गुणः"
    elif first_word.endswith("अ") and second_word.startswith("ऋ"):
        return first_word[:-1] + "अर्" + second_word[1:], "गुणः"
    elif first_word.endswith("आ") and second_word.startswith("ऋ"):
        return first_word[:-1] + "आर्" + second_word[1:], "गुणः"
    else:
        return "Invalid combination", None

# Display the result
if st.button("Apply गुण-वृद्धि"):
    st.subheader("Apply गुण-वृद्धि with Examples")
    if st.button("Apply गुण-वृद्धि"):
        if first_word and second_word:
            # Step 1: Character Separation
            first_word = separate_characters_and_map(first_word)
            second_word = separate_characters_and_map(second_word)

            # Apply the गुण-वृद्धि logic
            result, rule_applied = apply_guna_vriddhi(first_word, second_word)
            if rule_applied:
                st.success(f"Result: {result} ({rule_applied})")
            else:
                st.error(result)
        else:
            st.error("Please enter both the first and second words.")

    # Demo Examples
    st.subheader("Demo Examples")
    examples = [
        ("मिद्", "इति"),
        ("मृज्", "अनीयर्"),
        ("पठ्", "अनीयर्"),
        ("दिव्", "औ"),
        ("या", "अनीयर्")
    ]

    st.write("Here are some example inputs to try:")
    for i, (first, second) in enumerate(examples, start=1):
        st.write(f"Example {i}: {first} + {second}")
        demo_result, demo_rule = apply_guna_vriddhi(first, second)
        if demo_rule:
            st.write(f"Result: {demo_result} ({demo_rule})")
        else:
            st.write("Invalid combination")
    

# Explanation of Derivations
st.subheader("Examples and Explanation")

example_selected = st.selectbox("Choose an Example", [
    "मिदेर्गुणः",
    "मृजेर्वृद्धिः",
    "या अनीयर्",
    "दिव औत्"
])

if example_selected == "मिदेर्गुणः":
    st.write("""
    Example: मिद् + श्यन् → मेद्यति

    1. `मिदेर्गुणः 7.3.82`: The `मिद्` root undergoes `गुणः` substitution because `श्यन्` is a शित् प्रत्यय.
    2. The इकः is identified and replaced using the rule `इको गुणवृद्धी 1.1.3`.
    """)
elif example_selected == "मृजेर्वृद्धिः":
    st.write("""
    Example: मृज् + अनीयर् → मार्जनीय

    1. `मृजेर्वृद्धिः 7.2.114`: The `मृज्` root undergoes `वृद्धिः` substitution due to the प्रत्यय `अनीयर्`.
    2. The ऋकारः is replaced with `आर्` using `इको गुणवृद्धी 1.1.3`.
    """)
elif example_selected == "या अनीयर्":
    st.write("""
    Example: या + अनीयर् → यानीय

    1. Here, गुणः cannot apply since the final vowel is not an इक् letter.
    2. The result is achieved using `सवर्णदीर्घः 6.1.101`.
    """)
elif example_selected == "दिव औत्":
    st.write("""
    Example: दिव् + औ → द्यौः

    1. `दिव औत् 7.1.84`: The औकारः substitution does not involve इक्, so the rule does not apply.
    2. The final result is achieved using other rules like `अलोऽन्त्यस्य 1.1.52`.
    """)

# Sidebar for additional information
st.sidebar.header("Additional Information")
st.sidebar.write("""
- This app is designed to assist students of Vyākaraṇa.
- It provides derivation logic interactively for common rules.
""")

st.sidebar.write("Contact: Dr. Ajay Shukla for suggestions and enhancements.")
