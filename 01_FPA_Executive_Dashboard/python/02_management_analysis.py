from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"outputs"; OUT.mkdir(exist_ok=True)
df=pd.read_csv(ROOT/"data"/"fpa_budget_actual_enriched.csv",parse_dates=["Month"])
opex=["Payroll","Software","Travel","Facilities","Other OpEx"]
dept=df[df["Account"].isin(opex)].groupby("Department",as_index=False).agg(OpEx_Budget=("Budget","sum"),OpEx_Actual=("Actual","sum"))
dept["Variance"]=dept["OpEx_Actual"]-dept["OpEx_Budget"]; dept["VariancePct"]=dept["Variance"]/dept["OpEx_Budget"]
dept.to_csv(OUT/"department_variance_summary.csv",index=False)
monthly=df.pivot_table(index="Month",columns="Account",values="Actual",aggfunc="sum").reset_index()
monthly["GrossProfit"]=monthly["Revenue"]-monthly["COGS"]; monthly["TotalOpEx"]=monthly[opex].sum(axis=1); monthly["OperatingProfit"]=monthly["GrossProfit"]-monthly["TotalOpEx"]
monthly.to_csv(OUT/"monthly_pnl_summary.csv",index=False)