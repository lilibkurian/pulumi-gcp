// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Inputs
{

    public sealed class MetricDescriptorMetadataGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors. In `[duration format](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf?&amp;_ga=2.264881487.1507873253.1593446723-935052455.1591817775#google.protobuf.Duration)`.
        /// </summary>
        [Input("ingestDelay")]
        public Input<string>? IngestDelay { get; set; }

        /// <summary>
        /// The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period. In `[duration format](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf?&amp;_ga=2.264881487.1507873253.1593446723-935052455.1591817775#google.protobuf.Duration)`.
        /// </summary>
        [Input("samplePeriod")]
        public Input<string>? SamplePeriod { get; set; }

        public MetricDescriptorMetadataGetArgs()
        {
        }
    }
}
