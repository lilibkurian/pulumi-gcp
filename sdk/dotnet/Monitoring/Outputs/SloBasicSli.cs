// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Outputs
{

    [OutputType]
    public sealed class SloBasicSli
    {
        public readonly Outputs.SloBasicSliLatency Latency;
        public readonly ImmutableArray<string> Locations;
        public readonly ImmutableArray<string> Methods;
        public readonly ImmutableArray<string> Versions;

        [OutputConstructor]
        private SloBasicSli(
            Outputs.SloBasicSliLatency latency,

            ImmutableArray<string> locations,

            ImmutableArray<string> methods,

            ImmutableArray<string> versions)
        {
            Latency = latency;
            Locations = locations;
            Methods = methods;
            Versions = versions;
        }
    }
}
