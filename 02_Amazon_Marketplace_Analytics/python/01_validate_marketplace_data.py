from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data'/'fact_marketplace_orders.csv',parse_dates=['OrderDate'])
required={'OrderID','OrderDate','SellerID','SellerTier','Category','GMV','TakeRate','MarketplaceRevenue','RefundFlag','RefundAmount','ContributionMargin'}
missing=required-set(df.columns)
if missing: raise ValueError(f'Missing columns: {sorted(missing)}')
if df['OrderID'].duplicated().any(): raise ValueError('Duplicate OrderID detected')
if df[list(required)].isna().any().any(): raise ValueError('Null required fields detected')
if (df['GMV']<0).any(): raise ValueError('Negative GMV detected')
if (~df['RefundFlag'].isin([0,1])).any(): raise ValueError('RefundFlag must be 0/1')
df['CalculatedRevenue']=df['GMV']*df['TakeRate']
df['RevenueVariance']=df['MarketplaceRevenue']-df['CalculatedRevenue']
print(f'Validated {len(df):,} marketplace orders')
print(f'Max revenue reconciliation variance: {df["RevenueVariance"].abs().max():.2f}')