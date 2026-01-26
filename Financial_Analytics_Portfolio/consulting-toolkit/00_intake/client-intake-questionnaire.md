# Client Intake Questionnaire (Pre-Discovery)

Send this before the first meeting. Ask for answers + links to diagrams/repos/runbooks.

## A) Goals & Success
1. What business problem are we solving? Why now?
2. What does success look like in 30/60/90 days?
3. Top 3 KPIs to improve (e.g., cost, reliability, latency, security posture)?
4. Hard constraints (deadline, budget cap, vendor/tooling requirements)?

## B) Workload Overview
1. Workload type: API, batch, streaming, analytics, ML, IoT, mixed?
2. Peak and average usage:
   - requests/sec (APIs) or events/sec (streams)
   - daily/weekly data volume
   - concurrent users
3. Latency/data freshness requirements
4. Data classification (public/internal/confidential/regulated)

## C) Current Architecture
1. AWS accounts + environment strategy (single vs multi-account)
2. Networking: VPCs, subnets, routing, peering, TGW, VPN/Direct Connect
3. Compute: EC2/ECS/EKS/Lambda, autoscaling strategy
4. Storage: S3/EBS/EFS/FSx; lifecycle and backups
5. Databases: RDS/Aurora/DynamoDB/Redshift; HA/DR configuration
6. Integration: SQS/SNS/EventBridge/Kinesis; retry + DLQ strategy

## D) Delivery & Operations
1. IaC: Terraform/CloudFormation/CDK? How is it managed and reviewed?
2. CI/CD: tools used, branching strategy, deployment approach
3. Observability: CloudWatch, X-Ray, OpenTelemetry, external APM?
4. On-call: escalation path, incident process, postmortems?

## E) Security & Compliance
1. Identity provider (SSO/Okta/Azure AD) and access request process
2. MFA enforcement + break-glass approach
3. Encryption: in-transit, at-rest, key ownership (KMS/HSM)
4. Security monitoring: GuardDuty, Security Hub, Config, SIEM integration
5. Compliance framework(s): SOC2, HIPAA, PCI, GDPR, etc.

## F) Cost & FinOps
1. Monthly AWS spend (last 3 months) and biggest services
2. Tagging coverage (% of spend allocated to cost centers)
3. Savings Plans/Reserved Instances coverage
4. Known quick wins (idle resources, storage lifecycle, rightsizing)

## Attachments Requested
- Most recent architecture diagram
- Last 2 incident postmortems (if available)
- Current AWS Organizations/account list (sanitized is fine)
- A cost report snapshot (Cost Explorer export)
