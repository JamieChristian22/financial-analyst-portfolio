"""
Conversion, Retention & Revenue KPI Overview — Analysis Runner

Run:
  pip install -r requirements.txt
  python main.py

Outputs (created):
  outputs/
    - kpis.csv
    - charts/*.png
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "kpi_users.csv")

def main():
    df = pd.read_csv(DATA_PATH)
    os.makedirs("outputs", exist_ok=True)

    # Basic KPI table (customize as needed)
    kpis = {
        "users": int(len(df)),
        "paid_users": int(df['converted_to_paid'].sum()) if 'converted_to_paid' in df.columns else None,
        "conversion_rate": round(float(df['converted_to_paid'].mean()),3) if 'converted_to_paid' in df.columns else None,
        "retention_30d": round(float(df['retained_30d'].mean()),3) if 'retained_30d' in df.columns else None,
        "total_revenue_usd": round(float(df['total_revenue_usd'].sum()),2) if 'total_revenue_usd' in df.columns else None
    }
    kpi_df = pd.DataFrame(list(kpis.items()), columns=["metric", "value"])
    kpi_df.to_csv(os.path.join("outputs","kpis.csv"), index=False)

    # Simple chart (count by a dimension if available)
    dim = "acquisition_channel"
    if dim in df.columns:
        s = df[dim].value_counts().head(10)
        plt.figure()
        s.plot(kind="bar")
        plt.title(f"Top acquisition_channel")
        plt.tight_layout()
        os.makedirs(os.path.join("outputs","charts"), exist_ok=True)
        plt.savefig(os.path.join("outputs","charts","top_acquisition_channel.png"))
        plt.close()

if __name__ == "__main__":
    main()
