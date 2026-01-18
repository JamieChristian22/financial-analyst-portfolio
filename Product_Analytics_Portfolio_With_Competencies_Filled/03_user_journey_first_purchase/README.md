# User Journey to First Purchase

## Business Problem
Determine what user behaviors predict **faster first purchase** and which acquisition mediums produce the best journey quality.

## Dataset
`/data/first_purchase_journey.csv` includes aggregated journey metrics:
- sessions/visits before purchase
- median events and duration
- first purchase quantity and revenue
- first acquisition medium (first_medium)

## Key KPIs
- Avg sessions before purchase
- Avg events per journey
- Avg first purchase revenue
- Segment comparisons by medium

## How to Run
- SQL: `/sql/journey_summary.sql`
- Python: `cd python && pip install -r requirements.txt && python main.py`
