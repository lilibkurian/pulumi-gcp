// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The Google Compute Engine Regional Instance Group Manager API creates and manages pools
// of homogeneous Compute Engine virtual machine instances from a common instance
// template. For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups)
// and [API](https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers)
//
// > **Note:** Use [compute.InstanceGroupManager](https://www.terraform.io/docs/providers/google/r/compute_instance_group_manager.html) to create a single-zone instance group manager.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_instance_group_manager.html.markdown.
type RegionInstanceGroupManager struct {
	pulumi.CustomResourceState

	// The autohealing policies for this managed instance
	// group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).
	AutoHealingPolicies RegionInstanceGroupManagerAutoHealingPoliciesPtrOutput `pulumi:"autoHealingPolicies"`
	// The base instance name to use for
	// instances in this group. The value must be a valid
	// [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
	// are lowercase letters, numbers, and hyphens (-). Instances are named by
	// appending a hyphen and a random four-character string to the base instance
	// name.
	BaseInstanceName pulumi.StringOutput `pulumi:"baseInstanceName"`
	// An optional textual description of the instance
	// group manager.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The distribution policy for this managed instance
	// group. You can specify one or more values. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones).
	// - - -
	DistributionPolicyZones pulumi.StringArrayOutput `pulumi:"distributionPolicyZones"`
	// The fingerprint of the instance group manager.
	Fingerprint pulumi.StringOutput `pulumi:"fingerprint"`
	// The full URL of the instance group created by the manager.
	InstanceGroup pulumi.StringOutput `pulumi:"instanceGroup"`
	// - Version name.
	Name pulumi.StringOutput `pulumi:"name"`
	// The named port configuration. See the section below
	// for details on configuration.
	NamedPorts RegionInstanceGroupManagerNamedPortArrayOutput `pulumi:"namedPorts"`
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The region where the managed instance group resides.
	Region pulumi.StringOutput `pulumi:"region"`
	// The URL of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// The full URL of all target pools to which new
	// instances in the group are added. Updating the target pools attribute does
	// not affect existing instances.
	TargetPools pulumi.StringArrayOutput `pulumi:"targetPools"`
	// - The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.
	TargetSize pulumi.IntOutput `pulumi:"targetSize"`
	// The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch)
	UpdatePolicy RegionInstanceGroupManagerUpdatePolicyOutput `pulumi:"updatePolicy"`
	// Application versions managed by this instance group. Each
	// version deals with a specific instance template, allowing canary release scenarios.
	// Structure is documented below.
	Versions RegionInstanceGroupManagerVersionArrayOutput `pulumi:"versions"`
	// Whether to wait for all instances to be created/updated before
	// returning. Note that if this is set to true and the operation does not succeed, the provider will
	// continue trying until it times out.
	WaitForInstances pulumi.BoolPtrOutput `pulumi:"waitForInstances"`
}

// NewRegionInstanceGroupManager registers a new resource with the given unique name, arguments, and options.
func NewRegionInstanceGroupManager(ctx *pulumi.Context,
	name string, args *RegionInstanceGroupManagerArgs, opts ...pulumi.ResourceOption) (*RegionInstanceGroupManager, error) {
	if args == nil || args.BaseInstanceName == nil {
		return nil, errors.New("missing required argument 'BaseInstanceName'")
	}
	if args == nil || args.Region == nil {
		return nil, errors.New("missing required argument 'Region'")
	}
	if args == nil || args.Versions == nil {
		return nil, errors.New("missing required argument 'Versions'")
	}
	if args == nil {
		args = &RegionInstanceGroupManagerArgs{}
	}
	var resource RegionInstanceGroupManager
	err := ctx.RegisterResource("gcp:compute/regionInstanceGroupManager:RegionInstanceGroupManager", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRegionInstanceGroupManager gets an existing RegionInstanceGroupManager resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRegionInstanceGroupManager(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RegionInstanceGroupManagerState, opts ...pulumi.ResourceOption) (*RegionInstanceGroupManager, error) {
	var resource RegionInstanceGroupManager
	err := ctx.ReadResource("gcp:compute/regionInstanceGroupManager:RegionInstanceGroupManager", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RegionInstanceGroupManager resources.
type regionInstanceGroupManagerState struct {
	// The autohealing policies for this managed instance
	// group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).
	AutoHealingPolicies *RegionInstanceGroupManagerAutoHealingPolicies `pulumi:"autoHealingPolicies"`
	// The base instance name to use for
	// instances in this group. The value must be a valid
	// [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
	// are lowercase letters, numbers, and hyphens (-). Instances are named by
	// appending a hyphen and a random four-character string to the base instance
	// name.
	BaseInstanceName *string `pulumi:"baseInstanceName"`
	// An optional textual description of the instance
	// group manager.
	Description *string `pulumi:"description"`
	// The distribution policy for this managed instance
	// group. You can specify one or more values. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones).
	// - - -
	DistributionPolicyZones []string `pulumi:"distributionPolicyZones"`
	// The fingerprint of the instance group manager.
	Fingerprint *string `pulumi:"fingerprint"`
	// The full URL of the instance group created by the manager.
	InstanceGroup *string `pulumi:"instanceGroup"`
	// - Version name.
	Name *string `pulumi:"name"`
	// The named port configuration. See the section below
	// for details on configuration.
	NamedPorts []RegionInstanceGroupManagerNamedPort `pulumi:"namedPorts"`
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The region where the managed instance group resides.
	Region *string `pulumi:"region"`
	// The URL of the created resource.
	SelfLink *string `pulumi:"selfLink"`
	// The full URL of all target pools to which new
	// instances in the group are added. Updating the target pools attribute does
	// not affect existing instances.
	TargetPools []string `pulumi:"targetPools"`
	// - The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.
	TargetSize *int `pulumi:"targetSize"`
	// The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch)
	UpdatePolicy *RegionInstanceGroupManagerUpdatePolicy `pulumi:"updatePolicy"`
	// Application versions managed by this instance group. Each
	// version deals with a specific instance template, allowing canary release scenarios.
	// Structure is documented below.
	Versions []RegionInstanceGroupManagerVersion `pulumi:"versions"`
	// Whether to wait for all instances to be created/updated before
	// returning. Note that if this is set to true and the operation does not succeed, the provider will
	// continue trying until it times out.
	WaitForInstances *bool `pulumi:"waitForInstances"`
}

type RegionInstanceGroupManagerState struct {
	// The autohealing policies for this managed instance
	// group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).
	AutoHealingPolicies RegionInstanceGroupManagerAutoHealingPoliciesPtrInput
	// The base instance name to use for
	// instances in this group. The value must be a valid
	// [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
	// are lowercase letters, numbers, and hyphens (-). Instances are named by
	// appending a hyphen and a random four-character string to the base instance
	// name.
	BaseInstanceName pulumi.StringPtrInput
	// An optional textual description of the instance
	// group manager.
	Description pulumi.StringPtrInput
	// The distribution policy for this managed instance
	// group. You can specify one or more values. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones).
	// - - -
	DistributionPolicyZones pulumi.StringArrayInput
	// The fingerprint of the instance group manager.
	Fingerprint pulumi.StringPtrInput
	// The full URL of the instance group created by the manager.
	InstanceGroup pulumi.StringPtrInput
	// - Version name.
	Name pulumi.StringPtrInput
	// The named port configuration. See the section below
	// for details on configuration.
	NamedPorts RegionInstanceGroupManagerNamedPortArrayInput
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The region where the managed instance group resides.
	Region pulumi.StringPtrInput
	// The URL of the created resource.
	SelfLink pulumi.StringPtrInput
	// The full URL of all target pools to which new
	// instances in the group are added. Updating the target pools attribute does
	// not affect existing instances.
	TargetPools pulumi.StringArrayInput
	// - The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.
	TargetSize pulumi.IntPtrInput
	// The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch)
	UpdatePolicy RegionInstanceGroupManagerUpdatePolicyPtrInput
	// Application versions managed by this instance group. Each
	// version deals with a specific instance template, allowing canary release scenarios.
	// Structure is documented below.
	Versions RegionInstanceGroupManagerVersionArrayInput
	// Whether to wait for all instances to be created/updated before
	// returning. Note that if this is set to true and the operation does not succeed, the provider will
	// continue trying until it times out.
	WaitForInstances pulumi.BoolPtrInput
}

func (RegionInstanceGroupManagerState) ElementType() reflect.Type {
	return reflect.TypeOf((*regionInstanceGroupManagerState)(nil)).Elem()
}

type regionInstanceGroupManagerArgs struct {
	// The autohealing policies for this managed instance
	// group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).
	AutoHealingPolicies *RegionInstanceGroupManagerAutoHealingPolicies `pulumi:"autoHealingPolicies"`
	// The base instance name to use for
	// instances in this group. The value must be a valid
	// [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
	// are lowercase letters, numbers, and hyphens (-). Instances are named by
	// appending a hyphen and a random four-character string to the base instance
	// name.
	BaseInstanceName string `pulumi:"baseInstanceName"`
	// An optional textual description of the instance
	// group manager.
	Description *string `pulumi:"description"`
	// The distribution policy for this managed instance
	// group. You can specify one or more values. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones).
	// - - -
	DistributionPolicyZones []string `pulumi:"distributionPolicyZones"`
	// - Version name.
	Name *string `pulumi:"name"`
	// The named port configuration. See the section below
	// for details on configuration.
	NamedPorts []RegionInstanceGroupManagerNamedPort `pulumi:"namedPorts"`
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The region where the managed instance group resides.
	Region string `pulumi:"region"`
	// The full URL of all target pools to which new
	// instances in the group are added. Updating the target pools attribute does
	// not affect existing instances.
	TargetPools []string `pulumi:"targetPools"`
	// - The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.
	TargetSize *int `pulumi:"targetSize"`
	// The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch)
	UpdatePolicy *RegionInstanceGroupManagerUpdatePolicy `pulumi:"updatePolicy"`
	// Application versions managed by this instance group. Each
	// version deals with a specific instance template, allowing canary release scenarios.
	// Structure is documented below.
	Versions []RegionInstanceGroupManagerVersion `pulumi:"versions"`
	// Whether to wait for all instances to be created/updated before
	// returning. Note that if this is set to true and the operation does not succeed, the provider will
	// continue trying until it times out.
	WaitForInstances *bool `pulumi:"waitForInstances"`
}

// The set of arguments for constructing a RegionInstanceGroupManager resource.
type RegionInstanceGroupManagerArgs struct {
	// The autohealing policies for this managed instance
	// group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).
	AutoHealingPolicies RegionInstanceGroupManagerAutoHealingPoliciesPtrInput
	// The base instance name to use for
	// instances in this group. The value must be a valid
	// [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
	// are lowercase letters, numbers, and hyphens (-). Instances are named by
	// appending a hyphen and a random four-character string to the base instance
	// name.
	BaseInstanceName pulumi.StringInput
	// An optional textual description of the instance
	// group manager.
	Description pulumi.StringPtrInput
	// The distribution policy for this managed instance
	// group. You can specify one or more values. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones).
	// - - -
	DistributionPolicyZones pulumi.StringArrayInput
	// - Version name.
	Name pulumi.StringPtrInput
	// The named port configuration. See the section below
	// for details on configuration.
	NamedPorts RegionInstanceGroupManagerNamedPortArrayInput
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The region where the managed instance group resides.
	Region pulumi.StringInput
	// The full URL of all target pools to which new
	// instances in the group are added. Updating the target pools attribute does
	// not affect existing instances.
	TargetPools pulumi.StringArrayInput
	// - The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.
	TargetSize pulumi.IntPtrInput
	// The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch)
	UpdatePolicy RegionInstanceGroupManagerUpdatePolicyPtrInput
	// Application versions managed by this instance group. Each
	// version deals with a specific instance template, allowing canary release scenarios.
	// Structure is documented below.
	Versions RegionInstanceGroupManagerVersionArrayInput
	// Whether to wait for all instances to be created/updated before
	// returning. Note that if this is set to true and the operation does not succeed, the provider will
	// continue trying until it times out.
	WaitForInstances pulumi.BoolPtrInput
}

func (RegionInstanceGroupManagerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*regionInstanceGroupManagerArgs)(nil)).Elem()
}
