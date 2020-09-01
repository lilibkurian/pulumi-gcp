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
    public sealed class StandardAppVersionVpcAccessConnector
    {
        /// <summary>
        /// Full Serverless VPC Access Connector name e.g. /projects/my-project/locations/us-central1/connectors/c1.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private StandardAppVersionVpcAccessConnector(string name)
        {
            Name = name;
        }
    }
}
