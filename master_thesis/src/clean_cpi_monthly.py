import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)

FILE = RAW / "raw_cpi_division_2digit_monthly.csv"

df = pd.read_csv(FILE)
df.columns = df.columns.astype(str).str.strip()

# Parse types
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["division"] = df["division"].astype(str).str.strip().str.lower()
df["index"] = pd.to_numeric(df["index"], errors="coerce")

# Filter study period
df = df[(df["date"] >= "2020-01-01") & (df["date"] <= "2025-12-31")]

# --- Extract Transport CPI (division code = 7) ---
cpi_transport = df[df["division"] == "07"][["date", "index"]]
cpi_transport = cpi_transport.rename(columns={"index": "cpi_transport"})

if cpi_transport.empty:
    raise ValueError("Transport CPI (division=7) not found")

# --- Extract Headline CPI (overall) ---
cpi_headline = df[df["division"] == "overall"][["date", "index"]]
cpi_headline = cpi_headline.rename(columns={"index": "cpi_headline"})

if cpi_headline.empty:
    raise ValueError("Headline CPI (division=overall) not found")

# Clean & merge
cpi_transport = cpi_transport.dropna().sort_values("date").drop_duplicates("date")
cpi_headline = cpi_headline.dropna().sort_values("date").drop_duplicates("date")

cpi = pd.merge(cpi_transport, cpi_headline, on="date", how="inner")

outpath = PROCESSED / "cpi_monthly.csv"
cpi.to_csv(outpath, index=False)

print(f"Saved {outpath} with {len(cpi)} rows")
print(cpi.head())
