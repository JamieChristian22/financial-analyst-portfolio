-- StreamFlow DAU + Revenue
WITH d AS (
  SELECT
    event_date::date AS dt,
    COUNT(DISTINCT user_id) AS dau,
    SUM(revenue_usd) AS revenue_usd
  FROM streamflow_events
  GROUP BY 1
)
SELECT * FROM d ORDER BY dt;
