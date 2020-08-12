// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.IdentityPlatform.Inputs
{

    public sealed class InboundSamlConfigSpConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Callback URI where responses from IDP are handled. Must start with `https://`.
        /// </summary>
        [Input("callbackUri")]
        public Input<string>? CallbackUri { get; set; }

        [Input("spCertificates")]
        private InputList<Inputs.InboundSamlConfigSpConfigSpCertificateGetArgs>? _spCertificates;

        /// <summary>
        /// -
        /// The IDP's certificate data to verify the signature in the SAMLResponse issued by the IDP.
        /// Structure is documented below.
        /// </summary>
        public InputList<Inputs.InboundSamlConfigSpConfigSpCertificateGetArgs> SpCertificates
        {
            get => _spCertificates ?? (_spCertificates = new InputList<Inputs.InboundSamlConfigSpConfigSpCertificateGetArgs>());
            set => _spCertificates = value;
        }

        /// <summary>
        /// Unique identifier for all SAML entities.
        /// </summary>
        [Input("spEntityId")]
        public Input<string>? SpEntityId { get; set; }

        public InboundSamlConfigSpConfigGetArgs()
        {
        }
    }
}
