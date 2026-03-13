# 💰 Profitability & COGS Analysis Dashboard

![Excel](https://img.shields.io/badge/Tool-Excel-217346?style=for-the-badge&logo=microsoft-excel)
![SQL](https://img.shields.io/badge/Tool-SQL-4479A1?style=for-the-badge&logo=mysql)
![Python](https://img.shields.io/badge/Tool-Python-3776AB?style=for-the-badge&logo=python)
![Tableau](https://img.shields.io/badge/Tool-Tableau-E97627?style=for-the-badge&logo=tableau)

A **financial analytics project** focused on evaluating **gross margin performance, cost of goods sold (COGS), and discount impact across product lines and sales channels** using Excel, SQL, Python, and BI dashboards.

This project demonstrates how financial and data analysts analyze profitability drivers to support **pricing strategy, cost optimization, and revenue growth decisions**.

---

# 🎯 Project Objective

Businesses must understand how costs, pricing, and discounts affect overall profitability.

This project demonstrates how to:

- Analyze **gross margin performance**
- Break down **COGS by product line**
- Measure **discount impact on profitability**
- Evaluate **channel-level profitability**
- Identify **high-margin and low-margin products**

The goal is to transform raw financial and sales data into **clear profitability insights for decision-makers**.

---

# 🧠 Business Questions Answered

This analysis answers key business questions such as:

- Which product lines generate the highest **gross margins**?
- How does **COGS vary across product categories**?
- What impact do **discounts have on overall profitability**?
- Which sales channels produce the highest margins?
- Where can businesses improve pricing or reduce costs?

---

# 📊 Key Financial Metrics

The dashboard tracks several important profitability metrics:

- Revenue
- Cost of Goods Sold (COGS)
- Gross Profit
- Gross Margin (%)
- Discount Impact
- Profit by Product Line
- Profit by Sales Channel
- Margin Trends Over Time

---

# 🛠 Tools & Technologies

| Tool | Purpose |
|-----|------|
| Excel | Financial modeling and scenario analysis |
| SQL | Data aggregation and KPI calculations |
| Python (Pandas / Matplotlib) | Data cleaning and visualization |
| Power BI / Tableau | Interactive profitability dashboards |
| CSV datasets | Source transaction and cost data |

---

# 📁 Repository Structure

```
Profitability_COGS_Analysis_Project
│
├── data
│   ├── raw_sales_data.csv
│   └── cleaned_sales_data.csv
│
├── excel
│   └── profitability_model.xlsx
│
├── sql
│   ├── schema.sql
│   └── profitability_kpis.sql
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
│   ├── profitability_overview.png
│   ├── cogs_breakdown.png
│   └── margin_trends.png
│
└── RESULTS_INSIGHTS.md
```

---

# 📈 Example Profitability Insights

Example insights that could be generated from this analysis:

- Certain product lines produce significantly higher gross margins
- Discount-heavy products reduce overall profitability
- Some sales channels generate higher margins than others
- COGS fluctuations indicate potential supply chain cost pressures
- Margin trends highlight opportunities for pricing optimization

Full findings available in:

`RESULTS_INSIGHTS.md`

---

# 🚀 How to Run the Project

### 1️⃣ Open the Excel Financial Model

Navigate to:

```
/excel/profitability_model.xlsx
```

Use the **scenario dropdown** to analyze:

- pricing changes
- cost changes
- discount impact

---

### 2️⃣ Run SQL Analysis

Run SQL scripts in `/sql` to generate profitability KPIs.

Example query:

```sql
SELECT product_line,
SUM(revenue) AS total_revenue,
SUM(cogs) AS total_cogs,
SUM(revenue - cogs) AS gross_profit,
(SUM(revenue - cogs) / SUM(revenue)) * 100 AS gross_margin_percent
FROM sales_data
GROUP BY product_line;
```

Compatible with:

- PostgreSQL
- DuckDB
- SQLite
- MySQL

---

### 3️⃣ Run Python Scripts

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

Interactive dashboards allow users to analyze:

- product profitability
- margin trends
- discount impact
- channel performance

---

# 📊 Dashboard Sections

Typical dashboard views include:

### Profitability Overview
- Total revenue
- Total COGS
- Gross profit
- Overall gross margin

### Product Margin Analysis
- Gross margin by product line
- Top profitable products
- Low margin product identification

### Channel Profitability
- Profit by sales channel
- Revenue distribution across channels
- Margin comparison between channels

### Margin Trends
- Monthly margin trends
- Impact of discount campaigns
- Cost fluctuations over time

---

# 💼 Portfolio Relevance

This project demonstrates skills relevant to:

- Financial Analyst
- FP&A Analyst
- Business Analyst
- Data Analyst
- Business Intelligence Analyst

Key competencies showcased:

- Profitability analysis
- Cost analysis
- Financial KPI development
- SQL data modeling
- Data visualization
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
