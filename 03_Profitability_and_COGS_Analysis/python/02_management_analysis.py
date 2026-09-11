import pandas as pd
df=pd.read_csv('data/profitability_transactions.csv')
product=df.groupby('ProductLine').agg(NetRevenue=('NetRevenue','sum'),COGS=('COGS','sum'),GrossProfit=('GrossProfit','sum'))
product['GrossMarginPct']=product.GrossProfit/product.NetRevenue
product.sort_values('GrossProfit',ascending=False).to_csv('outputs/product_profitability.csv')
channel=df.groupby('Channel').agg(NetRevenue=('NetRevenue','sum'),GrossProfit=('GrossProfit','sum'))
channel['GrossMarginPct']=channel.GrossProfit/channel.NetRevenue
channel.to_csv('outputs/channel_profitability.csv')