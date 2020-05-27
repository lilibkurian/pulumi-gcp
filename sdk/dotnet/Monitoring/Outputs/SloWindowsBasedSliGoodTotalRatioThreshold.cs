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
    public sealed class SloWindowsBasedSliGoodTotalRatioThreshold
    {
        /// <summary>
        /// Basic SLI to evaluate to judge window quality.  Structure is documented below.
        /// </summary>
        public readonly Outputs.SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance? BasicSliPerformance;
        /// <summary>
        /// Request-based SLI to evaluate to judge window quality.  Structure is documented below.
        /// </summary>
        public readonly Outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformance? Performance;
        /// <summary>
        /// A duration string, e.g. 10s.
        /// Good service is defined to be the count of requests made to
        /// this service that return in no more than threshold.
        /// </summary>
        public readonly double? Threshold;

        [OutputConstructor]
        private SloWindowsBasedSliGoodTotalRatioThreshold(
            Outputs.SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance? basicSliPerformance,

            Outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformance? performance,

            double? threshold)
        {
            BasicSliPerformance = basicSliPerformance;
            Performance = performance;
            Threshold = threshold;
        }
    }
}
