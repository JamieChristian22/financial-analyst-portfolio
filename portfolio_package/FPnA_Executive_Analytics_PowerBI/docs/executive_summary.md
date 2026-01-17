# Executive Summary - FP&A Executive Analytics

## Objective
Provide a leadership-ready view of performance across **Revenue**, **Opex**, **Operating Income**, and **Gross Margin** with clear **Budget vs Actual** variance and drill-down by Region, ProductLine, and Department.

## Dataset design
- The model uses a single normalized fact table `finance_fact.csv` (monthly grain) with common FP&A dimensions:
  - `Scenario` (Actual/Budget/Forecast)
  - `Region`, `ProductLine`, `Department`
  - `Account` + `AccountCategory`
  - Amount is signed: Revenue positive; Expense categories negative.

## Decision examples embedded in the Excel model
- **Budget accountability**: identify departments where Opex variance is persistent across multiple months.
- **Growth investment**: evaluate marketing spend vs incremental gross profit (ROI section).
- **Valuation**: a lightweight DCF in `FPnA_Executive_Model.xlsx` ties assumptions to free cash flow and implied enterprise value.
