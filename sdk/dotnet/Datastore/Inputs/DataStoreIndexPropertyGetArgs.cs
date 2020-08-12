// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Datastore.Inputs
{

    public sealed class DataStoreIndexPropertyGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The direction the index should optimize for sorting.
        /// Possible values are `ASCENDING` and `DESCENDING`.
        /// </summary>
        [Input("direction", required: true)]
        public Input<string> Direction { get; set; } = null!;

        /// <summary>
        /// The property name to index.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public DataStoreIndexPropertyGetArgs()
        {
        }
    }
}
