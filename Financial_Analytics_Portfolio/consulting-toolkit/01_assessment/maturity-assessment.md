# Cloud Maturity Assessment (Lightweight)

Score each dimension 1–5. Use the notes to justify the score.

## Dimensions
1) **Governance & Landing Zone**
- accounts, guardrails, SCPs, org trails, shared services

2) **Security Operations**
- detection, response, evidence, access reviews, secrets, patching

3) **Delivery & Automation**
- IaC adoption, CI/CD, automated testing, release safety

4) **Reliability & DR**
- backups, restore drills, RTO/RPO, multi-AZ, chaos testing

5) **Cost & FinOps**
- tagging, budgets, reviews, optimization cadence, commitment strategy

## Output
| Dimension | Score (1–5) | Evidence | Top Improvement |
|---|---:|---|---|
| Governance | 3 | Multi-account exists; limited SCPs | Add SCP guardrails and central logging |
| Security | 2 | Partial findings monitoring | Enable Security Hub aggregation + SIEM |
| Delivery | 4 | Terraform + CI checks | Add policy-as-code + drift detection |
| Reliability | 3 | Backups configured | Quarterly restore drills + DR docs |
| FinOps | 2 | Limited tagging | Tag policy + monthly FinOps review |
