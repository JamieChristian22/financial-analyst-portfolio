-- FP&A Executive Analytics (PostgreSQL style)

CREATE TABLE finance_fact (
  TxnDate DATE NOT NULL,
  MonthYear DATE NOT NULL,
  FiscalYear INT NOT NULL,
  Scenario TEXT NOT NULL, -- Actual / Budget / Forecast
  Region TEXT NOT NULL,
  ProductLine TEXT NOT NULL,
  Department TEXT NOT NULL,
  AccountCategory TEXT NOT NULL, -- Revenue / COGS / Opex
  Account TEXT NOT NULL,
  Amount NUMERIC(14,2) NOT NULL
);

CREATE INDEX idx_finance_fact_month ON finance_fact (MonthYear);
CREATE INDEX idx_finance_fact_scenario ON finance_fact (Scenario);
