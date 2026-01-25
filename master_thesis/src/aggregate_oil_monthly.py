import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"

# Load cleaned daily oil data
df = pd.read_csv(PROCESSED / "oil_daily.csv")
df["date"] = pd.to_datetime(df["date"])

# Monthly aggregation (unweighted mean)
df_monthly = (
    df
    .set_index("date")
    .resample("M")
    .mean()
    .reset_index()
)

# Save
outpath = PROCESSED / "oil_monthly.csv"
df_monthly.to_csv(outpath, index=False)

print(f"Saved {outpath} with {len(df_monthly)} rows")
print(df_monthly.head())
