# Threat Model Template (Lightweight)

## 1) Assets
- What are we protecting? (PII/PHI, auth tokens, financial data, IP)

## 2) Entry Points
- APIs, web frontends, batch ingestion, admin consoles, CI/CD

## 3) Threats (STRIDE)
- Spoofing: identity misuse
- Tampering: data/code alteration
- Repudiation: lack of audit trails
- Information Disclosure: data leaks
- Denial of Service: availability attacks
- Elevation of Privilege: privilege escalation

## 4) Controls
- IAM least privilege + access reviews
- WAF + rate limiting
- Encryption + key governance
- Central logging + alerting
- Network segmentation + endpoints

## 5) Findings Table
| Threat | Scenario | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|---|
| DoS | API spam | High | Med | WAF rules + throttling | Platform |
