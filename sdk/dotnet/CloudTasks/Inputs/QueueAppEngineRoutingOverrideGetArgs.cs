// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudTasks.Inputs
{

    public sealed class QueueAppEngineRoutingOverrideGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// -
        /// The host that the task is sent to.
        /// </summary>
        [Input("host")]
        public Input<string>? Host { get; set; }

        /// <summary>
        /// App instance.
        /// By default, the task is sent to an instance which is available when the task is attempted.
        /// </summary>
        [Input("instance")]
        public Input<string>? Instance { get; set; }

        /// <summary>
        /// App service.
        /// By default, the task is sent to the service which is the default service when the task is attempted.
        /// </summary>
        [Input("service")]
        public Input<string>? Service { get; set; }

        /// <summary>
        /// App version.
        /// By default, the task is sent to the version which is the default version when the task is attempted.
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public QueueAppEngineRoutingOverrideGetArgs()
        {
        }
    }
}