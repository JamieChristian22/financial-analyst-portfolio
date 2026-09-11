# Data Quality Rules
- One row per OrderID.
- No duplicate OrderID.
- Required seller/category/date fields cannot be null.
- GMV must be non-negative.
- RefundFlag must be 0 or 1.
- Marketplace Revenue should reconcile to GMV × Take Rate within rounding tolerance.
- Every seller/category must map to a dimension.
- Excel and BI KPIs must reconcile before publishing.