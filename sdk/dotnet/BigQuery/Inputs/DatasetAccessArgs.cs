// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.BigQuery.Inputs
{

    public sealed class DatasetAccessArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A domain to grant access to. Any users signed in with the
        /// domain specified will be granted the specified access
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        /// <summary>
        /// An email address of a Google Group to grant access to.
        /// </summary>
        [Input("groupByEmail")]
        public Input<string>? GroupByEmail { get; set; }

        /// <summary>
        /// Describes the rights granted to the user specified by the other
        /// member of the access object. Primitive, Predefined and custom
        /// roles are supported. Predefined roles that have equivalent
        /// primitive roles are swapped by the API to their Primitive
        /// counterparts. See
        /// [official docs](https://cloud.google.com/bigquery/docs/access-control).
        /// </summary>
        [Input("role")]
        public Input<string>? Role { get; set; }

        /// <summary>
        /// A special group to grant access to. Possible values include:
        /// </summary>
        [Input("specialGroup")]
        public Input<string>? SpecialGroup { get; set; }

        /// <summary>
        /// An email address of a user to grant access to. For example:
        /// fred@example.com
        /// </summary>
        [Input("userByEmail")]
        public Input<string>? UserByEmail { get; set; }

        /// <summary>
        /// A view from a different dataset to grant access to. Queries
        /// executed against that view will have read access to tables in
        /// this dataset. The role field is not required when this field is
        /// set. If that view is updated by any user, access to the view
        /// needs to be granted again via an update operation.
        /// Structure is documented below.
        /// </summary>
        [Input("view")]
        public Input<Inputs.DatasetAccessViewArgs>? View { get; set; }

        public DatasetAccessArgs()
        {
        }
    }
}
