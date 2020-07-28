// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.OsConfig.Inputs
{

    public sealed class GuestPoliciesRecipeArtifactRemoteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Must be provided if allowInsecure is false. SHA256 checksum in hex format, to compare to the checksum of the artifact.
        /// If the checksum is not empty and it doesn't match the artifact then the recipe installation fails before running any
        /// of the steps.
        /// </summary>
        [Input("checkSum")]
        public Input<string>? CheckSum { get; set; }

        /// <summary>
        /// URI from which to fetch the object. It should contain both the protocol and path following the format {protocol}://{location}.
        /// </summary>
        [Input("uri")]
        public Input<string>? Uri { get; set; }

        public GuestPoliciesRecipeArtifactRemoteArgs()
        {
        }
    }
}
