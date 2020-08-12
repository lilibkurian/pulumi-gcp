// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Inputs
{

    public sealed class AlertPolicyConditionGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A condition that checks that a time series
        /// continues to receive new data points.
        /// Structure is documented below.
        /// </summary>
        [Input("conditionAbsent")]
        public Input<Inputs.AlertPolicyConditionConditionAbsentGetArgs>? ConditionAbsent { get; set; }

        /// <summary>
        /// A condition that compares a time series against a
        /// threshold.
        /// Structure is documented below.
        /// </summary>
        [Input("conditionThreshold")]
        public Input<Inputs.AlertPolicyConditionConditionThresholdGetArgs>? ConditionThreshold { get; set; }

        /// <summary>
        /// A short name or phrase used to identify the
        /// condition in dashboards, notifications, and
        /// incidents. To avoid confusion, don't use the same
        /// display name for multiple conditions in the same
        /// policy.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// -
        /// The unique resource name for this condition.
        /// Its syntax is:
        /// projects/[PROJECT_ID]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]
        /// [CONDITION_ID] is assigned by Stackdriver Monitoring when
        /// the condition is created as part of a new or updated alerting
        /// policy.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public AlertPolicyConditionGetArgs()
        {
        }
    }
}
