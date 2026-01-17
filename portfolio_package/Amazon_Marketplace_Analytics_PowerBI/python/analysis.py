"""Amazon Marketplace Analytics - quick KPI checks.

Run:
  python analysis.py

Outputs:
  - console KPI summary
  - charts/ directory with a few PNGs (matplotlib)
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
PROJ = HERE.parent
DATA = PROJ / 'data'
OUT = PROJ / 'python' / 'charts'
OUT.mkdir(parents=True, exist_ok=True)

fact = pd.read_csv(DATA / 'fact_orders.csv', parse_dates=['OrderDate'])
prod = pd.read_csv(DATA / 'dim_product.csv')
seller = pd.read_csv(DATA / 'dim_seller.csv')

fact['Month'] = fact['OrderDate'].dt.to_period('M').dt.to_timestamp()
monthly = fact.groupby('Month').agg(
    GMV=('GrossAmount','sum'),
    MarketplaceRevenue=('MarketplaceRevenue','sum'),
    Orders=('OrderID','nunique'),
    UnitsSold=('Quantity','sum'),
    NetSales=('NetAmount','sum')
).reset_index()
monthly['TakeRate'] = monthly['MarketplaceRevenue'] / monthly['GMV']
monthly['AOV'] = monthly['NetSales'] / monthly['Orders']

print('--- Marketplace KPI Snapshot ---')
print('GMV:', round(monthly['GMV'].sum(),2))
print('Marketplace Revenue:', round(monthly['MarketplaceRevenue'].sum(),2))
print('Take Rate:', round((monthly['MarketplaceRevenue'].sum()/monthly['GMV'].sum()),4))
print('Orders:', int(monthly['Orders'].sum()))
print('Units Sold:', int(monthly['UnitsSold'].sum()))
print('Avg AOV:', round(monthly['AOV'].mean(),2))

# Trend charts
plt.figure()
plt.plot(monthly['Month'], monthly['GMV'])
plt.title('GMV Trend')
plt.xlabel('Month'); plt.ylabel('GMV')
plt.tight_layout()
plt.savefig(OUT / 'gmv_trend.png', dpi=200)
plt.close()

plt.figure()
plt.plot(monthly['Month'], monthly['MarketplaceRevenue'])
plt.title('Marketplace Revenue Trend')
plt.xlabel('Month'); plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig(OUT / 'marketplace_revenue_trend.png', dpi=200)
plt.close()

# Category revenue bar
cat = fact.merge(prod, on='ProductID').groupby('Category').agg(Revenue=('MarketplaceRevenue','sum')).sort_values('Revenue', ascending=False)
plt.figure()
plt.bar(cat.index, cat['Revenue'])
plt.title('Marketplace Revenue by Category')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(OUT / 'revenue_by_category.png', dpi=200)
plt.close()
