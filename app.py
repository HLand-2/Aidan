import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import json
import os

# 1. WEB STYLING (Neon Green & Black)
st.set_page_config(page_title="Aidan AI Vault", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #39FF14; }
    .stTextInput>div>div>input { color: #39FF14; background-color: #111111; border: 1px solid #39FF14; }
    h1, h2, h3 { color: #39FF14 !important; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #111111; color: #39FF14; border: 1px solid #39FF14; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 2. DATABASE LOGIC
DB_FILE = "aidan_web_vault.json"

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f: return json.load(f)
    return {"users": {}}

def save_data(data):
    with open(DB_FILE, 'w') as f: json.dump(data, f, indent=4)

db = load_data()

# 3. WEB INTERFACE
st.title("📟 AIDAN SECURE GATEWAY")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["LOGIN", "REGISTER"])
    
    with tab2:
        new_user = st.text_input("Username")
        c1 = st.text_input("Code 1", type="password")
        c2 = st.text_input("Code 2 (Ghost)", type="password")
        if st.button("ENCRYPT & REGISTER"):
            db['users'][f"{c1}-{c2}"] = {"name": new_user, "history": []}
            save_data(db)
            st.success("Registration Complete.")

    with tab1:
        k1 = st.text_input("Entry Key 1", type="password")
        k2 = st.text_input("Entry Key 2", type="password")
        if st.button("ACCESS VAULT"):
            key = f"{k1}-{k2}"
            if key in db['users']:
                st.session_state.logged_in = True
                st.session_state.user_key = key
                st.session_state.user_name = db['users'][key]['name']
                st.rerun()
            else:
                st.error("INVALID ENCRYPTION KEYS")

else:
    # --- INSIDE THE VAULT ---
    user_name = st.session_state.user_name
    if user_name.lower() == "henry":
        st.subheader(f"hi Henry, do you wanna work on me more?")
    else:
        st.subheader(f"Welcome, Agent {user_name}")

    # Data Input
    raw_data = st.text_input("Enter numeric sequence (comma separated):")
    if st.button("ANALYZE SIGNAL"):
        nums = [float(n.strip()) for n in raw_data.split(',') if n.strip().replace('.','').isdigit()]
        if len(nums) >= 2:
            avg = sum(nums) / len(nums)
            new_entry = {"ts": datetime.now().strftime("%Y-%m-%d %H:%M"), "avg": avg, "data": nums}
            db['users'][st.session_state.user_key]['history'].append(new_entry)
            save_data(db)
            st.write(f"Average Detected: {round(avg, 2)}")
            
            # Interactive Neon Graph
            df = pd.DataFrame({"Value": nums, "Index": range(len(nums))})
            fig = px.line(df, x="Index", y="Value", template="plotly_dark")
            fig.update_traces(line_color='#39FF14')
            st.plotly_chart(fig)

    if st.button("LOGOUT"):
        st.session_state.logged_in = False
        st.rerun()
