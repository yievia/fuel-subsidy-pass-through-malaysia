import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"

df = pd.read_csv(PROCESSED / "fuel_weekly.csv")
df["date"] = pd.to_datetime(df["date"])

# Convert each week to its month, then take monthly mean
df["month"] = df["date"].dt.to_period("M")
df_monthly = df.groupby("month")[["ron95", "ron97", "diesel"]].mean().reset_index()
df_monthly["date"] = df_monthly["month"].dt.to_timestamp("M")  # month-end date
df_monthly = df_monthly.drop(columns="month")

outpath = PROCESSED / "fuel_monthly.csv"
df_monthly.to_csv(outpath, index=False)

print(f"Saved {outpath} with {len(df_monthly)} rows")
print(df_monthly.head())
