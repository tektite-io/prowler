from prowler.lib.check.models import Check, Check_Report_AWS
from prowler.providers.aws.services.apigatewayv2.apigatewayv2_client import (
    apigatewayv2_client,
)


class apigatewayv2_api_access_logging_enabled(Check):
    def execute(self):
        findings = []
        for api in apigatewayv2_client.apis:
            report = Check_Report_AWS(metadata=self.metadata(), resource=api)
            for stage in api.stages:
                if stage.logging:
                    report.status = "PASS"
                    report.status_extended = f"API Gateway V2 {api.name} ID {api.id} in stage {stage.name} has access logging enabled."
                    report.resource_id = f"{api.name}-{stage.name}"
                else:
                    report.status = "FAIL"
                    report.status_extended = f"API Gateway V2 {api.name} ID {api.id} in stage {stage.name} has access logging disabled."
                    report.resource_id = f"{api.name}-{stage.name}"

                findings.append(report)

        return findings
