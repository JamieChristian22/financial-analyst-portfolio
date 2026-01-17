-- Monthly P&L
SELECT
  DATE_TRUNC('month', Date)::date AS month,
  SUM(Sales) AS sales,
  SUM(COGS) AS cogs,
  SUM(Profit) AS profit,
  CASE WHEN SUM(Sales)=0 THEN 0 ELSE SUM(Profit)/SUM(Sales) END AS profit_margin
FROM financial_data
GROUP BY 1
ORDER BY 1;

-- Segment contribution
SELECT Segment, SUM(Sales) AS sales, SUM(Profit) AS profit
FROM financial_data
GROUP BY Segment
ORDER BY sales DESC;

-- Discount band effectiveness
SELECT "Discount Band" AS discount_band, SUM(Sales) AS sales, SUM(Units Sold) AS units, SUM(Profit) AS profit
FROM financial_data
GROUP BY 1
ORDER BY 1;
