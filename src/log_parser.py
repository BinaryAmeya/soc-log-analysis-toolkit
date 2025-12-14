import pandas as pd

df = pd.read_csv("data/raw_logs.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.to_csv("data/processed_logs.csv", index=False)

print("Logs parsed successfully")
