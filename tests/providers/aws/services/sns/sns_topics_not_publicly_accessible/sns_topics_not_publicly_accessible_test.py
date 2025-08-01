from typing import Any, Dict
from unittest import mock
from uuid import uuid4

import pytest

from prowler.providers.aws.services.sns.sns_service import Topic
from tests.providers.aws.utils import AWS_ACCOUNT_NUMBER, AWS_REGION_EU_WEST_1

kms_key_id = str(uuid4())
topic_name = "test-topic"
org_id = "o-123456"
topic_arn = f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}"
test_policy_restricted = {
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": f"{AWS_ACCOUNT_NUMBER}"},
            "Action": ["sns:Publish"],
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
        }
    ]
}

test_policy_restricted_condition = {
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": ["sns:Publish"],
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
            "Condition": {"StringEquals": {"aws:SourceAccount": AWS_ACCOUNT_NUMBER}},
        }
    ]
}

test_policy_restricted_default_condition = {
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": ["sns:Publish"],
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
            "Condition": {"StringEquals": {"aws:SourceOwner": AWS_ACCOUNT_NUMBER}},
        }
    ]
}

test_policy_not_restricted = {
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": ["sns:Publish"],
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
        }
    ]
}

test_policy_restricted_principal_org_id = {
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": ["sns:Publish"],
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
            "Condition": {"StringEquals": {"aws:PrincipalOrgID": org_id}},
        }
    ]
}

test_policy_restricted_all_org = {
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": ["sns:Publish"],
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
            "Condition": {"StringEquals": {"aws:PrincipalOrgID": "*"}},
        }
    ]
}


test_policy_restricted_principal_account_organization = {
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": ["sns:Publish"],
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": org_id,
                    "aws:SourceAccount": AWS_ACCOUNT_NUMBER,
                }
            },
        }
    ]
}

test_policy_restricted_source_arn = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": "SNS:Publish",
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
            "Condition": {
                "ArnLike": {"aws:SourceArn": "arn:aws:s3:::test-bucket-name"}
            },
        }
    ],
}

test_policy_invalid_source_arn = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": "SNS:Publish",
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
            "Condition": {"ArnLike": {"aws:SourceArn": "invalid-arn-format"}},
        }
    ],
}

test_policy_unrestricted_source_arn_wildcard = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": "SNS:Publish",
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
            "Condition": {"ArnLike": {"aws:SourceArn": "*"}},
        }
    ],
}

test_policy_unrestricted_source_arn_service_wildcard = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": "SNS:Publish",
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
            "Condition": {"ArnLike": {"aws:SourceArn": "arn:aws:s3:::*"}},
        }
    ],
}

test_policy_unrestricted_source_arn_multi_wildcard = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": "SNS:Publish",
            "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
            "Condition": {"ArnLike": {"aws:SourceArn": "arn:aws:*:*:*:*"}},
        }
    ],
}


def generate_policy_restricted_on_sns_endpoint(endpoint: str) -> Dict[str, Any]:
    return {
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": ["sns:Publish"],
                "Resource": f"arn:aws:sns:{AWS_REGION_EU_WEST_1}:{AWS_ACCOUNT_NUMBER}:{topic_name}",
                "Condition": {"StringEquals": {"SNS:Endpoint": endpoint}},
            }
        ]
    }


class Test_sns_topics_not_publicly_accessible:
    def test_no_topics(self):
        sns_client = mock.MagicMock
        sns_client.topics = []
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 0

    def test_topic_not_public(self):
        sns_client = mock.MagicMock
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=test_policy_restricted,
                region=AWS_REGION_EU_WEST_1,
            )
        )

        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is not publicly accessible."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_no_policy(self):
        sns_client = mock.MagicMock
        sns_client.topics = []
        sns_client.topics.append(
            Topic(arn=topic_arn, name=topic_name, region=AWS_REGION_EU_WEST_1)
        )

        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is not publicly accessible."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_public_with_condition(self):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=test_policy_restricted_condition,
                region=AWS_REGION_EU_WEST_1,
            )
        )
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is not public because its policy only allows access from the account {AWS_ACCOUNT_NUMBER}."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_public_with_default_condition(self):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=test_policy_restricted_default_condition,
                region=AWS_REGION_EU_WEST_1,
            )
        )
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is not public because its policy only allows access from the account {AWS_ACCOUNT_NUMBER}."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_public(self):
        sns_client = mock.MagicMock
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                region=AWS_REGION_EU_WEST_1,
                policy=test_policy_not_restricted,
            )
        )
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is public because its policy allows public access."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_public_with_principal_organization(self):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=test_policy_restricted_principal_org_id,
                region=AWS_REGION_EU_WEST_1,
            )
        )
        sns_client.provider = mock.MagicMock()
        sns_client.provider.organizations_metadata = mock.MagicMock()
        sns_client.provider.organizations_metadata.organization_id = org_id
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is not public because its policy only allows access from an organization."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_public_not_with_principal_organization(self):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=test_policy_restricted_all_org,
                region=AWS_REGION_EU_WEST_1,
            )
        )
        sns_client.provider = mock.MagicMock()
        sns_client.provider.organizations_metadata = mock.MagicMock()
        sns_client.provider.organizations_metadata.organization_id = org_id
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is public because its policy allows public access."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_public_with_principal_account_and_organization(self):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=test_policy_restricted_principal_account_organization,
                region=AWS_REGION_EU_WEST_1,
            )
        )
        sns_client.provider = mock.MagicMock()
        sns_client.provider.organizations_metadata = mock.MagicMock()
        sns_client.provider.organizations_metadata.organization_id = org_id
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is not public because its policy only allows access from the account {AWS_ACCOUNT_NUMBER} and an organization."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_public_with_source_arn_restriction(self):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=test_policy_restricted_source_arn,
                region=AWS_REGION_EU_WEST_1,
            )
        )
        sns_client.provider = mock.MagicMock()
        sns_client.provider.organizations_metadata = mock.MagicMock()
        sns_client.provider.organizations_metadata.organization_id = org_id
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is not publicly accessible."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_public_with_invalid_source_arn(self):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=test_policy_invalid_source_arn,
                region=AWS_REGION_EU_WEST_1,
            )
        )
        sns_client.provider = mock.MagicMock()
        sns_client.provider.organizations_metadata = mock.MagicMock()
        sns_client.provider.organizations_metadata.organization_id = org_id
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is not publicly accessible."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    @pytest.mark.parametrize(
        "endpoint",
        [
            ("*@example.com"),
            ("user@example.com"),
            ("https://events.pagerduty.com/integration/987654321/enqueue"),
            (
                "arn:aws:sns:eu-west-2:123456789012:example-topic:995be20c-a7e3-44ca-8c18-77cb263d15e7"
            ),
        ],
    )
    def test_topic_public_with_sns_endpoint(self, endpoint: str):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=generate_policy_restricted_on_sns_endpoint(endpoint=endpoint),
                region=AWS_REGION_EU_WEST_1,
            )
        )
        sns_client.provider = mock.MagicMock()
        sns_client.provider.organizations_metadata = mock.MagicMock()
        sns_client.provider.organizations_metadata.organization_id = org_id
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is not public because its policy only allows access from an endpoint."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_public_with_unrestricted_source_arn_wildcard(self):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=test_policy_unrestricted_source_arn_wildcard,
                region=AWS_REGION_EU_WEST_1,
            )
        )
        sns_client.provider = mock.MagicMock()
        sns_client.provider.organizations_metadata = mock.MagicMock()
        sns_client.provider.organizations_metadata.organization_id = org_id
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is public because its policy allows public access."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_public_with_unrestricted_source_arn_service_wildcard(self):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=test_policy_unrestricted_source_arn_service_wildcard,
                region=AWS_REGION_EU_WEST_1,
            )
        )
        sns_client.provider = mock.MagicMock()
        sns_client.provider.organizations_metadata = mock.MagicMock()
        sns_client.provider.organizations_metadata.organization_id = org_id
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is public because its policy allows public access."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    def test_topic_public_with_unrestricted_source_arn_multi_wildcard(self):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=test_policy_unrestricted_source_arn_multi_wildcard,
                region=AWS_REGION_EU_WEST_1,
            )
        )
        sns_client.provider = mock.MagicMock()
        sns_client.provider.organizations_metadata = mock.MagicMock()
        sns_client.provider.organizations_metadata.organization_id = org_id
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is public because its policy allows public access."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []

    @pytest.mark.parametrize(
        "endpoint",
        [
            ("*@*"),
            ("https://events.pagerduty.com/integration/*/enqueue"),
            ("arn:aws:sns:eu-west-2:*:example-topic:*"),
        ],
    )
    def test_topic_public_with_unrestricted_sns_endpoint(self, endpoint: str):
        sns_client = mock.MagicMock
        sns_client.audited_account = AWS_ACCOUNT_NUMBER
        sns_client.topics = []
        sns_client.topics.append(
            Topic(
                arn=topic_arn,
                name=topic_name,
                policy=generate_policy_restricted_on_sns_endpoint(endpoint=endpoint),
                region=AWS_REGION_EU_WEST_1,
            )
        )
        sns_client.provider = mock.MagicMock()
        sns_client.provider.organizations_metadata = mock.MagicMock()
        sns_client.provider.organizations_metadata.organization_id = org_id
        with mock.patch(
            "prowler.providers.aws.services.sns.sns_service.SNS",
            sns_client,
        ):
            from prowler.providers.aws.services.sns.sns_topics_not_publicly_accessible.sns_topics_not_publicly_accessible import (
                sns_topics_not_publicly_accessible,
            )

            check = sns_topics_not_publicly_accessible()
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"SNS topic {topic_name} is public because its policy allows public access."
            )
            assert result[0].resource_id == topic_name
            assert result[0].resource_arn == topic_arn
            assert result[0].region == AWS_REGION_EU_WEST_1
            assert result[0].resource_tags == []
