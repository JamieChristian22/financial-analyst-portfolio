# Executive Financial Performance (Tableau)

This folder contains a fully populated dataset and supporting assets tailored to **Executive Financial Performance Dashboard.twbx**.

## Included
- `data/financial_data.csv` - transaction-level finance/sales data (2023-2025)
- `excel/Executive_Financial_Model.xlsx` - monthly P&L, ratios, and ROI mini-case
- `sql/create_tables.sql` - DDL to recreate tables
- `python/ratios.py` - computes monthly ratios and exports charts to `outputs/`
- `docs/executive_summary.md` - leadership-facing summary and recommended decisions

## How to use
1. In Tableau, replace the existing extract with `data/financial_data.csv` (or connect as a text file).
2. Validate KPIs (Sales, Profit, Profit Margin) and ratios.
3. Optionally, run `python/ratios.py` for a separate KPI pack.

## Notes
Some columns are duplicated with trailing spaces (for compatibility with fields seen in the original packaged workbook).
