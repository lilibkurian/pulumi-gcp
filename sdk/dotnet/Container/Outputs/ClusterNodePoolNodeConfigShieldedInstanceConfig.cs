// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Container.Outputs
{

    [OutputType]
    public sealed class ClusterNodePoolNodeConfigShieldedInstanceConfig
    {
        /// <summary>
        /// Defines if the instance has integrity monitoring enabled.
        /// </summary>
        public readonly bool? EnableIntegrityMonitoring;
        /// <summary>
        /// Defines if the instance has Secure Boot enabled.
        /// </summary>
        public readonly bool? EnableSecureBoot;

        [OutputConstructor]
        private ClusterNodePoolNodeConfigShieldedInstanceConfig(
            bool? enableIntegrityMonitoring,

            bool? enableSecureBoot)
        {
            EnableIntegrityMonitoring = enableIntegrityMonitoring;
            EnableSecureBoot = enableSecureBoot;
        }
    }
}