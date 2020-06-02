// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Kms.Inputs
{

    public sealed class RegistryCredentialPublicKeyCertificateGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The certificate data.
        /// </summary>
        [Input("certificate", required: true)]
        public Input<string> Certificate { get; set; } = null!;

        /// <summary>
        /// The field allows only `X509_CERTIFICATE_PEM`.
        /// </summary>
        [Input("format", required: true)]
        public Input<string> Format { get; set; } = null!;

        public RegistryCredentialPublicKeyCertificateGetArgs()
        {
        }
    }
}
