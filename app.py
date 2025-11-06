import streamlit as st

# Page setup
st.set_page_config(page_title="Pounds ↔ Kilograms Converter", page_icon="⚖️", layout="centered")

# CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 1.5rem;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: auto;
        }
        h1 {
            text-align: center;
            color: #0d6efd;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1.1rem;
            color: #6c757d;
            margin-bottom: 2rem;
        }
        .stButton>button {
            background-color: #0d6efd;
            color: white;
            border-radius: 12px;
            padding: 0.6rem 1.5rem;
            border: none;
            font-size: 1rem;
        }
        .stButton>button:hover {
            background-color: #0b5ed7;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<h1>⚖️ Pounds ↔ Kilograms Converter</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Quick, simple, and accurate — convert instantly!</p>", unsafe_allow_html=True)

# Conversion logic
option = st.radio("Select conversion type:", ("Pounds ➜ Kilograms", "Kilograms ➜ Pounds"))

value = st.number_input("Enter value:", min_value=0.0, step=0.1, format="%.2f")

if st.button("Convert"):
    if option == "Pounds ➜ Kilograms":
        result = value * 0.45359237
        st.success(f"{value:.2f} lb = {result:.2f} kg")
    else:
        result = value / 0.45359237
        st.success(f"{value:.2f} kg = {result:.2f} lb")

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Made with ❤️ using Streamlit | Accurate up to 5 decimal places")
