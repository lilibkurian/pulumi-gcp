// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.AppEngine.Outputs
{

    [OutputType]
    public sealed class FlexibleAppVersionAutomaticScaling
    {
        /// <summary>
        /// The time period that the Autoscaler should wait before it starts collecting information from a new instance.
        /// This prevents the autoscaler from collecting information when the instance is initializing,
        /// during which the collected usage would not be reliable. Default: 120s
        /// </summary>
        public readonly string? CoolDownPeriod;
        /// <summary>
        /// Target scaling by CPU usage.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.FlexibleAppVersionAutomaticScalingCpuUtilization CpuUtilization;
        /// <summary>
        /// Target scaling by disk usage.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.FlexibleAppVersionAutomaticScalingDiskUtilization? DiskUtilization;
        /// <summary>
        /// Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance.
        /// Defaults to a runtime-specific value.
        /// </summary>
        public readonly int? MaxConcurrentRequests;
        /// <summary>
        /// Maximum number of idle instances that should be maintained for this version.
        /// </summary>
        public readonly int? MaxIdleInstances;
        /// <summary>
        /// Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it.
        /// </summary>
        public readonly string? MaxPendingLatency;
        /// <summary>
        /// Maximum number of instances that should be started to handle requests for this version. Default: 20
        /// </summary>
        public readonly int? MaxTotalInstances;
        /// <summary>
        /// Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service.
        /// </summary>
        public readonly int? MinIdleInstances;
        /// <summary>
        /// Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it.
        /// </summary>
        public readonly string? MinPendingLatency;
        /// <summary>
        /// Minimum number of running instances that should be maintained for this version. Default: 2
        /// </summary>
        public readonly int? MinTotalInstances;
        /// <summary>
        /// Target scaling by network usage.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.FlexibleAppVersionAutomaticScalingNetworkUtilization? NetworkUtilization;
        /// <summary>
        /// Target scaling by request utilization.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.FlexibleAppVersionAutomaticScalingRequestUtilization? RequestUtilization;

        [OutputConstructor]
        private FlexibleAppVersionAutomaticScaling(
            string? coolDownPeriod,

            Outputs.FlexibleAppVersionAutomaticScalingCpuUtilization cpuUtilization,

            Outputs.FlexibleAppVersionAutomaticScalingDiskUtilization? diskUtilization,

            int? maxConcurrentRequests,

            int? maxIdleInstances,

            string? maxPendingLatency,

            int? maxTotalInstances,

            int? minIdleInstances,

            string? minPendingLatency,

            int? minTotalInstances,

            Outputs.FlexibleAppVersionAutomaticScalingNetworkUtilization? networkUtilization,

            Outputs.FlexibleAppVersionAutomaticScalingRequestUtilization? requestUtilization)
        {
            CoolDownPeriod = coolDownPeriod;
            CpuUtilization = cpuUtilization;
            DiskUtilization = diskUtilization;
            MaxConcurrentRequests = maxConcurrentRequests;
            MaxIdleInstances = maxIdleInstances;
            MaxPendingLatency = maxPendingLatency;
            MaxTotalInstances = maxTotalInstances;
            MinIdleInstances = minIdleInstances;
            MinPendingLatency = minPendingLatency;
            MinTotalInstances = minTotalInstances;
            NetworkUtilization = networkUtilization;
            RequestUtilization = requestUtilization;
        }
    }
}
