// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.OsConfig.Inputs
{

    public sealed class GuestPoliciesRecipeInstallStepDpkgInstallationGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of the relevant artifact in the recipe.
        /// </summary>
        [Input("artifactId", required: true)]
        public Input<string> ArtifactId { get; set; } = null!;

        public GuestPoliciesRecipeInstallStepDpkgInstallationGetArgs()
        {
        }
    }
}
