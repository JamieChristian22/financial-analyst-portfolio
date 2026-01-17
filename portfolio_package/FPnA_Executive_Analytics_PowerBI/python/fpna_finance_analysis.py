"""FP&A analysis: actual vs budget, operating income, gross margin.

Run:
  python fpna_finance_analysis.py

Outputs:
  - outputs/monthly_kpis.csv
  - outputs/charts_*.png
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

fact = pd.read_csv(DATA / "finance_fact.csv", parse_dates=["TxnDate", "MonthYear"])

# Monthly rollup
m = fact.groupby(["MonthYear", "Scenario", "Account"])['Amount'].sum().reset_index()

# Pivot to compute KPIs
pivot = m.pivot_table(index=["MonthYear", "Scenario"], columns="Account", values="Amount", aggfunc="sum").fillna(0)

pivot["GrossMarginPct"] = (pivot["Gross Profit"] / pivot["Revenue"].replace({0: pd.NA})) * 100
pivot["OperatingIncome"] = pivot["Operating Income"]

kpi = pivot.reset_index()[["MonthYear", "Scenario", "Revenue", "Gross Profit", "Opex", "OperatingIncome", "GrossMarginPct"]]
kpi.to_csv(OUT / "monthly_kpis.csv", index=False)

# Charts
actual = kpi[kpi["Scenario"]=="Actual"].sort_values("MonthYear")
budget = kpi[kpi["Scenario"]=="Budget"].sort_values("MonthYear")

plt.figure()
plt.plot(actual["MonthYear"], actual["Revenue"], label="Actual")
plt.plot(budget["MonthYear"], budget["Revenue"], label="Budget")
plt.title("Revenue: Actual vs Budget")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT / "charts_revenue_actual_vs_budget.png", dpi=200)
plt.close()

plt.figure()
plt.plot(actual["MonthYear"], actual["GrossMarginPct"])
plt.title("Gross Margin % (Actual)")
plt.xlabel("Month")
plt.ylabel("Gross Margin %")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT / "charts_gross_margin_pct.png", dpi=200)
plt.close()

plt.figure()
plt.plot(actual["MonthYear"], actual["OperatingIncome"])
plt.title("Operating Income (Actual)")
plt.xlabel("Month")
plt.ylabel("Operating Income")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT / "charts_operating_income.png", dpi=200)
plt.close()

print("Wrote:", OUT)
