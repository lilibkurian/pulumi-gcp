// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Container.Inputs
{

    public sealed class ClusterNodeConfigLinuxNodeConfigArgs : Pulumi.ResourceArgs
    {
        [Input("sysctls", required: true)]
        private InputMap<string>? _sysctls;

        /// <summary>
        /// The Linux kernel parameters to be applied to the nodes
        /// and all pods running on the nodes. Specified as a map from the key, such as
        /// `net.core.wmem_max`, to a string value.
        /// </summary>
        public InputMap<string> Sysctls
        {
            get => _sysctls ?? (_sysctls = new InputMap<string>());
            set => _sysctls = value;
        }

        public ClusterNodeConfigLinuxNodeConfigArgs()
        {
        }
    }
}
