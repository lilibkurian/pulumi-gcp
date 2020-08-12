// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.AppEngine.Outputs
{

    [OutputType]
    public sealed class FlexibleAppVersionApiConfig
    {
        /// <summary>
        /// Action to take when users access resources that require authentication.
        /// Default value is `AUTH_FAIL_ACTION_REDIRECT`.
        /// Possible values are `AUTH_FAIL_ACTION_REDIRECT` and `AUTH_FAIL_ACTION_UNAUTHORIZED`.
        /// </summary>
        public readonly string? AuthFailAction;
        /// <summary>
        /// Level of login required to access this resource.
        /// Default value is `LOGIN_OPTIONAL`.
        /// Possible values are `LOGIN_OPTIONAL`, `LOGIN_ADMIN`, and `LOGIN_REQUIRED`.
        /// </summary>
        public readonly string? Login;
        /// <summary>
        /// Path to the script from the application root directory.
        /// </summary>
        public readonly string Script;
        /// <summary>
        /// Security (HTTPS) enforcement for this URL.
        /// Possible values are `SECURE_DEFAULT`, `SECURE_NEVER`, `SECURE_OPTIONAL`, and `SECURE_ALWAYS`.
        /// </summary>
        public readonly string? SecurityLevel;
        /// <summary>
        /// URL to serve the endpoint at.
        /// </summary>
        public readonly string? Url;

        [OutputConstructor]
        private FlexibleAppVersionApiConfig(
            string? authFailAction,

            string? login,

            string script,

            string? securityLevel,

            string? url)
        {
            AuthFailAction = authFailAction;
            Login = login;
            Script = script;
            SecurityLevel = securityLevel;
            Url = url;
        }
    }
}
