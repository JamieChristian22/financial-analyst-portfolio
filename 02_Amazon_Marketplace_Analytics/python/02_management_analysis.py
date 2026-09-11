from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
df=pd.read_csv(ROOT/'data'/'fact_marketplace_orders.csv',parse_dates=['OrderDate'])
category=df.groupby('Category',as_index=False).agg(GMV=('GMV','sum'),MarketplaceRevenue=('MarketplaceRevenue','sum'),Orders=('OrderID','count'),RefundRate=('RefundFlag','mean'),ContributionMargin=('ContributionMargin','sum'))
category['TakeRate']=category['MarketplaceRevenue']/category['GMV']; category['ContributionMarginPct']=category['ContributionMargin']/category['MarketplaceRevenue']; category.to_csv(OUT/'category_profitability_summary.csv',index=False)
seller=df.groupby(['SellerName','SellerTier'],as_index=False).agg(GMV=('GMV','sum'),MarketplaceRevenue=('MarketplaceRevenue','sum'),Orders=('OrderID','count'),RefundRate=('RefundFlag','mean'),ContributionMargin=('ContributionMargin','sum')); seller['ContributionMarginPct']=seller['ContributionMargin']/seller['MarketplaceRevenue']; seller.sort_values('GMV',ascending=False).to_csv(OUT/'seller_scorecard.csv',index=False)