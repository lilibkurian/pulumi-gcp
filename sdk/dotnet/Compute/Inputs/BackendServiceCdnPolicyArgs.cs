// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class BackendServiceCdnPolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The CacheKeyPolicy for this CdnPolicy.
        /// Structure is documented below.
        /// </summary>
        [Input("cacheKeyPolicy")]
        public Input<Inputs.BackendServiceCdnPolicyCacheKeyPolicyArgs>? CacheKeyPolicy { get; set; }

        /// <summary>
        /// Maximum number of seconds the response to a signed URL request
        /// will be considered fresh, defaults to 1hr (3600s). After this
        /// time period, the response will be revalidated before
        /// being served.
        /// When serving responses to signed URL requests, Cloud CDN will
        /// internally behave as though all responses from this backend had a
        /// "Cache-Control: public, max-age=[TTL]" header, regardless of any
        /// existing Cache-Control header. The actual headers served in
        /// responses will not be altered.
        /// </summary>
        [Input("signedUrlCacheMaxAgeSec")]
        public Input<int>? SignedUrlCacheMaxAgeSec { get; set; }

        public BackendServiceCdnPolicyArgs()
        {
        }
    }
}
