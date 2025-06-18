##  Implemented IAM Guardrails & Cloud Security Controls

This project meticulously designs and documents a comprehensive suite of IAM and cloud security guardrails, categorized by key security domains:

| Feature Category                      | Description                                                                  | Key Technologies / Concepts                                  | Status          |
|--------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------|-----------------|
| **1. Role-Based Access Control (RBAC)**  | Design principles for granular, least-privilege access for FinTech roles.     | IAM Users, Groups, Roles, Policies                           | ✅ Implemented   |
| **2. Threat Modeling & Mitigation**     | Identification of potential threats and corresponding mitigation strategies. | STRIDE, Least Privilege, Network Segmentation, Encryption    | ✅ Implemented   |
| **3. Cost Governance**                 | Proactive monitoring and alerting for unexpected cloud spend.                | AWS Budgets, SNS Notifications                               | ✅ Implemented   |
| **4. Automated Drift Detection**       | Continuous monitoring for deviations from desired security configurations.   | AWS Config, Managed Rules (root access key)                  | ✅ Implemented   |
| **5. AI-Powered Policy Drafting**      | Leveraging Generative AI (Google Gemini) for secure policy generation.       | Google Gemini, S3 Bucket Policies, SSE-KMS, IP Restrictions  | ✅ Implemented   |
| **6. External Access Review**          | Identifying resources shared with external entities.                         | AWS IAM Access Analyzer                                      | ✅ Implemented   |
| **7. IaC for IAM Compliance**          | Defining IAM security policies as Infrastructure as Code.                    | AWS CloudFormation, IAM Account Password Policy              | ✅ Implemented   |
| **8. Automated Remediation**           | Implementing self-healing mechanisms for common security misconfigurations.  | AWS Lambda (Python), S3 Public Access Block Remediation      | ✅ Implemented   |


---

###  Project Structure & Detailed Documentation

Each of the above sections is documented in its dedicated directory:

- [`rbac-setup/`](./rbac-setup/README.md)
- [`threat-models/`](./threat-models/README.md)
- [`cost-controls/`](./cost-controls/README.md)
- [`drift-detection/`](./drift-detection/README.md)
- [`ai-policy-drafting/`](./ai-policy-drafting/README.md)
- [`external-access-review/`](./external-access-review/README.md)
- [`cloudformation-compliance/`](./cloudformation-compliance/README.md)
- [`automated-remediation/`](./automated-remediation/README.md)

Each directory contains detailed markdown files, code snippets (JSON, YAML, Python), and screenshots where applicable.
