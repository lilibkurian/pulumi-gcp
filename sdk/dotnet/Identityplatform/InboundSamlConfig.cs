// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.IdentityPlatform
{
    public partial class InboundSamlConfig : Pulumi.CustomResource
    {
        /// <summary>
        /// Human friendly display name.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// If this config allows users to sign in with the provider.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// SAML IdP configuration when the project acts as the relying party
        /// </summary>
        [Output("idpConfig")]
        public Output<Outputs.InboundSamlConfigIdpConfig> IdpConfig { get; private set; } = null!;

        /// <summary>
        /// The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric
        /// characters, hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter,
        /// end with an alphanumeric character, and have at least 2 characters.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// SAML SP (Service Provider) configuration when the project acts as the relying party to receive and accept an
        /// authentication assertion issued by a SAML identity provider.
        /// </summary>
        [Output("spConfig")]
        public Output<Outputs.InboundSamlConfigSpConfig> SpConfig { get; private set; } = null!;


        /// <summary>
        /// Create a InboundSamlConfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public InboundSamlConfig(string name, InboundSamlConfigArgs args, CustomResourceOptions? options = null)
            : base("gcp:identityplatform/inboundSamlConfig:InboundSamlConfig", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private InboundSamlConfig(string name, Input<string> id, InboundSamlConfigState? state = null, CustomResourceOptions? options = null)
            : base("gcp:identityplatform/inboundSamlConfig:InboundSamlConfig", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing InboundSamlConfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static InboundSamlConfig Get(string name, Input<string> id, InboundSamlConfigState? state = null, CustomResourceOptions? options = null)
        {
            return new InboundSamlConfig(name, id, state, options);
        }
    }

    public sealed class InboundSamlConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Human friendly display name.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// If this config allows users to sign in with the provider.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// SAML IdP configuration when the project acts as the relying party
        /// </summary>
        [Input("idpConfig", required: true)]
        public Input<Inputs.InboundSamlConfigIdpConfigArgs> IdpConfig { get; set; } = null!;

        /// <summary>
        /// The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric
        /// characters, hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter,
        /// end with an alphanumeric character, and have at least 2 characters.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// SAML SP (Service Provider) configuration when the project acts as the relying party to receive and accept an
        /// authentication assertion issued by a SAML identity provider.
        /// </summary>
        [Input("spConfig", required: true)]
        public Input<Inputs.InboundSamlConfigSpConfigArgs> SpConfig { get; set; } = null!;

        public InboundSamlConfigArgs()
        {
        }
    }

    public sealed class InboundSamlConfigState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Human friendly display name.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// If this config allows users to sign in with the provider.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// SAML IdP configuration when the project acts as the relying party
        /// </summary>
        [Input("idpConfig")]
        public Input<Inputs.InboundSamlConfigIdpConfigGetArgs>? IdpConfig { get; set; }

        /// <summary>
        /// The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric
        /// characters, hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter,
        /// end with an alphanumeric character, and have at least 2 characters.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// SAML SP (Service Provider) configuration when the project acts as the relying party to receive and accept an
        /// authentication assertion issued by a SAML identity provider.
        /// </summary>
        [Input("spConfig")]
        public Input<Inputs.InboundSamlConfigSpConfigGetArgs>? SpConfig { get; set; }

        public InboundSamlConfigState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class InboundSamlConfigIdpConfigArgs : Pulumi.ResourceArgs
    {
        [Input("idpCertificates", required: true)]
        private InputList<InboundSamlConfigIdpConfigIdpCertificatesArgs>? _idpCertificates;
        public InputList<InboundSamlConfigIdpConfigIdpCertificatesArgs> IdpCertificates
        {
            get => _idpCertificates ?? (_idpCertificates = new InputList<InboundSamlConfigIdpConfigIdpCertificatesArgs>());
            set => _idpCertificates = value;
        }

        [Input("idpEntityId", required: true)]
        public Input<string> IdpEntityId { get; set; } = null!;

        [Input("signRequest")]
        public Input<bool>? SignRequest { get; set; }

        [Input("ssoUrl", required: true)]
        public Input<string> SsoUrl { get; set; } = null!;

        public InboundSamlConfigIdpConfigArgs()
        {
        }
    }

    public sealed class InboundSamlConfigIdpConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("idpCertificates", required: true)]
        private InputList<InboundSamlConfigIdpConfigIdpCertificatesGetArgs>? _idpCertificates;
        public InputList<InboundSamlConfigIdpConfigIdpCertificatesGetArgs> IdpCertificates
        {
            get => _idpCertificates ?? (_idpCertificates = new InputList<InboundSamlConfigIdpConfigIdpCertificatesGetArgs>());
            set => _idpCertificates = value;
        }

        [Input("idpEntityId", required: true)]
        public Input<string> IdpEntityId { get; set; } = null!;

        [Input("signRequest")]
        public Input<bool>? SignRequest { get; set; }

        [Input("ssoUrl", required: true)]
        public Input<string> SsoUrl { get; set; } = null!;

        public InboundSamlConfigIdpConfigGetArgs()
        {
        }
    }

    public sealed class InboundSamlConfigIdpConfigIdpCertificatesArgs : Pulumi.ResourceArgs
    {
        [Input("x509Certificate")]
        public Input<string>? X509Certificate { get; set; }

        public InboundSamlConfigIdpConfigIdpCertificatesArgs()
        {
        }
    }

    public sealed class InboundSamlConfigIdpConfigIdpCertificatesGetArgs : Pulumi.ResourceArgs
    {
        [Input("x509Certificate")]
        public Input<string>? X509Certificate { get; set; }

        public InboundSamlConfigIdpConfigIdpCertificatesGetArgs()
        {
        }
    }

    public sealed class InboundSamlConfigSpConfigArgs : Pulumi.ResourceArgs
    {
        [Input("callbackUri")]
        public Input<string>? CallbackUri { get; set; }

        [Input("spCertificates")]
        private InputList<InboundSamlConfigSpConfigSpCertificatesArgs>? _spCertificates;
        public InputList<InboundSamlConfigSpConfigSpCertificatesArgs> SpCertificates
        {
            get => _spCertificates ?? (_spCertificates = new InputList<InboundSamlConfigSpConfigSpCertificatesArgs>());
            set => _spCertificates = value;
        }

        [Input("spEntityId")]
        public Input<string>? SpEntityId { get; set; }

        public InboundSamlConfigSpConfigArgs()
        {
        }
    }

    public sealed class InboundSamlConfigSpConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("callbackUri")]
        public Input<string>? CallbackUri { get; set; }

        [Input("spCertificates")]
        private InputList<InboundSamlConfigSpConfigSpCertificatesGetArgs>? _spCertificates;
        public InputList<InboundSamlConfigSpConfigSpCertificatesGetArgs> SpCertificates
        {
            get => _spCertificates ?? (_spCertificates = new InputList<InboundSamlConfigSpConfigSpCertificatesGetArgs>());
            set => _spCertificates = value;
        }

        [Input("spEntityId")]
        public Input<string>? SpEntityId { get; set; }

        public InboundSamlConfigSpConfigGetArgs()
        {
        }
    }

    public sealed class InboundSamlConfigSpConfigSpCertificatesArgs : Pulumi.ResourceArgs
    {
        [Input("x509Certificate")]
        public Input<string>? X509Certificate { get; set; }

        public InboundSamlConfigSpConfigSpCertificatesArgs()
        {
        }
    }

    public sealed class InboundSamlConfigSpConfigSpCertificatesGetArgs : Pulumi.ResourceArgs
    {
        [Input("x509Certificate")]
        public Input<string>? X509Certificate { get; set; }

        public InboundSamlConfigSpConfigSpCertificatesGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class InboundSamlConfigIdpConfig
    {
        public readonly ImmutableArray<InboundSamlConfigIdpConfigIdpCertificates> IdpCertificates;
        public readonly string IdpEntityId;
        public readonly bool? SignRequest;
        public readonly string SsoUrl;

        [OutputConstructor]
        private InboundSamlConfigIdpConfig(
            ImmutableArray<InboundSamlConfigIdpConfigIdpCertificates> idpCertificates,
            string idpEntityId,
            bool? signRequest,
            string ssoUrl)
        {
            IdpCertificates = idpCertificates;
            IdpEntityId = idpEntityId;
            SignRequest = signRequest;
            SsoUrl = ssoUrl;
        }
    }

    [OutputType]
    public sealed class InboundSamlConfigIdpConfigIdpCertificates
    {
        public readonly string? X509Certificate;

        [OutputConstructor]
        private InboundSamlConfigIdpConfigIdpCertificates(string? x509Certificate)
        {
            X509Certificate = x509Certificate;
        }
    }

    [OutputType]
    public sealed class InboundSamlConfigSpConfig
    {
        public readonly string? CallbackUri;
        public readonly ImmutableArray<InboundSamlConfigSpConfigSpCertificates> SpCertificates;
        public readonly string? SpEntityId;

        [OutputConstructor]
        private InboundSamlConfigSpConfig(
            string? callbackUri,
            ImmutableArray<InboundSamlConfigSpConfigSpCertificates> spCertificates,
            string? spEntityId)
        {
            CallbackUri = callbackUri;
            SpCertificates = spCertificates;
            SpEntityId = spEntityId;
        }
    }

    [OutputType]
    public sealed class InboundSamlConfigSpConfigSpCertificates
    {
        public readonly string X509Certificate;

        [OutputConstructor]
        private InboundSamlConfigSpConfigSpCertificates(string x509Certificate)
        {
            X509Certificate = x509Certificate;
        }
    }
    }
}