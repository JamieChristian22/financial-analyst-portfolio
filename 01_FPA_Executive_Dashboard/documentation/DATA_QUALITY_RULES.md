# Data Quality Rules

## Grain
One row per Month × Department × Account.

## Required Fields
Month, Department, Account, Budget, Actual.

## Validation Rules
- No duplicate grain combinations.
- No null Month/Department/Account.
- Budget and Actual must be numeric.
- Variance = Actual - Budget.
- Variance % = Variance / Budget where Budget ≠ 0.
- All 12 fiscal months should exist.
- Only approved departments/accounts should appear.
- Revenue, COGS, and required OpEx categories must be present.
- Dashboard totals must reconcile to the Excel P&L.

## Exception Handling
Any failed validation should be resolved before publishing management reporting.
