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
    public sealed class GuestPoliciesRecipeUpdateStepFileExec
    {
        /// <summary>
        /// Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0]
        /// </summary>
        public readonly ImmutableArray<int> AllowedExitCodes;
        /// <summary>
        /// Arguments to be passed to the provided executable.
        /// </summary>
        public readonly ImmutableArray<string> Args;
        /// <summary>
        /// The id of the relevant artifact in the recipe.
        /// </summary>
        public readonly string? ArtifactId;
        /// <summary>
        /// The absolute path of the file on the local filesystem.
        /// </summary>
        public readonly string? LocalPath;

        [OutputConstructor]
        private GuestPoliciesRecipeUpdateStepFileExec(
            ImmutableArray<int> allowedExitCodes,

            ImmutableArray<string> args,

            string? artifactId,

            string? localPath)
        {
            AllowedExitCodes = allowedExitCodes;
            Args = args;
            ArtifactId = artifactId;
            LocalPath = localPath;
        }
    }
}
