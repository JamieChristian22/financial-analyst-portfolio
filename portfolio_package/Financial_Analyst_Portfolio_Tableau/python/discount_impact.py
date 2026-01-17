from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'final_data_brew_project.csv'
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=['Dt Transaction','Dt Product Launch'])

df['DiscountFlag'] = (df['Discount'] > 0).map({True:'Discounted', False:'No Discount'})
by_brand = df.groupby(['Brand','DiscountFlag']).agg(Sales=('Sales','sum'), Profit=('Profit','sum')).reset_index()
by_brand['Margin'] = by_brand['Profit'] / by_brand['Sales'].replace(0, pd.NA)
by_brand.to_csv(OUT / 'discount_impact_by_brand.csv', index=False)

# Simple margin chart for top 5 brands by sales
brand_sales = df.groupby('Brand')['Sales'].sum().sort_values(ascending=False).head(5).index
plot_df = by_brand[by_brand['Brand'].isin(brand_sales)].pivot(index='Brand', columns='DiscountFlag', values='Margin')

plt.figure()
plot_df.plot(kind='bar')
plt.title('Margin: Discounted vs No Discount (Top Brands)')
plt.ylabel('Margin')
plt.tight_layout()
plt.savefig(OUT / 'charts_discount_margin_by_brand.png', dpi=200)
plt.close()

print('Wrote outputs to', OUT)
