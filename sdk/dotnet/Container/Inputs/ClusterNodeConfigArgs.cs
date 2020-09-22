// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Container.Inputs
{

    public sealed class ClusterNodeConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption
        /// </summary>
        [Input("bootDiskKmsKey")]
        public Input<string>? BootDiskKmsKey { get; set; }

        /// <summary>
        /// Size of the disk attached to each node, specified
        /// in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.
        /// </summary>
        [Input("diskSizeGb")]
        public Input<int>? DiskSizeGb { get; set; }

        /// <summary>
        /// Type of the disk attached to each node
        /// (e.g. 'pd-standard', 'pd-balanced' or 'pd-ssd'). If unspecified, the default disk type is 'pd-standard'
        /// </summary>
        [Input("diskType")]
        public Input<string>? DiskType { get; set; }

        [Input("guestAccelerators")]
        private InputList<Inputs.ClusterNodeConfigGuestAcceleratorArgs>? _guestAccelerators;

        /// <summary>
        /// List of the type and count of accelerator cards attached to the instance.
        /// Structure documented below.
        /// </summary>
        public InputList<Inputs.ClusterNodeConfigGuestAcceleratorArgs> GuestAccelerators
        {
            get => _guestAccelerators ?? (_guestAccelerators = new InputList<Inputs.ClusterNodeConfigGuestAcceleratorArgs>());
            set => _guestAccelerators = value;
        }

        /// <summary>
        /// The image type to use for this node. Note that changing the image type
        /// will delete and recreate all nodes in the node pool.
        /// </summary>
        [Input("imageType")]
        public Input<string>? ImageType { get; set; }

        /// <summary>
        /// Kubelet configuration, currently supported attributes can be found [here](https://cloud.google.com/sdk/gcloud/reference/beta/container/node-pools/create#--system-config-from-file).
        /// Structure is documented below.
        /// </summary>
        [Input("kubeletConfig")]
        public Input<Inputs.ClusterNodeConfigKubeletConfigArgs>? KubeletConfig { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// The Kubernetes labels (key/value pairs) to be applied to each node. The kubernetes.io/ and k8s.io/ prefixes are
        /// reserved by Kubernetes Core components and cannot be specified.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// Linux node configuration, currently supported attributes can be found [here](https://cloud.google.com/sdk/gcloud/reference/beta/container/node-pools/create#--system-config-from-file).
        /// Note that validations happen all server side. All attributes are optional.
        /// Structure is documented below.
        /// </summary>
        [Input("linuxNodeConfig")]
        public Input<Inputs.ClusterNodeConfigLinuxNodeConfigArgs>? LinuxNodeConfig { get; set; }

        /// <summary>
        /// The amount of local SSD disks that will be
        /// attached to each cluster node. Defaults to 0.
        /// </summary>
        [Input("localSsdCount")]
        public Input<int>? LocalSsdCount { get; set; }

        /// <summary>
        /// The name of a Google Compute Engine machine type.
        /// Defaults to `e2-medium`. To create a custom machine type, value should be set as specified
        /// [here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
        /// </summary>
        [Input("machineType")]
        public Input<string>? MachineType { get; set; }

        [Input("metadata")]
        private InputMap<string>? _metadata;

        /// <summary>
        /// The metadata key/value pairs assigned to instances in
        /// the cluster. From GKE `1.12` onwards, `disable-legacy-endpoints` is set to
        /// `true` by the API; if `metadata` is set but that default value is not
        /// included, the provider will attempt to unset the value. To avoid this, set the
        /// value in your config.
        /// </summary>
        public InputMap<string> Metadata
        {
            get => _metadata ?? (_metadata = new InputMap<string>());
            set => _metadata = value;
        }

        /// <summary>
        /// Minimum CPU platform to be used by this instance.
        /// The instance may be scheduled on the specified or newer CPU platform. Applicable
        /// values are the friendly names of CPU platforms, such as `Intel Haswell`. See the
        /// [official documentation](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
        /// for more information.
        /// </summary>
        [Input("minCpuPlatform")]
        public Input<string>? MinCpuPlatform { get; set; }

        [Input("oauthScopes")]
        private InputList<string>? _oauthScopes;

        /// <summary>
        /// The set of Google API scopes to be made available
        /// on all of the node VMs under the "default" service account. These can be
        /// either FQDNs, or scope aliases. The following scopes are necessary to ensure
        /// the correct functioning of the cluster:
        /// </summary>
        public InputList<string> OauthScopes
        {
            get => _oauthScopes ?? (_oauthScopes = new InputList<string>());
            set => _oauthScopes = value;
        }

        /// <summary>
        /// A boolean that represents whether or not the underlying node VMs
        /// are preemptible. See the [official documentation](https://cloud.google.com/container-engine/docs/preemptible-vm)
        /// for more information. Defaults to false.
        /// </summary>
        [Input("preemptible")]
        public Input<bool>? Preemptible { get; set; }

        /// <summary>
        /// [GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) configuration. When enabling this feature you must specify `image_type = "COS_CONTAINERD"` and `node_version = "1.12.7-gke.17"` or later to use it.
        /// Structure is documented below.
        /// </summary>
        [Input("sandboxConfig")]
        public Input<Inputs.ClusterNodeConfigSandboxConfigArgs>? SandboxConfig { get; set; }

        /// <summary>
        /// The service account to be used by the Node VMs.
        /// If not specified, the "default" service account is used.
        /// In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
        /// [roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
        /// [roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
        /// </summary>
        [Input("serviceAccount")]
        public Input<string>? ServiceAccount { get; set; }

        /// <summary>
        /// Shielded Instance options. Structure is documented below.
        /// </summary>
        [Input("shieldedInstanceConfig")]
        public Input<Inputs.ClusterNodeConfigShieldedInstanceConfigArgs>? ShieldedInstanceConfig { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// The list of instance tags applied to all nodes. Tags are used to identify
        /// valid sources or targets for network firewalls.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        [Input("taints")]
        private InputList<Inputs.ClusterNodeConfigTaintArgs>? _taints;

        /// <summary>
        /// A list of [Kubernetes taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)
        /// to apply to nodes. GKE's API can only set this field on cluster creation.
        /// However, GKE will add taints to your nodes if you enable certain features such
        /// as GPUs. If this field is set, any diffs on this field will cause the provider to
        /// recreate the underlying resource. Taint values can be updated safely in
        /// Kubernetes (eg. through `kubectl`), and it's recommended that you do not use
        /// this field to manage taints. If you do, `lifecycle.ignore_changes` is
        /// recommended. Structure is documented below.
        /// </summary>
        public InputList<Inputs.ClusterNodeConfigTaintArgs> Taints
        {
            get => _taints ?? (_taints = new InputList<Inputs.ClusterNodeConfigTaintArgs>());
            set => _taints = value;
        }

        /// <summary>
        /// Metadata configuration to expose to workloads on the node pool.
        /// Structure is documented below.
        /// </summary>
        [Input("workloadMetadataConfig")]
        public Input<Inputs.ClusterNodeConfigWorkloadMetadataConfigArgs>? WorkloadMetadataConfig { get; set; }

        public ClusterNodeConfigArgs()
        {
        }
    }
}
