DROP TABLE IF EXISTS financial_performance;

CREATE TABLE financial_performance (
    month DATE NOT NULL,
    year INTEGER NOT NULL,
    quarter VARCHAR(2) NOT NULL,
    business_unit VARCHAR(30) NOT NULL,
    region VARCHAR(20) NOT NULL,
    actual_revenue NUMERIC(18,2) NOT NULL,
    budget_revenue NUMERIC(18,2) NOT NULL,
    forecast_revenue NUMERIC(18,2) NOT NULL,
    actual_cogs NUMERIC(18,2) NOT NULL,
    budget_cogs NUMERIC(18,2) NOT NULL,
    forecast_cogs NUMERIC(18,2) NOT NULL,
    actual_opex NUMERIC(18,2) NOT NULL,
    budget_opex NUMERIC(18,2) NOT NULL,
    forecast_opex NUMERIC(18,2) NOT NULL,
    assets NUMERIC(18,2) NOT NULL,
    operating_cash_flow NUMERIC(18,2) NOT NULL,
    headcount INTEGER NOT NULL
);

CREATE INDEX idx_financial_month ON financial_performance(month);
CREATE INDEX idx_financial_bu ON financial_performance(business_unit);
CREATE INDEX idx_financial_region ON financial_performance(region);
