import streamlit as st
import time, json, os, re, smtplib, ssl
from email.message import EmailMessage

# 1. ADMIN & ALARM CONFIG
ADMIN_SECRET = "1475963284521235789"
MY_EMAIL = "Henry.t.wilcock@gmail.com"
APP_PASS = st.secrets.get("EMAIL_PASS", "") # Set this in Streamlit Secrets for safety

if 'admin_expiry' not in st.session_state: st.session_state.admin_expiry = 0

def send_silent_alarm(details):
    """Sends a secret email if someone tries to hack the admin window."""
    if not APP_PASS: return # Skip if no password set
    msg = EmailMessage()
    msg.set_content(f"SECURITY ALERT: {details} at {time.strftime('%H:%M:%S')}")
    msg['Subject'] = "⚠️ AIDAN ADMIN BREACH ATTEMPT"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(MY_EMAIL, APP_PASS); server.send_message(msg)
    except: pass

# 2. STYLING (Back to Normal Sidebar Look)
st.set_page_config(page_title="Aidan Secure", layout="wide")
st.markdown(f"<style>.stApp {{ background-color: #000000; color: #39FF14; font-family: 'Courier New'; }}</style>", unsafe_allow_html=True)

# 3. INTERFACE
if 'user_name' not in st.session_state:
    if st.button("INIT LINK"):
        st.session_state.user_name = "Henry"; st.rerun()
else:
    # --- SIDEBAR (Looks Normal) ---
    with st.sidebar:
        st.header("📊 DATA HISTORY")
        st.write("Session active...")
        st.caption("Last Sync: " + time.strftime("%H:%M"))
        
        # SECRET INJECTION
        time_left = int(st.session_state.admin_expiry - time.time())
        if time_left > 0:
            st.divider()
            st.warning(f"MAINTENANCE OVERRIDE: {time_left}s")
            admin_key = st.text_input("Confirm Identity:", type="password")
            if st.button("PURGE CRASH LOGS"):
                if admin_key == ADMIN_SECRET:
                    if os.path.exists("aidan_blackbox.json"): os.remove("aidan_blackbox.json")
                    st.success("PURGE COMPLETE."); st.session_state.admin_expiry = 0; st.rerun()
                else:
                    send_silent_alarm(f"Failed Admin Key attempt by {st.session_state.user_name}")
                    st.error("ACCESS DENIED.")
            st.divider()
        
        st.write("ID: 0x442-99")
        if st.button("LOGOUT"): st.session_state.clear(); st.rerun()

    st.title(f"📟 {st.session_state.user_name.upper()} // CONSOLE")
    st.subheader("hi Henry, do you wanna work on me more?")
    
    chat = st.chat_input("Command...")
    if chat:
        if chat.lower() == 'admin':
            st.session_state.admin_expiry = time.time() + 15
            st.write("Aidan: Command processed."); st.rerun()
        st.write("Aidan: Signal clear.")
