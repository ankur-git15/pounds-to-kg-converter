import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Pounds ↔ Kilograms Converter",
    page_icon="⚖️",
    layout="centered"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
    body {
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #E3F2FD, #E8F5E9);
        border-radius: 20px;
        padding: 2em 3em;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        max-width: 550px;
        margin: auto;
    }
    h1 {
        text-align: center;
        color: #1B5E20;
        font-weight: 800;
    }
    .subtitle {
        text-align: center;
        color: #444;
        margin-bottom: 1em;
        font-size: 0.95em;
    }
    .result-box {
        background: #f0fdf4;
        border-left: 6px solid #43a047;
        padding: 1em;
        border-radius: 10px;
        font-size: 1.2em;
        text-align: center;
        font-weight: 600;
        margin-top: 1em;
    }
    .copy-btn {
        display: flex;
        justify-content: center;
        margin-top: 0.5em;
    }
    button[title="Copy to clipboard"] {
        background-color: #43a047 !important;
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.image("https://www.csir.res.in/sites/default/files/csirlogo.jpg", width=100)
st.markdown("<h1>⚖️ Pounds ↔ Kilograms Converter</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Accurate. Instant. Mobile-ready.</div>", unsafe_allow_html=True)

# ------------------ MODE TOGGLE ------------------
dark_mode = st.toggle("🌙 Dark mode")

if dark_mode:
    st.markdown("""
        <style>
        .stApp {background: linear-gradient(135deg, #212121, #424242); color: white;}
        h1, .subtitle {color: #E8F5E9;}
        .result-box {background: #263238; border-left: 6px solid #00E676; color: #E8F5E9;}
        </style>
    """, unsafe_allow_html=True)

# ------------------ CONVERTER ------------------
option = st.radio("Select conversion type:", ("Pounds ➜ Kilograms", "Kilograms ➜ Pounds"))
value = st.number_input("Enter value:", min_value=0.0, step=0.1, format="%.2f")

if option == "Pounds ➜ Kilograms":
    result = value * 0.45359237
    output_text = f"{value:.2f} lb = {result:.2f} kg"
else:
    result = value / 0.45359237
    output_text = f"{value:.2f} kg = {result:.2f} lb"

if value > 0:
    st.markdown(f"<div class='result-box'>{output_text}</div>", unsafe_allow_html=True)
    if value > 100:
        st.info("That’s quite heavy! 💪")
    elif value < 1:
        st.info("Light as a feather 🪶")
    else:
        st.success("✅ Conversion successful!")
    st.balloons()

    # Copy button
    st.markdown(f"""
        <div class='copy-btn'>
        <button title="Copy to clipboard" onclick="navigator.clipboard.writeText('{output_text}')">
            Copy Result
        </button>
        </div>
    """, unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.caption("Created with ❤️ using Streamlit • Accurate up to 5 decimal places")
