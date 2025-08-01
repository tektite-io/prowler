# Compliance

Prowler allows you to execute checks based on requirements defined in compliance frameworks. By default, it will execute and give you an overview of the status of each compliance framework:

<img src="../img/compliance/compliance.png"/>

You can find CSVs containing detailed compliance results in the compliance folder within Prowler's output folder.

## Execute Prowler based on Compliance Frameworks

Prowler can analyze your environment based on a specific compliance framework and get more details, to do it, you can use option `--compliance`:

```sh
prowler <provider> --compliance <compliance_framework>
```

Standard results will be shown and additionally the framework information as the sample below for CIS AWS 2.0. For details a CSV file has been generated as well.

<img src="../img/compliance/compliance-cis-sample1.png"/>

???+ note
	**If Prowler can't find a resource related with a check from a compliance requirement, this requirement won't appear on the output**

## List Available Compliance Frameworks

In order to see which compliance frameworks are covered by Prowler, you can use option `--list-compliance`:

```sh
prowler <provider> --list-compliance
```

### AWS (36 frameworks)

- `aws_account_security_onboarding_aws`
- `aws_audit_manager_control_tower_guardrails_aws`
- `aws_foundational_security_best_practices_aws`
- `aws_foundational_technical_review_aws`
- `aws_well_architected_framework_reliability_pillar_aws`
- `aws_well_architected_framework_security_pillar_aws`
- `cis_1.4_aws`
- `cis_1.5_aws`
- `cis_2.0_aws`
- `cis_3.0_aws`
- `cis_4.0_aws`
- `cis_5.0_aws`
- `cisa_aws`
- `ens_rd2022_aws`
- `fedramp_low_revision_4_aws`
- `fedramp_moderate_revision_4_aws`
- `ffiec_aws`
- `gdpr_aws`
- `gxp_21_cfr_part_11_aws`
- `gxp_eu_annex_11_aws`
- `hipaa_aws`
- `iso27001_2013_aws`
- `iso27001_2022_aws`
- `kisa_isms_p_2023_aws`
- `kisa_isms_p_2023_korean_aws`
- `mitre_attack_aws`
- `nis2_aws`
- `nist_800_171_revision_2_aws`
- `nist_800_53_revision_4_aws`
- `nist_800_53_revision_5_aws`
- `nist_csf_1.1_aws`
- `pci_3.2.1_aws`
- `pci_4.0_aws`
- `prowler_threatscore_aws`
- `rbi_cyber_security_framework_aws`
- `soc2_aws`

### Azure (10 frameworks)

- `cis_2.0_azure`
- `cis_2.1_azure`
- `cis_3.0_azure`
- `ens_rd2022_azure`
- `iso27001_2022_azure`
- `mitre_attack_azure`
- `nis2_azure`
- `pci_4.0_azure`
- `prowler_threatscore_azure`
- `soc2_azure`

### GCP (10 frameworks)

- `cis_2.0_gcp`
- `cis_3.0_gcp`
- `cis_4.0_gcp`
- `ens_rd2022_gcp`
- `iso27001_2022_gcp`
- `mitre_attack_gcp`
- `nis2_gcp`
- `pci_4.0_gcp`
- `prowler_threatscore_gcp`
- `soc2_gcp`

### Kubernetes (5 frameworks)

- `cis_1.10_kubernetes`
- `cis_1.11_kubernetes`
- `cis_1.8_kubernetes`
- `iso27001_2022_kubernetes`
- `pci_4.0_kubernetes`

### M365 (3 frameworks)

- `cis_4.0_m365`
- `iso27001_2022_m365`
- `prowler_threatscore_m365`

### GitHub (1 framework)

- `cis_1.0_github`

## List Requirements of Compliance Frameworks
For each compliance framework, you can use the `--list-compliance-requirements` option to list its requirements:

```sh
prowler <provider> --list-compliance-requirements <compliance_framework(s)>
```

Example for the first requirements of CIS 1.5 for AWS:

```
Listing CIS 1.5 AWS Compliance Requirements:

Requirement Id: 1.1
	- Description: Maintain current contact details
	- Checks:
 		account_maintain_current_contact_details

Requirement Id: 1.2
	- Description: Ensure security contact information is registered
	- Checks:
 		account_security_contact_information_is_registered

Requirement Id: 1.3
	- Description: Ensure security questions are registered in the AWS account
	- Checks:
 		account_security_questions_are_registered_in_the_aws_account

Requirement Id: 1.4
	- Description: Ensure no 'root' user account access key exists
	- Checks:
 		iam_no_root_access_key

Requirement Id: 1.5
	- Description: Ensure MFA is enabled for the 'root' user account
	- Checks:
 		iam_root_mfa_enabled

[redacted]

```

## Create and contribute adding other Security Frameworks

This information is part of the Developer Guide and can be found [here](../developer-guide/security-compliance-framework.md).
