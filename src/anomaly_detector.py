import pandas as pd

INPUT_FILE = "data/processed_logs.csv"
OUTPUT_FILE = "output/flagged_events.csv"

FAILED_THRESHOLD = 3
TIME_WINDOW_MINUTES = 5

df = pd.read_csv(INPUT_FILE)
df["timestamp"] = pd.to_datetime(df["timestamp"])

failed = df[df["status"] == "failed"]

alerts = []

grouped = failed.groupby(["ip_address", "username"])

for (ip, user), group in grouped:
    group = group.sort_values("timestamp")
    time_diff = (group["timestamp"].max() - group["timestamp"].min()).seconds / 60

    if len(group) >= FAILED_THRESHOLD and time_diff <= TIME_WINDOW_MINUTES:
        alerts.append({
            "ip_address": ip,
            "username": user,
            "failed_attempts": len(group),
            "time_window_minutes": round(time_diff, 2),
            "severity": "HIGH" if len(group) >= 5 else "MEDIUM",
            "threat_type": "Possible Brute Force"
        })

alerts_df = pd.DataFrame(alerts)
alerts_df.to_csv(OUTPUT_FILE, index=False)

print("SOC detection completed. Alerts generated.")
