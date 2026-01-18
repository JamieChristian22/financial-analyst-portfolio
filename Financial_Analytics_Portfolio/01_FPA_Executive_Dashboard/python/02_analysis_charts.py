import pandas as pd
import matplotlib.pyplot as plt

fpa = pd.read_csv('../data/fpa_budget_actual_enriched.csv', parse_dates=['Month'])

# Revenue trend (Budget vs Actual)
rev = fpa[fpa['Account']=='Revenue'].groupby('Month', as_index=False).agg(Budget=('Budget','sum'), Actual=('Actual','sum'))

plt.figure()
plt.plot(rev['Month'], rev['Budget'], label='Budget')
plt.plot(rev['Month'], rev['Actual'], label='Actual')
plt.title('Revenue: Budget vs Actual')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('../outputs/revenue_budget_vs_actual.png', dpi=160)

# OpEx variance by department
opex = fpa[fpa['Account'].isin(['Payroll','Software','Travel','Facilities','Other OpEx'])].groupby('Department', as_index=False).agg(Variance=('Variance','sum'))

plt.figure()
plt.bar(opex['Department'], opex['Variance'])
plt.title('OpEx Variance by Department')
plt.xlabel('Department')
plt.ylabel('Variance ($)')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('../outputs/opex_variance_by_department.png', dpi=160)

print('Saved charts to ../outputs/')
