CREATE TABLE profitability_transactions (
transaction_id BIGINT PRIMARY KEY, transaction_date DATE, product_line VARCHAR(60), channel VARCHAR(30), region VARCHAR(30),
units INTEGER, list_revenue DECIMAL(14,2), discount_pct DECIMAL(7,4), net_revenue DECIMAL(14,2),
material_cost DECIMAL(14,2), labor_cost DECIMAL(14,2), freight_cost DECIMAL(14,2), manufacturing_overhead DECIMAL(14,2),
cogs DECIMAL(14,2), gross_profit DECIMAL(14,2), gross_margin_pct DECIMAL(7,4));