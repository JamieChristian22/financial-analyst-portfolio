# FP&A Executive Analytics (Power BI)

This folder contains a complete FP&A dataset (Actual/Budget/Forecast) plus an Excel model (Budget vs Actual + DCF valuation) tailored to **FPnA_Executive_Analytics_Dashboard.pbix**.

## What is included
- `data/`
  - `finance_fact.csv` - monthly fact table (2023-2025)
  - `DateTable.csv` - daily date table with MonthYear, FiscalYear
- `excel/FPnA_Executive_Model.xlsx`
  - Assumptions, Monthly P&L, Budget vs Actual, Cash Flow, DCF Valuation, ROI case
- `sql/` create + KPI queries
- `python/` KPI script producing outputs + charts
- `docs/` executive summary

## Primary KPIs (aligned to dashboard)
- Revenue (Actual, Budget, Variance, Variance %)
- Opex (positive amount)
- Operating Income
- Gross Margin %

## Quick start
1. Open `FPnA_Executive_Analytics_Dashboard.pbix`.
2. Replace existing sources with the files in `data/`.
3. Run the Python script if you want the precomputed exports/charts:
   - `python python/fpa_kpis.py`

## Data dictionary (finance_fact)
- `TxnDate`, `MonthYear`, `FiscalYear`
- `Scenario` (Actual, Budget, Forecast)
- `Region`, `ProductLine`, `Department`
- `AccountCategory` (Revenue, COGS, Opex)
- `Account` (detailed line item)
- `Amount` (Revenue positive, COGS/Opex negative in the raw fact; the PBIX measure can flip sign for display)

