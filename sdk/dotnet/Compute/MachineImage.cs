// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    /// <summary>
    /// Represents a MachineImage resource. Machine images store all the configuration,
    /// metadata, permissions, and data from one or more disks required to create a
    /// Virtual machine (VM) instance.
    /// 
    /// To get more information about MachineImage, see:
    /// 
    /// * [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/machineImages)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/compute/docs/machine-images)
    /// 
    /// ## Example Usage
    /// </summary>
    public partial class MachineImage : Pulumi.CustomResource
    {
        /// <summary>
        /// A text description of the resource.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Name of the resource.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        /// <summary>
        /// The source instance used to create the machine image. You can provide this as a partial or full URL to the resource.
        /// </summary>
        [Output("sourceInstance")]
        public Output<string> SourceInstance { get; private set; } = null!;


        /// <summary>
        /// Create a MachineImage resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MachineImage(string name, MachineImageArgs args, CustomResourceOptions? options = null)
            : base("gcp:compute/machineImage:MachineImage", name, args ?? new MachineImageArgs(), MakeResourceOptions(options, ""))
        {
        }

        private MachineImage(string name, Input<string> id, MachineImageState? state = null, CustomResourceOptions? options = null)
            : base("gcp:compute/machineImage:MachineImage", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing MachineImage resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MachineImage Get(string name, Input<string> id, MachineImageState? state = null, CustomResourceOptions? options = null)
        {
            return new MachineImage(name, id, state, options);
        }
    }

    public sealed class MachineImageArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A text description of the resource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Name of the resource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The source instance used to create the machine image. You can provide this as a partial or full URL to the resource.
        /// </summary>
        [Input("sourceInstance", required: true)]
        public Input<string> SourceInstance { get; set; } = null!;

        public MachineImageArgs()
        {
        }
    }

    public sealed class MachineImageState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A text description of the resource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Name of the resource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        /// <summary>
        /// The source instance used to create the machine image. You can provide this as a partial or full URL to the resource.
        /// </summary>
        [Input("sourceInstance")]
        public Input<string>? SourceInstance { get; set; }

        public MachineImageState()
        {
        }
    }
}
