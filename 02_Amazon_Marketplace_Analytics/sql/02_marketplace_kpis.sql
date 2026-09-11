-- Marketplace KPI & management reporting queries
SELECT SUM(gmv) AS gmv, SUM(marketplace_revenue) AS marketplace_revenue, SUM(marketplace_revenue)/NULLIF(SUM(gmv),0) AS take_rate, AVG(refund_flag*1.0) AS refund_rate, SUM(contribution_margin) AS contribution_margin, SUM(contribution_margin)/NULLIF(SUM(marketplace_revenue),0) AS contribution_margin_pct, SUM(gmv)/NULLIF(COUNT(*),0) AS aov FROM fact_marketplace_orders;

SELECT category_name, SUM(gmv) AS gmv, SUM(marketplace_revenue) AS revenue, SUM(marketplace_revenue)/NULLIF(SUM(gmv),0) AS take_rate, AVG(refund_flag*1.0) AS refund_rate, SUM(contribution_margin) AS contribution_margin, SUM(contribution_margin)/NULLIF(SUM(marketplace_revenue),0) AS contribution_margin_pct FROM fact_marketplace_orders GROUP BY category_name ORDER BY contribution_margin DESC;

SELECT s.seller_name,s.seller_tier,SUM(f.gmv) AS gmv,SUM(f.marketplace_revenue) AS revenue,AVG(f.refund_flag*1.0) AS refund_rate,SUM(f.contribution_margin) AS contribution_margin FROM fact_marketplace_orders f JOIN dim_seller s ON s.seller_id=f.seller_id GROUP BY s.seller_name,s.seller_tier ORDER BY gmv DESC;

SELECT DATE_TRUNC('month',order_date) AS month,SUM(gmv) AS gmv,SUM(marketplace_revenue) AS revenue,SUM(contribution_margin) AS contribution_margin,AVG(refund_flag*1.0) AS refund_rate FROM fact_marketplace_orders GROUP BY 1 ORDER BY 1;

SELECT category_name,COUNT(*) AS orders,SUM(refund_flag) AS refunded_orders,AVG(refund_flag*1.0) AS refund_rate,SUM(refund_amount) AS refund_amount FROM fact_marketplace_orders GROUP BY category_name HAVING AVG(refund_flag*1.0)>=0.04 ORDER BY refund_rate DESC;