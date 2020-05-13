// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Billing.Outputs
{

    [OutputType]
    public sealed class BudgetAllUpdatesRule
    {
        /// <summary>
        /// The name of the Cloud Pub/Sub topic where budget related
        /// messages will be published, in the form
        /// projects/{project_id}/topics/{topic_id}. Updates are sent
        /// at regular intervals to the topic.
        /// </summary>
        public readonly string PubsubTopic;
        /// <summary>
        /// The schema version of the notification. Only "1.0" is
        /// accepted. It represents the JSON schema as defined in
        /// https://cloud.google.com/billing/docs/how-to/budgets#notification_format.
        /// </summary>
        public readonly string? SchemaVersion;

        [OutputConstructor]
        private BudgetAllUpdatesRule(
            string pubsubTopic,

            string? schemaVersion)
        {
            PubsubTopic = pubsubTopic;
            SchemaVersion = schemaVersion;
        }
    }
}