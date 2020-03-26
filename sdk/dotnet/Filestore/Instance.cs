// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Filestore
{
    /// <summary>
    /// A Google Cloud Filestore instance.
    /// 
    /// 
    /// To get more information about Instance, see:
    /// 
    /// * [API documentation](https://cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/create)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/filestore/docs/creating-instances)
    ///     * [Use with Kubernetes](https://cloud.google.com/filestore/docs/accessing-fileshares)
    ///     * [Copying Data In/Out](https://cloud.google.com/filestore/docs/copying-data)
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/filestore_instance.html.markdown.
    /// </summary>
    public partial class Instance : Pulumi.CustomResource
    {
        /// <summary>
        /// Creation timestamp in RFC3339 text format.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// A description of the instance.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// File system shares on the instance. For this version, only a single file share is supported.
        /// </summary>
        [Output("fileShares")]
        public Output<Outputs.InstanceFileShares> FileShares { get; private set; } = null!;

        /// <summary>
        /// Resource labels to represent user-provided metadata.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// The resource name of the instance.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// VPC networks to which the instance is connected. For this version, only a single network is supported.
        /// </summary>
        [Output("networks")]
        public Output<ImmutableArray<Outputs.InstanceNetworks>> Networks { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The service tier of the instance.
        /// </summary>
        [Output("tier")]
        public Output<string> Tier { get; private set; } = null!;

        /// <summary>
        /// The name of the Filestore zone of the instance.
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a Instance resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Instance(string name, InstanceArgs args, CustomResourceOptions? options = null)
            : base("gcp:filestore/instance:Instance", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Instance(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
            : base("gcp:filestore/instance:Instance", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Instance resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Instance Get(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
        {
            return new Instance(name, id, state, options);
        }
    }

    public sealed class InstanceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description of the instance.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// File system shares on the instance. For this version, only a single file share is supported.
        /// </summary>
        [Input("fileShares", required: true)]
        public Input<Inputs.InstanceFileSharesArgs> FileShares { get; set; } = null!;

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Resource labels to represent user-provided metadata.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The resource name of the instance.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networks", required: true)]
        private InputList<Inputs.InstanceNetworksArgs>? _networks;

        /// <summary>
        /// VPC networks to which the instance is connected. For this version, only a single network is supported.
        /// </summary>
        public InputList<Inputs.InstanceNetworksArgs> Networks
        {
            get => _networks ?? (_networks = new InputList<Inputs.InstanceNetworksArgs>());
            set => _networks = value;
        }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The service tier of the instance.
        /// </summary>
        [Input("tier", required: true)]
        public Input<string> Tier { get; set; } = null!;

        /// <summary>
        /// The name of the Filestore zone of the instance.
        /// </summary>
        [Input("zone", required: true)]
        public Input<string> Zone { get; set; } = null!;

        public InstanceArgs()
        {
        }
    }

    public sealed class InstanceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Creation timestamp in RFC3339 text format.
        /// </summary>
        [Input("createTime")]
        public Input<string>? CreateTime { get; set; }

        /// <summary>
        /// A description of the instance.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// File system shares on the instance. For this version, only a single file share is supported.
        /// </summary>
        [Input("fileShares")]
        public Input<Inputs.InstanceFileSharesGetArgs>? FileShares { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Resource labels to represent user-provided metadata.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The resource name of the instance.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networks")]
        private InputList<Inputs.InstanceNetworksGetArgs>? _networks;

        /// <summary>
        /// VPC networks to which the instance is connected. For this version, only a single network is supported.
        /// </summary>
        public InputList<Inputs.InstanceNetworksGetArgs> Networks
        {
            get => _networks ?? (_networks = new InputList<Inputs.InstanceNetworksGetArgs>());
            set => _networks = value;
        }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The service tier of the instance.
        /// </summary>
        [Input("tier")]
        public Input<string>? Tier { get; set; }

        /// <summary>
        /// The name of the Filestore zone of the instance.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstanceState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class InstanceFileSharesArgs : Pulumi.ResourceArgs
    {
        [Input("capacityGb", required: true)]
        public Input<int> CapacityGb { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public InstanceFileSharesArgs()
        {
        }
    }

    public sealed class InstanceFileSharesGetArgs : Pulumi.ResourceArgs
    {
        [Input("capacityGb", required: true)]
        public Input<int> CapacityGb { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public InstanceFileSharesGetArgs()
        {
        }
    }

    public sealed class InstanceNetworksArgs : Pulumi.ResourceArgs
    {
        [Input("ipAddresses")]
        private InputList<string>? _ipAddresses;
        public InputList<string> IpAddresses
        {
            get => _ipAddresses ?? (_ipAddresses = new InputList<string>());
            set => _ipAddresses = value;
        }

        [Input("modes", required: true)]
        private InputList<string>? _modes;
        public InputList<string> Modes
        {
            get => _modes ?? (_modes = new InputList<string>());
            set => _modes = value;
        }

        [Input("network", required: true)]
        public Input<string> Network { get; set; } = null!;

        [Input("reservedIpRange")]
        public Input<string>? ReservedIpRange { get; set; }

        public InstanceNetworksArgs()
        {
        }
    }

    public sealed class InstanceNetworksGetArgs : Pulumi.ResourceArgs
    {
        [Input("ipAddresses")]
        private InputList<string>? _ipAddresses;
        public InputList<string> IpAddresses
        {
            get => _ipAddresses ?? (_ipAddresses = new InputList<string>());
            set => _ipAddresses = value;
        }

        [Input("modes", required: true)]
        private InputList<string>? _modes;
        public InputList<string> Modes
        {
            get => _modes ?? (_modes = new InputList<string>());
            set => _modes = value;
        }

        [Input("network", required: true)]
        public Input<string> Network { get; set; } = null!;

        [Input("reservedIpRange")]
        public Input<string>? ReservedIpRange { get; set; }

        public InstanceNetworksGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class InstanceFileShares
    {
        public readonly int CapacityGb;
        public readonly string Name;

        [OutputConstructor]
        private InstanceFileShares(
            int capacityGb,
            string name)
        {
            CapacityGb = capacityGb;
            Name = name;
        }
    }

    [OutputType]
    public sealed class InstanceNetworks
    {
        public readonly ImmutableArray<string> IpAddresses;
        public readonly ImmutableArray<string> Modes;
        public readonly string Network;
        public readonly string ReservedIpRange;

        [OutputConstructor]
        private InstanceNetworks(
            ImmutableArray<string> ipAddresses,
            ImmutableArray<string> modes,
            string network,
            string reservedIpRange)
        {
            IpAddresses = ipAddresses;
            Modes = modes;
            Network = network;
            ReservedIpRange = reservedIpRange;
        }
    }
    }
}
