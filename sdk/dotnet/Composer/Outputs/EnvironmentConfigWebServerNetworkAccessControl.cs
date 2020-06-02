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
    public sealed class EnvironmentConfigWebServerNetworkAccessControl
    {
        /// <summary>
        /// -
        /// A collection of allowed IP ranges with descriptions. Structure is documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.EnvironmentConfigWebServerNetworkAccessControlAllowedIpRange> AllowedIpRanges;

        [OutputConstructor]
        private EnvironmentConfigWebServerNetworkAccessControl(ImmutableArray<Outputs.EnvironmentConfigWebServerNetworkAccessControlAllowedIpRange> allowedIpRanges)
        {
            AllowedIpRanges = allowedIpRanges;
        }
    }
}