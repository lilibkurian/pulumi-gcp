// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Dataproc.Outputs
{

    [OutputType]
    public sealed class ClusterClusterConfig
    {
        /// <summary>
        /// The autoscaling policy config associated with the cluster.
        /// Note that once set, if `autoscaling_config` is the only field set in `cluster_config`, it can
        /// only be removed by setting `policy_uri = ""`, rather than removing the whole block.
        /// Structure defined below.
        /// </summary>
        public readonly Outputs.ClusterClusterConfigAutoscalingConfig? AutoscalingConfig;
        public readonly string? Bucket;
        /// <summary>
        /// The Customer managed encryption keys settings for the cluster.
        /// Structure defined below.
        /// </summary>
        public readonly Outputs.ClusterClusterConfigEncryptionConfig? EncryptionConfig;
        /// <summary>
        /// The config settings for port access on the cluster.
        /// Structure defined below.
        /// - - -
        /// </summary>
        public readonly Outputs.ClusterClusterConfigEndpointConfig? EndpointConfig;
        /// <summary>
        /// Common config settings for resources of Google Compute Engine cluster
        /// instances, applicable to all instances in the cluster. Structure defined below.
        /// </summary>
        public readonly Outputs.ClusterClusterConfigGceClusterConfig? GceClusterConfig;
        /// <summary>
        /// Commands to execute on each node after config is completed.
        /// You can specify multiple versions of these. Structure defined below.
        /// </summary>
        public readonly ImmutableArray<Outputs.ClusterClusterConfigInitializationAction> InitializationActions;
        /// <summary>
        /// The settings for auto deletion cluster schedule.
        /// Structure defined below.
        /// </summary>
        public readonly Outputs.ClusterClusterConfigLifecycleConfig? LifecycleConfig;
        /// <summary>
        /// The Google Compute Engine config settings for the master instances
        /// in a cluster.. Structure defined below.
        /// </summary>
        public readonly Outputs.ClusterClusterConfigMasterConfig? MasterConfig;
        /// <summary>
        /// The Google Compute Engine config settings for the additional (aka
        /// preemptible) instances in a cluster. Structure defined below.
        /// </summary>
        public readonly Outputs.ClusterClusterConfigPreemptibleWorkerConfig? PreemptibleWorkerConfig;
        /// <summary>
        /// Security related configuration. Structure defined below.
        /// </summary>
        public readonly Outputs.ClusterClusterConfigSecurityConfig? SecurityConfig;
        /// <summary>
        /// The config settings for software inside the cluster.
        /// Structure defined below.
        /// </summary>
        public readonly Outputs.ClusterClusterConfigSoftwareConfig? SoftwareConfig;
        /// <summary>
        /// The Cloud Storage staging bucket used to stage files,
        /// such as Hadoop jars, between client machines and the cluster.
        /// Note: If you don't explicitly specify a `staging_bucket`
        /// then GCP will auto create / assign one for you. However, you are not guaranteed
        /// an auto generated bucket which is solely dedicated to your cluster; it may be shared
        /// with other clusters in the same region/zone also choosing to use the auto generation
        /// option.
        /// </summary>
        public readonly string? StagingBucket;
        /// <summary>
        /// The Google Compute Engine config settings for the worker instances
        /// in a cluster.. Structure defined below.
        /// </summary>
        public readonly Outputs.ClusterClusterConfigWorkerConfig? WorkerConfig;

        [OutputConstructor]
        private ClusterClusterConfig(
            Outputs.ClusterClusterConfigAutoscalingConfig? autoscalingConfig,

            string? bucket,

            Outputs.ClusterClusterConfigEncryptionConfig? encryptionConfig,

            Outputs.ClusterClusterConfigEndpointConfig? endpointConfig,

            Outputs.ClusterClusterConfigGceClusterConfig? gceClusterConfig,

            ImmutableArray<Outputs.ClusterClusterConfigInitializationAction> initializationActions,

            Outputs.ClusterClusterConfigLifecycleConfig? lifecycleConfig,

            Outputs.ClusterClusterConfigMasterConfig? masterConfig,

            Outputs.ClusterClusterConfigPreemptibleWorkerConfig? preemptibleWorkerConfig,

            Outputs.ClusterClusterConfigSecurityConfig? securityConfig,

            Outputs.ClusterClusterConfigSoftwareConfig? softwareConfig,

            string? stagingBucket,

            Outputs.ClusterClusterConfigWorkerConfig? workerConfig)
        {
            AutoscalingConfig = autoscalingConfig;
            Bucket = bucket;
            EncryptionConfig = encryptionConfig;
            EndpointConfig = endpointConfig;
            GceClusterConfig = gceClusterConfig;
            InitializationActions = initializationActions;
            LifecycleConfig = lifecycleConfig;
            MasterConfig = masterConfig;
            PreemptibleWorkerConfig = preemptibleWorkerConfig;
            SecurityConfig = securityConfig;
            SoftwareConfig = softwareConfig;
            StagingBucket = stagingBucket;
            WorkerConfig = workerConfig;
        }
    }
}
