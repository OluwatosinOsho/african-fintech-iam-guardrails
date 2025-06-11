# AWS Cost Budget Configuration

This document outlines the AWS Budget configured for the **"African Fintech IAM Guardrails"** project to ensure cost control, Free Tier adherence, and early warning alerts suitable for a cost-sensitive startup environment.

---

## Budget Details:

- **Name:** `FintechMonthlyBudget80USD`
- **Type:** Cost Budget
- **Period:** Monthly
- **Budgeted Amount:** $80 USD
- **Scope:** All AWS services
- **Region Scope:** All Regions (default)
- **Created On:** June 2025

---

## Alert Thresholds:

To ensure proactive cost management, the following alerts are configured:

- **50% of Budgeted Amount (Actual Spend)**  
  🔔 Alert triggered at **$40**

- **75% of Budgeted Amount (Actual Spend)**  
  🔔 Alert triggered at **$60**

- **90% of Budgeted Amount (Actual Spend)**  
  🔔 Alert triggered at **$72**

These multi-threshold alerts provide early warnings, allowing for timely review of resource usage and to prevent unexpected charges. This is especially critical for a startup operating on lean budgets.

---

## Notification Details:

- **Notification Recipients:**  
  - Primary email: `team@fintechstartup.io`  
  - Future SNS topic: `arn:aws:sns:us-east-1:123456789012:BudgetAlerts`

---

## Future Action Plans:

- **Automation Goals:**  
  I intend to integrate **AWS Budget Actions** to automate resource control in the future, such as stopping non-essential EC2 instances or triggering alerts via Slack webhook when thresholds are reached.

---

## Screenshot:

A visual representation of this budget's configuration can be found in the `screenshots/` directory:

📷 [`budget-alert.png`](./screenshots/budget-alert.png)

---

## Summary

This budget acts as a financial safeguard, ensuring the "African Fintech IAM Guardrails" project remains within a predictable and affordable monthly AWS spend. The configured alerts offer timely notifications, enabling fast response to avoid overage, a critical need for startup cost discipline. Over time, this budget system will evolve to include automation for proactive cloud cost governance.

---
