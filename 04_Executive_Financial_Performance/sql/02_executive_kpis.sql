-- Executive KPI reporting
SELECT
    year,
    SUM(actual_revenue) AS actual_revenue,
    SUM(budget_revenue) AS budget_revenue,
    SUM(actual_revenue) - SUM(budget_revenue) AS revenue_variance,
    (SUM(actual_revenue) - SUM(budget_revenue)) / NULLIF(SUM(budget_revenue),0) AS revenue_variance_pct,
    SUM(actual_revenue - actual_cogs) AS gross_profit,
    SUM(actual_revenue - actual_cogs) / NULLIF(SUM(actual_revenue),0) AS gross_margin,
    SUM(actual_revenue - actual_cogs - actual_opex) AS ebitda,
    SUM(actual_revenue - actual_cogs - actual_opex) / NULLIF(SUM(actual_revenue),0) AS ebitda_margin,
    SUM(operating_cash_flow) AS operating_cash_flow,
    SUM(operating_cash_flow) / NULLIF(SUM(actual_revenue - actual_cogs - actual_opex),0) AS cash_conversion
FROM financial_performance
GROUP BY year
ORDER BY year;
