# StreamFlow SaaS Product Analytics

## Business Problem
Understand product health for a SaaS product using core product analytics:
- DAU trends, MRR, paid users (30d)
- Feature engagement and activation behaviors
- Revenue patterns and plan performance

## Dataset
- `/data/streamflow_events.csv` (event-level)
- `/data/pricing_plans.csv` (plan dimension)

## Key KPIs
- DAU
- Current MRR (proxy via subscription revenue)
- Paid users (last 30 days)
- Feature adoption by event_name

## How to Run
- SQL: `/sql/dau_revenue.sql`
- Python: `cd python && pip install -r requirements.txt && python main.py`
