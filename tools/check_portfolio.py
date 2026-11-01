"""Offline portfolio link and artifact checks. Standard library only.

Checks local README destinations and core project-folder inventory.
Does not claim external links, dashboards, production deployments, or business impacts are verified.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
REQUIRED = {
    "product-manager-portfolio": [
        "Ecommerce_Conversion_Optimization", "Feature_Adoption_Intelligence",
        "Marketplace_Seller_Performance", "Revenue_Pricing_Strategy",
        "SaaS_Retention_Churn_Reduction", "User_Journey_First_Purchase",
    ],
    "product-owner-portfolio": [
        "01_Marketplace_Seller_Performance_Optimization",
        "02_Ecommerce_Product_Funnel_Retention",
        "03_Retail_Executive_KPI_Store_Operations",
        "04_Product_Performance_Pricing_Sales_Intelligence",
        "05_Experimentation_AB_Test_Feature_Impact",
    ],
    "marketing-analytics-portfolio": [
        "01_Amazon_Marketplace_Analytics_Dashboard",
        "02_Conversion_Funnel_Analytics",
        "03_User_Journey_First_Purchase_Analysis",
        "04_Marketing_ROI_And_Budget_Optimization",
        "05_AB_Testing_And_Feature_Impact_Analysis",
        "06_Ecommerce_Conversion_Funnel_Analysis",
    ],
    "financial-analyst-portfolio": [
        "01_FPA_Executive_Dashboard", "02_Amazon_Marketplace_Analytics",
        "03_Profitability_and_COGS_Analysis", "04_Executive_Financial_Performance",
    ],
    "multi-cloud-architect-portfolio": [
        "case-study", "infrastructure-as-code", "operations",
        "security", "tests-and-checklists", "VALIDATION_AND_LIMITATIONS.md",
    ],
}
errors = []
if not README.is_file():
    raise SystemExit("FAIL: README.md is missing")
md = README.read_text(encoding="utf-8")
for name in REQUIRED.get(ROOT.name, []):
    if not (ROOT / name).exists():
        errors.append("Required artifact missing: " + name)
if not any(word in md.lower() for word in ("simulat", "synthetic", "fictional", "portfolio scenario")):
    errors.append("README does not clearly identify portfolio simulations")

local_count = 0
for raw in re.findall(r"\]\(([^)\n]+)\)", md):
    target = raw.strip().strip("<>").split("#", 1)[0].split("?", 1)[0]
    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
        continue
    if "://" in target:
        continue
    relative = unquote(target)
    if relative.startswith("/"):
        relative = relative.lstrip("/")
    resolved = (ROOT / relative).resolve()
    if not resolved.is_relative_to(ROOT):
        errors.append("Link escapes repository: " + target)
        continue
    local_count += 1
    if not resolved.exists():
        errors.append("README link has no matching file or directory: " + target)

if local_count < 5:
    errors.append("Expected at least five linked local project artifacts")
print("Root README local links inspected:", local_count)
print("Required portfolio entries inspected:", len(REQUIRED.get(ROOT.name, [])))
for e in errors:
    print("FAIL:", e)
if errors:
    raise SystemExit(1)
print("PASS: local README targets, core project inventory and simulation disclosure")
print("LIMIT: external links, dashboards, live infrastructure, and business outcomes are not verified")
