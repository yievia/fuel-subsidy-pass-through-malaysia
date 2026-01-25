import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"

df = pd.read_csv(PROCESSED / "fx_daily.csv")
df["date"] = pd.to_datetime(df["date"])

df_monthly = (
    df
    .set_index("date")
    .resample("ME")
    .mean()
    .reset_index()
)

outpath = PROCESSED / "fx_monthly.csv"
df_monthly.to_csv(outpath, index=False)

print(f"Saved {outpath} with {len(df_monthly)} rows")
print(df_monthly.head())
