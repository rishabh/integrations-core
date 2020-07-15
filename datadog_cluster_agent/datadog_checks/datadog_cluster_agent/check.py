# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.base import OpenMetricsBaseCheck


class DatadogClusterAgentCheck(OpenMetricsBaseCheck):
    """
    Collect Cluster Agent metrics from its Prometheus endpoint
    """

    def __init__(self, name, init_config, instances):
        default_namespace = 'datadog.cluster_agent'
        default_instances = {
            'datadog.cluster_agent': {
                'namespace': default_namespace,
                'metrics': [
                    'aggregator.flush',
                    'aggregator.processed',
                    'api_requests',
                    'checks.events',
                    'checks.execution_time',
                    'checks.metrics_samples',
                    'checks.runs',
                    'checks.services_checks',
                    'checks.warnings',
                    'cluster_checks_busyness',
                    'datadog_requests',
                    'external_metrics',
                    'forwarder.transactions',
                    'leader_election_is_leader',
                    'metrics.event_split',
                    'rate_limit_queries_limit',
                    'rate_limit_queries_reset',
                    'running',
                    'scheduler.checks_entered',
                    'scheduler.queues_count',
                    'splitter.not_too_big',
                    'splitter.too_big',
                    'splitter.total_loops',
                    'started',
                    'transactions.dropped',
                    'transactions.errors',
                    'transactions.http_errors',
                    'transactions.requeud',
                    'transactions.retries',
                    'transactions.success',
                ],
                # 'label_joins': {
                #     'leader_election_is_leader': {'labels_to_match': ['join_leader'], 'labels_to_get': ['is_leader']}
                # }
            },
        }

        super(DatadogClusterAgentCheck, self).__init__(
            name, init_config, instances, default_namespace=default_namespace, default_instances=default_instances
        )
