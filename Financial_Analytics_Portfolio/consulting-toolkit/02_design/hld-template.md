# High-Level Design (HLD) Template

## 1. Executive Summary
- What we are building and why
- Business outcomes and measurable success criteria
- Key architectural choices and rationale

## 2. Requirements
### Functional
- (e.g., ingest events, serve API, run analytics, enable reporting)

### Non-Functional
- Availability target:
- Performance target:
- RTO/RPO:
- Security/compliance:
- Cost constraints:

## 3. Proposed Architecture (Overview)
- Diagram reference (include link/path)
- Major components and responsibilities
- Data flow narrative (end-to-end)

## 4. AWS Services
| Layer | Service | Purpose | Notes |
|---|---|---|---|
| Edge | CloudFront/WAF | Protection + caching | |
| API | API Gateway/Lambda | Serverless API | |
| Data | S3/Glue/Athena | Analytics | |

## 5. Security Model
- IAM strategy (SSO, roles, least privilege)
- Network segmentation and ingress/egress controls
- Encryption and key management
- Logging and monitoring strategy

## 6. Reliability + DR
- Multi-AZ strategy
- Backup/restore approach
- DR model (pilot light/warm standby/etc.)

## 7. Cost Model (High Level)
- Major cost drivers (compute, storage, data transfer, NAT)
- Cost allocation and tagging plan
- Savings plan assumptions

## 8. Delivery Plan
- Milestones (30/60/90 days)
- Key dependencies + risks

## 9. Open Questions
- List unresolved decisions
