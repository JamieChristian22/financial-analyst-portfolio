-- Budget vs Actual KPIs (Variance + Drivers)

-- 1) Monthly Revenue Variance
SELECT
  Month,
  SUM(CASE WHEN Account='Revenue' THEN Actual ELSE 0 END) AS revenue_actual,
  SUM(CASE WHEN Account='Revenue' THEN Budget ELSE 0 END) AS revenue_budget,
  SUM(CASE WHEN Account='Revenue' THEN (Actual-Budget) ELSE 0 END) AS revenue_variance
FROM fpa_budget_actual
GROUP BY Month
ORDER BY Month;

-- 2) Department OpEx Variance
SELECT
  Department,
  SUM(CASE WHEN Account IN ('Payroll','Software','Travel','Facilities','Other OpEx') THEN Actual ELSE 0 END) AS opex_actual,
  SUM(CASE WHEN Account IN ('Payroll','Software','Travel','Facilities','Other OpEx') THEN Budget ELSE 0 END) AS opex_budget,
  SUM(CASE WHEN Account IN ('Payroll','Software','Travel','Facilities','Other OpEx') THEN (Actual-Budget) ELSE 0 END) AS opex_variance
FROM fpa_budget_actual
GROUP BY Department
ORDER BY opex_variance DESC;

-- 3) Margin Bridge (Revenue - COGS)
SELECT
  Month,
  SUM(CASE WHEN Account='Revenue' THEN Actual ELSE 0 END) - SUM(CASE WHEN Account='COGS' THEN Actual ELSE 0 END) AS gross_profit_actual,
  SUM(CASE WHEN Account='Revenue' THEN Budget ELSE 0 END) - SUM(CASE WHEN Account='COGS' THEN Budget ELSE 0 END) AS gross_profit_budget
FROM fpa_budget_actual
GROUP BY Month
ORDER BY Month;
