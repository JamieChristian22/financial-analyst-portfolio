-- Marketplace Analytics | Star-ish schema
CREATE TABLE dim_product (
  ProductID INT PRIMARY KEY,
  SKU VARCHAR(20),
  Category VARCHAR(50),
  ListPrice DECIMAL(10,2),
  UnitCost DECIMAL(10,2)
);

CREATE TABLE dim_seller (
  SellerID INT PRIMARY KEY,
  SellerCode VARCHAR(20),
  SellerTier VARCHAR(20),
  SellerRating DECIMAL(3,2),
  Region VARCHAR(30)
);

CREATE TABLE fact_orders (
  OrderID BIGINT PRIMARY KEY,
  OrderDate DATE,
  ProductID INT,
  SellerID INT,
  Device VARCHAR(20),
  Quantity INT,
  DiscountPct DECIMAL(4,2),
  GMV DECIMAL(12,2),
  MarketplaceRevenue DECIMAL(12,2),
  IsRefund INT,
  FOREIGN KEY(ProductID) REFERENCES dim_product(ProductID),
  FOREIGN KEY(SellerID) REFERENCES dim_seller(SellerID)
);
