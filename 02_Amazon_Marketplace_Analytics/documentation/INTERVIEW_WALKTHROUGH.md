# Interview Walkthrough & Defense Guide

## 60-Second Project Pitch
I built a corporate-style marketplace analytics project to answer a finance question: is marketplace growth actually creating profitable value? I modeled 1,965 synthetic orders across 80 sellers and analyzed GMV, marketplace revenue, take rate, refunds, seller and category performance, contribution margin, promotion efficiency, fulfillment economics, working capital, and FY2026 scenarios. I used Excel for the operating and financial model, SQL for KPI reporting, Python for validation and analysis, and Power BI/DAX documentation for executive reporting. The model translates performance into actions such as protecting high-value sellers, addressing refund leakage, and allocating growth spend based on contribution economics rather than GMV alone.

## Questions You Should Be Able to Answer

### Why use GMV and marketplace revenue separately?
GMV measures merchandise value flowing through the platform. Marketplace revenue is the portion monetized by the platform. Separating them prevents confusing marketplace scale with company revenue.

### What is take rate?
Marketplace revenue divided by GMV. It measures monetization efficiency and can be affected by fee structure, seller/category mix, and commercial strategy.

### Why is contribution margin important?
GMV can grow while economics deteriorate. Contribution margin shows the value remaining after variable marketplace costs and is therefore a better measure of profitable growth.

### Why analyze refunds?
Refunds affect revenue quality, customer experience, support workload, and potentially seller economics. Elevated refunds can signal product, seller, fulfillment, or policy problems.

### How did you prioritize categories?
I combined monetization, contribution-margin quality, and refund behavior instead of ranking categories by sales volume alone.

### How would this work in a real company?
I would source data from the warehouse/ERP, establish governed dimensions, automate transformations, reconcile finance totals, publish a semantic BI model, and add controls around refreshes and material exceptions.

### What would you improve next?
Customer cohorts, seller churn, SKU return reasons, CAC/LTV, fulfillment SLAs, and automated data refreshes.

## Interview Warning
Do not present the synthetic results as Amazon's real financial performance. Describe them as a portfolio simulation inspired by marketplace business models.
