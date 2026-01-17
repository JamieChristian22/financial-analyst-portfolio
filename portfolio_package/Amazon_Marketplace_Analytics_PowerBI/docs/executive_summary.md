# Executive Summary - Amazon Marketplace Analytics

## Business context
This project models a multi-seller marketplace (Amazon-style) where revenue is earned through a commission ("take rate") on gross merchandise value (GMV).

## Key KPIs used in the dashboard
- **GMV** = sum(UnitPrice * Quantity)
- **Marketplace Revenue** = sum(CommissionAmount)
- **Take Rate %** = Marketplace Revenue / GMV
- **Orders** = distinct OrderID
- **Units Sold** = sum(Quantity)
- **AOV** = GMV / Orders

## What the dashboard answers
- Which **product categories** drive GMV and marketplace revenue?
- Which **seller tiers** and **regions/segments** contribute the most?
- Are we improving GMV **YoY** and is take rate stable?

## Decision examples (ROI-driven)
1) **Increase commission on low-price high-volume categories**
   - Hypothesis: small take rate increase (e.g., +0.3%) lifts revenue with minimal GMV impact.
2) **Prioritize Enterprise sellers**
   - Enterprise tier has larger baskets (higher AOV) and more consistent order cadence.
3) **Reduce refunds**
   - Even a 0.5-1.0 pp drop in refund rate can materially improve net marketplace revenue.
