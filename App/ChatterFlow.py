# Import libraries
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os
import shelve

# Get OPENAI API Key
load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

