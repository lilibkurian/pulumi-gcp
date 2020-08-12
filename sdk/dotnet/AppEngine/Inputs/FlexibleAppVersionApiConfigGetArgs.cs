// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.AppEngine.Inputs
{

    public sealed class FlexibleAppVersionApiConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Action to take when users access resources that require authentication.
        /// Default value is `AUTH_FAIL_ACTION_REDIRECT`.
        /// Possible values are `AUTH_FAIL_ACTION_REDIRECT` and `AUTH_FAIL_ACTION_UNAUTHORIZED`.
        /// </summary>
        [Input("authFailAction")]
        public Input<string>? AuthFailAction { get; set; }

        /// <summary>
        /// Level of login required to access this resource.
        /// Default value is `LOGIN_OPTIONAL`.
        /// Possible values are `LOGIN_OPTIONAL`, `LOGIN_ADMIN`, and `LOGIN_REQUIRED`.
        /// </summary>
        [Input("login")]
        public Input<string>? Login { get; set; }

        /// <summary>
        /// Path to the script from the application root directory.
        /// </summary>
        [Input("script", required: true)]
        public Input<string> Script { get; set; } = null!;

        /// <summary>
        /// Security (HTTPS) enforcement for this URL.
        /// Possible values are `SECURE_DEFAULT`, `SECURE_NEVER`, `SECURE_OPTIONAL`, and `SECURE_ALWAYS`.
        /// </summary>
        [Input("securityLevel")]
        public Input<string>? SecurityLevel { get; set; }

        /// <summary>
        /// URL to serve the endpoint at.
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        public FlexibleAppVersionApiConfigGetArgs()
        {
        }
    }
}
