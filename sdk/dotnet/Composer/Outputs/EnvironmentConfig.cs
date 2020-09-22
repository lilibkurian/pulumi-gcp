// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Composer.Outputs
{

    [OutputType]
    public sealed class EnvironmentConfig
    {
        public readonly string? AirflowUri;
        public readonly string? DagGcsPrefix;
        /// <summary>
        /// The configuration settings for Cloud SQL instance used internally by Apache Airflow software.
        /// </summary>
        public readonly Outputs.EnvironmentConfigDatabaseConfig? DatabaseConfig;
        public readonly string? GkeCluster;
        /// <summary>
        /// The configuration used for the Kubernetes Engine cluster.  Structure is documented below.
        /// </summary>
        public readonly Outputs.EnvironmentConfigNodeConfig? NodeConfig;
        /// <summary>
        /// The number of nodes in the Kubernetes Engine cluster that
        /// will be used to run this environment.
        /// </summary>
        public readonly int? NodeCount;
        /// <summary>
        /// The configuration used for the Private IP Cloud Composer environment. Structure is documented below.
        /// </summary>
        public readonly Outputs.EnvironmentConfigPrivateEnvironmentConfig? PrivateEnvironmentConfig;
        /// <summary>
        /// The configuration settings for software inside the environment.  Structure is documented below.
        /// </summary>
        public readonly Outputs.EnvironmentConfigSoftwareConfig? SoftwareConfig;
        /// <summary>
        /// The configuration settings for the Airflow web server App Engine instance.
        /// </summary>
        public readonly Outputs.EnvironmentConfigWebServerConfig? WebServerConfig;
        /// <summary>
        /// The network-level access control policy for the Airflow web server. If unspecified, no network-level access restrictions will be applied.
        /// </summary>
        public readonly Outputs.EnvironmentConfigWebServerNetworkAccessControl? WebServerNetworkAccessControl;

        [OutputConstructor]
        private EnvironmentConfig(
            string? airflowUri,

            string? dagGcsPrefix,

            Outputs.EnvironmentConfigDatabaseConfig? databaseConfig,

            string? gkeCluster,

            Outputs.EnvironmentConfigNodeConfig? nodeConfig,

            int? nodeCount,

            Outputs.EnvironmentConfigPrivateEnvironmentConfig? privateEnvironmentConfig,

            Outputs.EnvironmentConfigSoftwareConfig? softwareConfig,

            Outputs.EnvironmentConfigWebServerConfig? webServerConfig,

            Outputs.EnvironmentConfigWebServerNetworkAccessControl? webServerNetworkAccessControl)
        {
            AirflowUri = airflowUri;
            DagGcsPrefix = dagGcsPrefix;
            DatabaseConfig = databaseConfig;
            GkeCluster = gkeCluster;
            NodeConfig = nodeConfig;
            NodeCount = nodeCount;
            PrivateEnvironmentConfig = privateEnvironmentConfig;
            SoftwareConfig = softwareConfig;
            WebServerConfig = webServerConfig;
            WebServerNetworkAccessControl = webServerNetworkAccessControl;
        }
    }
}
