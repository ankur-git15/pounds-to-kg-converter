import streamlit as st

# ------------------ PAGE SETUP ------------------
st.set_page_config(
    page_title="Pounds ↔ Kilograms Converter | CSIR Phenome India",
    page_icon="⚖️",
    layout="centered"
)

# ------------------ CUSTOM STYLING ------------------
st.markdown("""
    <style>
        body {
            background-color: #f7f9fc;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background: white;
            padding: 2rem 3rem;
            border-radius: 1.5rem;
            box-shadow: 0 4px 25px rgba(0,0,0,0.08);
            max-width: 600px;
            margin: auto;
        }
        h1 {
            text-align: center;
            color: #004C97; /* CSIR blue */
            font-weight: 800;
            margin-bottom: 0.3rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1rem;
            color: #555;
            margin-bottom: 1.5rem;
        }
        .stButton>button {
            background-color: #004C97;
            color: white;
            border-radius: 10px;
            padding: 0.6rem 1.5rem;
            border: none;
            font-size: 1rem;
            font-weight: 600;
        }
        .stButton>button:hover {
            background-color: #0072CE;
        }
        .footer {
            text-align: center;
            color: #6c757d;
            font-size: 0.85rem;
            margin-top: 2rem;
        }
        .logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 1.5rem;
            margin-bottom: 1.2rem;
        }
        .logo-container img {
            height: 65px;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("""
<div class='logo-container'>
    <img src='https://upload.wikimedia.org/wikipedia/en/9/93/CSIR_INDIA_Logo.png' alt='CSIR logo'>
    <img src='https://cdn-icons-png.flaticon.com/512/197/197419.png' alt='India flag'>
</div>
""", unsafe_allow_html=True)

st.markdown("<h1>⚖️ Pounds ↔ Kilograms Converter</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Developed under the CSIR Phenome India Cohort | Reliable • Fast • Accurate</p>", unsafe_allow_html=True)

# ------------------ CONVERSION LOGIC ------------------
option = st.radio("Select conversion type:", ("Pounds ➜ Kilograms", "Kilograms ➜ Pounds"))
value = st.number_input("Enter value:", min_value=0.0, step=0.1, format="%.2f")

if st.button("Convert"):
    if option == "Pounds ➜ Kilograms":
        result = value * 0.45359237
        st.success(f"{value:.2f} lb = {result:.2f} kg")
    else:
        result = value / 0.45359237
        st.success(f"{value:.2f} kg = {result:.2f} lb")

# ------------------ FOOTER ------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div class='footer'>
    © 2025 CSIR Phenome India Initiative | Handgrip Strength & Anthropometric Study Reference Tool<br>
    Created with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
