-- FP&A Budget vs Actual
CREATE TABLE fpa_budget_actual (
  Month DATE,
  Department VARCHAR(30),
  Account VARCHAR(30),
  Budget DECIMAL(14,2),
  Actual DECIMAL(14,2)
);
