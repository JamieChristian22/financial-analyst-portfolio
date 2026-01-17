-- KPI Scorecard
-- GMV = sum(UnitPrice * Quantity)
-- Marketplace Revenue = sum(CommissionAmount)

SELECT
  DATE_TRUNC('month', fo.OrderDate)::date AS month,
  SUM(fo.GMV) AS gmv,
  SUM(fo.CommissionAmount) AS marketplace_revenue,
  COUNT(DISTINCT fo.OrderID) AS orders,
  SUM(fo.Quantity) AS units_sold,
  CASE WHEN COUNT(DISTINCT fo.OrderID)=0 THEN 0
       ELSE SUM(fo.GMV)/COUNT(DISTINCT fo.OrderID) END AS aov,
  CASE WHEN SUM(fo.GMV)=0 THEN 0
       ELSE SUM(fo.CommissionAmount)/SUM(fo.GMV) END AS take_rate
FROM fact_orders fo
GROUP BY 1
ORDER BY 1;

-- Revenue by Category
SELECT
  p.Category,
  SUM(fo.CommissionAmount) AS marketplace_revenue
FROM fact_orders fo
JOIN dim_product p USING (ProductID)
GROUP BY 1
ORDER BY marketplace_revenue DESC;

-- Seller Tier Performance
SELECT
  s.SellerTier,
  SUM(fo.CommissionAmount) AS marketplace_revenue,
  SUM(fo.GMV) AS gmv,
  COUNT(DISTINCT fo.OrderID) AS orders
FROM fact_orders fo
JOIN dim_seller s USING (SellerID)
GROUP BY 1
ORDER BY marketplace_revenue DESC;
