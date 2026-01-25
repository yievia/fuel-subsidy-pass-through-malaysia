import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)

FILE = RAW / "raw_fuelprice_weekly_mof.csv"

df = pd.read_csv(FILE)
df.columns = df.columns.astype(str).str.strip()

df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Keep the core series only
keep = ["date", "ron95", "ron97", "diesel"]
missing = [c for c in keep if c not in df.columns]
if missing:
    raise ValueError(f"Missing columns in fuel data: {missing}. Found: {list(df.columns)}")

df = df[keep].copy()

for c in ["ron95", "ron97", "diesel"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")

df = df[(df["date"] >= "2020-01-01") & (df["date"] <= "2025-12-31")]
df = df.dropna(subset=["date"]).sort_values("date").drop_duplicates("date")

outpath = PROCESSED / "fuel_weekly.csv"
df.to_csv(outpath, index=False)

print(f"Saved {outpath} with {len(df)} rows")
print(df.head())
