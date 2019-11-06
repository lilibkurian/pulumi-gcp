// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    public static partial class Invokes
    {
        /// <summary>
        /// Get a VPN gateway within GCE from its name.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_vpn_gateway.html.markdown.
        /// </summary>
        public static Task<GetVPNGatewayResult> GetVPNGateway(GetVPNGatewayArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetVPNGatewayResult>("gcp:compute/getVPNGateway:getVPNGateway", args, options.WithVersion());
    }

    public sealed class GetVPNGatewayArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the VPN gateway.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The project in which the resource belongs. If it
        /// is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The region in which the resource belongs. If it
        /// is not provided, the project region is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public GetVPNGatewayArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetVPNGatewayResult
    {
        /// <summary>
        /// Description of this VPN gateway.
        /// </summary>
        public readonly string Description;
        public readonly string Name;
        /// <summary>
        /// The network of this VPN gateway.
        /// </summary>
        public readonly string Network;
        public readonly string Project;
        /// <summary>
        /// Region of this VPN gateway.
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// The URI of the resource.
        /// </summary>
        public readonly string SelfLink;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetVPNGatewayResult(
            string description,
            string name,
            string network,
            string project,
            string region,
            string selfLink,
            string id)
        {
            Description = description;
            Name = name;
            Network = network;
            Project = project;
            Region = region;
            SelfLink = selfLink;
            Id = id;
        }
    }
}