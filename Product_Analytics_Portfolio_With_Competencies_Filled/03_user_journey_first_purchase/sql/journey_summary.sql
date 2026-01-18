-- Journey to first purchase: behavioral predictors
SELECT
  first_medium,
  COUNT(*) AS purchasers,
  ROUND(AVG(sessions_before_purchase),2) AS avg_sessions_before_purchase,
  ROUND(AVG(median_events),1) AS avg_events_per_journey,
  ROUND(AVG(first_purchase_revenue_usd),2) AS avg_first_purchase_revenue
FROM first_purchase_journey
GROUP BY 1
ORDER BY purchasers DESC;
