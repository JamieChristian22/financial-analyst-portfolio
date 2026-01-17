"""FP&A KPI computations from finance_fact.csv.

Run:
  python fpa_kpis.py

Outputs:
  - outputs/monthly_pnl.csv
  - outputs/charts_*.png
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "finance_fact.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["TxnDate", "MonthYear"])

# Monthly P&L (Actual only)
actual = df[df["Scenario"] == "Actual"].copy()

rev = actual[actual["AccountCategory"] == "Revenue"].groupby("MonthYear")["Amount"].sum()
cogs = actual[actual["AccountCategory"] == "COGS"].groupby("MonthYear")["Amount"].sum()
opex = actual[actual["AccountCategory"] == "Opex"].groupby("MonthYear")["Amount"].sum()

pnl = pd.DataFrame({
    "Revenue": rev,
    "COGS": cogs,
    "Opex": opex,
}).fillna(0).sort_index()

pnl["GrossProfit"] = pnl["Revenue"] - pnl["COGS"]
pnl["GrossMarginPct"] = pnl["GrossProfit"] / pnl["Revenue"].replace({0: pd.NA})
pnl["OperatingIncome"] = pnl["GrossProfit"] - pnl["Opex"]

pnl.to_csv(OUT / "monthly_pnl.csv")

plt.figure()
plt.plot(pnl.index, pnl["Revenue"], label="Revenue")
plt.plot(pnl.index, pnl["OperatingIncome"], label="Operating Income")
plt.title("Monthly Revenue and Operating Income (Actual)")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(OUT / "charts_rev_opinc.png", dpi=200)
plt.close()

# Budget vs Actual variance
bud = df[df["Scenario"] == "Budget"]
rev_b = bud[bud["AccountCategory"] == "Revenue"].groupby("MonthYear")["Amount"].sum()
var = (rev - rev_b).rename("RevenueVariance")
var.to_csv(OUT / "revenue_variance.csv")

plt.figure()
plt.plot(var.index, var.values)
plt.title("Revenue Variance (Actual - Budget)")
plt.xlabel("Month")
plt.ylabel("Variance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT / "charts_revenue_variance.png", dpi=200)
plt.close()

print("Wrote:", OUT)
