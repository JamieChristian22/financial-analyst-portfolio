# FinOps Playbook (AWS) — Practical Consulting Guide

## FinOps Cadence (Lightweight)
- **Weekly (30 min):** top spend drivers + anomalies
- **Monthly (60 min):** optimization actions, savings tracking, commitment review
- **Quarterly:** architecture cost review + roadmap

## What to Measure
- Total monthly spend + trend
- Cost per unit (per 1k requests, per GB ingested, per user)
- Savings Plans / RI coverage
- Tagging coverage
- Top 5 services by spend

## Core Plays
### 1) Rightsizing (Compute + DB)
- Use Compute Optimizer + CloudWatch metrics
- Reduce instance size OR shift to autoscaling/serverless
- Validate with load tests and error budgets

### 2) Storage Lifecycle
- S3:
  - Standard → IA → Glacier → Expire
- Logs:
  - define retention by log type (security vs app logs)
- Snapshots:
  - purge stale snapshots

### 3) Network Cost
- Reduce NAT GW dependency where possible
- Add Interface/Gateway VPC endpoints
- Reduce cross-AZ chatter

### 4) Commitment Strategy
- Start with conservative Savings Plans for steady baseline
- Review monthly; avoid over-committing if workload is volatile

## Executive Summary Template (Copy/Paste)
- This month spend: $____ (___% MoM)
- Top drivers: (1) __ (2) __ (3) __
- Savings delivered: $____
- Next month actions: ____
