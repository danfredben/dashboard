import pandas as pd
import json
import os

def load_log_file(log_path):
    if not os.path.exists(log_path):
        raise FileNotFoundError(f"Log file not found: {log_path}")

    data = []
    with open(log_path, "r") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if line:
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    if not data:
        raise ValueError("No valid data found in log file.")

    df = pd.DataFrame(data)

    if 'timestamp' not in df.columns:
        raise KeyError("Missing required column: 'timestamp'")

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='us', errors='coerce')
    df.dropna(subset=['timestamp'], inplace=True)
    return df
