from argparse import Namespace
from unittest.mock import MagicMock, patch

from kubernetes.config.config_exception import ConfigException

from kubernetes import client
from prowler.config.config import (
    default_config_file_path,
    default_fixer_config_file_path,
    load_and_validate_config_file,
)
from prowler.providers.kubernetes.exceptions.exceptions import (
    KubernetesSetUpSessionError,
)
from prowler.providers.kubernetes.kubernetes_provider import KubernetesProvider
from prowler.providers.kubernetes.models import (
    KubernetesIdentityInfo,
    KubernetesSession,
)
from tests.providers.kubernetes.kubernetes_fixtures import KUBERNETES_CONFIG


def mock_set_kubernetes_credentials(*_):
    return ("apiclient", "context")


def mock_get_context_user_roles(*_):
    return []


class TestKubernetesProvider:
    def test_kubernetes_provider_no_namespaces(
        self,
    ):
        context = {
            "name": "test-context",
            "context": {
                "user": "test-user",
                "cluster": "test-cluster",
            },
        }
        with (
            patch(
                "prowler.providers.kubernetes.kubernetes_provider.KubernetesProvider.setup_session",
                return_value=KubernetesSession(
                    api_client=client.ApiClient,
                    context=context,
                ),
            ),
            patch(
                "prowler.providers.kubernetes.kubernetes_provider.KubernetesProvider.get_all_namespaces",
                return_value=["namespace-1"],
            ),
        ):
            arguments = Namespace()
            arguments.kubeconfig_file = "dummy_path"
            arguments.context = None
            arguments.only_logs = False
            arguments.namespace = None
            fixer_config = load_and_validate_config_file(
                "kubernetes", default_fixer_config_file_path
            )

            # Instantiate the KubernetesProvider with mocked arguments
            kubernetes_provider = KubernetesProvider(
                arguments.kubeconfig_file,
                arguments.context,
                arguments.namespace,
                config_path=default_config_file_path,
                fixer_config=fixer_config,
            )
            assert isinstance(kubernetes_provider.session, KubernetesSession)
            assert kubernetes_provider.session.api_client is not None
            assert kubernetes_provider.session.context == {
                "name": "test-context",
                "context": {"cluster": "test-cluster", "user": "test-user"},
            }
            assert kubernetes_provider.namespaces == ["namespace-1"]
            assert isinstance(kubernetes_provider.identity, KubernetesIdentityInfo)
            assert kubernetes_provider.identity.context == "test-context"
            assert kubernetes_provider.identity.cluster == "test-cluster"
            assert kubernetes_provider.identity.user == "test-user"

            assert kubernetes_provider.audit_config == KUBERNETES_CONFIG

    @patch(
        "prowler.providers.kubernetes.kubernetes_provider.client.CoreV1Api.list_namespace"
    )
    @patch("kubernetes.config.list_kube_config_contexts")
    @patch("kubernetes.config.load_kube_config_from_dict")
    def test_kubernetes_test_connection_with_kubeconfig_content(
        self,
        mock_load_kube_config_from_dict,
        mock_list_kube_config_contexts,
        mock_list_namespace,
    ):
        mock_load_kube_config_from_dict.return_value = None
        mock_list_kube_config_contexts.return_value = (
            [
                {
                    "name": "example-context",
                    "context": {
                        "cluster": "example-cluster",
                        "user": "example-user",
                    },
                }
            ],
            None,
        )
        mock_list_namespace.return_value.items = [
            client.V1Namespace(metadata=client.V1ObjectMeta(name="namespace-1")),
        ]

        kubeconfig_content = '{"apiVersion": "v1", "clusters": [{"cluster": {"server": "https://kubernetes.example.com"}, "name": "example-cluster"}], "contexts": [{"context": {"cluster": "example-cluster", "user": "example-user"}, "name": "example-context"}], "current-context": "example-context", "kind": "Config", "preferences": {}, "users": [{"name": "example-user", "user": {"token": "EXAMPLE_TOKEN"}}]}'

        connection = KubernetesProvider.test_connection(
            kubeconfig_file=None,
            kubeconfig_content=kubeconfig_content,
            provider_id="example-context",
            raise_on_exception=False,
        )

        assert connection.is_connected
        assert connection.error is None

    @patch(
        "prowler.providers.kubernetes.kubernetes_provider.client.CoreV1Api.list_namespace"
    )
    @patch("kubernetes.config.list_kube_config_contexts")
    @patch("kubernetes.config.load_kube_config")
    def test_kubernetes_test_connection_with_kubeconfig_file(
        self, mock_load_kube_config, mock_list_kube_config_contexts, mock_list_namespace
    ):
        mock_load_kube_config.return_value = None
        mock_list_kube_config_contexts.return_value = (
            [
                {
                    "name": "test-context",
                    "context": {
                        "cluster": "test-cluster",
                        "user": "test-user",
                    },
                }
            ],
            None,
        )
        mock_list_namespace.return_value.items = [
            client.V1Namespace(metadata=client.V1ObjectMeta(name="namespace-1")),
        ]

        connection = KubernetesProvider.test_connection(
            kubeconfig_file="dummy_kubeconfig_path",
            kubeconfig_content="",
            provider_id="test-context",
            raise_on_exception=False,
        )

        assert connection.is_connected
        assert connection.error is None

    @patch(
        "prowler.providers.kubernetes.kubernetes_provider.client.CoreV1Api.list_namespaced_pod"
    )
    @patch("kubernetes.config.list_kube_config_contexts")
    @patch("kubernetes.config.load_kube_config")
    def test_kubernetes_test_connection_with_namespace_input(
        self,
        mock_load_kube_config,
        mock_list_kube_config_contexts,
        mock_list_namespaced_pod,
    ):
        mock_load_kube_config.return_value = None
        mock_list_kube_config_contexts.return_value = (
            [
                {
                    "name": "test-context",
                    "context": {
                        "cluster": "test-cluster",
                        "user": "test-user",
                    },
                }
            ],
            None,
        )
        mock_list_namespaced_pod.return_value.items = [
            client.V1Pod(metadata=client.V1ObjectMeta(name="pod-1")),
        ]

        connection = KubernetesProvider.test_connection(
            kubeconfig_file="",
            kubeconfig_content="",
            namespace="test-namespace",
            provider_id="test-context",
            raise_on_exception=False,
        )

        assert connection.is_connected
        assert connection.error is None

    @patch(
        "prowler.providers.kubernetes.kubernetes_provider.client.CoreV1Api.list_namespace"
    )
    @patch("kubernetes.config.list_kube_config_contexts")
    @patch("kubernetes.config.load_kube_config_from_dict")
    def test_kubernetes_test_connection_with_kubeconfig_content_invalid_provider_id(
        self,
        mock_load_kube_config_from_dict,
        mock_list_kube_config_contexts,
        mock_list_namespace,
    ):
        mock_load_kube_config_from_dict.return_value = None
        mock_list_kube_config_contexts.return_value = (
            [
                {
                    "name": "example-context",
                    "context": {
                        "cluster": "example-cluster",
                        "user": "example-user",
                    },
                }
            ],
            None,
        )
        mock_list_namespace.return_value.items = [
            client.V1Namespace(metadata=client.V1ObjectMeta(name="namespace-1")),
        ]

        kubeconfig_content = {
            "apiVersion": "v1",
            "clusters": [
                {
                    "cluster": {
                        "server": "https://kubernetes.example.com",
                    },
                    "name": "example-cluster",
                }
            ],
            "contexts": [
                {
                    "context": {
                        "cluster": "example-cluster",
                        "user": "example-user",
                    },
                    "name": "example-context",
                }
            ],
            "current-context": "example-context",
            "kind": "Config",
            "preferences": {},
            "users": [
                {
                    "name": "example-user",
                    "user": {
                        "token": "EXAMPLE_TOKEN",
                    },
                }
            ],
        }

        connection = KubernetesProvider.test_connection(
            kubeconfig_file=None,
            kubeconfig_content=kubeconfig_content,
            provider_id="example-context-invalid",
            raise_on_exception=False,
        )

        assert not connection.is_connected
        assert connection.error is not None
        assert isinstance(connection.error, KubernetesSetUpSessionError)

    @patch(
        "prowler.providers.kubernetes.kubernetes_provider.client.CoreV1Api.list_namespace"
    )
    @patch("kubernetes.config.list_kube_config_contexts")
    @patch("kubernetes.config.load_kube_config_from_dict")
    def test_kubernetes_test_connection_with_kubeconfig_content_valid_provider_id(
        self,
        mock_load_kube_config_from_dict,
        mock_list_kube_config_contexts,
        mock_list_namespace,
    ):
        mock_load_kube_config_from_dict.return_value = None
        mock_list_kube_config_contexts.return_value = (
            [
                {
                    "name": "example-context",
                    "context": {
                        "cluster": "example-cluster",
                        "user": "example-user",
                    },
                }
            ],
            None,
        )
        mock_list_namespace.return_value.items = [
            client.V1Namespace(metadata=client.V1ObjectMeta(name="namespace-1")),
        ]

        kubeconfig_content = '{"apiVersion": "v1", "clusters": [{"cluster": {"server": "https://kubernetes.example.com"}, "name": "example-cluster"}], "contexts": [{"context": {"cluster": "example-cluster", "user": "example-user"}, "name": "example-context"}], "current-context": "example-context", "kind": "Config", "preferences": {}, "users": [{"name": "example-user", "user": {"token": "EXAMPLE_TOKEN"}}]}'

        connection = KubernetesProvider.test_connection(
            kubeconfig_file=None,
            kubeconfig_content=kubeconfig_content,
            provider_id="example-context",
            raise_on_exception=False,
        )

        assert connection.is_connected
        assert connection.error is None

    def test_kubernetes_provider_incluster_with_env_var(self, monkeypatch):
        monkeypatch.setenv("CLUSTER_NAME", "env-cluster-name")

        with (
            patch(
                "kubernetes.config.load_kube_config",
                side_effect=ConfigException("No kubeconfig"),
            ),
            patch("kubernetes.config.load_incluster_config", return_value=None),
            patch("prowler.providers.kubernetes.kubernetes_provider.client.ApiClient"),
            patch(
                "prowler.providers.kubernetes.kubernetes_provider.KubernetesProvider.get_all_namespaces",
                return_value=["default"],
            ),
        ):
            session = KubernetesProvider.setup_session(
                kubeconfig_file=None,
                kubeconfig_content=None,
                context=None,
                cluster_name=None,
            )
            assert isinstance(session, KubernetesSession)
            assert session.context["context"]["cluster"] == "env-cluster-name"

    def test_kubernetes_provider_incluster_with_cli_flag(self):
        with (
            patch(
                "kubernetes.config.load_kube_config",
                side_effect=ConfigException("No kubeconfig"),
            ),
            patch("kubernetes.config.load_incluster_config", return_value=None),
            patch("prowler.providers.kubernetes.kubernetes_provider.client.ApiClient"),
            patch(
                "prowler.providers.kubernetes.kubernetes_provider.KubernetesProvider.get_all_namespaces",
                return_value=["default"],
            ),
        ):
            session = KubernetesProvider.setup_session(
                kubeconfig_file=None,
                kubeconfig_content=None,
                context=None,
                cluster_name="cli-cluster-name",
            )
            assert isinstance(session, KubernetesSession)
            assert session.context["context"]["cluster"] == "cli-cluster-name"

    def test_kubernetes_provider_proxy_from_env(self, monkeypatch):
        monkeypatch.setenv("HTTPS_PROXY", "http://my.internal.proxy:8888")

        captured = {}

        def fake_api_client(configuration):
            captured["proxy"] = getattr(configuration, "proxy", None)
            return MagicMock()

        with (
            patch(
                "kubernetes.config.load_kube_config",
                side_effect=ConfigException("No kubeconfig"),
            ),
            patch("kubernetes.config.load_incluster_config", return_value=None),
            patch(
                "prowler.providers.kubernetes.kubernetes_provider.ApiClient",
                side_effect=fake_api_client,
            ),
            patch(
                "prowler.providers.kubernetes.kubernetes_provider.KubernetesProvider.get_all_namespaces",
                return_value=["default"],
            ),
        ):
            KubernetesProvider.setup_session()

        assert captured["proxy"] == "http://my.internal.proxy:8888"

    def test_kubernetes_provider_disable_tls_verification(self, monkeypatch):
        monkeypatch.setenv("K8S_SKIP_TLS_VERIFY", "true")

        captured = {}

        def fake_api_client(configuration):
            captured["verify_ssl"] = getattr(configuration, "verify_ssl", True)
            return MagicMock()

        with (
            patch(
                "kubernetes.config.load_kube_config",
                side_effect=ConfigException("No kubeconfig"),
            ),
            patch("kubernetes.config.load_incluster_config", return_value=None),
            patch(
                "prowler.providers.kubernetes.kubernetes_provider.ApiClient",
                side_effect=fake_api_client,
            ),
            patch(
                "prowler.providers.kubernetes.kubernetes_provider.KubernetesProvider.get_all_namespaces",
                return_value=["default"],
            ),
        ):
            KubernetesProvider.setup_session()

        assert captured["verify_ssl"] is False
