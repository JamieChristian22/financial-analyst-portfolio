"""FP&A metric computation for dashboard validation.

Run:
  python fpna_metrics.py

Outputs:
  - outputs/monthly_pl.csv
  - outputs/budget_vs_actual_revenue.csv
  - outputs/charts_pl_trend.png
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "finance_fact.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["TxnDate", "MonthYear"])

monthly = df.pivot_table(
    index=["MonthYear", "Scenario"],
    columns="AccountCategory",
    values="Amount",
    aggfunc="sum",
    fill_value=0,
).reset_index()

monthly["GrossProfit"] = monthly.get("Revenue", 0) - monthly.get("COGS", 0)
monthly["GrossMarginPct"] = (monthly["GrossProfit"] / monthly.get("Revenue", 0).replace({0: pd.NA}))
monthly["Opex"] = monthly.get("Opex", 0)
monthly["OperatingIncome"] = monthly["GrossProfit"] - monthly["Opex"]

monthly.to_csv(OUT / "monthly_pl.csv", index=False)

rev = df[df["AccountCategory"] == "Revenue"].pivot_table(
    index="MonthYear",
    columns="Scenario",
    values="Amount",
    aggfunc="sum",
    fill_value=0,
).reset_index()

rev["Variance"] = rev.get("Actual", 0) - rev.get("Budget", 0)
rev["VariancePct"] = rev["Variance"] / rev.get("Budget", 0).replace({0: pd.NA})
rev.to_csv(OUT / "budget_vs_actual_revenue.csv", index=False)

# Simple chart
actual = monthly[monthly["Scenario"] == "Actual"].sort_values("MonthYear")
plt.figure()
plt.plot(actual["MonthYear"], actual.get("Revenue", 0), label="Revenue")
plt.plot(actual["MonthYear"], actual["OperatingIncome"], label="Operating Income")
plt.title("Actual Revenue vs Operating Income")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(OUT / "charts_pl_trend.png", dpi=200)
plt.close()

print("Wrote:", OUT)
