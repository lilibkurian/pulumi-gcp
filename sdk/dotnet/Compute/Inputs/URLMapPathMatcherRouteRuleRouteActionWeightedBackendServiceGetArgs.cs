// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The full or partial URL to the BackendService resource being mirrored to.
        /// </summary>
        [Input("backendService", required: true)]
        public Input<string> BackendService { get; set; } = null!;

        /// <summary>
        /// Specifies changes to request and response headers that need to take effect for
        /// the selected backendService.
        /// headerAction specified here take effect before headerAction in the enclosing
        /// HttpRouteRule, PathMatcher and UrlMap.
        /// Structure is documented below.
        /// </summary>
        [Input("headerAction")]
        public Input<Inputs.URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderActionGetArgs>? HeaderAction { get; set; }

        /// <summary>
        /// Specifies the fraction of traffic sent to backendService, computed as
        /// weight / (sum of all weightedBackendService weights in routeAction) .
        /// The selection of a backend service is determined only for new traffic. Once a user's request
        /// has been directed to a backendService, subsequent requests will be sent to the same backendService
        /// as determined by the BackendService's session affinity policy.
        /// The value must be between 0 and 1000
        /// </summary>
        [Input("weight", required: true)]
        public Input<int> Weight { get; set; } = null!;

        public URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceGetArgs()
        {
        }
    }
}
