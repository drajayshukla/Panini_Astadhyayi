# Markdown Notes Section
st.sidebar.title("नोट्स")
st.sidebar.write("यहां अपने नोट्स जोड़ें:")

# Create a placeholder for notes
notes = st.sidebar.text_area("नोट्स:", value="", height=200)

# Optionally, allow downloading or saving notes
if st.sidebar.button("नोट्स सहेजें"):
    st.sidebar.write("नोट्स सहेजे गए।")

if st.sidebar.button("नोट्स डाउनलोड करें"):
    notes_file = "notes.txt"
    with open(notes_file, "w", encoding="utf-8") as file:
        file.write(notes)
    with open(notes_file, "rb") as file:
        st.sidebar.download_button("डाउनलोड करें", file, file_name=notes_file)

# Display the app content
st.title("धातुरूप प्रदर्शनी")

search_query = st.text_input("धातु कोड या रूप खोजें:")
if search_query:
    search_results = search_dhatu(search_query, DATA)
    form_results = search_form(search_query, DATA)

    if search_results:
        st.write("## कोड के लिए खोज परिणाम:")
        for set_name, dhatus in search_results.items():
            st.write(f"### {set_name}")
            for code, details in dhatus.items():
                display_dhatu(code, details)

    if form_results:
        st.write("## रूप के लिए खोज परिणाम:")
        for set_name, dhatus in form_results.items():
            st.write(f"### {set_name}")
            for code, details in dhatus.items():
                st.write(f"#### धातु कोड: {code}")
                for lakar, forms in details.items():
                    if lakar in LAKAR_MAP:
                        st.write(f"##### {LAKAR_MAP[lakar]}")
                        table = create_table(forms)
                        st.table(table)

    if not search_results and not form_results:
        st.write("### कोई परिणाम नहीं मिला।")
else:
    for set_name, dhatus in DATA.items():
        st.write(f"## {set_name}")
        dhatu_codes = list(dhatus.keys())
        selected_dhatu = st.selectbox(f"{set_name} से धातु कोड चुनें:", dhatu_codes)
        display_dhatu(selected_dhatu, dhatus[selected_dhatu])
