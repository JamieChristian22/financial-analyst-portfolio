-- Monthly actual vs budget / forecast
SELECT
    month,
    business_unit,
    region,
    SUM(actual_revenue) AS actual_revenue,
    SUM(budget_revenue) AS budget_revenue,
    SUM(forecast_revenue) AS forecast_revenue,
    SUM(actual_revenue - budget_revenue) AS budget_variance,
    SUM(actual_revenue - forecast_revenue) AS forecast_variance,
    SUM(actual_revenue - actual_cogs - actual_opex) AS ebitda,
    SUM(actual_revenue - actual_cogs - actual_opex) / NULLIF(SUM(actual_revenue),0) AS ebitda_margin
FROM financial_performance
GROUP BY month, business_unit, region
ORDER BY month, business_unit, region;
