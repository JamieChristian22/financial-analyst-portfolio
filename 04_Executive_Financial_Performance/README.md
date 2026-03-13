# 📊 Executive Financial Performance Dashboard

![Excel](https://img.shields.io/badge/Tool-Excel-217346?style=for-the-badge&logo=microsoft-excel)
![SQL](https://img.shields.io/badge/Tool-SQL-4479A1?style=for-the-badge&logo=mysql)
![Python](https://img.shields.io/badge/Tool-Python-3776AB?style=for-the-badge&logo=python)
![Tableau](https://img.shields.io/badge/Tool-Tableau-E97627?style=for-the-badge&logo=tableau)

An **executive financial analytics project** designed to monitor key financial performance indicators such as **Revenue, Expenses, Net Income, Profit Margin, and Return on Assets (ROA)** using Excel, SQL, Python, and BI dashboards.

This project demonstrates how financial analysts and business intelligence teams create **executive KPI scorecards and performance dashboards** to help leadership evaluate business performance and make strategic decisions.

---

# 🎯 Project Objective

Executives rely on financial dashboards to quickly understand the health of the business.

This project demonstrates how to:

- Track **revenue and expense performance**
- Analyze **net income trends**
- Monitor **profit margins**
- Evaluate **return on assets (ROA)**
- Provide **executive-level KPI dashboards**

The goal is to transform financial data into **clear performance insights for leadership teams**.

---

# 🧠 Business Questions Answered

This analysis helps answer questions such as:

- Is company revenue growing or declining?
- How are operating expenses trending over time?
- Is profitability improving or decreasing?
- Which areas of the business drive the most financial performance?
- Are company assets being used efficiently?

---

# 📊 Key Financial Metrics

The executive dashboard tracks the following metrics:

- Total Revenue
- Total Expenses
- Net Income
- Profit Margin
- Return on Assets (ROA)
- Revenue Growth Rate
- Expense Trends
- Profitability Trends

---

# 🛠 Tools & Technologies

| Tool | Purpose |
|-----|------|
| Excel | Financial modeling and scenario analysis |
| SQL | Data aggregation and KPI calculations |
| Python (Pandas / Matplotlib) | Data cleaning and financial visualization |
| Power BI / Tableau | Executive dashboards and performance reporting |
| CSV datasets | Source financial data |

---

# 📁 Repository Structure

```
Executive_Financial_Performance_Project
│
├── data
│   ├── raw_financial_data.csv
│   └── cleaned_financial_data.csv
│
├── excel
│   └── executive_financial_model.xlsx
│
├── sql
│   ├── schema.sql
│   └── financial_kpis.sql
│
├── python
│   ├── 01_data_cleaning.py
│   └── 02_analysis_charts.py
│
├── outputs
│   └── charts_generated_by_python
│
├── dashboards
│   ├── powerbi_dashboard.pbix
│   └── tableau_dashboard.twbx
│
├── images
│   ├── executive_overview.png
│   ├── revenue_trends.png
│   └── profitability_analysis.png
│
└── RESULTS_INSIGHTS.md
```

---

# 📈 Example Financial Insights

Example insights that could be generated:

- Revenue growth increased significantly during certain quarters
- Expense increases impacted net income performance
- Profit margins improved through cost control initiatives
- Asset utilization efficiency changed over time
- Profitability trends indicate potential areas for operational improvement

Full analysis results available in:

`RESULTS_INSIGHTS.md`

---

# 🚀 How to Run the Project

### 1️⃣ Open the Excel Financial Model

Navigate to:

```
/excel/executive_financial_model.xlsx
```

Use the **scenario dropdown** to explore:

- revenue projections
- expense scenarios
- profitability simulations

---

### 2️⃣ Run SQL Analysis

Run SQL scripts in `/sql` to generate financial KPI tables.

Example query:

```sql
SELECT
SUM(revenue) AS total_revenue,
SUM(expenses) AS total_expenses,
SUM(revenue - expenses) AS net_income,
(SUM(revenue - expenses) / SUM(revenue)) * 100 AS profit_margin
FROM financial_data;
```

Compatible with:

- PostgreSQL
- DuckDB
- SQLite
- MySQL

---

### 3️⃣ Run Python Analysis

Install dependencies:

```bash
pip install pandas matplotlib
```

Run scripts:

```bash
python python/01_data_cleaning.py
python python/02_analysis_charts.py
```

Python scripts generate charts stored in:

```
/outputs
```

---

### 4️⃣ Explore the BI Dashboards

Load the dataset into:

- Power BI
- Tableau

Interactive dashboards allow users to explore:

- financial performance trends
- revenue vs expense breakdown
- profitability analysis
- executive KPI scorecards

---

# 📊 Dashboard Sections

Typical executive dashboard views include:

### Executive KPI Overview
- Total revenue
- Total expenses
- Net income
- Profit margin
- ROA

### Revenue Trends
- Monthly revenue performance
- Growth rate analysis
- Revenue breakdown by business unit

### Expense Analysis
- Expense categories
- Operating cost trends
- Cost management insights

### Profitability Analysis
- Net income trends
- Margin analysis
- Performance comparisons over time

---

# 💼 Portfolio Relevance

This project demonstrates skills relevant to:

- Financial Analyst
- FP&A Analyst
- Business Analyst
- Data Analyst
- Business Intelligence Analyst

Key competencies showcased:

- Financial performance analysis
- KPI development
- SQL data modeling
- Data visualization
- Financial dashboard development
- Business performance analytics

---

# 👤 Author

**Jamie Christian**

Financial Analytics | Business Intelligence | Data Analytics

LinkedIn  
https://www.linkedin.com/in/jamiechristian2  

GitHub  
https://github.com/JamieChristian22  

---

⭐ If you found this project helpful, feel free to explore the rest of my analytics portfolio projects.
