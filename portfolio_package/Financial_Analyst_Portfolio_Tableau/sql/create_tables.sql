-- Sales / profitability dataset
CREATE TABLE brew_sales (
  "Sr No" INT,
  "Dt Transaction" DATE,
  "Dt Product Launch" DATE,
  Country TEXT,
  State TEXT,
  City TEXT,
  Retailer TEXT,
  "Retailer Id" TEXT,
  "Sales Channel" TEXT,
  Brand TEXT,
  Category TEXT,
  Product TEXT,
  "Product Item Id" TEXT,
  "Order Qty" INT,
  "Mrp Unit Price" NUMERIC(10,2),
  "Cost Per Unit" NUMERIC(10,2),
  Discount NUMERIC(10,2),
  Sales NUMERIC(14,2),
  COGS NUMERIC(14,2),
  Profit NUMERIC(14,2)
);
