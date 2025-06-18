# IAM Unused Access Analysis

This document outlines how unused IAM access is monitored and managed in the AWS environment as part of the **African Fintech IAM Guardrails** project. Regular access reviews are essential to keeping AWS accounts secure and aligned with best practices for **identity and access management (IAM)**.

---

##  Purpose

Cleaning up unused IAM users, roles, passwords, and access keys isn't just good housekeeping, it's a key part of a strong AWS security posture. This process helps:

- ** Reduce Security Risks**  
  Old credentials or inactive permissions can quietly become security risks, especially if someone gains unauthorized access to your AWS account.

- ** Improve Auditability**  
  Keeping IAM clean and minimal makes it easier to stay compliant and respond quickly if something goes wrong.

- ** Enforce Least Privilege**  
  Regular reviews ensure only actively used permissions are kept, supporting the principle of least privilege.

---

##  Methodology

We used **AWS IAM Access Analyzer's "Unused Access"** feature to identify any IAM resources that are not being used. This tool helps detect:

- IAM **roles** that haven’t been assumed over a defined period (e.g., 30 days).
- IAM **users** with unused **access keys** or **passwords**.

This is a native and cost-effective way to tighten **AWS IAM security** and avoid unnecessary attack surfaces.

---

##  Findings

> **Analysis Result:** `0 unused access findings`

This result is expected for a new AWS account. Most IAM users and roles have been recently created and are already in use. The clean slate confirms that no dormant credentials currently exist, a great start for enforcing secure IAM practices from day one.

---

##  Screenshot

You can view a snapshot of the IAM Access Analyzer result here:  
 [`iam-unused-access-analysis.png`](./screenshots/iam-unused-access-analysis.png)

---

##  What Happens if We Find Unused Access?

In a real production environment, unused IAM access would be addressed with a structured remediation plan:

1. ** Investigate**  
   Confirm whether the IAM entity is obsolete or still needed for upcoming work.

2. ** Notify**  
   Alert the owner or responsible team about the inactive access.

3. ** Revoke or Remove Access**  
   - Delete unused IAM users and roles.  
   - Rotate (replace with a new one) or disable stale access keys.  
   - Reset unused passwords.

4. ** Archive if Needed**  
   If the IAM role is tied to business-critical functions but unused, consider moving it into an “inactive” group with no permissions instead of deleting it right away.

This approach ensures you’re not just reacting to risks but actively preventing them.

---

##  Final Thoughts

Running **IAM unused access analysis** on AWS should be part of any cloud security routine. It reinforces **least privilege access**, reduces unnecessary exposure, and simplifies audits.

Even though there were no findings in this scan, regular checks like this one help maintain a secure, scalable, and audit-friendly AWS environment as your infrastructure grows.

---

*Keywords: AWS IAM, unused IAM access, access key management, IAM governance, AWS Access Analyzer, least privilege, AWS security best practices, IAM cleanup, audit readiness*
