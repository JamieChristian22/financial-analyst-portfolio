# Cost Optimization Assessment (Quick Wins + Strategic)

## Data to Pull (last 30–90 days)
- Cost Explorer by service, account, tag
- Usage type trends (EC2 hours, data transfer, NAT GW, EBS)
- Rightsizing recommendations (Compute Optimizer)
- Savings Plans / RI coverage
- S3 storage class distribution + lifecycle status

## Quick Wins (Typical)
1. **Idle resource cleanup**
   - Unattached EBS volumes, old snapshots, unused EIPs, orphaned load balancers
2. **Storage lifecycle**
   - Move infrequently accessed data to IA/Glacier, expire transient logs
3. **NAT Gateway + data transfer**
   - Identify cross-AZ traffic and public egress; consider VPC endpoints and architecture changes
4. **Rightsize compute**
   - Identify over-provisioned EC2/RDS; reduce instance sizes or adopt autoscaling/serverless
5. **Savings Plans strategy**
   - Baseline steady-state compute; commit to conservative coverage and monitor drift

## Strategic (30–90 days)
- Re-architect always-on services to scale-to-zero
- Introduce event-driven patterns (SQS/EventBridge) to reduce peak provisioning
- Standardize tagging + chargeback/showback model
- FinOps operating model: monthly review + governance

## Output (Client-Ready)
| Opportunity | Monthly Savings | Effort | Risk | Recommendation |
|---|---:|---:|---:|---|
| EBS cleanup | $450 | Low | Low | Remove unattached volumes; snapshot policy |
| S3 lifecycle | $800 | Low | Low | IA/Glacier + retention rules |
| NAT optimization | $1,200 | Med | Med | Add VPC endpoints + reduce public egress |
