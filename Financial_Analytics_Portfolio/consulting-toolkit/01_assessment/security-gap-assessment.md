# Security Gap Assessment (Framework)

## How to Use
1. Identify the control category
2. Record current state evidence
3. Rate gap severity (High/Med/Low)
4. Propose remediation + owner + timeline

## 1) Identity & Access Management
- Control: SSO enforced, MFA, least privilege, periodic access reviews
- Evidence to collect:
  - IAM Access Analyzer results
  - IAM credential report summary
  - Role trust policies review (cross-account access)
- Common gaps:
  - overly permissive roles (`*` actions/resources)
  - long-lived access keys
  - missing access review cadence
- Recommended remediation:
  - SSO + permission sets
  - SCP guardrails to prevent risky actions
  - break-glass procedure with monitoring

## 2) Logging & Detection
- Control: CloudTrail org trail, Config, GuardDuty, Security Hub
- Evidence:
  - Org trail enabled in all regions
  - Log retention policy (CloudWatch/S3)
  - Alerts routed to ticketing/Slack/SIEM
- Common gaps:
  - logs not centralized
  - insufficient retention for audit
- Remediation:
  - central security account + log archive account
  - set retention standards (e.g., 365 days hot + archival)

## 3) Data Protection
- Control: encryption at rest/in transit; KMS key governance
- Evidence:
  - S3 default encryption, bucket policies, TLS enforcement
  - RDS/Aurora encryption enabled
  - Secrets stored in managed services
- Common gaps:
  - public buckets, missing TLS-only policies
  - keys without rotation or ownership
- Remediation:
  - KMS CMKs with rotation, key policies reviewed
  - enforce bucket policies and Block Public Access

## 4) Network Security
- Control: segmentation, least exposure, egress control
- Evidence:
  - VPC design, subnets, NACL/SG posture
  - WAF rules, CloudFront protections
  - private endpoints (Interface VPC endpoints) for AWS APIs
- Common gaps:
  - workloads in public subnets unnecessarily
  - wide-open SGs (0.0.0.0/0)
- Remediation:
  - private subnets + ALB/NLB ingress
  - tighten SGs; use WAF + rate limiting

## 5) Vulnerability & Patch Management
- Control: image scanning, patching cadence, SBOM practices (where applicable)
- Evidence:
  - ECR scan results, SSM Patch Manager, Inspector
- Remediation:
  - automate patching in maintenance windows
  - enforce base images and dependency scanning

## Assessment Output Table (Copy into your report)
| Control Area | Current State | Gap | Severity | Remediation | Owner | ETA |
|---|---|---|---|---|---|---|
| IAM | SSO partial; some legacy IAM users | Reduce IAM users, enforce MFA | High | Move to SSO permission sets; disable long-lived keys | Security | 30 days |
