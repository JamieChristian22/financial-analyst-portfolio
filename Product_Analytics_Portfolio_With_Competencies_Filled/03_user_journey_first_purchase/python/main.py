"""
User Journey to First Purchase — Analysis Runner

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

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "first_purchase_journey.csv")

def main():
    df = pd.read_csv(DATA_PATH)
    os.makedirs("outputs", exist_ok=True)

    # Basic KPI table (customize as needed)
    kpis = {
        "purchasers": int(len(df)),
        "avg_sessions_before_purchase": round(float(df['sessions_before_purchase'].mean()),2) if 'sessions_before_purchase' in df.columns else None,
        "avg_first_purchase_revenue": round(float(df['first_purchase_revenue_usd'].mean()),2) if 'first_purchase_revenue_usd' in df.columns else None
    }
    kpi_df = pd.DataFrame(list(kpis.items()), columns=["metric", "value"])
    kpi_df.to_csv(os.path.join("outputs","kpis.csv"), index=False)

    # Simple chart (count by a dimension if available)
    dim = "first_medium"
    if dim in df.columns:
        s = df[dim].value_counts().head(10)
        plt.figure()
        s.plot(kind="bar")
        plt.title(f"Top first_medium")
        plt.tight_layout()
        os.makedirs(os.path.join("outputs","charts"), exist_ok=True)
        plt.savefig(os.path.join("outputs","charts","top_first_medium.png"))
        plt.close()

if __name__ == "__main__":
    main()
