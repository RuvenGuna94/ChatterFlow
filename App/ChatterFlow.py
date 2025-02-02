# Import libraries
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os
import shelve

# Get OPENAI API Key
load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

# Set up the bot
st.title("ChatterFlow")
"""
ChatterFlow is an intelligent chatbot powered by **OpenAI** and **Streamlit**, 
designed to provide an interactive and user-friendly experience. 
This chatbot leverages natural language processing (NLP) to 
generate human-like responses and can be easily customized for various use cases.
"""

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ensure openai_model is initialized in session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Create opening message
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm ChatterFlow. How can I help you?"}
    ]