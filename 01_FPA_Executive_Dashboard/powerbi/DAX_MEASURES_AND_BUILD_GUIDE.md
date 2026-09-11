# Power BI DAX Library
```DAX
Total Budget = SUM(Financials[Budget])
Total Actual = SUM(Financials[Actual])
Variance $ = [Total Actual] - [Total Budget]
Variance % = DIVIDE([Variance $], [Total Budget])
Revenue Actual = CALCULATE([Total Actual], Financials[Account] = "Revenue")
COGS Actual = CALCULATE([Total Actual], Financials[Account] = "COGS")
Gross Profit = [Revenue Actual] - [COGS Actual]
Gross Margin % = DIVIDE([Gross Profit], [Revenue Actual])
Total OpEx = CALCULATE([Total Actual], Financials[Account] IN {"Payroll","Software","Travel","Facilities","Other OpEx"})
Operating Profit = [Gross Profit] - [Total OpEx]
Operating Margin % = DIVIDE([Operating Profit], [Revenue Actual])
Material Variance Flag = IF(ABS([Variance %]) >= 0.05, 1, 0)
```
Recommended pages: Executive Overview, P&L Trend, Department Variance, Account Drivers, Forecast & Scenario, Variance Commentary.