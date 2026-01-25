import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)

FILE = RAW / "raw_eia_spot_prices_daily.xlsx"

# Read the correct sheet
df0 = pd.read_excel(FILE, sheet_name="Data 1", header=0, engine="openpyxl")

# Expected structure:
# Row 0: Sourcekey | RWTC | RBRTE
# Row 1: Date | (WTI long name) | (Brent long name)
# Row 2+: data
new_cols = df0.iloc[1].astype(str).str.strip().tolist()

df = df0.iloc[2:].copy()
df.columns = new_cols

# Keep first 3 cols and standardize names
df = df.iloc[:, :3].copy()
df.columns = ["date", "wti", "brent"]

# Parse types
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["wti"] = pd.to_numeric(df["wti"], errors="coerce")
df["brent"] = pd.to_numeric(df["brent"], errors="coerce")

# Filter study period
df = df[(df["date"] >= "2020-01-01") & (df["date"] <= "2025-12-31")]

# Clean up
df = (
    df.dropna(subset=["date"])
      .sort_values("date")
      .drop_duplicates("date")
)

outpath = PROCESSED / "oil_daily.csv"
df.to_csv(outpath, index=False)

print(f"Saved {outpath} with {len(df)} rows")
print(df.head())
