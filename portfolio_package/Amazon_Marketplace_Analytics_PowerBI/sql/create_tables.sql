-- Amazon Marketplace Analytics (PostgreSQL style)
-- Load order:
-- 1) dim_product 2) dim_seller 3) dim_customer 4) dim_calendar 5) fact_orders

CREATE TABLE dim_product (
  ProductID INT PRIMARY KEY,
  ProductName TEXT NOT NULL,
  Category TEXT NOT NULL,
  Subcategory TEXT NOT NULL,
  UnitCost NUMERIC(10,2) NOT NULL,
  UnitPrice NUMERIC(10,2) NOT NULL
);

CREATE TABLE dim_seller (
  SellerID INT PRIMARY KEY,
  SellerName TEXT NOT NULL,
  SellerTier TEXT NOT NULL,
  Country TEXT NOT NULL,
  CommissionRate NUMERIC(5,4) NOT NULL
);

CREATE TABLE dim_customer (
  CustomerID INT PRIMARY KEY,
  CustomerSegment TEXT NOT NULL,
  Region TEXT NOT NULL,
  City TEXT NOT NULL
);

CREATE TABLE dim_calendar (
  Date DATE PRIMARY KEY,
  Year INT NOT NULL,
  Month INT NOT NULL,
  MonthName TEXT NOT NULL,
  Quarter TEXT NOT NULL,
  YearMonth TEXT NOT NULL,
  WeekdayName TEXT NOT NULL
);

CREATE TABLE fact_orders (
  OrderID BIGINT PRIMARY KEY,
  OrderDate DATE NOT NULL REFERENCES dim_calendar(Date),
  ProductID INT NOT NULL REFERENCES dim_product(ProductID),
  SellerID INT NOT NULL REFERENCES dim_seller(SellerID),
  CustomerID INT NOT NULL REFERENCES dim_customer(CustomerID),
  Quantity INT NOT NULL,
  UnitPrice NUMERIC(10,2) NOT NULL,
  DiscountPct NUMERIC(6,4) NOT NULL,
  ShippingFee NUMERIC(10,2) NOT NULL,
  Tax NUMERIC(10,2) NOT NULL,
  GrossAmount NUMERIC(12,2) NOT NULL,
  NetAmount NUMERIC(12,2) NOT NULL,
  SellerPayout NUMERIC(12,2) NOT NULL,
  MarketplaceRevenue NUMERIC(12,2) NOT NULL
);
