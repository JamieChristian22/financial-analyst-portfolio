# Operations Acceptance Checklist

## Observability
- [ ] Logs centralized and searchable
- [ ] Metrics dashboards exist for key SLIs
- [ ] Alerts tuned (low noise) and routed to on-call
- [ ] Runbooks linked from alerts

## Security
- [ ] Least privilege IAM reviewed
- [ ] Secrets stored properly
- [ ] CloudTrail/Config/GuardDuty enabled and monitored

## Reliability
- [ ] Backups configured and restore tested
- [ ] RTO/RPO documented
- [ ] DR plan documented (if required)

## Delivery
- [ ] IaC is source of truth
- [ ] CI checks run on PR
- [ ] Rollback plan exists

## Handover
- [ ] KT completed
- [ ] Owners identified
- [ ] Open risks tracked in RAID log
