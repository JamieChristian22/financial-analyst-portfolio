-- Revenue (Actual vs Budget) by month
SELECT
  MonthYear,
  SUM(CASE WHEN Scenario='Actual' AND AccountCategory='Revenue' THEN Amount ELSE 0 END) AS revenue_actual,
  SUM(CASE WHEN Scenario='Budget' AND AccountCategory='Revenue' THEN Amount ELSE 0 END) AS revenue_budget,
  SUM(CASE WHEN Scenario='Actual' AND AccountCategory='Revenue' THEN Amount ELSE 0 END)
  - SUM(CASE WHEN Scenario='Budget' AND AccountCategory='Revenue' THEN Amount ELSE 0 END) AS revenue_variance,
  CASE WHEN SUM(CASE WHEN Scenario='Budget' AND AccountCategory='Revenue' THEN Amount ELSE 0 END)=0 THEN 0
       ELSE (
        (SUM(CASE WHEN Scenario='Actual' AND AccountCategory='Revenue' THEN Amount ELSE 0 END)
         - SUM(CASE WHEN Scenario='Budget' AND AccountCategory='Revenue' THEN Amount ELSE 0 END))
        / SUM(CASE WHEN Scenario='Budget' AND AccountCategory='Revenue' THEN Amount ELSE 0 END)
       ) END AS revenue_variance_pct
FROM finance_fact
GROUP BY 1
ORDER BY 1;

-- Gross Margin % (Actual)
SELECT
  MonthYear,
  (SUM(CASE WHEN Scenario='Actual' AND Account='Gross Profit' THEN Amount ELSE 0 END)
   / NULLIF(SUM(CASE WHEN Scenario='Actual' AND Account='Revenue' THEN Amount ELSE 0 END),0)) AS gross_margin_pct
FROM finance_fact
GROUP BY 1
ORDER BY 1;
