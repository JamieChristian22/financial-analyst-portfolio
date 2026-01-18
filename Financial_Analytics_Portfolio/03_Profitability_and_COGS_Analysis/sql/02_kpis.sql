-- KPI Tables and Joins

-- 1) Revenue / GMV by Category
SELECT
  p.Category,
  SUM(CASE WHEN o.IsRefund=1 THEN 0 ELSE o.GMV END) AS gmv_net,
  SUM(CASE WHEN o.IsRefund=1 THEN 0 ELSE o.MarketplaceRevenue END) AS marketplace_revenue_net,
  AVG(o.DiscountPct) AS avg_discount_pct,
  COUNT(DISTINCT o.OrderID) AS orders
FROM fact_orders o
JOIN dim_product p ON o.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY marketplace_revenue_net DESC;

-- 2) Seller Tier Performance
SELECT
  s.SellerTier,
  COUNT(DISTINCT o.SellerID) AS active_sellers,
  SUM(CASE WHEN o.IsRefund=1 THEN 0 ELSE o.GMV END) AS gmv_net,
  SUM(CASE WHEN o.IsRefund=1 THEN 0 ELSE o.MarketplaceRevenue END) AS marketplace_revenue_net,
  SUM(CASE WHEN o.IsRefund=1 THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS refund_rate
FROM fact_orders o
JOIN dim_seller s ON o.SellerID = s.SellerID
GROUP BY s.SellerTier
ORDER BY marketplace_revenue_net DESC;

-- 3) Unit Economics: Take Rate and Contribution Margin Proxy
SELECT
  DATE_TRUNC('month', o.OrderDate) AS month,
  SUM(CASE WHEN o.IsRefund=1 THEN 0 ELSE o.GMV END) AS gmv_net,
  SUM(CASE WHEN o.IsRefund=1 THEN 0 ELSE o.MarketplaceRevenue END) AS marketplace_revenue_net,
  (SUM(CASE WHEN o.IsRefund=1 THEN 0 ELSE o.MarketplaceRevenue END) / NULLIF(SUM(CASE WHEN o.IsRefund=1 THEN 0 ELSE o.GMV END),0)) AS take_rate
FROM fact_orders o
GROUP BY 1
ORDER BY 1;
