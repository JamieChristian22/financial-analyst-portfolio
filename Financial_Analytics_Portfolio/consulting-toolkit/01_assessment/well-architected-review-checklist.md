# AWS Well-Architected Review Checklist (Client-Ready)

Use this checklist to run a structured review across the 6 pillars. Score each section:
- **Green**: meets intent; controls in place
- **Yellow**: partial; improvement needed
- **Red**: gap; high priority

## 1) Operational Excellence
- [ ] Workload has documented runbooks + SOPs
- [ ] Defined SLIs/SLOs and error budgets (or availability targets)
- [ ] CI/CD with automated tests and safe deployments (canary/blue-green where needed)
- [ ] Incident process exists (on-call, severity levels, postmortems)
- [ ] Operational metrics reviewed regularly (weekly/monthly)

## 2) Security
- [ ] Centralized identity (SSO) and least privilege IAM
- [ ] MFA enforced; break-glass accounts protected + monitored
- [ ] Encryption in-transit and at-rest across data stores
- [ ] Logging enabled: CloudTrail org trail, VPC Flow Logs where appropriate
- [ ] GuardDuty/Security Hub/Config enabled and monitored
- [ ] Secrets in managed store (Secrets Manager/SSM), not in code
- [ ] Security findings triaged within defined SLAs

## 3) Reliability
- [ ] Multi-AZ where required; clear blast radius strategy
- [ ] RTO/RPO documented; backups tested (restore drills)
- [ ] Resilience patterns: retries, backoff, circuit breakers, DLQs
- [ ] Dependencies identified; failure mode analysis performed
- [ ] DR plan exists (pilot light/warm standby/active-active) as needed

## 4) Performance Efficiency
- [ ] Workload uses managed services when feasible (reduce undifferentiated heavy lifting)
- [ ] Autoscaling policies exist and are tested
- [ ] Appropriate data partitioning and caching strategies
- [ ] Load testing performed for peak scenarios
- [ ] Performance KPIs tracked (p95/p99 latency, throughput)

## 5) Cost Optimization
- [ ] Cost allocation tags + account structure support chargeback/showback
- [ ] Budgets + alerts in place; anomaly detection enabled
- [ ] Rightsizing process exists (EC2/RDS/EKS/ECS) with cadence
- [ ] Storage lifecycle policies in place (S3 IA/Glacier)
- [ ] Savings Plans / RIs strategy defined and tracked
- [ ] Idle resources detection (EBS snapshots, unattached IPs, old AMIs)

## 6) Sustainability
- [ ] Compute scales to zero where possible; avoid always-on dev environments
- [ ] Efficient data retention and lifecycle policies
- [ ] Workload regions selected intentionally; avoid over-provisioning
- [ ] Observability helps reduce waste and accelerate root-cause

## Outputs
- Findings list (risk/impact/effort)
- Top 10 prioritized improvements (quick wins + strategic)
- 30/60/90-day roadmap
