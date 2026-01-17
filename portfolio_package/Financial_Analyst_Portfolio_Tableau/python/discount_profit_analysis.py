from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'final_data_brew_project.csv'
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=['Dt Transaction','Dt Product Launch'])
df['Month'] = df['Dt Transaction'].dt.to_period('M').dt.to_timestamp()
monthly = df.groupby('Month').agg({'Sales':'sum','Profit':'sum','Discount':'mean'}).reset_index()
monthly.to_csv(OUT/'monthly_sales_profit.csv', index=False)

plt.figure()
plt.plot(monthly['Month'], monthly['Sales'])
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT/'charts_sales_trend.png', dpi=200)
plt.close()

plt.figure()
plt.plot(monthly['Month'], monthly['Profit'])
plt.title('Monthly Profit Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT/'charts_profit_trend.png', dpi=200)
plt.close()

print('Wrote:', OUT)
