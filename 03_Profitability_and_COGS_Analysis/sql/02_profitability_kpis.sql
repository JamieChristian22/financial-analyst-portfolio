-- Product profitability
SELECT product_line, SUM(net_revenue) revenue, SUM(cogs) cogs, SUM(gross_profit) gross_profit,
SUM(gross_profit)/NULLIF(SUM(net_revenue),0) gross_margin_pct
FROM profitability_transactions GROUP BY product_line ORDER BY gross_profit DESC;

-- Channel profitability
SELECT channel, SUM(net_revenue) revenue, SUM(gross_profit) gross_profit,
SUM(gross_profit)/NULLIF(SUM(net_revenue),0) gross_margin_pct
FROM profitability_transactions GROUP BY channel ORDER BY gross_margin_pct DESC;

-- Discount leakage
SELECT CASE WHEN discount_pct < .05 THEN '0-5%' WHEN discount_pct < .10 THEN '5-10%'
WHEN discount_pct < .15 THEN '10-15%' ELSE '15%+' END discount_band,
SUM(list_revenue-net_revenue) discount_leakage,
SUM(gross_profit)/NULLIF(SUM(net_revenue),0) gross_margin_pct
FROM profitability_transactions GROUP BY 1 ORDER BY 1;

-- COGS structure
SELECT SUM(material_cost) material, SUM(labor_cost) labor, SUM(freight_cost) freight,
SUM(manufacturing_overhead) overhead, SUM(cogs) total_cogs FROM profitability_transactions;

-- Monthly margin trend
SELECT DATE_TRUNC('month',transaction_date) month, SUM(net_revenue) revenue, SUM(cogs) cogs,
SUM(gross_profit) gross_profit, SUM(gross_profit)/NULLIF(SUM(net_revenue),0) gross_margin_pct
FROM profitability_transactions GROUP BY 1 ORDER BY 1;