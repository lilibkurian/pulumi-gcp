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
    public sealed class ClusterNodeConfigLinuxNodeConfig
    {
        /// <summary>
        /// The Linux kernel parameters to be applied to the nodes
        /// and all pods running on the nodes. Specified as a map from the key, such as
        /// `net.core.wmem_max`, to a string value.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Sysctls;

        [OutputConstructor]
        private ClusterNodeConfigLinuxNodeConfig(ImmutableDictionary<string, string> sysctls)
        {
            Sysctls = sysctls;
        }
    }
}
