-- Ecommerce funnel KPIs (Postgres-style SQL)
WITH events AS (
  SELECT *
  FROM ecommerce_events
)
SELECT
  year_month,
  COUNT(*) FILTER (WHERE event_name='viewed') AS viewed,
  COUNT(*) FILTER (WHERE event_name='add_to_cart') AS added_to_cart,
  COUNT(*) FILTER (WHERE event_name='checkout_started') AS checkout_started,
  COUNT(*) FILTER (WHERE event_name='purchased') AS purchased,
  ROUND( (COUNT(*) FILTER (WHERE event_name='purchased')::numeric / NULLIF(COUNT(*) FILTER (WHERE event_name='viewed'),0)) * 100, 2) AS view_to_purchase_pct
FROM events
GROUP BY 1
ORDER BY 1;
