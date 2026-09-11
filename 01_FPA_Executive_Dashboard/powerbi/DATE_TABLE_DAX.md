# Power BI Date Table

```DAX
Date =
ADDCOLUMNS(
    CALENDAR(DATE(2025,1,1), DATE(2026,12,31)),
    "Year", YEAR([Date]),
    "Month Number", MONTH([Date]),
    "Month", FORMAT([Date], "MMM"),
    "Month Year", FORMAT([Date], "MMM YYYY"),
    "Quarter", "Q" & FORMAT([Date], "Q"),
    "Year Month Sort", YEAR([Date]) * 100 + MONTH([Date])
)
```

Create a one-to-many relationship:
`Date[Date]` → `Financials[Month]`

Sort `Date[Month Year]` by `Date[Year Month Sort]`.
