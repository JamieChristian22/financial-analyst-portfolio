# Financial Analyst Portfolio Dashboard (Tableau)

This folder contains a fully populated dataset and supporting assets tailored to **Financial Analyst Portfolio Dashboard.twbx**.

## Included
- `data/final_data_brew_project.csv` - transaction-level sales and profitability data (2023-2025)
- `excel/Financial_Analyst_Model.xlsx` - monthly sales/profit rollup + discount impact + ROI mini-case
- `sql/create_tables.sql` - DDL to recreate tables
- `python/discount_profit_analysis.py` - discount vs profit impact exports + charts
- `docs/executive_summary.md` - business summary and recommendations

## How to use
1. In Tableau, connect to `data/final_data_brew_project.csv` (text file).
2. If any fields are missing, check that Tableau is using the first row as headers.
3. Run `python/discount_profit_analysis.py` to generate `outputs/` KPI tables and charts.

## Notes
The CSV includes both Title Case and snake_case columns for compatibility with different workbook field naming conventions.
