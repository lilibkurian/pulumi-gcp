// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Logging.Inputs
{

    public sealed class MetricMetricDescriptorLabelArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description of this metric, which is used in documentation. The maximum length of the
        /// description is 8000 characters.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The label key.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// The type of data that can be assigned to the label.
        /// Default value is `STRING`.
        /// Possible values are `BOOL`, `INT64`, and `STRING`.
        /// </summary>
        [Input("valueType")]
        public Input<string>? ValueType { get; set; }

        public MetricMetricDescriptorLabelArgs()
        {
        }
    }
}
