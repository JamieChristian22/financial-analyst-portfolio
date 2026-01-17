"""Marketplace KPI computation + lightweight charts.

Run:
  python marketplace_kpis.py

Outputs:
  - outputs/kpi_monthly.csv
  - outputs/top_categories.csv
  - outputs/top_sellers.csv
  - outputs/charts_*.png
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

fact = pd.read_csv(DATA / "fact_orders.csv", parse_dates=["OrderDate"])
prod = pd.read_csv(DATA / "dim_product.csv")
seller = pd.read_csv(DATA / "dim_seller.csv")

fact["Month"] = fact["OrderDate"].dt.to_period("M").dt.to_timestamp()

kpi = fact.groupby("Month").agg(
    GMV=("GMV", "sum"),
    MarketplaceRevenue=("CommissionAmount", "sum"),
    Orders=("OrderID", "nunique"),
    UnitsSold=("Quantity", "sum"),
).reset_index()
kpi["AOV"] = (kpi["GMV"] / kpi["Orders"]).round(2)
kpi["TakeRatePct"] = (kpi["MarketplaceRevenue"] / kpi["GMV"] * 100).round(2)

kpi.to_csv(OUT / "kpi_monthly.csv", index=False)

# Top categories
fc = fact.merge(prod[["ProductID", "Category"]], on="ProductID", how="left")
cat = fc.groupby("Category").agg(GMV=("GMV", "sum"), Orders=("OrderID", "nunique")).sort_values("GMV", ascending=False)
cat.to_csv(OUT / "top_categories.csv")

# Top sellers
fs = fact.merge(seller[["SellerID", "SellerName", "SellerTier"]], on="SellerID", how="left")
sel = fs.groupby(["SellerTier", "SellerName"]).agg(MarketplaceRevenue=("CommissionAmount", "sum"), GMV=("GMV", "sum")).sort_values("MarketplaceRevenue", ascending=False)
sel.head(25).to_csv(OUT / "top_sellers.csv")

# Charts
plt.figure()
plt.plot(kpi["Month"], kpi["GMV"])
plt.title("GMV Trend")
plt.xlabel("Month")
plt.ylabel("GMV")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT / "charts_gmv_trend.png", dpi=200)
plt.close()

plt.figure()
plt.plot(kpi["Month"], kpi["TakeRatePct"])
plt.title("Take Rate (%) Trend")
plt.xlabel("Month")
plt.ylabel("Take Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT / "charts_take_rate_trend.png", dpi=200)
plt.close()

print("Wrote:", OUT)
