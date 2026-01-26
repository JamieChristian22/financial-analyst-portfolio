# Low-Level Design (LLD) Template

## 1. Component Details
For each component include:
- Purpose
- Inputs/outputs
- Scaling behavior
- Failure modes + retries/DLQs
- Monitoring + alerting
- Security controls

## 2. Networking
- VPCs, subnets, route tables
- Security groups/NACLs
- VPC endpoints
- DNS and certificates

## 3. IAM (Least Privilege)
- Roles and policies per service
- Cross-account access patterns
- Break-glass access design

## 4. Data Stores
- Schema/partitioning (if applicable)
- Retention and lifecycle
- Backup strategy

## 5. CI/CD
- Pipeline stages
- Testing gates
- Deployment strategy (blue/green/canary)
- Rollback plan

## 6. Observability
- Logs, metrics, traces
- Key dashboards
- Alert thresholds aligned to SLOs

## 7. IaC Notes
- Terraform modules structure
- State management
- Drift detection
