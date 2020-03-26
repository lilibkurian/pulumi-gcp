// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package datafusion

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Represents a Data Fusion instance.
//
// To get more information about Instance, see:
//
// * [API documentation](https://cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/data-fusion/docs/)
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/data_fusion_instance.html.markdown.
type Instance struct {
	pulumi.CustomResourceState

	// The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// An optional description of the instance.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Option to enable Stackdriver Logging.
	EnableStackdriverLogging pulumi.BoolPtrOutput `pulumi:"enableStackdriverLogging"`
	// Option to enable Stackdriver Monitoring.
	EnableStackdriverMonitoring pulumi.BoolPtrOutput `pulumi:"enableStackdriverMonitoring"`
	// The resource labels for instance to use to annotate any related underlying resources, such as Compute Engine VMs.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// The ID of the instance or a fully qualified identifier for the instance.
	Name pulumi.StringOutput `pulumi:"name"`
	// Network configuration options. These are required when a private Data Fusion instance is to be created.
	NetworkConfig InstanceNetworkConfigPtrOutput `pulumi:"networkConfig"`
	// Map of additional options used to configure the behavior of Data Fusion instance.
	Options pulumi.StringMapOutput `pulumi:"options"`
	// Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP
	// addresses and will not be able to access the public internet.
	PrivateInstance pulumi.BoolPtrOutput `pulumi:"privateInstance"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The region of the Data Fusion instance.
	Region pulumi.StringOutput `pulumi:"region"`
	// Service account which will be used to access resources in the customer project.
	ServiceAccount pulumi.StringOutput `pulumi:"serviceAccount"`
	// Endpoint on which the Data Fusion UI and REST APIs are accessible.
	ServiceEndpoint pulumi.StringOutput `pulumi:"serviceEndpoint"`
	// The current state of this Data Fusion instance. - CREATING: Instance is being created - RUNNING: Instance is running and
	// ready for requests - FAILED: Instance creation failed - DELETING: Instance is being deleted - UPGRADING: Instance is
	// being upgraded - RESTARTING: Instance is being restarted
	State pulumi.StringOutput `pulumi:"state"`
	// Additional information about the current state of this Data Fusion instance if available.
	StateMessage pulumi.StringOutput `pulumi:"stateMessage"`
	// Represents the type of Data Fusion instance. Each type is configured with the default settings for processing and
	// memory. - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines using point
	// and click UI. However, there are certain limitations, such as fewer number of concurrent pipelines, no support for
	// streaming pipelines, etc. - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more
	// features available, such as support for streaming pipelines, higher number of concurrent pipelines, etc.
	Type pulumi.StringOutput `pulumi:"type"`
	// The time the instance was last updated in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
	// Current version of the Data Fusion.
	Version pulumi.StringOutput `pulumi:"version"`
}

// NewInstance registers a new resource with the given unique name, arguments, and options.
func NewInstance(ctx *pulumi.Context,
	name string, args *InstanceArgs, opts ...pulumi.ResourceOption) (*Instance, error) {
	if args == nil || args.Type == nil {
		return nil, errors.New("missing required argument 'Type'")
	}
	if args == nil {
		args = &InstanceArgs{}
	}
	var resource Instance
	err := ctx.RegisterResource("gcp:datafusion/instance:Instance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstance gets an existing Instance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceState, opts ...pulumi.ResourceOption) (*Instance, error) {
	var resource Instance
	err := ctx.ReadResource("gcp:datafusion/instance:Instance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Instance resources.
type instanceState struct {
	// The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
	CreateTime *string `pulumi:"createTime"`
	// An optional description of the instance.
	Description *string `pulumi:"description"`
	// Option to enable Stackdriver Logging.
	EnableStackdriverLogging *bool `pulumi:"enableStackdriverLogging"`
	// Option to enable Stackdriver Monitoring.
	EnableStackdriverMonitoring *bool `pulumi:"enableStackdriverMonitoring"`
	// The resource labels for instance to use to annotate any related underlying resources, such as Compute Engine VMs.
	Labels map[string]string `pulumi:"labels"`
	// The ID of the instance or a fully qualified identifier for the instance.
	Name *string `pulumi:"name"`
	// Network configuration options. These are required when a private Data Fusion instance is to be created.
	NetworkConfig *InstanceNetworkConfig `pulumi:"networkConfig"`
	// Map of additional options used to configure the behavior of Data Fusion instance.
	Options map[string]string `pulumi:"options"`
	// Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP
	// addresses and will not be able to access the public internet.
	PrivateInstance *bool `pulumi:"privateInstance"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The region of the Data Fusion instance.
	Region *string `pulumi:"region"`
	// Service account which will be used to access resources in the customer project.
	ServiceAccount *string `pulumi:"serviceAccount"`
	// Endpoint on which the Data Fusion UI and REST APIs are accessible.
	ServiceEndpoint *string `pulumi:"serviceEndpoint"`
	// The current state of this Data Fusion instance. - CREATING: Instance is being created - RUNNING: Instance is running and
	// ready for requests - FAILED: Instance creation failed - DELETING: Instance is being deleted - UPGRADING: Instance is
	// being upgraded - RESTARTING: Instance is being restarted
	State *string `pulumi:"state"`
	// Additional information about the current state of this Data Fusion instance if available.
	StateMessage *string `pulumi:"stateMessage"`
	// Represents the type of Data Fusion instance. Each type is configured with the default settings for processing and
	// memory. - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines using point
	// and click UI. However, there are certain limitations, such as fewer number of concurrent pipelines, no support for
	// streaming pipelines, etc. - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more
	// features available, such as support for streaming pipelines, higher number of concurrent pipelines, etc.
	Type *string `pulumi:"type"`
	// The time the instance was last updated in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
	UpdateTime *string `pulumi:"updateTime"`
	// Current version of the Data Fusion.
	Version *string `pulumi:"version"`
}

type InstanceState struct {
	// The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
	CreateTime pulumi.StringPtrInput
	// An optional description of the instance.
	Description pulumi.StringPtrInput
	// Option to enable Stackdriver Logging.
	EnableStackdriverLogging pulumi.BoolPtrInput
	// Option to enable Stackdriver Monitoring.
	EnableStackdriverMonitoring pulumi.BoolPtrInput
	// The resource labels for instance to use to annotate any related underlying resources, such as Compute Engine VMs.
	Labels pulumi.StringMapInput
	// The ID of the instance or a fully qualified identifier for the instance.
	Name pulumi.StringPtrInput
	// Network configuration options. These are required when a private Data Fusion instance is to be created.
	NetworkConfig InstanceNetworkConfigPtrInput
	// Map of additional options used to configure the behavior of Data Fusion instance.
	Options pulumi.StringMapInput
	// Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP
	// addresses and will not be able to access the public internet.
	PrivateInstance pulumi.BoolPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The region of the Data Fusion instance.
	Region pulumi.StringPtrInput
	// Service account which will be used to access resources in the customer project.
	ServiceAccount pulumi.StringPtrInput
	// Endpoint on which the Data Fusion UI and REST APIs are accessible.
	ServiceEndpoint pulumi.StringPtrInput
	// The current state of this Data Fusion instance. - CREATING: Instance is being created - RUNNING: Instance is running and
	// ready for requests - FAILED: Instance creation failed - DELETING: Instance is being deleted - UPGRADING: Instance is
	// being upgraded - RESTARTING: Instance is being restarted
	State pulumi.StringPtrInput
	// Additional information about the current state of this Data Fusion instance if available.
	StateMessage pulumi.StringPtrInput
	// Represents the type of Data Fusion instance. Each type is configured with the default settings for processing and
	// memory. - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines using point
	// and click UI. However, there are certain limitations, such as fewer number of concurrent pipelines, no support for
	// streaming pipelines, etc. - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more
	// features available, such as support for streaming pipelines, higher number of concurrent pipelines, etc.
	Type pulumi.StringPtrInput
	// The time the instance was last updated in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
	UpdateTime pulumi.StringPtrInput
	// Current version of the Data Fusion.
	Version pulumi.StringPtrInput
}

func (InstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceState)(nil)).Elem()
}

type instanceArgs struct {
	// An optional description of the instance.
	Description *string `pulumi:"description"`
	// Option to enable Stackdriver Logging.
	EnableStackdriverLogging *bool `pulumi:"enableStackdriverLogging"`
	// Option to enable Stackdriver Monitoring.
	EnableStackdriverMonitoring *bool `pulumi:"enableStackdriverMonitoring"`
	// The resource labels for instance to use to annotate any related underlying resources, such as Compute Engine VMs.
	Labels map[string]string `pulumi:"labels"`
	// The ID of the instance or a fully qualified identifier for the instance.
	Name *string `pulumi:"name"`
	// Network configuration options. These are required when a private Data Fusion instance is to be created.
	NetworkConfig *InstanceNetworkConfig `pulumi:"networkConfig"`
	// Map of additional options used to configure the behavior of Data Fusion instance.
	Options map[string]string `pulumi:"options"`
	// Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP
	// addresses and will not be able to access the public internet.
	PrivateInstance *bool `pulumi:"privateInstance"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The region of the Data Fusion instance.
	Region *string `pulumi:"region"`
	// Represents the type of Data Fusion instance. Each type is configured with the default settings for processing and
	// memory. - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines using point
	// and click UI. However, there are certain limitations, such as fewer number of concurrent pipelines, no support for
	// streaming pipelines, etc. - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more
	// features available, such as support for streaming pipelines, higher number of concurrent pipelines, etc.
	Type string `pulumi:"type"`
}

// The set of arguments for constructing a Instance resource.
type InstanceArgs struct {
	// An optional description of the instance.
	Description pulumi.StringPtrInput
	// Option to enable Stackdriver Logging.
	EnableStackdriverLogging pulumi.BoolPtrInput
	// Option to enable Stackdriver Monitoring.
	EnableStackdriverMonitoring pulumi.BoolPtrInput
	// The resource labels for instance to use to annotate any related underlying resources, such as Compute Engine VMs.
	Labels pulumi.StringMapInput
	// The ID of the instance or a fully qualified identifier for the instance.
	Name pulumi.StringPtrInput
	// Network configuration options. These are required when a private Data Fusion instance is to be created.
	NetworkConfig InstanceNetworkConfigPtrInput
	// Map of additional options used to configure the behavior of Data Fusion instance.
	Options pulumi.StringMapInput
	// Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP
	// addresses and will not be able to access the public internet.
	PrivateInstance pulumi.BoolPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The region of the Data Fusion instance.
	Region pulumi.StringPtrInput
	// Represents the type of Data Fusion instance. Each type is configured with the default settings for processing and
	// memory. - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines using point
	// and click UI. However, there are certain limitations, such as fewer number of concurrent pipelines, no support for
	// streaming pipelines, etc. - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more
	// features available, such as support for streaming pipelines, higher number of concurrent pipelines, etc.
	Type pulumi.StringInput
}

func (InstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceArgs)(nil)).Elem()
}
