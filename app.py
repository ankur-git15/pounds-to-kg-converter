import streamlit as st

# Page setup
st.set_page_config(
    page_title="Pounds ↔ Kilograms Converter",
    page_icon="⚖️",
    layout="centered"
)

# Custom styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #e0f7fa, #f1f8e9);
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background-color: #ffffffcc;
        padding: 2em 3em;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        max-width: 500px;
        margin: auto;
    }
    h1 {
        color: #2E7D32;
        text-align: center;
        font-weight: 800;
        letter-spacing: 0.5px;
        margin-bottom: 0.5em;
    }
    .subtitle {
        text-align: center;
        color: #555;
        font-size: 0.9em;
        margin-bottom: 1.5em;
    }
    .result-box {
        background: #f0fdf4;
        border-left: 6px solid #43a047;
        padding: 1em;
        border-radius: 10px;
        font-size: 1.2em;
        text-align: center;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Title + subtitle
st.markdown("<h1>⚖️ Pounds ↔ Kilograms Converter</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>A simple, elegant tool to convert instantly</div>", unsafe_allow_html=True)

# Conversion selection
option = st.radio("Choose conversion type:", ("Pounds ➜ Kilograms", "Kilograms ➜ Pounds"))

# Input value
value = st.number_input("Enter value:", min_value=0.0, step=0.1, format="%.2f", key="input_value")

# Perform conversion
if option == "Pounds ➜ Kilograms":
    result = value * 0.45359237
    output_text = f"{value:.2f} lb = {result:.2f} kg"
else:
    result = value / 0.45359237
    output_text = f"{value:.2f} kg = {result:.2f} lb"

# Display result nicely
st.markdown(f"<div class='result-box'>{output_text}</div>", unsafe_allow_html=True)

st.caption("Created with ❤️ using Streamlit • Accurate to 5 decimal places")

