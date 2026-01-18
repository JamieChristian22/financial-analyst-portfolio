# Conversion, Retention & Revenue KPI Overview

## Business Problem
Provide a KPI overview that connects:
- Acquisition channel performance
- Conversion to paid
- 30-day retention
- Revenue by plan and channel

## Datasets
- `/data/kpi_users.csv` (user-level KPI dataset)
- `/data/marketing_spend_daily.csv` (CAC/ROI-style model inputs)

## Key KPIs
- Conversion Rate (to paid)
- Retention Rate (30d)
- Total Revenue, ARPPU (proxy)
- Channel ROI = (Attributed Revenue - Spend) / Spend

## How to Run
- SQL: `/sql/kpi_overview.sql`
- Python: `cd python && pip install -r requirements.txt && python main.py`
