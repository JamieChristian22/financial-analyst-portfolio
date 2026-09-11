# Power BI Data Model Specification

## Fact Table
**Financials**
- Month
- Department
- Account
- Budget
- Actual
- Variance
- VariancePct

## Dimensions
### Date
Calendar dimension for period filtering and time-series reporting.

### Department
Optional normalized dimension if the project is expanded beyond the flat portfolio dataset.

### Account
Recommended attributes:
- Account
- Account Group
- P&L Order
- Expense Type
- Favorability Direction

## Relationships
- Date[Date] 1:* Financials[Month]
- Department[Department] 1:* Financials[Department]
- Account[Account] 1:* Financials[Account]

## Recommended Modeling Rules
- Use a star schema.
- Hide raw numeric columns when measures exist.
- Use explicit measures rather than implicit aggregations.
- Keep business-facing measure names consistent with the Excel model.
- Reconcile total Revenue, COGS, OpEx, and Operating Profit to Excel before publishing.
