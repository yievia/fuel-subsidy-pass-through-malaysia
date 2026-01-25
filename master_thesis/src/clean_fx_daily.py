import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)

FILE = RAW / "raw_fx_bnm_2020_2025.csv"

df = pd.read_csv(FILE)

# Strip column names
df.columns = df.columns.astype(str).str.strip()

# If first column is unnamed, treat it as date
first_col = df.columns[0]
if first_col.lower().startswith("unnamed") or first_col == "":
    df = df.rename(columns={first_col: "date"})
else:
    df = df.rename(columns={first_col: "date"})  # defensive, date is always first

# Check USD exists
if "USD" not in df.columns:
    raise ValueError(f"'USD' column not found. Columns: {list(df.columns)}")

# Keep only date + USD
df = df[["date", "USD"]].rename(columns={"USD": "usdmyr"})

# Parse types
df["date"] = pd.to_datetime(df["date"], format="%d-%b-%y", errors="coerce")
df["usdmyr"] = pd.to_numeric(df["usdmyr"], errors="coerce")

# Filter study period
df = df[(df["date"] >= "2020-01-01") & (df["date"] <= "2025-12-31")]

# Clean
df = (
    df.dropna(subset=["date"])
      .sort_values("date")
      .drop_duplicates("date")
)

outpath = PROCESSED / "fx_daily.csv"
df.to_csv(outpath, index=False)

print(f"Saved {outpath} with {len(df)} rows")
print(df.head())
