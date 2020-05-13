// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudScheduler.Outputs
{

    [OutputType]
    public sealed class JobAppEngineHttpTargetAppEngineRouting
    {
        /// <summary>
        /// App instance.
        /// By default, the job is sent to an instance which is available when the job is attempted.
        /// </summary>
        public readonly string? Instance;
        /// <summary>
        /// App service.
        /// By default, the job is sent to the service which is the default service when the job is attempted.
        /// </summary>
        public readonly string? Service;
        /// <summary>
        /// App version.
        /// By default, the job is sent to the version which is the default version when the job is attempted.
        /// </summary>
        public readonly string? Version;

        [OutputConstructor]
        private JobAppEngineHttpTargetAppEngineRouting(
            string? instance,

            string? service,

            string? version)
        {
            Instance = instance;
            Service = service;
            Version = version;
        }
    }
}