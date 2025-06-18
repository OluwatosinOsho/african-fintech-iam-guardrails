#  AWS Cost Budget Configuration for "African Fintech IAM Guardrails"

This document outlines how AWS Budgets are configured for the **African Fintech IAM Guardrails** project, a key initiative to stay within AWS Free Tier limits, prevent surprise charges, and maintain financial discipline for a resource-conscious startup.

---

##  Why Set Up a Cost Budget?

Tracking AWS spend in real time helps early-stage teams:

- Avoid Free Tier overruns  
- Stay within predictable cloud costs  
- Get notified before budgets are breached  
- Make data-driven decisions on scaling or shutting down resources

---

##  Budget Details

- **Name:** `FintechMonthlyBudget80USD`  
- **Type:** Cost Budget  
- **Period:** Monthly  
- **Budgeted Amount:** **$80 USD**  
- **Applies To:** All AWS services  
- **Region Scope:** Global (default)  
- **Date Created:** June 2025  

This budget reflects the monthly Free Tier buffer and extra allowance for small-scale experiments.

---

##  Alert Thresholds

To ensure proactive cost management, we've set up the following alert triggers:

| Threshold | Spend Amount | Alert Description            |
|-----------|--------------|------------------------------|
| **50%**   | $40          | First warning: review usage  |
| **75%**   | $60          | High usage alert             |
| **90%**   | $72          | Urgent: budget nearly exhausted |

These multi-tier alerts give us time to investigate and act before real cost impact occurs.

---

##  Notification Settings

- **Email Recipients:**  
  - `team@fintechstartup.io` (primary recipient)

- **(Planned)** SNS Topic Integration:  
  `arn:aws:sns:us-east-1:123456789012:BudgetAlerts`  
  *To support automation and Slack alerting in the future.*

---

##  Future Automation Plans

We're working toward integrating **AWS Budgets Actions** that can:

- Automatically **shut down non-critical EC2 instances**  
- Send alerts to **Slack** or **Jira** via webhook  
- Trigger **Lambda functions** for cost mitigation  

This will move us from **cost awareness** to **automated cost control**, crucial for long-term sustainability.

---

##  Budget Screenshot

Visual reference for the configured budget is available here:  
📷 [`budget-alert.png`](./screenshots/budget-alert.png)

---

##  Summary

Setting this monthly AWS budget is a foundational part of our cloud governance strategy. It ensures the **"African Fintech IAM Guardrails"** project stays cost-effective, with early alerts and a clear ceiling on spend.  

Over time, this will evolve into an **automated cost management system** that aligns with startup agility and engineering best practices.

---

