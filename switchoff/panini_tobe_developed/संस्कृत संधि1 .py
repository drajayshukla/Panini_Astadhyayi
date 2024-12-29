import streamlit as st

# Streamlit app title
st.title("Sanskrit Sandhi Rule Application")

# Define phonetic groups
mahe = ['अ', 'इ', 'उ', 'ण्', 'ऋ', 'ऌ', 'क्', 'ए', 'ओ', 'ङ्', 'ऐ', 'औ', 'च्', 'ह', 'य', 'व', 'र', 'ट्', 'ल', 'ण्',
        'ञ', 'म', 'ङ', 'ण', 'न', 'म्', 'झ', 'भ', 'ञ्', 'घ', 'ढ', 'ध', 'ष्', 'ज', 'ब', 'ग', 'ड', 'द', 'श्',
        'ख', 'फ', 'छ', 'ठ', 'थ', 'च', 'ट', 'त', 'व्', 'क', 'प', 'य्', 'श', 'ष', 'स', 'र्', 'ह', 'ल्']

ach = ['अ', 'इ', 'उ', 'ऋ', 'ऌ', 'ए', 'ओ', 'ऐ', 'औ']
ik = ['इ', 'उ', 'ऋ', 'ऌ']
yan = ['य', 'व', 'र', 'ल']
ech = ['ए', 'ओ', 'ऐ', 'औ']
ak = ['अ', 'इ', 'उ', 'ऋ', 'ऌ']
aat = ['अ', 'आ']

# Display phonetic groups
st.header("Phonetic Groups")
st.write("ik =", ik)
st.write("ech =", ech)

# Options for sandhi rules
st.header("Sandhi Rule Lagaye")
b = st.radio("'ach' ke basis par operations lagaye?", options=["Haan (Yes)", "Nahi (No)"])
if b == "Haan (Yes)":
    st.write("LUNG, LANG, Lṛṅ lakāras ke liye 6.4.72 rule se 'āt'-āgama (prefix) aata hai.")

    a1234 = st.radio("'ak' varṇa ke baad 'am' jo 'a' par khatam hota hai, us par lagaye?",
                     options=["Haan (Yes)", "Nahi (No)"])
    if a1234 == "Haan (Yes)":
        st.write("'ak' varṇa ke baad 'am' hone par, pehla akshar apne original form mein rehta hai.")
        st.write("Udaharan: t + am → tam.")

    b234 = st.radio("'ech' varṇa jo word ke end mein ho aur uske baad short 'a' ho?",
                    options=["Haan (Yes)", "Nahi (No)"])
    if b234 == "Haan (Yes)":
        st.write("Udaharan: vane + asmin → vanesmin.")

    c1234 = st.radio("'pluta' ya 'pragṛhya' saṁjñaka words, jo ach se follow hote hain, un par lagaye?",
                     options=["Haan (Yes)", "Nahi (No)"])
    if c1234 == "Haan (Yes)":
        st.write("'Pluta' ya 'pragṛhya' saṁjñaka words ke baad ach aaye toh sandhi nahi hota.")
        st.write("Udaharan: agar pluta word ach se follow hota hai, sandhi lagana padega.")

# Notes Section
st.header("Notes")
st.markdown("""
1. **App Ka Maksad**: Ye app Sanskrit grammar ke Sandhi rules ko explore karne aur apply karne ke liye banaya gaya hai.
2. **Phonetic Groups**: Groups jaise 'ik', 'ech' Pāṇini ke varṇa classification ke hisaab se banaye gaye hain.
3. **Interactive Design**: Users alag-alag rules ke saath experiment kar sakte hain.
4. **Extensibility**: Naye rules future mein add kiye ja sakte hain.
5. **Examples Provided**: Transformations ko samajhne ke liye examples diye gaye hain.
""")
