# Amazon Marketplace Analytics (Power BI)

This folder contains a fully populated, portfolio-ready dataset and analysis assets tailored to the metrics used in **Amazon_Marketplace_Analytics_Dashboard.pbix**.

## What is included
- `data/`
  - `dim_calendar.csv` - daily calendar (2023-2025) with YearMonth
  - `dim_product.csv` - products + pricing
  - `dim_seller.csv` - seller tiers + commission rates
  - `dim_customer.csv` - segment + region
  - `fact_orders.csv` - order line level facts with precomputed GMV, CommissionAmount, and ShippingRevenue
- `excel/Marketplace_Analytics_Model.xlsx`
  - KPI scorecard + monthly rollups + take-rate / ROI calculator
- `sql/`
  - `create_tables.sql` - DDL to load into a database
  - `analysis_queries.sql` - common KPI queries (monthly KPIs, top categories, take rate)
- `python/marketplace_kpis.py`
  - computes KPIs and exports charts/CSVs
- `docs/executive_summary.md`

## How to use with Power BI
1. Open the provided PBIX.
2. In **Transform data**, point each table to the matching CSVs in `data/`.
3. Refresh - visuals should populate immediately.

## Data notes
- Dates span **2023-01-01 to 2025-12-31**.
- Commission rate is stored in `dim_seller` and applied to order lines.
- Refunds and shipping are included to enable deeper profitability questions.
