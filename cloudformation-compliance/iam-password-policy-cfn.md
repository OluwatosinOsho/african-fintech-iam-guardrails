# 🔐 CloudFormation Template: IAM Account Password Policy

This section documents an **AWS CloudFormation** template that enforces a robust IAM password policy as part of the **African Fintech IAM Guardrails** project. By defining this policy using **Infrastructure as Code (IaC)**, your team ensures repeatable, auditable, and automated application of AWS security standards.

---

## 🎯 Purpose: Why Enforce a Strong IAM Password Policy?

In FinTech, where cloud environments store and process sensitive financial data, enforcing strong password policies is a baseline control for security and compliance. This CloudFormation template ensures:

- ✅ **Centralized Security Management**  
  Set strong password standards across all users through one reusable CloudFormation template.

- ⚙️ **Consistent Enforcement**  
  Prevent configuration drift and human error by codifying IAM standards.

- 🔍 **Compliance Readiness**  
  Aligns with GDPR, PCI DSS, and other financial regulatory standards requiring strong authentication controls.

- 🧱 **Infrastructure as Code Benefits**  
  Automate deployment, track changes in Git, and integrate policy enforcement into CI/CD pipelines.

---

## 📄 CloudFormation Template Overview

- **Template File:** `iam-password-policy.yaml`  
- **Resource Type:** `AWS::IAM::AccountPasswordPolicy`  
- **Deployment Target:** Account level IAM security control  
- **Tooling Support:** CloudFormation console, CLI, or CI/CD pipelines

### ✅ YAML Configuration (Preview)

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'CloudFormation template for IAM Account Password Policy - FinTech Guardrails'

Resources:
  IAMAccountPasswordPolicy:
    Type: AWS::IAM::AccountPasswordPolicy
    Properties:
      MinimumPasswordLength: 14
      RequireSymbols: true
      RequireNumbers: true
      RequireUppercaseCharacters: true
      RequireLowercaseCharacters: true
      AllowUsersToChangePassword: true
      MaxPasswordAge: 90
      PasswordReusePrevention: 24
      HardExpiry: false

Outputs:
  PasswordPolicyStatus:
    Description: 'Status of the IAM Account Password Policy'
    Value: 'IAM Password Policy deployed successfully.'

---
## 🔎 Key Security Features

| **Policy Setting**                  | **Security Impact**                                                                 |
|------------------------------------|--------------------------------------------------------------------------------------|
| `MinimumPasswordLength: 14`        | Increases authentication strength with longer passwords                             |
| `RequireSymbols: true`             | Ensures inclusion of special characters                                             |
| `RequireNumbers: true`             | Forces numeric complexity                                                           |
| `RequireUppercaseCharacters: true` | Requires uppercase characters                                                       |
| `RequireLowercaseCharacters: true` | Ensures lowercase usage                                                             |
| `MaxPasswordAge: 90`               | Enforces regular password rotation every 90 days                                   |
| `PasswordReusePrevention: 24`      | Prevents reuse of last 24 passwords, reducing password cycling risks                |
| `HardExpiry: false`                | Allows grace login after expiry (can be set to `true` for stricter enforcement)     |

---

## 💼 Relevance for FinTech & DevSecOps Teams

### 🔐 User Account Protection  
Mitigates unauthorized access by enforcing **credential security** for IAM users.

### 🛡️ Automated Compliance  
Codified policy helps meet regulatory standards (e.g., **GDPR**, **PCI DSS**) without manual drift.

### 🔁 CI/CD Ready  
Easily integrates into **Infrastructure as Code (IaC)** pipelines for continuous security enforcement.

### 📚 Audit-Ready & Versioned  
YAML is machine readable, supports version control, and enables traceable change management.

---
## 🚀 Next Steps (Real-world Deployment)

In a production scenario, this template would be deployed using **AWS CloudFormation**, typically integrated into a **CI/CD pipeline**, to automatically set the account password policy. This ensures new IAM users automatically inherit strong password requirements.


