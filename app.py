import streamlit as st
from thesis_writer_agent import generate_thesis

st.title("Multi-Agent Financial Research Analyst")

symbol = st.text_input(
    "Enter Stock Symbol",
    value="TCS.NS"
)

if st.button("Generate Investment Thesis"):

    thesis = generate_thesis(symbol)

    st.text_area(
        "Investment Thesis Report",
        thesis,
        height=500
    )