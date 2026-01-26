# Tagging Standard (Cost Allocation)

## Required Tags (Recommended)
| Tag Key | Example | Purpose |
|---|---|---|
| `CostCenter` | `CC-4102` | Finance allocation |
| `Application` | `orders-api` | Workload grouping |
| `Environment` | `prod` | dev/test/stage/prod |
| `Owner` | `platform-team` | Accountability |
| `DataClass` | `confidential` | Governance |
| `Project` | `cloud-modernization` | Initiative tracking |

## Policy Guidance
- Enforce tagging via IaC modules + CI checks
- Use AWS Tag Policies (Organizations) for allowed values where possible
- Report tagging coverage monthly: **% of spend with required tags**

## Common Reports
- Spend by CostCenter (monthly)
- Top 10 untagged resources
- Spend by Application + Environment
