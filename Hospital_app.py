import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import scikit-learn

st.set_page_config(page_title="Smart Hospital Patient Navigator", page_icon="🏥", layout="wide")

st.markdown("""
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
def load_model():
  with open('hospital_model.pkl', 'rb') as f:
    return pickle.load(f)
    
bundle=load_model()
model=bundle['model']
scaler=bundle['scaler']
features=bundle['features']
cols_to_scale=bundle['cols_to_scale']
dept_map_ivy=bundle['dept_map_ivy']
gender_map=bundle['gender_map']
temp_map=bundle['temp_map']
hr_map=bundle['hr_map']
dur_map=bundle['dur_map']
cc_map=bundle['cc_map']

DEPT_INFO = {
  'Respiratory Medicine' : {
    'icon': '🫁', 'color':'#0284c7','bg':'#e0f2fe','border':'#fca5a5',
    'desc':'Specialises in conditions affecting the lungs and airway.',
    'next':['Visit Level 2, Wing B', 'Estimated wait time: 15-25 min','please wear a mask']
},
'Cardiology':{
'icon':'❤️', 'color':'#dc2626','bg':'#fee2e2','border':'#fca5a5',
'desc' :'specialises in heart realted diesease/problems',
'next' :['Visit level 3, Wing A','Estimated wait time 20-30 minutes','Bring previous ECG reports']

},
'Gastromenterology' : {
    'icon': '🫃', 'color':'#0284c7','bg':'#e0f2fe','border':'#fca5a5',
    'desc' :'Specialises in stomach,digestive and other related areas.',
'next':['Visit Level 1, Wing c', 'Estimated wait time: 10-20 min','Avoid eating before entering']

},
'Neurology' : {
    'icon': '🧠', 'color':'#0284c7','bg':'#e0f2fe','border':'#fca5a5',
    'desc' :'Specialises in mind/brain related injuries.',
'next':['Visit Level 4, Wing A', 'Estimated wait time: 25-35 min','Bring list of medicine']

},
'General Medicine' : {
    'icon': '💊', 'color':'#0284c7','bg':'#e0f2fe','border':'#fca5a5',
    'desc' :'Handles general related medicine,comman health concerns and non-specialist conditions.',
'next':['Visit Level 1, Wing A', 'Estimated wait time: 15-20 min','Registration desk is open 24/7']

},
'Dermatology' : {
    'icon': '🔬', 'color':'#0284c7','bg':'#e0f2fe','border':'#fca5a5',
    'desc' :'Specialises in skin, hair, and nail conditions.',
'next':['Visit Level 2, Wing D', 'Estimated wait time: 15-20 min','Bring phto of affected areas if possible']

},
}
#--Hero Header ---
st.markdown("""
<div style = "background:linear-gradiet(135deg,#1e3a8a 0%, #1a5db 60&, #0ea5e9 100%);
padding:3rem 2rem 2.5rem;margin:-1rem - 1rem 2rem;text-align:center;">
<div style="font-size:14px;font-weight:500;color:rgba(255,255,255,0.7);
text-transform:uppercase;letter-spacing:0.1em;margin-bottom:12px,">
Future Classroom Machine Learning
</div>
<div style="font-size:36px;font-weight:700;color:#ffffff;margin-bottom:12px;letter=spacing:-0.02em;">
  Smart Hostpital Patient Navigator
  </div>
</div>
""",unsafe_allow_html=True)
