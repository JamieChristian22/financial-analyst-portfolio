# 🛒 Amazon Marketplace Analytics Dashboard

![Excel](https://img.shields.io/badge/Tool-Excel-217346?style=for-the-badge&logo=microsoft-excel)
![SQL](https://img.shields.io/badge/Tool-SQL-4479A1?style=for-the-badge&logo=mysql)
![Python](https://img.shields.io/badge/Tool-Python-3776AB?style=for-the-badge&logo=python)
![Power BI](https://img.shields.io/badge/Tool-Power%20BI-F2C811?style=for-the-badge&logo=powerbi)

A **marketplace analytics project** that evaluates **Amazon seller performance, unit economics, and category trends** using SQL, Excel, Python, and BI dashboards.

This project simulates the type of analysis performed by **e-commerce analysts, marketplace analysts, and product analytics teams** to understand seller performance and marketplace profitability.

---

# 🎯 Project Objective

Online marketplaces generate large volumes of transaction data.  
This project demonstrates how analysts can convert that data into **business insights for marketplace strategy**.

Key objectives:

- Analyze **Gross Merchandise Value (GMV)**
- Evaluate **take rate and marketplace revenue**
- Calculate **contribution margin**
- Analyze **seller tier performance**
- Identify **category-level growth opportunities**

The goal is to provide insights that help **marketplace operators optimize seller performance and revenue growth**.

---

# 🧠 Business Questions Answered

This analysis answers key marketplace questions such as:

- Which seller tiers generate the most GMV?
- What categories drive the highest marketplace revenue?
- How does the marketplace **take rate impact profitability**?
- Which sellers contribute the highest margins?
- What trends indicate **growth opportunities or risk areas**?

---

# 📊 Marketplace Metrics Analyzed

Key metrics included in this analysis:

- Gross Merchandise Value (GMV)
- Marketplace Take Rate
- Marketplace Revenue
- Contribution Margin
- Seller Tier Performance
- Category-Level Sales
- Average Order Value
- Revenue Trends Over Time

---

# 🛠 Tools & Technologies

| Tool | Purpose |
|-----|------|
| Excel | Marketplace financial modeling and scenario analysis |
| SQL | Data aggregation and KPI queries |
| Python (Pandas / Matplotlib) | Data cleaning and visualization |
| Power BI / Tableau | Interactive analytics dashboards |
| CSV datasets | Marketplace transaction data |

---

# 📁 Repository Structure

```
Amazon_Marketplace_Analytics_Project
│
├── data
│   ├── marketplace_transactions.csv
│   └── cleaned_marketplace_data.csv
│
├── excel
│   └── marketplace_financial_model.xlsx
│
├── sql
│   ├── schema.sql
│   └── marketplace_kpis.sql
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
│   ├── dashboard_overview.png
│   ├── seller_performance.png
│   └── category_analysis.png
│
└── RESULTS_INSIGHTS.md
```

---

# 📈 Example Analysis

Example marketplace insights that could be generated:

- Top-tier sellers produce the majority of GMV
- Certain product categories drive significantly higher margins
- Mid-tier sellers contribute steady revenue growth
- Low-tier sellers show inconsistent sales patterns
- Category concentration indicates possible expansion opportunities

Full results available in:

`RESULTS_INSIGHTS.md`

---

# 🚀 How to Run the Project

### 1️⃣ Explore the Excel Marketplace Model

Navigate to:

```
/excel/marketplace_financial_model.xlsx
```

Use the **scenario toggles** to analyze:

- Seller growth
- Marketplace take rate changes
- Revenue projections

---

### 2️⃣ Run SQL Analysis

Run queries in `/sql` to calculate marketplace KPIs.

Example query:

```sql
SELECT seller_tier,
SUM(gmv) AS total_gmv,
AVG(take_rate) AS avg_take_rate,
SUM(revenue) AS marketplace_revenue
FROM marketplace_sales
GROUP BY seller_tier;
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

Python scripts will generate charts stored in:

```
/outputs
```

---

### 4️⃣ Explore the BI Dashboards

Load the dataset into:

- Power BI
- Tableau

These dashboards provide interactive views of:

- Seller performance
- Marketplace revenue
- Category trends
- Unit economics

---

# 📊 Dashboard Sections

Typical dashboard views include:

### Marketplace Overview
- Total GMV
- Marketplace revenue
- Average take rate

### Seller Performance
- GMV by seller tier
- Revenue contribution by seller
- Seller growth trends

### Category Analysis
- Top performing categories
- Category-level GMV distribution
- Margin contribution by category

---

# 💼 Portfolio Relevance

This project demonstrates skills relevant to:

- Marketplace Analyst
- E-commerce Analyst
- Product Analyst
- Data Analyst
- Business Intelligence Analyst

Key competencies:

- Marketplace unit economics
- Revenue analytics
- KPI development
- SQL data modeling
- Data visualization
- Business performance analysis

---

# 👤 Author

**Jamie Christian**

Data Analytics | Business Intelligence | Marketplace Analytics

LinkedIn  
https://www.linkedin.com/in/jamiechristian2

GitHub  
https://github.com/JamieChristian22

---

⭐ If you found this project helpful, feel free to explore the rest of my analytics portfolio projects.
