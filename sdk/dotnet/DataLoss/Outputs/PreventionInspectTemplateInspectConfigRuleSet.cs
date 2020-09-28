// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.DataLoss.Outputs
{

    [OutputType]
    public sealed class PreventionInspectTemplateInspectConfigRuleSet
    {
        /// <summary>
        /// If a finding is matched by any of the infoType detectors listed here, the finding will be excluded from the scan results.
        /// Structure is documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.PreventionInspectTemplateInspectConfigRuleSetInfoType> InfoTypes;
        /// <summary>
        /// Set of rules to be applied to infoTypes. The rules are applied in order.
        /// Structure is documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.PreventionInspectTemplateInspectConfigRuleSetRule> Rules;

        [OutputConstructor]
        private PreventionInspectTemplateInspectConfigRuleSet(
            ImmutableArray<Outputs.PreventionInspectTemplateInspectConfigRuleSetInfoType> infoTypes,

            ImmutableArray<Outputs.PreventionInspectTemplateInspectConfigRuleSetRule> rules)
        {
            InfoTypes = infoTypes;
            Rules = rules;
        }
    }
}