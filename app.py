import streamlit as st

# Main navigation
st.sidebar.title("Pāṇini Aṣṭādhyāyī Explorer")
st.sidebar.write("Select a feature to explore:")

# Navigation options
page = st.sidebar.radio(
    "Go to:",
    ("Home", "Cheta (Character Processing)", "Vriddhi", "Sandhi", "Samasa")
)

# Navigate to the selected page
if page == "Home":
    st.title("Welcome to the Pāṇini Aṣṭādhyāyī Explorer")
    st.write("Explore the brilliance of Pāṇini's grammar through modern tools.")
elif page == "Cheta (Character Processing)":
    from pages import cheta
    cheta.run()
elif page == "vriddhi_testing":
    from pages import vriddhi
    vriddhi.run()
elif page == "Sandhi":
    from pages import sandhi
    sandhi.run()
elif page == "Samasa":
    from pages import samasa
    samasa.run()
