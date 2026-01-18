"""
StreamFlow SaaS Product Analytics — Analysis Runner

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

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "streamflow_events.csv")

def main():
    df = pd.read_csv(DATA_PATH)
    os.makedirs("outputs", exist_ok=True)

    # Basic KPI table (customize as needed)
    kpis = {
        "distinct_users": int(df['user_id'].nunique()) if 'user_id' in df.columns else None,
        "events": int(len(df)),
        "revenue_usd_sum": float(df['revenue_usd'].sum()) if 'revenue_usd' in df.columns else None
    }
    kpi_df = pd.DataFrame(list(kpis.items()), columns=["metric", "value"])
    kpi_df.to_csv(os.path.join("outputs","kpis.csv"), index=False)

    # Simple chart (count by a dimension if available)
    dim = "event_name"
    if dim in df.columns:
        s = df[dim].value_counts().head(10)
        plt.figure()
        s.plot(kind="bar")
        plt.title(f"Top event_name")
        plt.tight_layout()
        os.makedirs(os.path.join("outputs","charts"), exist_ok=True)
        plt.savefig(os.path.join("outputs","charts","top_event_name.png"))
        plt.close()

if __name__ == "__main__":
    main()
