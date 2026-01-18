"""
Ecommerce Funnel Optimization — Analysis Runner

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

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "ecommerce_events.csv")

def main():
    df = pd.read_csv(DATA_PATH)
    os.makedirs("outputs", exist_ok=True)

    # Basic KPI table (customize as needed)
    kpis = {
        "viewed": int((df['event_name']=='viewed').sum()),
        "added_to_cart": int((df['event_name']=='add_to_cart').sum()),
        "checkout_started": int((df['event_name']=='checkout_started').sum()),
        "purchased": int((df['event_name']=='purchased').sum()),
        "view_to_purchase_pct": round(((df['event_name']=='purchased').sum() / max((df['event_name']=='viewed').sum(),1))*100, 2)
    }
    kpi_df = pd.DataFrame(list(kpis.items()), columns=["metric", "value"])
    kpi_df.to_csv(os.path.join("outputs","kpis.csv"), index=False)

    # Simple chart (count by a dimension if available)
    dim = "device_type"
    if dim in df.columns:
        s = df[dim].value_counts().head(10)
        plt.figure()
        s.plot(kind="bar")
        plt.title(f"Top device_type")
        plt.tight_layout()
        os.makedirs(os.path.join("outputs","charts"), exist_ok=True)
        plt.savefig(os.path.join("outputs","charts","top_device_type.png"))
        plt.close()

if __name__ == "__main__":
    main()
