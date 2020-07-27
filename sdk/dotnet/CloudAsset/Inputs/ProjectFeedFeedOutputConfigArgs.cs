// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudAsset.Inputs
{

    public sealed class ProjectFeedFeedOutputConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Destination on Cloud Pubsub.  Structure is documented below.
        /// </summary>
        [Input("pubsubDestination", required: true)]
        public Input<Inputs.ProjectFeedFeedOutputConfigPubsubDestinationArgs> PubsubDestination { get; set; } = null!;

        public ProjectFeedFeedOutputConfigArgs()
        {
        }
    }
}
