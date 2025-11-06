import streamlit as st

st.set_page_config(page_title="Pounds ↔ Kilograms Converter", page_icon="⚖️", layout="centered")

st.title("⚖️ Pounds ↔ Kilograms Converter")

option = st.radio("Choose conversion type:", ("Pounds to Kilograms", "Kilograms to Pounds"))

value = st.number_input("Enter value:", min_value=0.0, step=0.1, format="%.2f")

if option == "Pounds to Kilograms":
    result = value * 0.45359237
    st.success(f"{value:.2f} lb = {result:.2f} kg")
else:
    result = value / 0.45359237
    st.success(f"{value:.2f} kg = {result:.2f} lb")

st.caption("Created using Streamlit • Accurate to ~5 decimal places")
