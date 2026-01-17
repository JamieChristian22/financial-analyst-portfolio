"""Compute monthly financial KPIs + simple charts."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "financial_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()
monthly = df.groupby("Month", as_index=False).agg(
    Revenue=("Sales","sum"),
    COGS=("COGS","sum"),
    Profit=("Profit","sum"),
    Opex=("Actual Expenses","sum"),
    NetIncome=("Net Income","sum"),
)
monthly["GrossMarginPct"] = (monthly["Profit"]/monthly["Revenue"]).fillna(0)*100
monthly.to_csv(OUT/"monthly_pnl.csv", index=False)

plt.figure()
plt.plot(monthly["Month"], monthly["Revenue"])
plt.xticks(rotation=45)
plt.title("Revenue Trend")
plt.tight_layout()
plt.savefig(OUT/"charts_revenue_trend.png", dpi=200)
plt.close()

plt.figure()
plt.plot(monthly["Month"], monthly["GrossMarginPct"])
plt.xticks(rotation=45)
plt.title("Gross Margin %")
plt.tight_layout()
plt.savefig(OUT/"charts_gm_pct.png", dpi=200)
plt.close()

print("Wrote", OUT)
