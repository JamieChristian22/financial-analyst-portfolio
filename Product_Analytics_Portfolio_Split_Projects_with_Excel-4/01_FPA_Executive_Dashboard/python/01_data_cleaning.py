import pandas as pd

fpa = pd.read_csv('../data/fpa_budget_actual.csv', parse_dates=['Month'])

# Standardize
fpa['Account'] = fpa['Account'].str.strip()
fpa['Department'] = fpa['Department'].str.strip()

# Variances
fpa['Variance'] = fpa['Actual'] - fpa['Budget']
fpa['VariancePct'] = fpa.apply(lambda r: 0 if r['Budget']==0 else r['Variance']/r['Budget'], axis=1)

fpa.to_csv('../data/fpa_budget_actual_enriched.csv', index=False)
print('Wrote ../data/fpa_budget_actual_enriched.csv')
