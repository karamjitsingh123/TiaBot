import streamlit as st
import google.generativeai as genai

# API Key Setup
API_KEY = "AIzaSyDRf9qCL1cJj7bi4jXxEiFfdvJ_zMox3wQ"
genai.configure(api_key=API_KEY)

# Page Setup
st.set_page_config(page_title="karamjit - AI Agent", page_icon="✈️")
st.title("✈️ kamrai - Assistant")

# Knowledge Base
knowledge_text = """
Air India Express Rules:
- Baggage: Economy mein 20kg Check-in aur 7kg Cabin bag allowed hai.
- Food: Flight mein paid meals available hain.
- Refund: Non-refundable tickets mein paisa wapas nahi hota.
"""

# Model Setup
model = genai.GenerativeModel('gemini-pro', system_instruction=knowledge_text)

# Chat Session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# User Input
prompt = st.chat_input("how are you")

if prompt:
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt)
    st.chat_message("assistant").markdown(response.text)
