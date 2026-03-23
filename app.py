import streamlit as st
import google.generativeai as genai

# API Key Setup
genai.configure(api_key=st.secrets["AIzaSyDn1ECuMKG1z0zgv82Np1292vyoqy13VvI"])

# Page Setup
st.set_page_config(page_title="Tia - AI Agent", page_icon="✈️")
st.title("✈️ Tia - Air India Express Assistant")


# Knowledge Base
knowledge_text = """
Air India Express Rules:
- Baggage: Economy mein 20kg Check-in aur 7kg Cabin bag allowed hai.
- Food: Flight mein paid meals available hain.
- Refund: Non-refundable tickets mein paisa wapas nahi hota.
"""
# Key Check
if API_KEY == "AIzaSyDn1ECuMKG1z0zgv82Np1292vyoqy13VvI":
    st.error("AIzaSyDn1ECuMKG1z0zgv82Np1292vyoqy13VvI")
    st.stop()

try:
    genai.configure(api_key=API_KEY)
    
    # Model Setup (Simple Version)
    model = genai.GenerativeModel('gemini-pro')
    
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
