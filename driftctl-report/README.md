---

# Automated Drift Detection with AWS Config

This directory documents how we implemented **automated configuration drift detection** for IAM security using AWS Config, an essential part of maintaining cloud security standards in fintech environments. Drift happens when your current AWS resource states deviate from security baselines or policy intent, leading to blind spots, weak compliance, and elevated risk.

---

## Why Drift Detection Matters in Fintech IAM

In a fintech startup, especially one operating in a mobile first, regulated environment, proactive IAM drift detection offers:

* **Continuous Compliance at Scale:** Automatically monitors IAM configuration (MFA, root access, password policies) against internal controls and external regulatory expectations.
* **Early Detection of Anti Patterns:** Instantly flags high risk missteps like active **root access keys**, a known security anti pattern and breach vector.
* **Audit-Ready Trail:** Creates a persistent compliance record, vital for demonstrating maturity to auditors, partners, and investors.
* **Reduced Manual Load:** Frees security and DevOps teams from repetitive IAM audits with always on monitoring.
* **Minimized Security Exposure::** Early detection of IAM drift ensures misconfigurations are resolved before they evolve into security liabilities.

---

## Implemented Rule: IAM Root Access Key Check

### ✅ AWS Config Rule: `iam-root-access-key-check`

* **Purpose:** Checks for **active root account access keys**, which should never exist under secure IAM operations.
* **Type:** AWS Managed Rule  
* **Trigger:** Runs automatically when IAM-related changes are detected  
* **Compliance Status:** ✅ `COMPLIANT` in our environment

**Why This Rule Matters:**

* Root access keys are a **prime target** for attackers.  
* Removing them **reduces security exposure** in the event of a breach.  
* Flags drift without manual oversight and keeps us aligned with **cloud security best practices**.  
* Provides **verifiable proof of IAM maturity** to stakeholders in regulated environments.

📄 See the full breakdown: [`iam-config-rule.md`](./iam-config-rule.md)  
🖼️ Screenshot available here: [`config-iam-root-access-key-check.png`](./screenshots/config-iam-root-access-key-check.png)

---

## What’s Next

We're extending our drift detection baseline to cover broader IAM hygiene with:

* 📌 **Automated Remediation**: Trigger Lambda functions to fix drift (e.g., disable root keys, enforce MFA).
* 🔔 **SNS Alerts**: Notify teams when violations are detected, ideal for Slack/SMS/email integrations.
* 🧩 **Additional Config Rules**: Expand to detect:

  * IAM users without MFA  
  * Weak password policies  
  * Overly permissive roles/policies  

---

## Directory Contents

* `iam-config-rule.md`: In-depth explanation and results of the root key drift rule.
* `screenshots/`: Visual proof of rule status and drift detection results.

---
