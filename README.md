# Fuel Price Pass-Through and Inflation in Malaysia (2020–2025)

This repository contains the complete reproducible Python code used in the Master of Data Science thesis:

"Fuel Subsidy Regimes and Inflation Pass-Through in Malaysia"

The analysis examines the pass-through of global oil prices and exchange rates into domestic fuel prices and consumer inflation under subsidised and market-linked pricing regimes.

---

## Repository Structure

data/
raw/ # Raw data downloaded from official sources
processed/ # Final monthly dataset used in estimation

notebooks/
00_engineering_qc.ipynb
01_eda_stationarity.ipynb
02_ardl_diesel.ipynb
03_ardl_ron97.ipynb
04_ardl_cpi07.ipynb
05_ardl_ron95.ipynb
06_ardl_cpihd.ipynb
07_ardl_ron97_wti.ipynb
08_ardl_diesel_wti.ipynb

outputs/
figures/
tables/

---

## Data Sources

All data were obtained from official public sources:
- Department of Statistics Malaysia (CPI)
- Bank Negara Malaysia (USD/MYR exchange rate)
- Ministry of Finance Malaysia (retail fuel prices)
- U.S. Energy Information Administration (Brent and WTI crude oil prices)

Details on data extraction choices and transformations are documented in the thesis Appendix B.

---

## Reproducibility Instructions

1. Create a Python environment (Python 3.10 recommended)
2. Install required packages:
pip install -r requirements.txt

3. Run notebooks sequentially from `00_engineering_qc.ipynb` to `08_ardl_diesel_wti.ipynb`

All figures and tables reported in the thesis can be reproduced from these notebooks.


## Notes

- Raw data files are included for transparency.
- Minor differences in numerical precision may occur across systems.
- This repository is provided for academic and replication purposes.
