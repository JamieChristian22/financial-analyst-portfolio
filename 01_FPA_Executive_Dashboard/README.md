# 📊 FP&A Executive Financial Analytics Dashboard

![Excel](https://img.shields.io/badge/Tool-Excel-217346?style=for-the-badge&logo=microsoft-excel)
![SQL](https://img.shields.io/badge/Tool-SQL-4479A1?style=for-the-badge&logo=mysql)
![Python](https://img.shields.io/badge/Tool-Python-3776AB?style=for-the-badge&logo=python)
![Power BI](https://img.shields.io/badge/Tool-Power%20BI-F2C811?style=for-the-badge&logo=powerbi)

A **Financial Planning & Analysis (FP&A) analytics project** that tracks **Budget vs Actual performance**, identifies **variance drivers**, and visualizes **department financial trends** using Excel, SQL, Python, and BI dashboards.

This project simulates the type of reporting used by **finance teams, CFO offices, and financial analysts** to monitor operational spending and support **data-driven financial decisions**.

---

# 🎯 Project Objective

Finance teams must constantly monitor whether the organization is **spending according to plan**.

This project demonstrates how to:

- Track **Budget vs Actual financial performance**
- Identify **positive and negative variances**
- Monitor **department expense trends**
- Analyze **month-over-month financial performance**
- Provide **executive-ready financial dashboards**

The goal is to transform raw financial data into **clear insights leadership can act on**.

---

# 🧠 Business Questions Answered

This analysis answers key financial questions such as:

- Which departments are **over budget or under budget**?
- What are the **largest cost drivers across departments**?
- Are expenses **increasing or decreasing over time**?
- Which teams require **cost control or forecast adjustments**?
- What financial patterns can help improve **future planning and budgeting**?

---

# 🛠 Tools & Technologies

| Tool | Purpose |
|-----|------|
| Excel | Financial modeling, scenario analysis, forecasting |
| SQL | KPI calculations, data queries, joins |
| Python (Pandas / Matplotlib) | Data cleaning, transformation, financial charts |
| Power BI / Tableau | Executive dashboards & visual reporting |
| CSV datasets | Source financial data |

---

# 📁 Repository Structure

```
FPnA_Executive_Analytics_Project
│
├── data
│   ├── raw_financial_data.csv
│   └── cleaned_financial_data.csv
│
├── excel
│   └── FPnA_Model.xlsx
│
├── sql
│   ├── financial_schema.sql
│   └── kpi_queries.sql
│
├── python
│   ├── data_cleaning.py
│   └── financial_analysis.py
│
├── dashboards
│   ├── powerbi_dashboard.pbix
│   └── tableau_dashboard.twbx
│
├── images
│   ├── executive_dashboard.png
│   ├── department_variance.png
│   └── monthly_trends.png
│
└── RESULTS_INSIGHTS.md
```

---

# 📈 Key Financial Metrics

The dashboard tracks several core FP&A metrics:

- Total Budget
- Total Actual Spend
- Variance ($)
- Variance (%)
- Department Expense Breakdown
- Month-over-Month Financial Trends
- Forecast vs Actual Performance
- Top Overspending / Underspending Departments

---

# 📊 Dashboard Overview

## Executive Financial Overview

Displays the overall company performance against budget.

Example metrics shown:

- Total budget vs total spend
- Overall variance
- Department cost distribution
- Financial performance summary

---

## Department Variance Analysis

Identifies departments exceeding or underspending their budgets.

Helps finance teams:

- Pinpoint cost overruns
- Analyze spending patterns
- Identify cost-saving opportunities

---

## Monthly Expense Trend Analysis

Tracks how company spending changes over time.

Useful for:

- Forecasting future expenses
- Identifying seasonal spending patterns
- Monitoring operational efficiency

---

# 🔍 Example Financial Insights

Example insights from the analysis may include:

- Marketing exceeded budget due to increased advertising spend
- IT maintained spending below budget through infrastructure optimization
- Operations had the highest cost variance across departments
- HR expenses remained stable month-over-month

Full findings available in:

`RESULTS_INSIGHTS.md`

---

# 🚀 How to Run the Project

### 1️⃣ Open the Excel Model

Navigate to:

```
/excel/FPnA_Model.xlsx
```

Review:

- Budget vs Actual comparison
- Forecast assumptions
- Financial scenarios

---

### 2️⃣ Run SQL Queries

Example query:

```sql
SELECT department,
SUM(actual_expense) AS total_actual,
SUM(budget) AS total_budget,
SUM(actual_expense) - SUM(budget) AS variance
FROM financial_data
GROUP BY department;
```

---

### 3️⃣ Run Python Analysis

Install dependencies:

```bash
pip install pandas matplotlib
```

Run scripts:

```bash
python python/data_cleaning.py
python python/financial_analysis.py
```

These scripts generate financial charts and insights.

---

### 4️⃣ Explore the Dashboards

Load the dataset into:

- Power BI
- Tableau

Interactive dashboards allow stakeholders to explore financial performance dynamically.

---

# 💼 Portfolio Relevance

This project demonstrates practical skills used by:

- Financial Analysts
- FP&A Analysts
- Business Analysts
- BI Analysts
- Data Analysts

Key competencies showcased:

- Financial Modeling
- Variance Analysis
- KPI Development
- Financial Data Visualization
- Budget Monitoring
- Executive Reporting

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
