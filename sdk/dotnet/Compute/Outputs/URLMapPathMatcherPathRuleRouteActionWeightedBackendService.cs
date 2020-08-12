// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Outputs
{

    [OutputType]
    public sealed class URLMapPathMatcherPathRuleRouteActionWeightedBackendService
    {
        /// <summary>
        /// The full or partial URL to the BackendService resource being mirrored to.
        /// </summary>
        public readonly string BackendService;
        /// <summary>
        /// Specifies changes to request and response headers that need to take effect for
        /// the selected backendService.
        /// headerAction specified here take effect before headerAction in the enclosing
        /// HttpRouteRule, PathMatcher and UrlMap.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderAction? HeaderAction;
        /// <summary>
        /// Specifies the fraction of traffic sent to backendService, computed as
        /// weight / (sum of all weightedBackendService weights in routeAction) .
        /// The selection of a backend service is determined only for new traffic. Once a user's request
        /// has been directed to a backendService, subsequent requests will be sent to the same backendService
        /// as determined by the BackendService's session affinity policy.
        /// The value must be between 0 and 1000
        /// </summary>
        public readonly int Weight;

        [OutputConstructor]
        private URLMapPathMatcherPathRuleRouteActionWeightedBackendService(
            string backendService,

            Outputs.URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderAction? headerAction,

            int weight)
        {
            BackendService = backendService;
            HeaderAction = headerAction;
            Weight = weight;
        }
    }
}
