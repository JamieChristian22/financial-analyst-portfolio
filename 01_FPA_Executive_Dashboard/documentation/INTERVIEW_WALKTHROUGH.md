# FP&A Interview Walkthrough

## 60-Second Project Pitch
“I built an end-to-end FP&A planning and performance model that mirrors a monthly corporate finance process. I started with department- and account-level budget and actual data, validated the source, created a monthly P&L and KPI scorecard, analyzed department and account variances, and translated those results into management commentary. I then built a driver-based FY2026 forecast, a forecast bridge, base/upside/downside scenarios, a sensitivity matrix, headcount and payroll planning, a cash forecast, and an illustrative DCF. I also documented controls, KPI definitions, version history, SQL reporting logic, Python validation, and a Power BI deployment blueprint. The focus was to show how FP&A moves from source data to management decisions.”

## Questions & Strong Answers

### What is the purpose of FP&A?
FP&A helps management understand performance, plan future results, allocate resources, and make decisions using financial and operational data.

### Budget vs Forecast
Budget is the approved annual plan. Forecast is the latest expectation using actual results and updated assumptions.

### Why use both variance $ and variance %?
Dollar variance communicates financial impact; percentage variance communicates relative magnitude. Both are needed because a small percentage on a large account may be more important than a large percentage on a small account.

### Why a 5% threshold?
It is an illustrative materiality threshold. In a real company I would calibrate it based on account size, volatility, company policy, and leadership preference.

### How would you investigate an unfavorable variance?
1. Validate the data.
2. Identify department/account/month.
3. Separate timing vs permanent variance.
4. Determine price, volume, mix, headcount, or one-time drivers.
5. Confirm with the business owner.
6. Update the forecast if the driver is recurring.
7. Assign an action and owner.

### How would you improve forecast accuracy?
- Driver-based assumptions
- actual-vs-prior-forecast tracking
- bias analysis
- business-partner input
- separate fixed and variable costs
- versioned assumption changes
- scenario ranges where uncertainty is high

### How is headcount linked to FP&A?
Headcount is often the largest controllable OpEx driver. FP&A should connect approved positions, hiring timing, salary, bonuses, and benefits to payroll forecasts.

### Why include cash?
Profit does not equal cash. A corporate forecast should show whether operating performance and investment assumptions create liquidity pressure.

### Why include controls?
Management reporting must be trusted. Source tie-outs, completeness checks, KPI definitions, assumption logs, and version control reduce reporting risk.

### What would change in a real company?
I would connect directly to the ERP/GL and HRIS, use actual chart-of-accounts mappings, automate refreshes, align materiality rules to finance policy, and work with budget owners on commentary and forecast updates.
