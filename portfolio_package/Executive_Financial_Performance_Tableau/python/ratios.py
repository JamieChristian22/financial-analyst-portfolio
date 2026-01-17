from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'financial_data.csv'
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=['Date'])
df['Month'] = df['Date'].dt.to_period('M').dt.to_timestamp()
monthly = df.groupby('Month').agg({
    'Sales':'sum',
    'COGS':'sum',
    'Net Income':'sum',
    'Total assets':'mean',
    'Liabilities':'mean',
    'Equity':'mean',
    'Inventory':'mean'
}).reset_index()

monthly['Current Ratio'] = (monthly['Total assets'] / monthly['Liabilities']).round(3)
monthly['Quick Ratio'] = ((monthly['Total assets'] - monthly['Inventory']) / monthly['Liabilities']).round(3)
monthly['Debt-to-Equity Ratio'] = (monthly['Liabilities'] / monthly['Equity']).round(3)
monthly['Return on Assets'] = (monthly['Net Income'] / monthly['Total assets']).round(4)

monthly.to_csv(OUT / 'monthly_ratios.csv', index=False)

plt.figure()
plt.plot(monthly['Month'], monthly['Current Ratio'])
plt.title('Current Ratio Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT / 'charts_current_ratio.png', dpi=200)
plt.close()

plt.figure()
plt.plot(monthly['Month'], monthly['Debt-to-Equity Ratio'])
plt.title('Debt-to-Equity Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT / 'charts_de_ratio.png', dpi=200)
plt.close()

print('Wrote:', OUT)
