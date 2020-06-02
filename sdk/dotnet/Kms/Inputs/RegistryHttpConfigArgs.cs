// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Kms.Inputs
{

    public sealed class RegistryHttpConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The field allows `HTTP_ENABLED` or `HTTP_DISABLED`.
        /// </summary>
        [Input("httpEnabledState", required: true)]
        public Input<string> HttpEnabledState { get; set; } = null!;

        public RegistryHttpConfigArgs()
        {
        }
    }
}
