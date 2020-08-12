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
    public sealed class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut
    {
        /// <summary>
        /// A TimeSeries [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters)
        /// aggregating values to quantify the good service provided.
        /// Must have ValueType = DISTRIBUTION and
        /// MetricKind = DELTA or MetricKind = CUMULATIVE.
        /// </summary>
        public readonly string DistributionFilter;
        /// <summary>
        /// Range of numerical values. The computed good_service
        /// will be the count of values x in the Distribution such
        /// that range.min &lt;= x &lt; range.max. inclusive of min and
        /// exclusive of max. Open ranges can be defined by setting
        /// just one of min or max. Summed value `X` should satisfy
        /// `range.min &lt;= X &lt; range.max` for a good window.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange Range;

        [OutputConstructor]
        private SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut(
            string distributionFilter,

            Outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange range)
        {
            DistributionFilter = distributionFilter;
            Range = range;
        }
    }
}
