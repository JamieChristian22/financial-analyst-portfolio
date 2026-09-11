-- Corporate FP&A KPI queries
WITH p AS (
 SELECT month,
 SUM(CASE WHEN a.account_name='Revenue' THEN f.actual ELSE 0 END) revenue,
 SUM(CASE WHEN a.account_name='COGS' THEN f.actual ELSE 0 END) cogs,
 SUM(CASE WHEN a.account_group='OpEx' THEN f.actual ELSE 0 END) opex
 FROM fact_financials f JOIN dim_account a ON a.account_id=f.account_id GROUP BY month
)
SELECT month,revenue,cogs,revenue-cogs gross_profit,
(revenue-cogs)/NULLIF(revenue,0) gross_margin_pct,opex,
revenue-cogs-opex operating_profit,
(revenue-cogs-opex)/NULLIF(revenue,0) operating_margin_pct
FROM p ORDER BY month;

SELECT d.department_name,SUM(f.budget) opex_budget,SUM(f.actual) opex_actual,
SUM(f.actual-f.budget) variance_dollars,
SUM(f.actual-f.budget)/NULLIF(SUM(f.budget),0) variance_pct,
CASE WHEN ABS(SUM(f.actual-f.budget)/NULLIF(SUM(f.budget),0))>=0.05 THEN 'Escalate' ELSE 'Monitor' END review_status
FROM fact_financials f JOIN dim_department d ON d.department_id=f.department_id
JOIN dim_account a ON a.account_id=f.account_id WHERE a.account_group='OpEx'
GROUP BY d.department_name ORDER BY ABS(SUM(f.actual-f.budget)) DESC;

SELECT month,SUM(actual) monthly_actual,
AVG(SUM(actual)) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) rolling_3m_actual
FROM fact_financials GROUP BY month ORDER BY month;