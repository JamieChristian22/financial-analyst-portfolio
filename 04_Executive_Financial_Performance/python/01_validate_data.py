"""Data-quality checks for the Executive Financial Performance portfolio.
Uses only Python standard library so it runs without extra dependencies.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "executive_financial_performance_data.csv"

required = {
    "Month","Year","Quarter","Business_Unit","Region",
    "Actual_Revenue","Budget_Revenue","Forecast_Revenue",
    "Actual_COGS","Budget_COGS","Forecast_COGS",
    "Actual_Opex","Budget_Opex","Forecast_Opex","Assets",
    "Operating_Cash_Flow","Headcount"
}

with DATA.open() as f:
    rows = list(csv.DictReader(f))

assert rows, "Dataset is empty."
assert required.issubset(rows[0]), "Missing required columns."

keys = set()
for i, row in enumerate(rows, start=2):
    key = (row["Month"], row["Business_Unit"], row["Region"])
    assert key not in keys, f"Duplicate record at row {i}: {key}"
    keys.add(key)
    for col in ["Actual_Revenue","Budget_Revenue","Forecast_Revenue","Actual_COGS","Actual_Opex","Assets"]:
        assert float(row[col]) >= 0, f"Negative value in {col}, row {i}"
    assert int(row["Headcount"]) > 0, f"Invalid headcount, row {i}"

print(f"PASS: {len(rows)} rows validated with no duplicate dimensional keys.")
