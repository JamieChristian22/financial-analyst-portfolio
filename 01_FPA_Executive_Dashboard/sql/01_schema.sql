CREATE TABLE dim_department (department_id INTEGER PRIMARY KEY, department_name VARCHAR(50) UNIQUE NOT NULL);
CREATE TABLE dim_account (account_id INTEGER PRIMARY KEY, account_name VARCHAR(50) UNIQUE NOT NULL, account_group VARCHAR(30) NOT NULL);
CREATE TABLE fact_financials (month DATE NOT NULL, department_id INTEGER NOT NULL REFERENCES dim_department(department_id), account_id INTEGER NOT NULL REFERENCES dim_account(account_id), budget DECIMAL(14,2) NOT NULL, actual DECIMAL(14,2) NOT NULL, PRIMARY KEY (month, department_id, account_id));
CREATE INDEX idx_financials_month ON fact_financials(month);
CREATE INDEX idx_financials_department ON fact_financials(department_id);
CREATE INDEX idx_financials_account ON fact_financials(account_id);