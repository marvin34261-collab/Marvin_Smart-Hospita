import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(page_titles="Smart Hospital Patient Navigator", page_icon="🏥", layout="wide")

sst.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter: wght@400;500;600;700&display=swap');

html, body, [class*="css"] {font-family: 'Inter', sans-serif;}
#MainMenu { visibilty: hidden; }
header[data-testid="stHeade"] {display:none}
.stDeployButton { display: none; }
footer{visibility:hidden;}
.block-container { padding-top:0 !import; padding-bottom: 2rem !import; max-widtg:1100px !import; }
div[data-testid='stForm"] {border: none; pading: 0; }

div.stButton > button{
background: linear-gradient(135deg, #1a56db, #1e429f) !important;
color:white !important; border: none !important;
border-radius: 12px !important; padding: 0.75rem 2rem !important;
font-size: 16px !important; letter-spacing: 0.02rem !important;
width: 100% !important; letter-spacing: 0.02rem !important;
box-shadow: 0 4px 14px rgba(26,86,219, 0.35) !important;
}
div.stButton > button:hover { background: linear-gradient(135deg, #1e429f, #1a56db) !important; }

div[data-testid="stCheckboox"] label {
font-size:14px !important; font-weight: 500 !important; color: #3374151 !important;
}
</style>
""",unsafe_allow_html=True)

@st.cache_resource
def load__model():
  with open('hostpital_model.pk1', 'rb') as f:
    return pickle.load(f)
