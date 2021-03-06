// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring
{
    public static class GetAppEngineService
    {
        /// <summary>
        /// A Monitoring Service is the root resource under which operational aspects of a
        /// generic service are accessible. A service is some discrete, autonomous, and
        /// network-accessible unit, designed to solve an individual concern
        /// 
        /// An App Engine monitoring service is automatically created by GCP to monitor
        /// App Engine services.
        /// 
        /// 
        /// To get more information about Service, see:
        /// 
        /// * [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services)
        /// * How-to Guides
        ///     * [Service Monitoring](https://cloud.google.com/monitoring/service-monitoring)
        ///     * [Monitoring API Documentation](https://cloud.google.com/monitoring/api/v3/)
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetAppEngineServiceResult> InvokeAsync(GetAppEngineServiceArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAppEngineServiceResult>("gcp:monitoring/getAppEngineService:getAppEngineService", args ?? new GetAppEngineServiceArgs(), options.WithVersion());
    }


    public sealed class GetAppEngineServiceArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the App Engine module underlying this
        /// service. Corresponds to the moduleId resource label in the [gae_app](https://cloud.google.com/monitoring/api/resources#tag_gae_app) monitored resource, or the service/module name.
        /// </summary>
        [Input("moduleId", required: true)]
        public string ModuleId { get; set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public string? Project { get; set; }

        public GetAppEngineServiceArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetAppEngineServiceResult
    {
        public readonly string DisplayName;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string ModuleId;
        public readonly string Name;
        public readonly string? Project;
        public readonly string ServiceId;
        public readonly ImmutableArray<Outputs.GetAppEngineServiceTelemetryResult> Telemetries;

        [OutputConstructor]
        private GetAppEngineServiceResult(
            string displayName,

            string id,

            string moduleId,

            string name,

            string? project,

            string serviceId,

            ImmutableArray<Outputs.GetAppEngineServiceTelemetryResult> telemetries)
        {
            DisplayName = displayName;
            Id = id;
            ModuleId = moduleId;
            Name = name;
            Project = project;
            ServiceId = serviceId;
            Telemetries = telemetries;
        }
    }
}
