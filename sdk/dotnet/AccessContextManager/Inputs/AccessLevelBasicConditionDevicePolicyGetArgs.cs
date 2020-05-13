// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.AccessContextManager.Inputs
{

    public sealed class AccessLevelBasicConditionDevicePolicyGetArgs : Pulumi.ResourceArgs
    {
        [Input("allowedDeviceManagementLevels")]
        private InputList<string>? _allowedDeviceManagementLevels;

        /// <summary>
        /// A list of allowed device management levels.
        /// An empty list allows all management levels.
        /// </summary>
        public InputList<string> AllowedDeviceManagementLevels
        {
            get => _allowedDeviceManagementLevels ?? (_allowedDeviceManagementLevels = new InputList<string>());
            set => _allowedDeviceManagementLevels = value;
        }

        [Input("allowedEncryptionStatuses")]
        private InputList<string>? _allowedEncryptionStatuses;

        /// <summary>
        /// A list of allowed encryptions statuses.
        /// An empty list allows all statuses.
        /// </summary>
        public InputList<string> AllowedEncryptionStatuses
        {
            get => _allowedEncryptionStatuses ?? (_allowedEncryptionStatuses = new InputList<string>());
            set => _allowedEncryptionStatuses = value;
        }

        [Input("osConstraints")]
        private InputList<Inputs.AccessLevelBasicConditionDevicePolicyOsConstraintGetArgs>? _osConstraints;

        /// <summary>
        /// A list of allowed OS versions.
        /// An empty list allows all types and all versions.  Structure is documented below.
        /// </summary>
        public InputList<Inputs.AccessLevelBasicConditionDevicePolicyOsConstraintGetArgs> OsConstraints
        {
            get => _osConstraints ?? (_osConstraints = new InputList<Inputs.AccessLevelBasicConditionDevicePolicyOsConstraintGetArgs>());
            set => _osConstraints = value;
        }

        /// <summary>
        /// Whether the device needs to be approved by the customer admin.
        /// </summary>
        [Input("requireAdminApproval")]
        public Input<bool>? RequireAdminApproval { get; set; }

        /// <summary>
        /// Whether the device needs to be corp owned.
        /// </summary>
        [Input("requireCorpOwned")]
        public Input<bool>? RequireCorpOwned { get; set; }

        /// <summary>
        /// Whether or not screenlock is required for the DevicePolicy
        /// to be true. Defaults to false.
        /// </summary>
        [Input("requireScreenLock")]
        public Input<bool>? RequireScreenLock { get; set; }

        public AccessLevelBasicConditionDevicePolicyGetArgs()
        {
        }
    }
}