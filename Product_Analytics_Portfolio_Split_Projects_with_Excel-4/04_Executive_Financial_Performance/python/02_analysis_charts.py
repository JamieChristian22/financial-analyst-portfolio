import pandas as pd
import matplotlib.pyplot as plt

# Load enriched data
_df = pd.read_csv('../data/model_orders_enriched.csv', parse_dates=['OrderDate','Month'])

# KPI: monthly take rate
kpi = _df.groupby('Month', as_index=False).agg(gmv=('GMV_Net','sum'), rev=('MarketplaceRevenue_Net','sum'))
kpi['take_rate'] = kpi['rev'] / kpi['gmv']

plt.figure()
plt.plot(kpi['Month'], kpi['take_rate'])
plt.title('Take Rate Trend (Net)')
plt.xlabel('Month')
plt.ylabel('Take Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../outputs/take_rate_trend.png', dpi=160)

# KPI: revenue by category
cat = _df.groupby('Category', as_index=False).agg(rev=('MarketplaceRevenue_Net','sum')).sort_values('rev', ascending=False)
plt.figure()
plt.bar(cat['Category'], cat['rev'])
plt.title('Marketplace Revenue by Category (Net)')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig('../outputs/revenue_by_category.png', dpi=160)

print('Saved charts to ../outputs/')
