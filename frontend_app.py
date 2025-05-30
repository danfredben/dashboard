import streamlit as st
import pandas as pd
from utils.data_loader import load_log_file

LOG_PATH = "data/logs/ato_log.log"
TARGET_FIELDS = ["vehicle_state_avg", "gear_avg", "gas_pedal_avg", "steering_wheel_avg"]

st.set_page_config(page_title="Teleops Signal Dashboard", layout="wide")
st.title("Teleops Signal Dashboard")

try:
    df = load_log_file(LOG_PATH)
except Exception as e:
    st.error(f"Error loading log file: {e}")
    st.stop()

# Optional: Resample
df.set_index('timestamp', inplace=True)
df = df.resample("500ms").mean().dropna(how='all').reset_index()

# Time range slider
min_time, max_time = df['timestamp'].min(), df['timestamp'].max()
start_time, end_time = st.slider("Select Time Range", min_time, max_time, (min_time, max_time))
df = df[(df['timestamp'] >= start_time) & (df['timestamp'] <= end_time)]

# Plotting
for field in TARGET_FIELDS:
    if field in df.columns:
        st.subheader(f"{field}")
        st.line_chart(df.set_index('timestamp')[[field]].dropna())
