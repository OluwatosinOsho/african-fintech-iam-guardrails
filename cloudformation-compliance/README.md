# 🛡️ Infrastructure as Code (IaC) for IAM Compliance

This directory demonstrates how to leverage **AWS CloudFormation** to automate and enforce IAM security controls as **Infrastructure as Code (IaC)**. For **FinTech organizations**, using IaC is important, it ensures **secure, auditable, and repeatable** deployments across all environments, minimizing human error and improving compliance with industry standards.

---

## 🎯 Why IAM Compliance with IaC Matters

✅ **Automated Deployments**  
Provision IAM policies and controls consistently across development, staging, and production.

✅ **Version Control & Traceability**  
Store all policy definitions in Git for change history, audit trails, and rollbacks.

✅ **Compliance by Design**  
Integrate IAM policy checks early in your CI/CD workflows to prevent misconfigurations before deployment.

✅ **Configuration Drift Protection**  
Continuously enforce desired security states across environments.

✅ **Faster Audit Readiness**  
Demonstrate compliance (e.g., PCI DSS, SOC 2, NDPR) through automated policies.

---

## 🔐 Implemented Control: IAM Password Policy (CloudFormation)

This section includes a **CloudFormation template** that enforces a strong account wide password policy for IAM users.

### 📜 `iam-password-policy.yaml`

**What it does:**

- Enforces a minimum password length
- Requires uppercase, lowercase, numbers, and symbols
- Prevents password reuse
- Enforces password expiration/rotation (max age)
- Disallows changing passwords before a minimum age

**Why it matters:**

- Protects against **unauthorized access** and **unauthorized access attempts via compromised credentials**
- Enhances **protection against unauthorized login attempts**
- Helps meet compliance requiremets like **PCI DSS** and **ISO 27001**

> 🔁 **Deployed via CI/CD pipelines**, this template ensures new IAM users inherit strong, standardized security policies.

---

## 🔧 Files in This Directory

| File | Description |
|------|-------------|
| [`iam-password-policy.yaml`](./iam-password-policy.yaml) | CloudFormation YAML for enforcing password policy |
| [`iam-password-policy-cfn.md`](./iam-password-policy-cfn.md) | Documentation outlining policy rationale, fields, and compliance implications |

---

## 🚀 Future Enhancements

- **Least Privilege Role Templates:** Define secure defaults for IAM roles and service permissions  
- **MFA Enforcement:** Enforce console MFA access through automated controls  
- **AWS Organizations SCPs:** Prevent root account usage, block risky actions or unapproved regions  
- **Automated Remediation:** Deploy Lambda functions to auto remediate misconfigurations flagged by AWS Config or Access Analyzer

---

## ✅ Next Steps (Production Grade Deployment)

In a real world setup, this template would be deployed through **AWS CloudFormation** integrated with a **CI/CD pipeline**, ensuring:

- **Automatic enforcement** of IAM password policies across accounts/environments  
- **Audit ready infrastructure** changes via Git version control  
- **Consistent security controls** across FinTech staging, QA, and production
