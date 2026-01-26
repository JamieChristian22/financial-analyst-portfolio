# Change Management Plan (AWS)

## Objectives
- Reduce risk from production changes
- Ensure rollbacks are safe and rehearsed
- Maintain auditability of who changed what and why

## Change Types
- **Standard**: low-risk, repeatable (approved in advance)
- **Normal**: planned changes requiring review/approval
- **Emergency**: expedited due to incident/outage

## Required Fields (per change)
- Change description + reason
- Impacted systems and blast radius
- Rollout plan + validation steps
- Rollback plan
- Approvals (Owner, Security if needed)
- Communication plan (who/when)

## Controls (Recommended)
- IaC-only changes for infrastructure
- PR reviews + CI checks
- Maintenance windows for disruptive changes
- Post-change verification checklist
