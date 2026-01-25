import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)

def to_month_end(s):
    """Convert any monthly date to month-end timestamp."""
    s = pd.to_datetime(s)
    return s.dt.to_period("M").dt.to_timestamp("M")

# Load monthly datasets
oil = pd.read_csv(PROCESSED / "oil_monthly.csv")
fx = pd.read_csv(PROCESSED / "fx_monthly.csv")
fuel = pd.read_csv(PROCESSED / "fuel_monthly.csv")
cpi = pd.read_csv(PROCESSED / "cpi_monthly.csv")

# Standardize dates to month-end
oil["date"] = to_month_end(oil["date"])
fx["date"] = to_month_end(fx["date"])
fuel["date"] = to_month_end(fuel["date"])
cpi["date"] = to_month_end(cpi["date"])

# Merge (inner join = keep only months where ALL series exist)
df = oil.merge(fx, on="date", how="inner") \
        .merge(fuel, on="date", how="inner") \
        .merge(cpi, on="date", how="inner") \
        .sort_values("date")

# Keep and order columns
df = df[[
    "date",
    "brent", "wti",
    "usdmyr",
    "ron95", "ron97", "diesel",
    "cpi_transport", "cpi_headline"
]]

# Basic sanity checks
print("Date range:", df["date"].min(), "to", df["date"].max())
print("Rows:", len(df))
print(df.head())

outpath = PROCESSED / "passthrough_dataset.csv"
df.to_csv(outpath, index=False)

print(f"\nSaved {outpath}")
