import streamlit as st

# ------------------ PAGE SETUP ------------------
st.set_page_config(
    page_title="Handgrip Strength Reference | CSIR Phenome India",
    page_icon="⚖️",
    layout="centered"
)

# ------------------ CLEAN STYLING ------------------
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background-color: #ffffff;
            padding: 2.5rem 3rem;
            border-radius: 1.5rem;
            box-shadow: none;
            max-width: 700px;
            margin: auto;
        }
        h1 {
            text-align: center;
            color: #002855;
            font-weight: 800;
            margin-bottom: 0.1rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1rem;
            color: #444;
            margin-bottom: 2rem;
        }
        .stButton>button {
            background-color: #002855;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1.2rem;
            border: none;
            font-size: 1rem;
            font-weight: 600;
        }
        .stButton>button:hover {
            background-color: #004C97;
        }
        .footer {
            text-align: center;
            color: #6c757d;
            font-size: 0.85rem;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("<h1>Handgrip Strength Reference Tool</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>A data-driven reference for quick handgrip strength assessment</p>", unsafe_allow_html=True)

# ------------------ CONVERTER ------------------
st.subheader("Pounds to Kilograms Converter")

value = st.number_input("Enter handgrip strength (in pounds):", min_value=0.0, step=0.1, format="%.2f")

converted_value = None
if st.button("Convert to Kilograms"):
    converted_value = value * 0.45359237
    st.success(f"{value:.2f} lb = {converted_value:.2f} kg")

if converted_value:
    st.session_state["converted_value"] = round(converted_value, 2)

# ------------------ NORMATIVE DATA ------------------
normative_data = {
    "Male": {
        "18–29": {"p5": 29.66, "p25": 36.70, "p50": 40.80, "p75": 45.80, "p95": 57.24},
        "30–39": {"p5": 27.20, "p25": 36.30, "p50": 41.30, "p75": 45.80, "p95": 52.56},
        "40–49": {"p5": 27.55, "p25": 35.80, "p50": 39.50, "p75": 45.15, "p95": 51.70},
        "50–59": {"p5": 27.50, "p25": 34.00, "p50": 38.10, "p75": 43.10, "p95": 49.60},
        "≥60": {"p5": 20.40, "p25": 29.50, "p50": 34.00, "p75": 38.60, "p95": 47.57},
    },
    "Female": {
        "18–29": {"p5": 18.10, "p25": 23.60, "p50": 26.80, "p75": 29.50, "p95": 31.80},
        "30–39": {"p5": 18.10, "p25": 22.70, "p50": 26.55, "p75": 29.50, "p95": 34.50},
        "40–49": {"p5": 16.24, "p25": 22.20, "p50": 24.90, "p75": 28.60, "p95": 33.60},
        "50–59": {"p5": 15.90, "p25": 20.65, "p50": 22.70, "p75": 27.20, "p95": 31.80},
        "≥60": {"p5": 11.30, "p25": 18.10, "p50": 20.40, "p75": 22.90, "p95": 26.16},
    }
}

# ------------------ NORMATIVE COMPARISON ------------------
st.subheader("Handgrip Strength Normative Comparison")

col1, col2 = st.columns(2)
with col1:
    sex = st.radio("Select Sex:", ["Male", "Female"])
with col2:
    age_group = st.selectbox("Select Age Group:", ["18–29", "30–39", "40–49", "50–59", "≥60"])

default_val = st.session_state.get("converted_value", 0.0)
grip_strength = st.number_input("Enter Handgrip Strength (kg):", min_value=0.0, step=0.1, value=default_val, format="%.2f")

if st.button("Compare with Normative Data"):
    ref = normative_data[sex][age_group]
    p5, p25, p50, p75, p95 = ref["p5"], ref["p25"], ref["p50"], ref["p75"], ref["p95"]

    if grip_strength < p5:
        band, category, color = "<5th percentile", "Very Low Strength", "#C0392B"
    elif grip_strength < p25:
        band, category, color = "5th–25th percentile", "Low Strength", "#E67E22"
    elif grip_strength < p50:
        band, category, color = "25th–50th percentile", "Below Median", "#F1C40F"
    elif grip_strength < p75:
        band, category, color = "50th–75th percentile", "Normal Range", "#27AE60"
    elif grip_strength < p95:
        band, category, color = "75th–95th percentile", "Above Average", "#2980B9"
    else:
        band, category, color = "≥95th percentile", "Exceptional Strength", "#6C3483"

    st.markdown(f"""
        <div style='background-color:{color}; color:white; padding:1rem; border-radius:10px; text-align:center;'>
            <h3>{category}</h3>
            <p>For a <b>{sex}</b> aged <b>{age_group}</b>, a grip strength of <b>{grip_strength:.2f} kg</b> 
            lies within the <b>{band}</b>.</p>
        </div>
    """, unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div class='footer'>
    © 2025 CSIR Phenome India Initiative | Handgrip Strength Reference Tool
</div>
""", unsafe_allow_html=True)
