-- Monthly sales and profit
SELECT
  DATE_TRUNC('month', "Dt Transaction")::date AS month,
  SUM(Sales) AS sales,
  SUM(Profit) AS profit,
  CASE WHEN SUM(Sales)=0 THEN 0 ELSE SUM(Profit)/SUM(Sales) END AS margin
FROM brew_sales
GROUP BY 1
ORDER BY 1;

-- Discount impact by brand
SELECT
  Brand,
  SUM(Sales) AS sales,
  AVG(Discount) AS avg_discount_pct,
  SUM(Profit) AS profit,
  CASE WHEN SUM(Sales)=0 THEN 0 ELSE SUM(Profit)/SUM(Sales) END AS margin
FROM brew_sales
GROUP BY 1
ORDER BY profit DESC;
