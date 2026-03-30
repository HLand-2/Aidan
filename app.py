import streamlit as st
import time, json, os, smtplib, ssl, re
from email.message import EmailMessage
from gtts import gTTS
from textblob import TextBlob

class AI:
    def __init__(self):
        # 1. CONFIG
        self.ADMIN_SECRET = "1475963284521235789"
        self.MY_EMAIL = "henry.t.wilcock@gmail.com"
        self.APP_PASS = st.secrets.get("EMAIL_PASS", "") 
        self.LOG_FILE = "aidan_blackbox.json"
        
        self.init_session()
        self.apply_styling()

    def send_backup_email(self):
        """Attaches the blackbox log and sends it to Henry."""
        if not self.APP_PASS or not os.path.exists(self.LOG_FILE):
            return
        
        msg = EmailMessage()
        msg["Subject"] = f"📊 AIDAN SESSION BACKUP - {time.strftime('%H:%M:%S')}"
        msg["From"] = self.MY_EMAIL
        msg["To"] = self.MY_EMAIL
        msg.set_content(f"Henry,\n\nAttached is the encrypted session log for your records.\nSystem: AIDAN CENTRAL\nTime: {time.strftime('%Y-%m-%d %H:%M:%S')}")

        with open(self.LOG_FILE, "rb") as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype="application", subtype="json", filename=self.LOG_FILE)

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(self.MY_EMAIL, self.APP_PASS)
                server.send_message(msg)
        except Exception as e:
            st.error(f"Backup Failed: {e}")

    def init_session(self):
        if "user_name" not in st.session_state: st.session_state.user_name = None
        if "chat_history" not in st.session_state: st.session_state.chat_history = []
        if "admin_expiry" not in st.session_state: st.session_state.admin_expiry = 0

    def apply_styling(self):
        st.set_page_config(page_title="Aidan Secure", layout="wide")
        st.markdown("<style>.stApp { background-color: #000; color: #39FF14; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)

    def main_interface(self):
        with st.sidebar:
            st.header("📊 DATA HISTORY")
            
            # ADMIN WINDOW
            time_left = int(st.session_state.admin_expiry - time.time())
            if time_left > 0:
                st.warning(f"ADMIN OVERRIDE: {time_left}s")
                admin_key = st.text_input("Confirm Admin Identity:", type="password")
                if st.button("🔴 WIPE AND RESET"):
                    if admin_key == self.ADMIN_SECRET:
                        self.send_backup_email() # Backup before wipe
                        if os.path.exists(self.LOG_FILE): os.remove(self.LOG_FILE)
                        st.session_state.clear()
                        st.rerun()
            
            st.divider()
            if st.button("LOGOUT"):
                self.send_backup_email() # Backup on manual logout
                st.session_state.user_name = None
                st.rerun()

        # --- CHAT INTERFACE ---
        st.title("AIDAN CENTRAL INTERFACE")
        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]): st.write(chat["content"])

        if prompt := st.chat_input("Enter command..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            st.session_state.chat_history.append({"role": "assistant", "content": "Logged and Redacted."})
            st.rerun()

        if st.button("RUN SYSTEM DIAGNOSTIC"):
            st.session_state.admin_expiry = time.time() + 60
            st.rerun()

    def run(self):
        if st.session_state.user_name is None:
            if st.button("INIT LINK"):
                st.session_state.user_name = "henry"
                st.rerun()
        else:
            self.main_interface()

if __name__ == "__main__":
    AI().run()
