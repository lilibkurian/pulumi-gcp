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
    public sealed class StandardAppVersionHandler
    {
        /// <summary>
        /// Actions to take when the user is not logged in.
        /// </summary>
        public readonly string? AuthFailAction;
        /// <summary>
        /// Methods to restrict access to a URL based on login status.
        /// </summary>
        public readonly string? Login;
        /// <summary>
        /// 30x code to use when performing redirects for the secure field.
        /// </summary>
        public readonly string? RedirectHttpResponseCode;
        /// <summary>
        /// Executes a script to handle the requests that match this URL pattern.
        /// Only the auto value is supported for Node.js in the App Engine standard environment, for example "script:" "auto".  Structure is documented below.
        /// </summary>
        public readonly Outputs.StandardAppVersionHandlerScript? Script;
        /// <summary>
        /// Security (HTTPS) enforcement for this URL.
        /// </summary>
        public readonly string? SecurityLevel;
        /// <summary>
        /// Files served directly to the user for a given URL, such as images, CSS stylesheets, or JavaScript source files. Static file handlers describe which files in the application directory are static files, and which URLs serve them.  Structure is documented below.
        /// </summary>
        public readonly Outputs.StandardAppVersionHandlerStaticFiles? StaticFiles;
        /// <summary>
        /// URL prefix. Uses regular expression syntax, which means regexp special characters must be escaped, but should not contain groupings.
        /// All URLs that begin with this prefix are handled by this handler, using the portion of the URL after the prefix as part of the file path.
        /// </summary>
        public readonly string? UrlRegex;

        [OutputConstructor]
        private StandardAppVersionHandler(
            string? authFailAction,

            string? login,

            string? redirectHttpResponseCode,

            Outputs.StandardAppVersionHandlerScript? script,

            string? securityLevel,

            Outputs.StandardAppVersionHandlerStaticFiles? staticFiles,

            string? urlRegex)
        {
            AuthFailAction = authFailAction;
            Login = login;
            RedirectHttpResponseCode = redirectHttpResponseCode;
            Script = script;
            SecurityLevel = securityLevel;
            StaticFiles = staticFiles;
            UrlRegex = urlRegex;
        }
    }
}