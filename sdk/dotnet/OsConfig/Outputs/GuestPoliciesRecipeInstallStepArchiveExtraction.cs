// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.OsConfig.Outputs
{

    [OutputType]
    public sealed class GuestPoliciesRecipeInstallStepArchiveExtraction
    {
        /// <summary>
        /// The id of the relevant artifact in the recipe.
        /// </summary>
        public readonly string ArtifactId;
        /// <summary>
        /// Directory to extract archive to. Defaults to / on Linux or C:\ on Windows.
        /// </summary>
        public readonly string? Destination;
        /// <summary>
        /// The type of the archive to extract.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GuestPoliciesRecipeInstallStepArchiveExtraction(
            string artifactId,

            string? destination,

            string type)
        {
            ArtifactId = artifactId;
            Destination = destination;
            Type = type;
        }
    }
}
