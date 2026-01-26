# Discovery Workshop Agenda (60–90 min)

## 1) Introductions + Outcomes (5 min)
- Confirm attendees + roles (Product, Engineering, Security, Finance/FinOps, Ops)
- Workshop outcomes:
  - align business goals + constraints
  - identify current-state pain points
  - capture success metrics and guardrails
  - agree on next steps + owners

## 2) Business Context (10–15 min)
- What is the product / workload and who are the users?
- Critical KPIs (revenue, latency, availability, data freshness, cost caps)
- Growth expectations (users, traffic, data volume) over 6/12/24 months
- Hard constraints: deadlines, budget, compliance, data residency

## 3) Current-State Architecture (15–20 min)
- Walkthrough: network, compute, storage, data flows
- Environments: dev/test/stage/prod, account strategy, deployment model
- CI/CD + release process
- Observability: logs/metrics/traces, alerting, SLOs/SLIs

## 4) Security + Compliance (10–15 min)
- Identity: IAM, SSO, access reviews, break-glass
- Data: classification, encryption, key management, retention
- Audit needs: CloudTrail, Config, SIEM, evidence collection
- Regulatory: HIPAA/PCI/SOC2/GDPR (as applicable)

## 5) Reliability + DR (10–15 min)
- Availability targets (e.g., 99.9%, 99.99%)
- RTO/RPO requirements
- Failure modes experienced in last 90 days
- Backup + restore testing cadence

## 6) Cost + FinOps (10–15 min)
- Monthly spend trend + biggest drivers
- Cost allocation: tags, accounts, chargeback/showback
- Reserved/Savings Plans usage
- Top optimization opportunities suspected

## 7) Next Steps + Owners (5–10 min)
- Confirm artifacts to produce (HLD/LLD, roadmap, LOE, security gaps)
- Assign owners for data collection
- Schedule next checkpoint (architecture review + findings readout)

## Deliverables Produced From This Workshop
- Current-state inventory (systems/services/data stores)
- Stakeholder map + RACI draft
- Risk register + initial RAID log
- Findings backlog (prioritized) + roadmap
