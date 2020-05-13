// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudBuild.Inputs
{

    public sealed class TriggerGithubPullRequestArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Regex of branches to match.  Specify only one of branch or tag.
        /// </summary>
        [Input("branch", required: true)]
        public Input<string> Branch { get; set; } = null!;

        /// <summary>
        /// Whether to block builds on a "/gcbrun" comment from a repository owner or collaborator.
        /// </summary>
        [Input("commentControl")]
        public Input<string>? CommentControl { get; set; }

        public TriggerGithubPullRequestArgs()
        {
        }
    }
}