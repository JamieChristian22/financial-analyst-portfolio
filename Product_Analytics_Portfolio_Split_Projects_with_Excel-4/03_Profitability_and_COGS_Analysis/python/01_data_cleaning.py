import pandas as pd

orders = pd.read_csv('../data/fact_orders.csv', parse_dates=['OrderDate'])
product = pd.read_csv('../data/dim_product.csv')
seller = pd.read_csv('../data/dim_seller.csv')

# Clean / enrich
orders['GMV_Net'] = orders.apply(lambda r: 0 if r['IsRefund']==1 else r['GMV'], axis=1)
orders['MarketplaceRevenue_Net'] = orders.apply(lambda r: 0 if r['IsRefund']==1 else r['MarketplaceRevenue'], axis=1)

df = orders.merge(product, on='ProductID').merge(seller, on='SellerID')
df['Month'] = df['OrderDate'].dt.to_period('M').dt.to_timestamp()

# Save a model-ready table
out = df[['OrderID','OrderDate','Month','Category','SellerTier','Region','Device','Quantity','DiscountPct','GMV_Net','MarketplaceRevenue_Net','UnitCost','ListPrice']]
out.to_csv('../data/model_orders_enriched.csv', index=False)
print('Wrote ../data/model_orders_enriched.csv with', len(out), 'rows')
