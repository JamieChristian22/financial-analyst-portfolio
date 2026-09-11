from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data"/"fpa_budget_actual_enriched.csv",parse_dates=["Month"])
required={"Month","Department","Account","Budget","Actual","Variance","VariancePct"}
missing=required-set(df.columns)
if missing: raise ValueError(f"Missing required columns: {sorted(missing)}")
if df[["Month","Department","Account"]].duplicated().any(): raise ValueError("Duplicate grain detected")
if df[["Budget","Actual"]].isna().any().any(): raise ValueError("Null finance values detected")
df["Variance"]=df["Actual"]-df["Budget"]
df["VariancePct"]=df["Variance"].div(df["Budget"]).fillna(0)
df["MaterialVarianceFlag"]=df["VariancePct"].abs().ge(0.05)
df.to_csv(ROOT/"data"/"fpa_budget_actual_validated.csv",index=False)
print(f"Validated {len(df):,} rows")