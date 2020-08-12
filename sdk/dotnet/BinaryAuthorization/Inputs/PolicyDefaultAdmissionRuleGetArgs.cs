// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.BinaryAuthorization.Inputs
{

    public sealed class PolicyDefaultAdmissionRuleGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action when a pod creation is denied by the admission rule.
        /// Possible values are `ENFORCED_BLOCK_AND_AUDIT_LOG` and `DRYRUN_AUDIT_LOG_ONLY`.
        /// </summary>
        [Input("enforcementMode", required: true)]
        public Input<string> EnforcementMode { get; set; } = null!;

        /// <summary>
        /// How this admission rule will be evaluated.
        /// Possible values are `ALWAYS_ALLOW`, `REQUIRE_ATTESTATION`, and `ALWAYS_DENY`.
        /// </summary>
        [Input("evaluationMode", required: true)]
        public Input<string> EvaluationMode { get; set; } = null!;

        [Input("requireAttestationsBies")]
        private InputList<string>? _requireAttestationsBies;

        /// <summary>
        /// The resource names of the attestors that must attest to a
        /// container image. If the attestor is in a different project from the
        /// policy, it should be specified in the format `projects/*/attestors/*`.
        /// Each attestor must exist before a policy can reference it. To add an
        /// attestor to a policy the principal issuing the policy change
        /// request must be able to read the attestor resource.
        /// Note: this field must be non-empty when the evaluation_mode field
        /// specifies REQUIRE_ATTESTATION, otherwise it must be empty.
        /// </summary>
        public InputList<string> RequireAttestationsBies
        {
            get => _requireAttestationsBies ?? (_requireAttestationsBies = new InputList<string>());
            set => _requireAttestationsBies = value;
        }

        public PolicyDefaultAdmissionRuleGetArgs()
        {
        }
    }
}
