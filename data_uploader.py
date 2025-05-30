import streamlit as st
import os

UPLOAD_DIR = "data/logs"

st.title("🔧 Data Uploader")

uploaded_file = st.file_uploader("Upload a new Teleops Log File", type=["log", "json"])
if uploaded_file:
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    save_path = os.path.join(UPLOAD_DIR, "ato_log.log")
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File uploaded successfully and saved as: {save_path}")
