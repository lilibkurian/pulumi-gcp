// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Redis
{
    /// <summary>
    /// A Google Cloud Redis instance.
    /// 
    /// To get more information about Instance, see:
    /// 
    /// * [API documentation](https://cloud.google.com/memorystore/docs/redis/reference/rest/)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/memorystore/docs/redis/)
    /// 
    /// ## Example Usage
    /// </summary>
    public partial class Instance : Pulumi.CustomResource
    {
        /// <summary>
        /// Only applicable to STANDARD_HA tier which protects the instance
        /// against zonal failures by provisioning it across two zones.
        /// If provided, it must be a different zone from the one provided in
        /// [locationId].
        /// </summary>
        [Output("alternativeLocationId")]
        public Output<string> AlternativeLocationId { get; private set; } = null!;

        /// <summary>
        /// The full name of the Google Compute Engine network to which the
        /// instance is connected. If left unspecified, the default network
        /// will be used.
        /// </summary>
        [Output("authorizedNetwork")]
        public Output<string> AuthorizedNetwork { get; private set; } = null!;

        /// <summary>
        /// The connection mode of the Redis instance.
        /// Default value is `DIRECT_PEERING`.
        /// Possible values are `DIRECT_PEERING` and `PRIVATE_SERVICE_ACCESS`.
        /// </summary>
        [Output("connectMode")]
        public Output<string?> ConnectMode { get; private set; } = null!;

        /// <summary>
        /// The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
        /// [locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
        /// [alternativeLocationId] and can change after a failover event.
        /// </summary>
        [Output("currentLocationId")]
        public Output<string> CurrentLocationId { get; private set; } = null!;

        /// <summary>
        /// An arbitrary and optional user-provided name for the instance.
        /// </summary>
        [Output("displayName")]
        public Output<string?> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
        /// </summary>
        [Output("host")]
        public Output<string> Host { get; private set; } = null!;

        /// <summary>
        /// Resource labels to represent user provided metadata.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// The zone where the instance will be provisioned. If not provided,
        /// the service will choose a zone for the instance. For STANDARD_HA tier,
        /// instances will be created across two zones for protection against
        /// zonal failures. If [alternativeLocationId] is also provided, it must
        /// be different from [locationId].
        /// </summary>
        [Output("locationId")]
        public Output<string> LocationId { get; private set; } = null!;

        /// <summary>
        /// Redis memory size in GiB.
        /// </summary>
        [Output("memorySizeGb")]
        public Output<int> MemorySizeGb { get; private set; } = null!;

        /// <summary>
        /// The ID of the instance or a fully qualified identifier for the instance.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Output only. Cloud IAM identity used by import / export operations to transfer data to/from Cloud Storage. Format is
        /// "serviceAccount:". The value may change over time for a given instance so should be checked before each import/export
        /// operation.
        /// </summary>
        [Output("persistenceIamIdentity")]
        public Output<string> PersistenceIamIdentity { get; private set; } = null!;

        /// <summary>
        /// The port number of the exposed Redis endpoint.
        /// </summary>
        [Output("port")]
        public Output<int> Port { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// Redis configuration parameters, according to http://redis.io/topics/config.
        /// Please check Memorystore documentation for the list of supported parameters:
        /// https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
        /// </summary>
        [Output("redisConfigs")]
        public Output<ImmutableDictionary<string, string>?> RedisConfigs { get; private set; } = null!;

        /// <summary>
        /// The version of Redis software. If not provided, latest supported
        /// version will be used. Currently, the supported values are:
        /// - REDIS_5_0 for Redis 5.0 compatibility
        /// - REDIS_4_0 for Redis 4.0 compatibility
        /// - REDIS_3_2 for Redis 3.2 compatibility
        /// </summary>
        [Output("redisVersion")]
        public Output<string> RedisVersion { get; private set; } = null!;

        /// <summary>
        /// The name of the Redis region of the instance.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The CIDR range of internal addresses that are reserved for this
        /// instance. If not provided, the service will choose an unused /29
        /// block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
        /// unique and non-overlapping with existing subnets in an authorized
        /// network.
        /// </summary>
        [Output("reservedIpRange")]
        public Output<string> ReservedIpRange { get; private set; } = null!;

        /// <summary>
        /// The service tier of the instance. Must be one of these values:
        /// - BASIC: standalone instance
        /// - STANDARD_HA: highly available primary/replica instances
        /// Default value is `BASIC`.
        /// Possible values are `BASIC` and `STANDARD_HA`.
        /// </summary>
        [Output("tier")]
        public Output<string?> Tier { get; private set; } = null!;


        /// <summary>
        /// Create a Instance resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Instance(string name, InstanceArgs args, CustomResourceOptions? options = null)
            : base("gcp:redis/instance:Instance", name, args ?? new InstanceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Instance(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
            : base("gcp:redis/instance:Instance", name, state, MakeResourceOptions(options, id))
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
        /// Only applicable to STANDARD_HA tier which protects the instance
        /// against zonal failures by provisioning it across two zones.
        /// If provided, it must be a different zone from the one provided in
        /// [locationId].
        /// </summary>
        [Input("alternativeLocationId")]
        public Input<string>? AlternativeLocationId { get; set; }

        /// <summary>
        /// The full name of the Google Compute Engine network to which the
        /// instance is connected. If left unspecified, the default network
        /// will be used.
        /// </summary>
        [Input("authorizedNetwork")]
        public Input<string>? AuthorizedNetwork { get; set; }

        /// <summary>
        /// The connection mode of the Redis instance.
        /// Default value is `DIRECT_PEERING`.
        /// Possible values are `DIRECT_PEERING` and `PRIVATE_SERVICE_ACCESS`.
        /// </summary>
        [Input("connectMode")]
        public Input<string>? ConnectMode { get; set; }

        /// <summary>
        /// An arbitrary and optional user-provided name for the instance.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Resource labels to represent user provided metadata.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The zone where the instance will be provisioned. If not provided,
        /// the service will choose a zone for the instance. For STANDARD_HA tier,
        /// instances will be created across two zones for protection against
        /// zonal failures. If [alternativeLocationId] is also provided, it must
        /// be different from [locationId].
        /// </summary>
        [Input("locationId")]
        public Input<string>? LocationId { get; set; }

        /// <summary>
        /// Redis memory size in GiB.
        /// </summary>
        [Input("memorySizeGb", required: true)]
        public Input<int> MemorySizeGb { get; set; } = null!;

        /// <summary>
        /// The ID of the instance or a fully qualified identifier for the instance.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("redisConfigs")]
        private InputMap<string>? _redisConfigs;

        /// <summary>
        /// Redis configuration parameters, according to http://redis.io/topics/config.
        /// Please check Memorystore documentation for the list of supported parameters:
        /// https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
        /// </summary>
        public InputMap<string> RedisConfigs
        {
            get => _redisConfigs ?? (_redisConfigs = new InputMap<string>());
            set => _redisConfigs = value;
        }

        /// <summary>
        /// The version of Redis software. If not provided, latest supported
        /// version will be used. Currently, the supported values are:
        /// - REDIS_5_0 for Redis 5.0 compatibility
        /// - REDIS_4_0 for Redis 4.0 compatibility
        /// - REDIS_3_2 for Redis 3.2 compatibility
        /// </summary>
        [Input("redisVersion")]
        public Input<string>? RedisVersion { get; set; }

        /// <summary>
        /// The name of the Redis region of the instance.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The CIDR range of internal addresses that are reserved for this
        /// instance. If not provided, the service will choose an unused /29
        /// block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
        /// unique and non-overlapping with existing subnets in an authorized
        /// network.
        /// </summary>
        [Input("reservedIpRange")]
        public Input<string>? ReservedIpRange { get; set; }

        /// <summary>
        /// The service tier of the instance. Must be one of these values:
        /// - BASIC: standalone instance
        /// - STANDARD_HA: highly available primary/replica instances
        /// Default value is `BASIC`.
        /// Possible values are `BASIC` and `STANDARD_HA`.
        /// </summary>
        [Input("tier")]
        public Input<string>? Tier { get; set; }

        public InstanceArgs()
        {
        }
    }

    public sealed class InstanceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Only applicable to STANDARD_HA tier which protects the instance
        /// against zonal failures by provisioning it across two zones.
        /// If provided, it must be a different zone from the one provided in
        /// [locationId].
        /// </summary>
        [Input("alternativeLocationId")]
        public Input<string>? AlternativeLocationId { get; set; }

        /// <summary>
        /// The full name of the Google Compute Engine network to which the
        /// instance is connected. If left unspecified, the default network
        /// will be used.
        /// </summary>
        [Input("authorizedNetwork")]
        public Input<string>? AuthorizedNetwork { get; set; }

        /// <summary>
        /// The connection mode of the Redis instance.
        /// Default value is `DIRECT_PEERING`.
        /// Possible values are `DIRECT_PEERING` and `PRIVATE_SERVICE_ACCESS`.
        /// </summary>
        [Input("connectMode")]
        public Input<string>? ConnectMode { get; set; }

        /// <summary>
        /// The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
        /// </summary>
        [Input("createTime")]
        public Input<string>? CreateTime { get; set; }

        /// <summary>
        /// The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
        /// [locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
        /// [alternativeLocationId] and can change after a failover event.
        /// </summary>
        [Input("currentLocationId")]
        public Input<string>? CurrentLocationId { get; set; }

        /// <summary>
        /// An arbitrary and optional user-provided name for the instance.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
        /// </summary>
        [Input("host")]
        public Input<string>? Host { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Resource labels to represent user provided metadata.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The zone where the instance will be provisioned. If not provided,
        /// the service will choose a zone for the instance. For STANDARD_HA tier,
        /// instances will be created across two zones for protection against
        /// zonal failures. If [alternativeLocationId] is also provided, it must
        /// be different from [locationId].
        /// </summary>
        [Input("locationId")]
        public Input<string>? LocationId { get; set; }

        /// <summary>
        /// Redis memory size in GiB.
        /// </summary>
        [Input("memorySizeGb")]
        public Input<int>? MemorySizeGb { get; set; }

        /// <summary>
        /// The ID of the instance or a fully qualified identifier for the instance.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Output only. Cloud IAM identity used by import / export operations to transfer data to/from Cloud Storage. Format is
        /// "serviceAccount:". The value may change over time for a given instance so should be checked before each import/export
        /// operation.
        /// </summary>
        [Input("persistenceIamIdentity")]
        public Input<string>? PersistenceIamIdentity { get; set; }

        /// <summary>
        /// The port number of the exposed Redis endpoint.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("redisConfigs")]
        private InputMap<string>? _redisConfigs;

        /// <summary>
        /// Redis configuration parameters, according to http://redis.io/topics/config.
        /// Please check Memorystore documentation for the list of supported parameters:
        /// https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
        /// </summary>
        public InputMap<string> RedisConfigs
        {
            get => _redisConfigs ?? (_redisConfigs = new InputMap<string>());
            set => _redisConfigs = value;
        }

        /// <summary>
        /// The version of Redis software. If not provided, latest supported
        /// version will be used. Currently, the supported values are:
        /// - REDIS_5_0 for Redis 5.0 compatibility
        /// - REDIS_4_0 for Redis 4.0 compatibility
        /// - REDIS_3_2 for Redis 3.2 compatibility
        /// </summary>
        [Input("redisVersion")]
        public Input<string>? RedisVersion { get; set; }

        /// <summary>
        /// The name of the Redis region of the instance.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The CIDR range of internal addresses that are reserved for this
        /// instance. If not provided, the service will choose an unused /29
        /// block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
        /// unique and non-overlapping with existing subnets in an authorized
        /// network.
        /// </summary>
        [Input("reservedIpRange")]
        public Input<string>? ReservedIpRange { get; set; }

        /// <summary>
        /// The service tier of the instance. Must be one of these values:
        /// - BASIC: standalone instance
        /// - STANDARD_HA: highly available primary/replica instances
        /// Default value is `BASIC`.
        /// Possible values are `BASIC` and `STANDARD_HA`.
        /// </summary>
        [Input("tier")]
        public Input<string>? Tier { get; set; }

        public InstanceState()
        {
        }
    }
}
