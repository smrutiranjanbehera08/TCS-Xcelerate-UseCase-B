import streamlit as st
from thesis_writer_agent import generate_thesis

st.title("📈 Multi-Agent Financial Research Analyst")

st.write(
    "AI-Powered Investment Research using Multi-Agent Architecture and Google Gemini"
)

symbol = st.text_input(
    "Enter Stock Symbol",
    value="TCS.NS"
)

if st.button("Generate Investment Thesis"):

    thesis = generate_thesis(symbol)

    st.success("Investment Thesis Generated Successfully!")

    st.text_area(
        "Investment Thesis Report",
        thesis,
        height=600
    )

    st.download_button(
        label="📥 Download Thesis Report",
        data=thesis,
        file_name=f"{symbol}_Investment_Thesis.txt",
        mime="text/plain"
    )