import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ai_thesis(company, sector, news):

    prompt = f"""
    Company: {company}
    Sector: {sector}

    Recent News:
    {news}

    Generate:

    1. Bull Case (2-3 lines)
    2. Bear Case (2-3 lines)
    3. Key Risks (2-3 lines)

    Keep the response concise and professional.
    """

    response = model.generate_content(prompt)

    return response.text