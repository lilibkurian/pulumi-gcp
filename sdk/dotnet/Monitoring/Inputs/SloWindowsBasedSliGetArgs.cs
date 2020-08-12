// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Inputs
{

    public sealed class SloWindowsBasedSliGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A TimeSeries [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters)
        /// with ValueType = BOOL. The window is good if any true values
        /// appear in the window. One of `good_bad_metric_filter`,
        /// `good_total_ratio_threshold`, `metric_mean_in_range`,
        /// `metric_sum_in_range` must be set for `windows_based_sli`.
        /// </summary>
        [Input("goodBadMetricFilter")]
        public Input<string>? GoodBadMetricFilter { get; set; }

        /// <summary>
        /// Criterion that describes a window as good if its performance is
        /// high enough. One of `good_bad_metric_filter`,
        /// `good_total_ratio_threshold`, `metric_mean_in_range`,
        /// `metric_sum_in_range` must be set for `windows_based_sli`.
        /// Structure is documented below.
        /// </summary>
        [Input("goodTotalRatioThreshold")]
        public Input<Inputs.SloWindowsBasedSliGoodTotalRatioThresholdGetArgs>? GoodTotalRatioThreshold { get; set; }

        /// <summary>
        /// Criterion that describes a window as good if the metric's value
        /// is in a good range, *averaged* across returned streams.
        /// One of `good_bad_metric_filter`,
        /// `good_total_ratio_threshold`, `metric_mean_in_range`,
        /// `metric_sum_in_range` must be set for `windows_based_sli`.
        /// Average value X of `time_series` should satisfy
        /// `range.min &lt;= X &lt; range.max` for a good window.
        /// Structure is documented below.
        /// </summary>
        [Input("metricMeanInRange")]
        public Input<Inputs.SloWindowsBasedSliMetricMeanInRangeGetArgs>? MetricMeanInRange { get; set; }

        /// <summary>
        /// Criterion that describes a window as good if the metric's value
        /// is in a good range, *summed* across returned streams.
        /// Summed value `X` of `time_series` should satisfy
        /// `range.min &lt;= X &lt; range.max` for a good window.
        /// One of `good_bad_metric_filter`,
        /// `good_total_ratio_threshold`, `metric_mean_in_range`,
        /// `metric_sum_in_range` must be set for `windows_based_sli`.
        /// Structure is documented below.
        /// </summary>
        [Input("metricSumInRange")]
        public Input<Inputs.SloWindowsBasedSliMetricSumInRangeGetArgs>? MetricSumInRange { get; set; }

        /// <summary>
        /// Duration over which window quality is evaluated, given as a
        /// duration string "{X}s" representing X seconds. Must be an
        /// integer fraction of a day and at least 60s.
        /// </summary>
        [Input("windowPeriod")]
        public Input<string>? WindowPeriod { get; set; }

        public SloWindowsBasedSliGetArgs()
        {
        }
    }
}
