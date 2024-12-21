import streamlit as st
import inspect
import panini.modules.separate_characters as separate_characters_module
import panini.modules.halant_handling as halant_handling_module
import panini.modules.merging_in_list as merging_in_list_module

def register_shared_resources():
    """
    Register all callable functions from the specified modules into `st.session_state.shared_resources`.
    """
    shared_resources = {}

    # List of modules to import functions from
    modules = [separate_characters_module, halant_handling_module, merging_in_list_module]

    for module in modules:
        # Add all callable objects (functions) to shared resources
        for name, obj in inspect.getmembers(module, inspect.isfunction):
            shared_resources[name] = obj

    st.session_state.shared_resources = shared_resources

# Register shared resources at app startup
if "shared_resources" not in st.session_state:
    register_shared_resources()

# Streamlit app title
st.title("Pāṇini's Sanskrit Grammar Toolkit")
st.sidebar.title("Navigation")
st.sidebar.markdown("Use the sidebar to navigate between grammar modules.")
