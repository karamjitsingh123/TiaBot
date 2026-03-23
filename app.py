import streamlit as st
import google.generativeai as genai

# Page Setup
st.set_page_config(page_title="Tia - AI Agent", page_icon="✈️")
st.title("✈️ Tia - Air India Express Assistant")

# API Key Setup
genai.configure(api_key="AIzaSyAA23Um66iv6OhkyZBdV-Ezd6luDg6QEv4")
# Knowledge Base
knowledge_text = """
Air India Express Rules:
- Baggage: Economy mein 20kg Check-in aur 7kg Cabin bag allowed hai.
- Food: Flight mein paid meals available hain.
- Refund: Non-refundable tickets mein paisa wapas nahi hota.
"""

# Chat Session
if "chat" not in st.session_state:
    model = genai.GenerativeModel('gemini-1.5-flash', 
                                  system_instruction=f"Tum 'Tia' ho, Air India Express ki helper ho. Info: {knowledge_text}")
    st.session_state.chat = model.start_chat(history=[])

# User Input
prompt = st.chat_input("Apna sawaal likhein...")

if prompt:
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt)
    st.chat_message("assistant").markdown(response.text)
