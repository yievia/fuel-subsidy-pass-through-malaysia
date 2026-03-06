# Fuel Price Pass-Through and Inflation in Malaysia (2020–2025)

This repository contains the reproducible Python code for analyzing the pass-through of global oil prices and exchange rates into domestic fuel prices and consumer inflation under subsidised and market-linked pricing regimes.

---

## Methods

All data were obtained from official public sources:
- ARIMA / ARIMAX / ETS forecasting
- ARDL pass-through modeling
- Multi-frequency economic data integration

---

## Data Sources

All data were obtained from official public sources:
- Department of Statistics Malaysia (CPI)
- Bank Negara Malaysia (USD/MYR exchange rate)
- Ministry of Finance Malaysia (retail fuel prices)
- U.S. Energy Information Administration (Brent and WTI crude oil prices)

---

## Reproducibility Instructions

1. Create a Python environment (Python 3.10 recommended)
2. Install required packages: pip install -r requirements.txt
3. Run notebooks sequentially from `00_engineering_qc.ipynb` to `08_ardl_diesel_wti.ipynb`

All figures and tables reported in the thesis can be reproduced from these notebooks.


## Notes

- Raw data files are included for transparency.
- Minor differences in numerical precision may occur across systems.
- This repository is provided for academic and replication purposes.
