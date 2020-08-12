// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.OsConfig.Inputs
{

    public sealed class GuestPoliciesAssignmentGetArgs : Pulumi.ResourceArgs
    {
        [Input("groupLabels")]
        private InputList<Inputs.GuestPoliciesAssignmentGroupLabelGetArgs>? _groupLabels;

        /// <summary>
        /// Targets instances matching at least one of these label sets. This allows an assignment to target disparate groups,
        /// for example "env=prod or env=staging".
        /// Structure is documented below.
        /// </summary>
        public InputList<Inputs.GuestPoliciesAssignmentGroupLabelGetArgs> GroupLabels
        {
            get => _groupLabels ?? (_groupLabels = new InputList<Inputs.GuestPoliciesAssignmentGroupLabelGetArgs>());
            set => _groupLabels = value;
        }

        [Input("instanceNamePrefixes")]
        private InputList<string>? _instanceNamePrefixes;

        /// <summary>
        /// Targets VM instances whose name starts with one of these prefixes.
        /// Like labels, this is another way to group VM instances when targeting configs,
        /// for example prefix="prod-".
        /// Only supported for project-level policies.
        /// </summary>
        public InputList<string> InstanceNamePrefixes
        {
            get => _instanceNamePrefixes ?? (_instanceNamePrefixes = new InputList<string>());
            set => _instanceNamePrefixes = value;
        }

        [Input("instances")]
        private InputList<string>? _instances;

        /// <summary>
        /// Targets any of the instances specified. Instances are specified by their URI in the form
        /// zones/[ZONE]/instances/[INSTANCE_NAME].
        /// Instance targeting is uncommon and is supported to facilitate the management of changes
        /// by the instance or to target specific VM instances for development and testing.
        /// Only supported for project-level policies and must reference instances within this project.
        /// </summary>
        public InputList<string> Instances
        {
            get => _instances ?? (_instances = new InputList<string>());
            set => _instances = value;
        }

        [Input("osTypes")]
        private InputList<Inputs.GuestPoliciesAssignmentOsTypeGetArgs>? _osTypes;

        /// <summary>
        /// Targets VM instances matching at least one of the following OS types.
        /// VM instances must match all supplied criteria for a given OsType to be included.
        /// Structure is documented below.
        /// </summary>
        public InputList<Inputs.GuestPoliciesAssignmentOsTypeGetArgs> OsTypes
        {
            get => _osTypes ?? (_osTypes = new InputList<Inputs.GuestPoliciesAssignmentOsTypeGetArgs>());
            set => _osTypes = value;
        }

        [Input("zones")]
        private InputList<string>? _zones;

        /// <summary>
        /// Targets instances in any of these zones. Leave empty to target instances in any zone.
        /// Zonal targeting is uncommon and is supported to facilitate the management of changes by zone.
        /// </summary>
        public InputList<string> Zones
        {
            get => _zones ?? (_zones = new InputList<string>());
            set => _zones = value;
        }

        public GuestPoliciesAssignmentGetArgs()
        {
        }
    }
}
