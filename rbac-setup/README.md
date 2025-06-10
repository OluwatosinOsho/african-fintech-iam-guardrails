# RBAC Setup for Fintech IAM – Secure AWS Permissions by Role

This repository captures the Role-Based Access Control (RBAC) setup for a simulated fintech startup based in Lagos. The goal is to implement secure, scalable AWS IAM roles tailored to job functions, not individuals.

RBAC helps enforce cloud security by assigning permissions based on responsibilities. In this project, we built and tested two IAM roles following AWS best practices for least privilege access.

---

## 🔐 IAM Roles Defined

### 1. FintechDevRole

- **Purpose:** Supports developers with the ability to build, deploy, and manage applications across AWS services, without giving away the keys to the kingdom.
- **Key Policy:** `PowerUserAccess` – intentionally excludes IAM permissions to prevent role escalation.
- **Why It Matters:** Developers can move fast without relying on admin users. This improves team autonomy while maintaining a secure boundary around identity management.

---

### 2. FintechAuditorRole

- **Purpose:** Provides internal auditors and security reviewers with visibility across the AWS environment, without write or delete privileges.
- **Key Policies:**
  - `SecurityAudit` – covers detailed insights into logs, IAM configurations, and other security-relevant services.
  - `ReadOnlyAccess` – ensures auditors can view but not modify resources.
- **Why It Matters:** Crucial for financial compliance, security posture reviews, and risk audits. This role guarantees traceability and accountability without the risk of accidental changes.

---

## 🔒 Principle of Least Privilege in Practice

Both roles are built with least privilege as the foundation. Instead of assigning permissions to individual users, access is granted via tightly scoped roles. This minimizes your attack surface and makes permission management more transparent and scalable.

---

## 📁 Content

- `fintech-dev-role.json`: Policy definition for developer role.
- `fintech-auditor-role-security-audit.json`: Security audit permissions.
- `fintech-auditor-role-readonly-access.json`: Read-only access policy.
- `screenshots/`: Visual walkthrough of IAM role configurations.

---

## 🔍 SEO Tags (For Repo Metadata)

`aws iam roles`, `rbac in aws`, `cloud security fintech`, `least privilege aws`, `iam policy examples`, `fintech devops`, `aws audit role`, `secure cloud infrastructure`, `iam best practices`
