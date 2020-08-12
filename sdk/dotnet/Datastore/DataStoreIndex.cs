// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Datastore
{
    /// <summary>
    /// Describes a composite index for Cloud Datastore.
    /// 
    /// To get more information about Index, see:
    /// 
    /// * [API documentation](https://cloud.google.com/datastore/docs/reference/admin/rest/v1/projects.indexes)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/datastore/docs/concepts/indexes)
    /// 
    /// ## Example Usage
    /// </summary>
    public partial class DataStoreIndex : Pulumi.CustomResource
    {
        /// <summary>
        /// Policy for including ancestors in the index.
        /// Default value is `NONE`.
        /// Possible values are `NONE` and `ALL_ANCESTORS`.
        /// </summary>
        [Output("ancestor")]
        public Output<string?> Ancestor { get; private set; } = null!;

        /// <summary>
        /// The index id.
        /// </summary>
        [Output("indexId")]
        public Output<string> IndexId { get; private set; } = null!;

        /// <summary>
        /// The entity kind which the index applies to.
        /// </summary>
        [Output("kind")]
        public Output<string> Kind { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// An ordered list of properties to index on.
        /// Structure is documented below.
        /// </summary>
        [Output("properties")]
        public Output<ImmutableArray<Outputs.DataStoreIndexProperty>> Properties { get; private set; } = null!;


        /// <summary>
        /// Create a DataStoreIndex resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataStoreIndex(string name, DataStoreIndexArgs args, CustomResourceOptions? options = null)
            : base("gcp:datastore/dataStoreIndex:DataStoreIndex", name, args ?? new DataStoreIndexArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataStoreIndex(string name, Input<string> id, DataStoreIndexState? state = null, CustomResourceOptions? options = null)
            : base("gcp:datastore/dataStoreIndex:DataStoreIndex", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DataStoreIndex resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataStoreIndex Get(string name, Input<string> id, DataStoreIndexState? state = null, CustomResourceOptions? options = null)
        {
            return new DataStoreIndex(name, id, state, options);
        }
    }

    public sealed class DataStoreIndexArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Policy for including ancestors in the index.
        /// Default value is `NONE`.
        /// Possible values are `NONE` and `ALL_ANCESTORS`.
        /// </summary>
        [Input("ancestor")]
        public Input<string>? Ancestor { get; set; }

        /// <summary>
        /// The entity kind which the index applies to.
        /// </summary>
        [Input("kind", required: true)]
        public Input<string> Kind { get; set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("properties")]
        private InputList<Inputs.DataStoreIndexPropertyArgs>? _properties;

        /// <summary>
        /// An ordered list of properties to index on.
        /// Structure is documented below.
        /// </summary>
        public InputList<Inputs.DataStoreIndexPropertyArgs> Properties
        {
            get => _properties ?? (_properties = new InputList<Inputs.DataStoreIndexPropertyArgs>());
            set => _properties = value;
        }

        public DataStoreIndexArgs()
        {
        }
    }

    public sealed class DataStoreIndexState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Policy for including ancestors in the index.
        /// Default value is `NONE`.
        /// Possible values are `NONE` and `ALL_ANCESTORS`.
        /// </summary>
        [Input("ancestor")]
        public Input<string>? Ancestor { get; set; }

        /// <summary>
        /// The index id.
        /// </summary>
        [Input("indexId")]
        public Input<string>? IndexId { get; set; }

        /// <summary>
        /// The entity kind which the index applies to.
        /// </summary>
        [Input("kind")]
        public Input<string>? Kind { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("properties")]
        private InputList<Inputs.DataStoreIndexPropertyGetArgs>? _properties;

        /// <summary>
        /// An ordered list of properties to index on.
        /// Structure is documented below.
        /// </summary>
        public InputList<Inputs.DataStoreIndexPropertyGetArgs> Properties
        {
            get => _properties ?? (_properties = new InputList<Inputs.DataStoreIndexPropertyGetArgs>());
            set => _properties = value;
        }

        public DataStoreIndexState()
        {
        }
    }
}
