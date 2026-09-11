-- Business unit ranking
SELECT
    business_unit,
    SUM(actual_revenue) AS actual_revenue,
    SUM(budget_revenue) AS budget_revenue,
    SUM(actual_revenue - budget_revenue) AS revenue_variance,
    SUM(actual_revenue - actual_cogs - actual_opex) AS ebitda,
    SUM(actual_revenue - actual_cogs - actual_opex) / NULLIF(SUM(actual_revenue),0) AS ebitda_margin,
    SUM(actual_revenue) / NULLIF(SUM(SUM(actual_revenue)) OVER (),0) AS revenue_mix
FROM financial_performance
WHERE year = 2026
GROUP BY business_unit
ORDER BY actual_revenue DESC;
