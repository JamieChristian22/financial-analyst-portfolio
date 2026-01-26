# Architecture Diagram Standards (AWS Consulting)

## Principles
- One diagram per audience:
  - **Executive** (business outcomes + major systems)
  - **Architecture** (services + data flows)
  - **Network/Security** (subnets, routes, endpoints)
  - **Ops** (monitoring, alarms, runbooks)
- Keep diagrams readable at 100% zoom in a PDF.

## Naming & Versioning
- `diagrams/`
  - `HLD-Overview-v1.png`
  - `Network-Security-v1.png`
  - `DataFlow-v1.png`
- Update version on every major design change.

## Required Annotations
- Regions/AZs
- Trust boundaries (public/private)
- Data classification labels (PII/PHI/etc.)
- Critical controls (WAF, KMS, logging)

## Common Mistakes to Avoid
- Mixing LLD-level detail into executive diagrams
- Missing arrows / unclear direction
- Not labeling accounts/environments
