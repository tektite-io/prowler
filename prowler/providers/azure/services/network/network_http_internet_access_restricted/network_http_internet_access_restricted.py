from prowler.lib.check.models import Check, Check_Report_Azure
from prowler.providers.azure.services.network.network_client import network_client


class network_http_internet_access_restricted(Check):
    def execute(self) -> Check_Report_Azure:
        findings = []
        for subscription, security_groups in network_client.security_groups.items():
            for security_group in security_groups:
                report = Check_Report_Azure(
                    metadata=self.metadata(), resource=security_group
                )
                report.subscription = subscription
                report.status = "PASS"
                report.status_extended = f"Security Group {security_group.name} from subscription {subscription} has HTTP internet access restricted."
                rule_fail_condition = any(
                    (
                        rule.destination_port_range == "80"
                        or (
                            (
                                rule.destination_port_range
                                and "-" in rule.destination_port_range
                            )
                            and int(rule.destination_port_range.split("-")[0]) <= 80
                            and int(rule.destination_port_range.split("-")[1]) >= 80
                        )
                    )
                    and rule.protocol in ["TCP", "Tcp", "*"]
                    and rule.source_address_prefix in ["Internet", "*", "0.0.0.0/0"]
                    and rule.access == "Allow"
                    and rule.direction == "Inbound"
                    for rule in security_group.security_rules
                )
                if rule_fail_condition:
                    report.status = "FAIL"
                    report.status_extended = f"Security Group {security_group.name} from subscription {subscription} has HTTP internet access allowed."
                findings.append(report)

        return findings
