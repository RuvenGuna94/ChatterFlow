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