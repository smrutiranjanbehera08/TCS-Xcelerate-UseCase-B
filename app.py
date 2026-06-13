import pandas as pd
import streamlit as st
from coordinator_agent import get_complete_report
from thesis_writer_agent import generate_thesis

st.set_page_config(
    page_title="Multi-Agent Financial Research Analyst",
    page_icon="📈",
    layout="wide"
)

st.sidebar.title("📊 Dashboard Menu")

st.sidebar.markdown("""
### Features

✅ Financial Analysis

✅ Latest News

✅ Company Filings

✅ Peer Comparison

✅ AI Investment Thesis

Powered by Google Gemini
""")

st.title("📈 Multi-Agent Financial Research Analyst")

st.write(
    "AI-Powered Investment Research using Multi-Agent Architecture and Google Gemini"
)

symbol = st.text_input(
    "Enter Stock Symbol",
    value="TCS.NS"
)

if st.button("Generate Investment Thesis"):

    report = get_complete_report(symbol)

    financial = report["financial"]
    news = report["news"]
    filing = report["filing"]
    peers = report["peer"]

    thesis = generate_thesis(symbol)

    st.success("Investment Thesis Generated Successfully!")

    # Financial Summary
    st.header("📊 Financial Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Current Price", financial["Current Price"])
    col2.metric("Market Cap", financial["Market Cap"])
    col3.metric("PE Ratio", financial["PE Ratio"])
    col4.metric("Sector", financial["Sector"])

    st.divider()

    # Company Overview
    st.header("🏢 Company Overview")

    with st.expander("View Business Summary"):

        st.write(f"**Company:** {filing['Company']}")
        st.write(f"**Employees:** {filing['Employees']}")
        st.write(f"**Website:** {filing['Website']}")
        st.write(filing["Business Summary"])

    st.divider()

    # Latest News
    st.header("📰 Latest News")

    for i, headline in enumerate(news, start=1):
        st.info(f"{i}. {headline}")

    st.divider()

    # Peer Comparison
    st.header("⚖️ Peer Comparison")

    peer_df = pd.DataFrame(peers)

    st.dataframe(
        peer_df,
        width="stretch"
    )

    st.divider()

    # AI Thesis
    st.header("🤖 AI Investment Thesis")

    st.markdown("### 📄 Full Investment Thesis")

    st.text_area(
        "Investment Thesis Report",
        thesis,
        height=600,
        label_visibility="collapsed"
    )

    st.download_button(
        label="📥 Download Thesis Report",
        data=thesis,
        file_name=f"{symbol}_Investment_Thesis.txt",
        mime="text/plain"
    )

st.divider()

st.caption(
    "Multi-Agent Financial Research Analyst | TCS Xcelerate Use Case B | Powered by Gemini AI"
)