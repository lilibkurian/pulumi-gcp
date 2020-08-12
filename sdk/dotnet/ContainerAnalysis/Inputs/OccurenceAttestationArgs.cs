// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.ContainerAnalysis.Inputs
{

    public sealed class OccurenceAttestationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The serialized payload that is verified by one or
        /// more signatures. A base64-encoded string.
        /// </summary>
        [Input("serializedPayload", required: true)]
        public Input<string> SerializedPayload { get; set; } = null!;

        [Input("signatures", required: true)]
        private InputList<Inputs.OccurenceAttestationSignatureArgs>? _signatures;

        /// <summary>
        /// One or more signatures over serializedPayload.
        /// Verifier implementations should consider this attestation
        /// message verified if at least one signature verifies
        /// serializedPayload. See Signature in common.proto for more
        /// details on signature structure and verification.
        /// Structure is documented below.
        /// </summary>
        public InputList<Inputs.OccurenceAttestationSignatureArgs> Signatures
        {
            get => _signatures ?? (_signatures = new InputList<Inputs.OccurenceAttestationSignatureArgs>());
            set => _signatures = value;
        }

        public OccurenceAttestationArgs()
        {
        }
    }
}
