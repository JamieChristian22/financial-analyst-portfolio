"""Generate a text executive summary from the portfolio CSV."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "executive_financial_performance_data.csv"

with DATA.open() as f:
    rows = list(csv.DictReader(f))

ytd = [r for r in rows if r["Year"] == "2026" and int(r["Month"][5:7]) <= 8]

def s(col):
    return sum(float(r[col]) for r in ytd)

revenue = s("Actual_Revenue")
budget = s("Budget_Revenue")
ebitda = revenue - s("Actual_COGS") - s("Actual_Opex")
ocf = s("Operating_Cash_Flow")

print("2026 YTD Executive Summary")
print(f"Revenue: ${revenue:,.0f}")
print(f"Revenue vs Budget: ${revenue-budget:,.0f} ({(revenue-budget)/budget:.1%})")
print(f"EBITDA: ${ebitda:,.0f} ({ebitda/revenue:.1%} margin)")
print(f"Operating Cash Flow: ${ocf:,.0f} ({ocf/ebitda:.1%} cash conversion)")
