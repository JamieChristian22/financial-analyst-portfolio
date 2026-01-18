-- KPI overview by acquisition channel
SELECT
  acquisition_channel,
  COUNT(*) AS users,
  ROUND(AVG(converted_to_paid::int)::numeric,3) AS conversion_rate,
  ROUND(AVG(retained_30d::int)::numeric,3) AS retention_30d,
  ROUND(SUM(total_revenue_usd),2) AS total_revenue_usd
FROM kpi_users
GROUP BY 1
ORDER BY total_revenue_usd DESC;
