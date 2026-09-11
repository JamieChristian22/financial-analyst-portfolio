# FP&A Executive Planning & Performance Management Portfolio

## Executive Overview
This project is a corporate-style FP&A work sample designed to simulate the recurring finance process an analyst supports in a real organization: data validation, monthly close support, budget vs. actual reporting, variance analysis, driver-based forecasting, scenario planning, headcount planning, liquidity monitoring, executive reporting, and finance controls.

The model uses a fully synthetic dataset so it can be shared publicly without exposing confidential company information.

## Business Questions Answered
- Are revenue, gross margin, OpEx, operating profit, and cash tracking to plan?
- Which departments and accounts are driving material variance?
- Which unfavorable variances require management escalation?
- How should the forecast change when revenue growth, COGS, payroll, software, or travel assumptions move?
- What is the FY2026 base, upside, and downside outlook?
- Is planned headcount financially supportable?
- Does the business maintain adequate liquidity?
- Can every executive KPI be traced to a documented definition and source?

## End-to-End FP&A Workflow
**Source Data → Validation → Monthly P&L → KPI Scorecard → Variance Analysis → Management Commentary → Forecast Bridge → Rolling Forecast → Scenario & Sensitivity Analysis → Headcount Plan → Cash Forecast → Executive Dashboard → Governance & Controls**

## Main Excel Deliverable
`excel/FPnA_Corporate_Planning_Model.xlsx`

### Workbook Structure
1. **Executive Dashboard** — leadership-ready KPI and decision-support view
2. **KPI Scorecard** — plan vs actual status across core financial KPIs
3. **Assumptions** — centralized base/upside/downside planning drivers
4. **Raw Data** — 420-row department/account/month budget and actual dataset
5. **Monthly P&L** — monthly and FY actual performance
6. **Department Variance** — department OpEx variance and materiality status
7. **Forecast Bridge** — FY2025 actual to FY2026 forecast walk
8. **Forecast** — driver-based FY2026 monthly outlook
9. **Scenario Planning** — base/upside/downside planning cases
10. **Sensitivity Analysis** — revenue growth vs COGS sensitivity matrix
11. **Headcount Plan** — staffing, compensation, benefits, payroll impact
12. **Cash Flow Forecast** — monthly free cash flow and liquidity monitoring
13. **DCF Valuation** — illustrative five-year unlevered DCF
14. **Management Commentary** — root cause, financial impact, action, owner
15. **Controls** — recurring close/reporting control framework
16. **Data Dictionary** — KPI and field definitions
17. **Assumption Change Log** — forecast governance and approval trail
18. **Version Control** — model change history and release status

## Core KPIs
- Revenue
- Gross Profit
- Gross Margin %
- Total OpEx
- Operating Profit
- Operating Margin %
- Budget vs Actual Variance $
- Budget vs Actual Variance %
- Department OpEx Variance %
- Material Variance Status
- FY2026 Forecast Revenue
- FY2026 Forecast Operating Profit
- Headcount / Payroll
- Free Cash Flow
- Ending Cash
- Liquidity Status

## Finance Model Conventions
- **Blue font** = hardcoded user inputs / assumptions
- **Green font** = links to other worksheets
- **Black font** = formulas / calculations
- **Yellow fill** = key assumptions requiring review
- **Negative values** = red parentheses
- **Zeros** = dash
- **Materiality threshold** = absolute variance ≥ 5% for management review

## Technical Stack
### Excel
Financial modeling, P&L reporting, assumptions, forecast logic, scenario planning, variance analysis, DCF, controls, and executive reporting.

### SQL
Corporate-style reporting schema plus KPI, variance, rolling-trend, and management reporting queries.

### Power BI / DAX
A deployment-ready BI handoff pack includes DAX measures, a date table, data-model specification, executive dashboard page blueprint, corporate theme, refresh checklist, and reconciliation process.

### Python
Validation and management-analysis scripts demonstrate how finance data could be checked and prepared before recurring reporting.

## Corporate Controls Demonstrated
- Source-to-model reconciliation
- Completeness checks
- Duplicate/null validation
- Material variance review
- Forecast assumption change log
- Dashboard-to-model tie-out
- Version control
- Access-review concept
- Monthly archive process

## Why This Project Is Job-Ready
This project demonstrates more than spreadsheet mechanics. It shows the full FP&A thought process:
1. Validate financial data.
2. Translate actuals into a structured P&L.
3. Explain plan vs actual performance.
4. Identify financial drivers and management risks.
5. Update the forward outlook.
6. Evaluate scenarios and sensitivities.
7. Link headcount and operating assumptions to the forecast.
8. Monitor liquidity.
9. Communicate actions to business partners and leadership.
10. Maintain traceability, controls, and version discipline.

## Portfolio Disclosure
All financial values, assumptions, departments, and scenarios are synthetic and created solely for portfolio demonstration.

## Author
Jamie Christian  
Financial Analysis | FP&A | Business Intelligence | Data Analytics
