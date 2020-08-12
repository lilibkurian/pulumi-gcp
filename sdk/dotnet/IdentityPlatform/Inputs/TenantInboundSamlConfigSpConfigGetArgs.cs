// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.IdentityPlatform.Inputs
{

    public sealed class TenantInboundSamlConfigSpConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Callback URI where responses from IDP are handled. Must start with `https://`.
        /// </summary>
        [Input("callbackUri", required: true)]
        public Input<string> CallbackUri { get; set; } = null!;

        [Input("spCertificates")]
        private InputList<Inputs.TenantInboundSamlConfigSpConfigSpCertificateGetArgs>? _spCertificates;

        /// <summary>
        /// -
        /// The IDP's certificate data to verify the signature in the SAMLResponse issued by the IDP.
        /// Structure is documented below.
        /// </summary>
        public InputList<Inputs.TenantInboundSamlConfigSpConfigSpCertificateGetArgs> SpCertificates
        {
            get => _spCertificates ?? (_spCertificates = new InputList<Inputs.TenantInboundSamlConfigSpConfigSpCertificateGetArgs>());
            set => _spCertificates = value;
        }

        /// <summary>
        /// Unique identifier for all SAML entities.
        /// </summary>
        [Input("spEntityId", required: true)]
        public Input<string> SpEntityId { get; set; } = null!;

        public TenantInboundSamlConfigSpConfigGetArgs()
        {
        }
    }
}
