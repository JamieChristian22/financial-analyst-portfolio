"""Compute monthly financial KPIs + ratios used in the executive tableau view."""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "financial_data.csv", parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()

m = df.groupby("Month").agg(
    Revenue=("Sales", "sum"),
    COGS=("COGS", "sum"),
    Profit=("Profit", "sum"),
    Expenses=("Actual Expenses", "sum"),
    NetIncome=("Net Income", "sum"),
    Assets=("Total assets", "mean"),
    Liabilities=("Liabilities", "mean"),
    Equity=("Equity", "mean"),
).reset_index()

m["GrossMarginPct"] = (m["Revenue"] - m["COGS"]) / m["Revenue"]
m["OperatingMarginPct"] = (m["Profit"] - m["Expenses"]) / m["Revenue"]
m["ROA"] = m["NetIncome"] / m["Assets"]
m["DebtToEquity"] = m["Liabilities"] / m["Equity"]

out = ROOT / "outputs"
out.mkdir(exist_ok=True)
m.to_csv(out / "monthly_financial_kpis.csv", index=False)
print("Wrote", out / "monthly_financial_kpis.csv")
