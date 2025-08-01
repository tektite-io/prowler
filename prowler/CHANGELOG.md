# Prowler SDK Changelog

All notable changes to the **Prowler SDK** are documented in this file.

## [v5.10.0] (Prowler UNRELEASED)

### Added
- `bedrock_api_key_no_administrative_privileges` check for AWS provider [(#8321)](https://github.com/prowler-cloud/prowler/pull/8321)
- Support App Key Content in GitHub provider [(#8271)](https://github.com/prowler-cloud/prowler/pull/8271)
- CIS 4.0 for the Azure provider [(#7782)](https://github.com/prowler-cloud/prowler/pull/7782)
- `vm_desired_sku_size` check for Azure provider [(#8191)](https://github.com/prowler-cloud/prowler/pull/8191)
- `vm_scaleset_not_empty` check for Azure provider [(#8192)](https://github.com/prowler-cloud/prowler/pull/8192)
- GitHub repository and organization scoping support with `--repository/respositories` and `--organization/organizations` flags [(#8329)](https://github.com/prowler-cloud/prowler/pull/8329)

### Changed
- Handle some AWS errors as warnings instead of errors [(#8347)](https://github.com/prowler-cloud/prowler/pull/8347)
- Revert import of `checkov` python library [(#8385)](https://github.com/prowler-cloud/prowler/pull/8385)
- Updated policy mapping in ISMS-P compliance file for improved alignment [(#8367)](https://github.com/prowler-cloud/prowler/pull/8367)

### Fixed
- False positives in SQS encryption check for ephemeral queues [(#8330)](https://github.com/prowler-cloud/prowler/pull/8330)
- Add protocol validation check in security group checks to ensure proper protocol matching [(#8374)](https://github.com/prowler-cloud/prowler/pull/8374)
- Add missing audit evidence for controls 1.1.4 and 2.5.5 for ISMS-P compliance. [(#8386)](https://github.com/prowler-cloud/prowler/pull/8386)

---

## [v5.9.3] (Prowler UNRELEASED)

### Fixed
- Add more validations to Azure Storage models when some values are None to avoid serialization issues [(#8325)](https://github.com/prowler-cloud/prowler/pull/8325)
- `sns_topics_not_publicly_accessible` false positive with `aws:SourceArn` conditions [(#8326)](https://github.com/prowler-cloud/prowler/issues/8326)
- Remove typo from description req 1.2.3 - Prowler ThreatScore m365 [(#8384)](https://github.com/prowler-cloud/prowler/pull/8384)
- Way of counting FAILED/PASS reqs from `kisa_isms_p_2023_aws` table [(#8382)](https://github.com/prowler-cloud/prowler/pull/8382)
- Avoid multiple module error calls in M365 provider [(#8353)](https://github.com/prowler-cloud/prowler/pull/8353)

---

## [v5.9.2] (Prowler v5.9.2)

### Fixed
- Use the correct resource name in `defender_domain_dkim_enabled` check [(#8334)](https://github.com/prowler-cloud/prowler/pull/8334)

---

## [v5.9.0] (Prowler v5.9.0)

### Added
- `storage_smb_channel_encryption_with_secure_algorithm` check for Azure provider [(#8123)](https://github.com/prowler-cloud/prowler/pull/8123)
- `storage_smb_protocol_version_is_latest` check for Azure provider [(#8128)](https://github.com/prowler-cloud/prowler/pull/8128)
- `vm_backup_enabled` check for Azure provider [(#8182)](https://github.com/prowler-cloud/prowler/pull/8182)
- `vm_linux_enforce_ssh_authentication` check for Azure provider [(#8149)](https://github.com/prowler-cloud/prowler/pull/8149)
- `vm_ensure_using_approved_images` check for Azure provider [(#8168)](https://github.com/prowler-cloud/prowler/pull/8168)
- `vm_scaleset_associated_load_balancer` check for Azure provider [(#8181)](https://github.com/prowler-cloud/prowler/pull/8181)
- `defender_attack_path_notifications_properly_configured` check for Azure provider [(#8245)](https://github.com/prowler-cloud/prowler/pull/8245)
- `entra_intune_enrollment_sign_in_frequency_every_time` check for M365 provider [(#8223)](https://github.com/prowler-cloud/prowler/pull/8223)
- Support for remote repository scanning in IaC provider [(#8193)](https://github.com/prowler-cloud/prowler/pull/8193)
- Add `test_connection` method to GitHub provider [(#8248)](https://github.com/prowler-cloud/prowler/pull/8248)

### Changed
- Refactor the Azure Defender get security contact configuration method to use the API REST endpoint instead of the SDK [(#8241)](https://github.com/prowler-cloud/prowler/pull/8241)

### Fixed
- Title & description wording for `iam_user_accesskey_unused` check for AWS provider [(#8233)](https://github.com/prowler-cloud/prowler/pull/8233)
- Add GitHub provider to lateral panel in documentation and change -h environment variable output [(#8246)](https://github.com/prowler-cloud/prowler/pull/8246)
- Show `m365_identity_type` and `m365_identity_id` in cloud reports [(#8247)](https://github.com/prowler-cloud/prowler/pull/8247)
- Ensure `is_service_role` only returns `True` for service roles [(#8274)](https://github.com/prowler-cloud/prowler/pull/8274)
- Update DynamoDB check metadata to fix broken link [(#8273)](https://github.com/prowler-cloud/prowler/pull/8273)
- Show correct count of findings in Dashboard Security Posture page [(#8270)](https://github.com/prowler-cloud/prowler/pull/8270)
- Add Check's metadata service name validator [(#8289)](https://github.com/prowler-cloud/prowler/pull/8289)
- Use subscription ID in Azure mutelist [(#8290)](https://github.com/prowler-cloud/prowler/pull/8290)
- `ServiceName` field in Network Firewall checks metadata [(#8280)](https://github.com/prowler-cloud/prowler/pull/8280)
- Update `entra_users_mfa_capable` check to use the correct resource name and ID [(#8288)](https://github.com/prowler-cloud/prowler/pull/8288)
- Handle multiple services and severities while listing checks [(#8302)](https://github.com/prowler-cloud/prowler/pull/8302)
- Handle `tenant_id` for M365 Mutelist [(#8306)](https://github.com/prowler-cloud/prowler/pull/8306)
- Fix error in Dashboard Overview page when reading CSV files [(#8257)](https://github.com/prowler-cloud/prowler/pull/8257)

---

## [v5.8.1] (Prowler 5.8.1)

### Fixed
- Detect wildcarded ARNs in sts:AssumeRole policy resources [(#8164)](https://github.com/prowler-cloud/prowler/pull/8164)
- List all streams and `firehose_stream_encrypted_at_rest` logic [(#8213)](https://github.com/prowler-cloud/prowler/pull/8213)
- Allow empty values for http_endpoint in templates [(#8184)](https://github.com/prowler-cloud/prowler/pull/8184)
- Convert all Azure Storage models to Pydantic models to avoid serialization issues [(#8222)](https://github.com/prowler-cloud/prowler/pull/8222)

---

## [v5.8.0] (Prowler v5.8.0)

### Added

- `storage_geo_redundant_enabled` check for Azure provider [(#7980)](https://github.com/prowler-cloud/prowler/pull/7980)
- `storage_cross_tenant_replication_disabled` check for Azure provider [(#7977)](https://github.com/prowler-cloud/prowler/pull/7977)
- CIS 1.11 compliance framework for Kubernetes [(#7790)](https://github.com/prowler-cloud/prowler/pull/7790)
- Support `HTTPS_PROXY` and `K8S_SKIP_TLS_VERIFY` in Kubernetes [(#7720)](https://github.com/prowler-cloud/prowler/pull/7720)
- Weight for Prowler ThreatScore scoring [(#7795)](https://github.com/prowler-cloud/prowler/pull/7795)
- `entra_users_mfa_capable` check for M365 provider [(#7734)](https://github.com/prowler-cloud/prowler/pull/7734)
- `admincenter_organization_customer_lockbox_enabled` check for M365 provider [(#7732)](https://github.com/prowler-cloud/prowler/pull/7732)
- `admincenter_external_calendar_sharing_disabled` check for M365 provider [(#7733)](https://github.com/prowler-cloud/prowler/pull/7733)
- Level for Prowler ThreatScore in the accordion in Dashboard [(#7739)](https://github.com/prowler-cloud/prowler/pull/7739)
- CIS 4.0 compliance framework for GCP [(7785)](https://github.com/prowler-cloud/prowler/pull/7785)
- `repository_has_codeowners_file` check for GitHub provider [(#7752)](https://github.com/prowler-cloud/prowler/pull/7752)
- `repository_default_branch_requires_signed_commits` check for GitHub provider [(#7777)](https://github.com/prowler-cloud/prowler/pull/7777)
- `repository_inactive_not_archived` check for GitHub provider [(#7786)](https://github.com/prowler-cloud/prowler/pull/7786)
- `repository_dependency_scanning_enabled` check for GitHub provider [(#7771)](https://github.com/prowler-cloud/prowler/pull/7771)
- `repository_secret_scanning_enabled` check for GitHub provider [(#7759)](https://github.com/prowler-cloud/prowler/pull/7759)
- `repository_default_branch_requires_codeowners_review` check for GitHub provider [(#7753)](https://github.com/prowler-cloud/prowler/pull/7753)
- NIS 2 compliance framework for AWS [(#7839)](https://github.com/prowler-cloud/prowler/pull/7839)
- NIS 2 compliance framework for Azure [(#7857)](https://github.com/prowler-cloud/prowler/pull/7857)
- Search bar in Dashboard Overview page [(#7804)](https://github.com/prowler-cloud/prowler/pull/7804)
- NIS 2 compliance framework for GCP [(#7912)](https://github.com/prowler-cloud/prowler/pull/7912)
- `storage_account_key_access_disabled` check for Azure provider [(#7974)](https://github.com/prowler-cloud/prowler/pull/7974)
- `storage_ensure_file_shares_soft_delete_is_enabled` check for Azure provider [(#7966)](https://github.com/prowler-cloud/prowler/pull/7966)
- Make `validate_mutelist` method static inside `Mutelist` class [(#7811)](https://github.com/prowler-cloud/prowler/pull/7811)
- Avoid bypassing IAM check using wildcards [(#7708)](https://github.com/prowler-cloud/prowler/pull/7708)
- `storage_blob_versioning_is_enabled` new check for Azure provider [(#7927)](https://github.com/prowler-cloud/prowler/pull/7927)
- New method to authenticate in AppInsights in check `app_function_application_insights_enabled` [(#7763)](https://github.com/prowler-cloud/prowler/pull/7763)
- ISO 27001 2022 for M365 provider [(#7985)](https://github.com/prowler-cloud/prowler/pull/7985)
- `codebuild_project_uses_allowed_github_organizations` check for AWS provider [(#7595)](https://github.com/prowler-cloud/prowler/pull/7595)
- IaC provider [(#7852)](https://github.com/prowler-cloud/prowler/pull/7852)
- Azure Databricks service integration for Azure provider, including the `databricks_workspace_vnet_injection_enabled` check [(#8008)](https://github.com/prowler-cloud/prowler/pull/8008)
- `databricks_workspace_cmk_encryption_enabled` check for Azure provider [(#8017)](https://github.com/prowler-cloud/prowler/pull/8017)
- Appication auth for PowerShell in M365 provider [(#7992)](https://github.com/prowler-cloud/prowler/pull/7992)
- `storage_account_default_to_entra_authorization_enabled` check for Azure provider [(#7981)](https://github.com/prowler-cloud/prowler/pull/7981)
- Improve overview page from Prowler Dashboard [(#8118)](https://github.com/prowler-cloud/prowler/pull/8118)
- `keyvault_ensure_public_network_access_disabled` check for Azure provider [(#8072)](https://github.com/prowler-cloud/prowler/pull/8072)
- `monitor_alert_service_health_exists` check for Azure provider [(#8067)](https://github.com/prowler-cloud/prowler/pull/8067)
- Replace `Domain.Read.All` with `Directory.Read.All` in Azure and M365 docs [(#8075)](https://github.com/prowler-cloud/prowler/pull/8075)
- Refactor IaC provider to use Checkov as Python library [(#8093)](https://github.com/prowler-cloud/prowler/pull/8093)
- New check `codebuild_project_not_publicly_accessible` for AWS provider [(#8127)](https://github.com/prowler-cloud/prowler/pull/8127)

### Fixed
- Consolidate Azure Storage file service properties to the account level, improving the accuracy of the `storage_ensure_file_shares_soft_delete_is_enabled` check [(#8087)](https://github.com/prowler-cloud/prowler/pull/8087)
- Migrate Azure VM service and managed disk logic to Pydantic models for better serialization and type safety, and update all related tests to use the new models and fix UUID handling [(#https://github.com/prowler-cloud/prowler/pull/8151)](https://github.com/prowler-cloud/prowler/pull/https://github.com/prowler-cloud/prowler/pull/8151)
- `organizations_scp_check_deny_regions` check to pass when SCP policies have no statements [(#8091)](https://github.com/prowler-cloud/prowler/pull/8091)
- Fix logic in VPC and ELBv2 checks [(#8077)](https://github.com/prowler-cloud/prowler/pull/8077)
- Retrieve correctly ECS Container insights settings [(#8097)](https://github.com/prowler-cloud/prowler/pull/8097)
- Fix correct handling for different accounts-dates in prowler dashboard compliance page [(#8108)](https://github.com/prowler-cloud/prowler/pull/8108)
- Handling of `block-project-ssh-keys` in GCP check `compute_instance_block_project_wide_ssh_keys_disabled` [(#8115)](https://github.com/prowler-cloud/prowler/pull/8115)
- Handle empty name in Azure Defender and GCP checks [(#8120)](https://github.com/prowler-cloud/prowler/pull/8120)

### Changed
- Reworked `S3.test_connection` to match the AwsProvider logic [(#8088)](https://github.com/prowler-cloud/prowler/pull/8088)

### Removed
- OCSF version number references to point always to the latest [(#8064)](https://github.com/prowler-cloud/prowler/pull/8064)

---

## [v5.7.5] (Prowler 5.7.5)

### Fixed
- Use unified timestamp for all requirements [(#8059)](https://github.com/prowler-cloud/prowler/pull/8059)
- Add EKS to service without subservices [(#7959)](https://github.com/prowler-cloud/prowler/pull/7959)
- `apiserver_strong_ciphers_only` check for K8S provider [(#7952)](https://github.com/prowler-cloud/prowler/pull/7952)
- Handle `0` at the start and end of account uids in Prowler Dashboard [(#7955)](https://github.com/prowler-cloud/prowler/pull/7955)
- Typo in PCI 4.0 for K8S provider [(#7971)](https://github.com/prowler-cloud/prowler/pull/7971)
- AWS root credentials checks always verify if root credentials are enabled [(#7967)](https://github.com/prowler-cloud/prowler/pull/7967)
- Github provider to `usage` section of `prowler -h`: [(#7906)](https://github.com/prowler-cloud/prowler/pull/7906)
- `network_flow_log_more_than_90_days` check to pass when retention policy is 0 days [(#7975)](https://github.com/prowler-cloud/prowler/pull/7975)
- Update SDK Azure call for ftps_state in the App Service [(#7923)](https://github.com/prowler-cloud/prowler/pull/7923)
- Validate ResourceType in CheckMetadata [(#8035)](https://github.com/prowler-cloud/prowler/pull/8035)
- Missing ResourceType values in check's metadata [(#8028)](https://github.com/prowler-cloud/prowler/pull/8028)
- Avoid user requests in setup_identity app context and user auth log enhancement [(#8043)](https://github.com/prowler-cloud/prowler/pull/8043)

---

## [v5.7.3] (Prowler v5.7.3)

### Fixed
- Automatically encrypt password in Microsoft365 provider [(#7784)](https://github.com/prowler-cloud/prowler/pull/7784)
- Remove last encrypted password appearances [(#7825)](https://github.com/prowler-cloud/prowler/pull/7825)

---

## [v5.7.2] (Prowler v5.7.2)

### Fixed
- `m365_powershell test_credentials` to use sanitized credentials [(#7761)](https://github.com/prowler-cloud/prowler/pull/7761)
- `admincenter_users_admins_reduced_license_footprint` check logic to pass when admin user has no license [(#7779)](https://github.com/prowler-cloud/prowler/pull/7779)
- `m365_powershell` to close the PowerShell sessions in msgraph services [(#7816)](https://github.com/prowler-cloud/prowler/pull/7816)
- `defender_ensure_notify_alerts_severity_is_high`check to accept high or lower severity [(#7862)](https://github.com/prowler-cloud/prowler/pull/7862)
- Replace `Directory.Read.All` permission with `Domain.Read.All` which is more restrictive [(#7888)](https://github.com/prowler-cloud/prowler/pull/7888)
- Split calls to list Azure Functions attributes [(#7778)](https://github.com/prowler-cloud/prowler/pull/7778)

---

## [v5.7.0] (Prowler v5.7.0)

### Added
- Update the compliance list supported for each provider from docs [(#7694)](https://github.com/prowler-cloud/prowler/pull/7694)
- Allow setting cluster name in in-cluster mode in Kubernetes [(#7695)](https://github.com/prowler-cloud/prowler/pull/7695)
- Prowler ThreatScore for M365 provider [(#7692)](https://github.com/prowler-cloud/prowler/pull/7692)
- GitHub provider [(#5787)](https://github.com/prowler-cloud/prowler/pull/5787)
- `repository_default_branch_requires_multiple_approvals` check for GitHub provider [(#6160)](https://github.com/prowler-cloud/prowler/pull/6160)
- `repository_default_branch_protection_enabled` check for GitHub provider [(#6161)](https://github.com/prowler-cloud/prowler/pull/6161)
- `repository_default_branch_requires_linear_history` check for GitHub provider [(#6162)](https://github.com/prowler-cloud/prowler/pull/6162)
- `repository_default_branch_disallows_force_push` check for GitHub provider [(#6197)](https://github.com/prowler-cloud/prowler/pull/6197)
- `repository_default_branch_deletion_disabled` check for GitHub provider [(#6200)](https://github.com/prowler-cloud/prowler/pull/6200)
- `repository_default_branch_status_checks_required` check for GitHub provider [(#6204)](https://github.com/prowler-cloud/prowler/pull/6204)
- `repository_default_branch_protection_applies_to_admins` check for GitHub provider [(#6205)](https://github.com/prowler-cloud/prowler/pull/6205)
- `repository_branch_delete_on_merge_enabled` check for GitHub provider [(#6209)](https://github.com/prowler-cloud/prowler/pull/6209)
- `repository_default_branch_requires_conversation_resolution` check for GitHub provider [(#6208)](https://github.com/prowler-cloud/prowler/pull/6208)
- `organization_members_mfa_required` check for GitHub provider [(#6304)](https://github.com/prowler-cloud/prowler/pull/6304)
- GitHub provider documentation and CIS v1.0.0 compliance [(#6116)](https://github.com/prowler-cloud/prowler/pull/6116)
- CIS 5.0 compliance framework for AWS [(7766)](https://github.com/prowler-cloud/prowler/pull/7766)

### Fixed
- Update CIS 4.0 for M365 provider [(#7699)](https://github.com/prowler-cloud/prowler/pull/7699)
- Update and upgrade CIS for all the providers [(#7738)](https://github.com/prowler-cloud/prowler/pull/7738)
- Cover policies with conditions with SNS endpoint in `sns_topics_not_publicly_accessible` [(#7750)](https://github.com/prowler-cloud/prowler/pull/7750)
- Change severity logic for `ec2_securitygroup_allow_ingress_from_internet_to_all_ports` check [(#7764)](https://github.com/prowler-cloud/prowler/pull/7764)

---

## [v5.6.0] (Prowler v5.6.0)

### Added
- SOC2 compliance framework to Azure [(#7489)](https://github.com/prowler-cloud/prowler/pull/7489)
- Check for unused Service Accounts in GCP [(#7419)](https://github.com/prowler-cloud/prowler/pull/7419)
- Powershell to Microsoft365 [(#7331)](https://github.com/prowler-cloud/prowler/pull/7331)
- Service Defender to Microsoft365 with one check for Common Attachments filter enabled in Malware Policies [(#7425)](https://github.com/prowler-cloud/prowler/pull/7425)
- Check for Outbound Antispam Policy well configured in service Defender for M365 [(#7480)](https://github.com/prowler-cloud/prowler/pull/7480)
- Check for Antiphishing Policy well configured in service Defender in M365 [(#7453)](https://github.com/prowler-cloud/prowler/pull/7453)
- Check for Notifications for Internal users enabled in Malware Policies from service Defender in M365 [(#7435)](https://github.com/prowler-cloud/prowler/pull/7435)
- Support CLOUDSDK_AUTH_ACCESS_TOKEN in GCP [(#7495)](https://github.com/prowler-cloud/prowler/pull/7495)
- Service Exchange to Microsoft365 with one check for Organizations Mailbox Auditing enabled [(#7408)](https://github.com/prowler-cloud/prowler/pull/7408)
- Check for Bypass Disable in every Mailbox for service Defender in M365 [(#7418)](https://github.com/prowler-cloud/prowler/pull/7418)
- New check `teams_external_domains_restricted` [(#7557)](https://github.com/prowler-cloud/prowler/pull/7557)
- New check `teams_email_sending_to_channel_disabled` [(#7533)](https://github.com/prowler-cloud/prowler/pull/7533)
- New check for External Mails Tagged for service Exchange in M365 [(#7580)](https://github.com/prowler-cloud/prowler/pull/7580)
- New check for WhiteList not used in Transport Rules for service Defender in M365 [(#7569)](https://github.com/prowler-cloud/prowler/pull/7569)
- Check for Inbound Antispam Policy with no allowed domains from service Defender in M365 [(#7500)](https://github.com/prowler-cloud/prowler/pull/7500)
- New check `teams_meeting_anonymous_user_join_disabled` [(#7565)](https://github.com/prowler-cloud/prowler/pull/7565)
- New check `teams_unmanaged_communication_disabled` [(#7561)](https://github.com/prowler-cloud/prowler/pull/7561)
- New check `teams_external_users_cannot_start_conversations` [(#7562)](https://github.com/prowler-cloud/prowler/pull/7562)
- New check for AllowList not used in the Connection Filter Policy from service Defender in M365 [(#7492)](https://github.com/prowler-cloud/prowler/pull/7492)
- New check for SafeList not enabled in the Connection Filter Policy from service Defender in M365 [(#7492)](https://github.com/prowler-cloud/prowler/pull/7492)
- New check for DKIM enabled for service Defender in M365 [(#7485)](https://github.com/prowler-cloud/prowler/pull/7485)
- New check `teams_meeting_anonymous_user_start_disabled` [(#7567)](https://github.com/prowler-cloud/prowler/pull/7567)
- New check `teams_meeting_external_lobby_bypass_disabled` [(#7568)](https://github.com/prowler-cloud/prowler/pull/7568)
- New check `teams_meeting_dial_in_lobby_bypass_disabled` [(#7571)](https://github.com/prowler-cloud/prowler/pull/7571)
- New check `teams_meeting_external_control_disabled` [(#7604)](https://github.com/prowler-cloud/prowler/pull/7604)
- New check `teams_meeting_external_chat_disabled` [(#7605)](https://github.com/prowler-cloud/prowler/pull/7605)
- New check `teams_meeting_recording_disabled` [(#7607)](https://github.com/prowler-cloud/prowler/pull/7607)
- New check `teams_meeting_presenters_restricted` [(#7613)](https://github.com/prowler-cloud/prowler/pull/7613)
- New check `teams_security_reporting_enabled` [(#7614)](https://github.com/prowler-cloud/prowler/pull/7614)
- New check `defender_chat_report_policy_configured` [(#7614)](https://github.com/prowler-cloud/prowler/pull/7614)
- New check `teams_meeting_chat_anonymous_users_disabled` [(#7579)](https://github.com/prowler-cloud/prowler/pull/7579)
- Prowler Threat Score Compliance Framework [(#7603)](https://github.com/prowler-cloud/prowler/pull/7603)
- Documentation for M365 provider [(#7622)](https://github.com/prowler-cloud/prowler/pull/7622)
- Support for m365 provider in Prowler Dashboard [(#7633)](https://github.com/prowler-cloud/prowler/pull/7633)
- New check for Modern Authentication enabled for Exchange Online in M365 [(#7636)](https://github.com/prowler-cloud/prowler/pull/7636)
- New check `sharepoint_onedrive_sync_restricted_unmanaged_devices` [(#7589)](https://github.com/prowler-cloud/prowler/pull/7589)
- New check for Additional Storage restricted for Exchange in M365 [(#7638)](https://github.com/prowler-cloud/prowler/pull/7638)
- New check for Roles Assignment Policy with no AddIns for Exchange in M365 [(#7644)](https://github.com/prowler-cloud/prowler/pull/7644)
- New check for Auditing Mailbox on E3 users is enabled for Exchange in M365 [(#7642)](https://github.com/prowler-cloud/prowler/pull/7642)
- New check for SMTP Auth disabled for Exchange in M365 [(#7640)](https://github.com/prowler-cloud/prowler/pull/7640)
- New check for MailTips full enabled for Exchange in M365 [(#7637)](https://github.com/prowler-cloud/prowler/pull/7637)
- New check for Comprehensive Attachments Filter Applied for Defender in M365 [(#7661)](https://github.com/prowler-cloud/prowler/pull/7661)
- Modified check `exchange_mailbox_properties_auditing_enabled` to make it configurable [(#7662)](https://github.com/prowler-cloud/prowler/pull/7662)
- snapshots to m365 documentation [(#7673)](https://github.com/prowler-cloud/prowler/pull/7673)
- support for static credentials for sending findings to Amazon S3 and AWS Security Hub [(#7322)](https://github.com/prowler-cloud/prowler/pull/7322)
- Prowler ThreatScore for M365 provider [(#7692)](https://github.com/prowler-cloud/prowler/pull/7692)
- Microsoft User and User Credential auth to reports [(#7681)](https://github.com/prowler-cloud/prowler/pull/7681)

### Fixed
- Package name location in pyproject.toml while replicating for prowler-cloud [(#7531)](https://github.com/prowler-cloud/prowler/pull/7531)
- Remove cache in PyPI release action [(#7532)](https://github.com/prowler-cloud/prowler/pull/7532)
- The correct values for logger.info inside iam service [(#7526)](https://github.com/prowler-cloud/prowler/pull/7526)
- Update S3 bucket naming validation to accept dots [(#7545)](https://github.com/prowler-cloud/prowler/pull/7545)
- Handle new FlowLog model properties in Azure [(#7546)](https://github.com/prowler-cloud/prowler/pull/7546)
- Improve compliance and dashboard [(#7596)](https://github.com/prowler-cloud/prowler/pull/7596)
- Remove invalid parameter `create_file_descriptor` [(#7600)](https://github.com/prowler-cloud/prowler/pull/7600)
- Remove first empty line in HTML output [(#7606)](https://github.com/prowler-cloud/prowler/pull/7606)
- Remove empty files in Prowler [(#7627)](https://github.com/prowler-cloud/prowler/pull/7627)
- Ensure that ContentType in upload_file matches the uploaded file's format [(#7635)](https://github.com/prowler-cloud/prowler/pull/7635)
- Incorrect check inside 4.4.1 requirement for Azure CIS 2.0 [(#7656)](https://github.com/prowler-cloud/prowler/pull/7656)
- Remove muted findings on compliance page from Prowler Dashboard [(#7683)](https://github.com/prowler-cloud/prowler/pull/7683)
- Remove duplicated findings on compliance page from Prowler Dashboard [(#7686)](https://github.com/prowler-cloud/prowler/pull/7686)
- Incorrect values for Prowler Threatscore compliance LevelOfRisk inside requirements [(#7667)](https://github.com/prowler-cloud/prowler/pull/7667)

---

## [v5.5.1] (Prowler v5.5.1)

### Fixed
- Default name to contacts in Azure Defender [(#7483)](https://github.com/prowler-cloud/prowler/pull/7483)
- Handle projects without ID in GCP [(#7496)](https://github.com/prowler-cloud/prowler/pull/7496)
- Restore packages location in PyProject [(#7510)](https://github.com/prowler-cloud/prowler/pull/7510)

---
