// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Kms.Inputs
{

    public sealed class RegistryMqttConfigArgs : Pulumi.ResourceArgs
    {
        [Input("mqttEnabledState", required: true)]
        public Input<string> MqttEnabledState { get; set; } = null!;

        public RegistryMqttConfigArgs()
        {
        }
    }
}
