import pandas as pd
df=pd.read_csv('data/profitability_transactions.csv')
assert df.TransactionID.is_unique
assert not df.isna().any().any()
assert (abs(df.COGS-(df.MaterialCost+df.LaborCost+df.FreightCost+df.ManufacturingOverhead)) < .06).all()
assert (abs(df.GrossProfit-(df.NetRevenue-df.COGS)) < .06).all()
print(f'Validated {len(df):,} transactions')