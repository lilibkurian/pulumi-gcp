// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class SecurityPolicyRuleMatchConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("srcIpRanges", required: true)]
        private InputList<string>? _srcIpRanges;

        /// <summary>
        /// Set of IP addresses or ranges (IPV4 or IPV6) in CIDR notation
        /// to match against inbound traffic. There is a limit of 10 IP ranges per rule. A value of '\*' matches all IPs
        /// (can be used to override the default behavior).
        /// </summary>
        public InputList<string> SrcIpRanges
        {
            get => _srcIpRanges ?? (_srcIpRanges = new InputList<string>());
            set => _srcIpRanges = value;
        }

        public SecurityPolicyRuleMatchConfigGetArgs()
        {
        }
    }
}
