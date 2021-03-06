// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package notebooks

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// A Cloud AI Platform Notebook instance.
//
// > **Note:** Due to limitations of the Notebooks Instance API, many fields
// in this resource do not properly detect drift. These fields will also not
// appear in state once imported.
//
// To get more information about Instance, see:
//
// * [API documentation](https://cloud.google.com/ai-platform/notebooks/docs/reference/rest)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/ai-platform-notebooks)
//
// ## Example Usage
type Instance struct {
	pulumi.CustomResourceState

	// The hardware accelerator used on this instance. If you use accelerators,
	// make sure that your configuration has enough vCPUs and memory to support the
	// machineType you have selected.
	// Structure is documented below.
	AcceleratorConfig InstanceAcceleratorConfigPtrOutput `pulumi:"acceleratorConfig"`
	// The size of the boot disk in GB attached to this instance,
	// up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB.
	// If not specified, this defaults to 100.
	BootDiskSizeGb pulumi.IntPtrOutput `pulumi:"bootDiskSizeGb"`
	// Possible disk types for notebook instances.
	// Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
	BootDiskType pulumi.StringPtrOutput `pulumi:"bootDiskType"`
	// Use a container image to start the notebook instance.
	// Structure is documented below.
	ContainerImage InstanceContainerImagePtrOutput `pulumi:"containerImage"`
	// Instance creation time
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Specify a custom Cloud Storage path where the GPU driver is stored.
	// If not specified, we'll automatically choose from official GPU drivers.
	CustomGpuDriverPath pulumi.StringPtrOutput `pulumi:"customGpuDriverPath"`
	// The size of the data disk in GB attached to this instance,
	// up to a maximum of 64000 GB (64 TB).
	// You can choose the size of the data disk based on how big your notebooks and data are.
	// If not specified, this defaults to 100.
	DataDiskSizeGb pulumi.IntPtrOutput `pulumi:"dataDiskSizeGb"`
	// Possible disk types for notebook instances.
	// Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
	DataDiskType pulumi.StringPtrOutput `pulumi:"dataDiskType"`
	// Disk encryption method used on the boot and data disks, defaults to GMEK.
	// Possible values are `DISK_ENCRYPTION_UNSPECIFIED`, `GMEK`, and `CMEK`.
	DiskEncryption pulumi.StringPtrOutput `pulumi:"diskEncryption"`
	// Whether the end user authorizes Google Cloud to install GPU driver
	// on this instance. If this field is empty or set to false, the GPU driver
	// won't be installed. Only applicable to instances with GPUs.
	InstallGpuDriver pulumi.BoolPtrOutput `pulumi:"installGpuDriver"`
	// The list of owners of this instance after creation.
	// Format: alias@example.com.
	// Currently supports one owner only.
	// If not specified, all of the service account users of
	// your VM instance's service account can use the instance.
	InstanceOwners pulumi.StringPtrOutput `pulumi:"instanceOwners"`
	// The KMS key used to encrypt the disks, only applicable if diskEncryption is CMEK.
	// Format: projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}
	KmsKey pulumi.StringPtrOutput `pulumi:"kmsKey"`
	// Labels to apply to this instance. These can be later modified by the setLabels method.
	// An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// A reference to the zone where the machine resides.
	Location pulumi.StringOutput `pulumi:"location"`
	// A reference to a machine type which defines VM kind.
	MachineType pulumi.StringOutput `pulumi:"machineType"`
	// Custom metadata to apply to this instance.
	// An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
	Metadata pulumi.StringMapOutput `pulumi:"metadata"`
	// The name specified for the Notebook instance.
	Name pulumi.StringOutput `pulumi:"name"`
	// The name of the VPC that this instance is in.
	// Format: projects/{project_id}/global/networks/{network_id}
	Network pulumi.StringOutput `pulumi:"network"`
	// the notebook instance will not register with the proxy..
	NoProxyAccess pulumi.BoolPtrOutput `pulumi:"noProxyAccess"`
	// no public IP will be assigned to this instance.
	NoPublicIp pulumi.BoolPtrOutput `pulumi:"noPublicIp"`
	// If true, the data disk will not be auto deleted when deleting the instance.
	NoRemoveDataDisk pulumi.BoolPtrOutput `pulumi:"noRemoveDataDisk"`
	// Path to a Bash script that automatically runs after a
	// notebook instance fully boots up. The path must be a URL
	// or Cloud Storage path (gs://path-to-file/file-name).
	PostStartupScript pulumi.StringPtrOutput `pulumi:"postStartupScript"`
	// The name of the Google Cloud project that this VM image belongs to.
	// Format: projects/{project_id}
	Project pulumi.StringOutput `pulumi:"project"`
	// The proxy endpoint that is used to access the Jupyter notebook.
	ProxyUri pulumi.StringOutput `pulumi:"proxyUri"`
	// The service account on this instance, giving access to other
	// Google Cloud services. You can use any service account within
	// the same project, but you must have the service account user
	// permission to use the instance. If not specified,
	// the Compute Engine default service account is used.
	ServiceAccount pulumi.StringOutput `pulumi:"serviceAccount"`
	// The state of this instance.
	State pulumi.StringOutput `pulumi:"state"`
	// The name of the subnet that this instance is in.
	// Format: projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}
	Subnet pulumi.StringOutput `pulumi:"subnet"`
	// Instance update time.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
	// Use a Compute Engine VM image to start the notebook instance.
	// Structure is documented below.
	VmImage InstanceVmImagePtrOutput `pulumi:"vmImage"`
}

// NewInstance registers a new resource with the given unique name, arguments, and options.
func NewInstance(ctx *pulumi.Context,
	name string, args *InstanceArgs, opts ...pulumi.ResourceOption) (*Instance, error) {
	if args == nil || args.Location == nil {
		return nil, errors.New("missing required argument 'Location'")
	}
	if args == nil || args.MachineType == nil {
		return nil, errors.New("missing required argument 'MachineType'")
	}
	if args == nil {
		args = &InstanceArgs{}
	}
	var resource Instance
	err := ctx.RegisterResource("gcp:notebooks/instance:Instance", name, args, &resource, opts...)
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
	err := ctx.ReadResource("gcp:notebooks/instance:Instance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Instance resources.
type instanceState struct {
	// The hardware accelerator used on this instance. If you use accelerators,
	// make sure that your configuration has enough vCPUs and memory to support the
	// machineType you have selected.
	// Structure is documented below.
	AcceleratorConfig *InstanceAcceleratorConfig `pulumi:"acceleratorConfig"`
	// The size of the boot disk in GB attached to this instance,
	// up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB.
	// If not specified, this defaults to 100.
	BootDiskSizeGb *int `pulumi:"bootDiskSizeGb"`
	// Possible disk types for notebook instances.
	// Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
	BootDiskType *string `pulumi:"bootDiskType"`
	// Use a container image to start the notebook instance.
	// Structure is documented below.
	ContainerImage *InstanceContainerImage `pulumi:"containerImage"`
	// Instance creation time
	CreateTime *string `pulumi:"createTime"`
	// Specify a custom Cloud Storage path where the GPU driver is stored.
	// If not specified, we'll automatically choose from official GPU drivers.
	CustomGpuDriverPath *string `pulumi:"customGpuDriverPath"`
	// The size of the data disk in GB attached to this instance,
	// up to a maximum of 64000 GB (64 TB).
	// You can choose the size of the data disk based on how big your notebooks and data are.
	// If not specified, this defaults to 100.
	DataDiskSizeGb *int `pulumi:"dataDiskSizeGb"`
	// Possible disk types for notebook instances.
	// Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
	DataDiskType *string `pulumi:"dataDiskType"`
	// Disk encryption method used on the boot and data disks, defaults to GMEK.
	// Possible values are `DISK_ENCRYPTION_UNSPECIFIED`, `GMEK`, and `CMEK`.
	DiskEncryption *string `pulumi:"diskEncryption"`
	// Whether the end user authorizes Google Cloud to install GPU driver
	// on this instance. If this field is empty or set to false, the GPU driver
	// won't be installed. Only applicable to instances with GPUs.
	InstallGpuDriver *bool `pulumi:"installGpuDriver"`
	// The list of owners of this instance after creation.
	// Format: alias@example.com.
	// Currently supports one owner only.
	// If not specified, all of the service account users of
	// your VM instance's service account can use the instance.
	InstanceOwners *string `pulumi:"instanceOwners"`
	// The KMS key used to encrypt the disks, only applicable if diskEncryption is CMEK.
	// Format: projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}
	KmsKey *string `pulumi:"kmsKey"`
	// Labels to apply to this instance. These can be later modified by the setLabels method.
	// An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
	Labels map[string]string `pulumi:"labels"`
	// A reference to the zone where the machine resides.
	Location *string `pulumi:"location"`
	// A reference to a machine type which defines VM kind.
	MachineType *string `pulumi:"machineType"`
	// Custom metadata to apply to this instance.
	// An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
	Metadata map[string]string `pulumi:"metadata"`
	// The name specified for the Notebook instance.
	Name *string `pulumi:"name"`
	// The name of the VPC that this instance is in.
	// Format: projects/{project_id}/global/networks/{network_id}
	Network *string `pulumi:"network"`
	// the notebook instance will not register with the proxy..
	NoProxyAccess *bool `pulumi:"noProxyAccess"`
	// no public IP will be assigned to this instance.
	NoPublicIp *bool `pulumi:"noPublicIp"`
	// If true, the data disk will not be auto deleted when deleting the instance.
	NoRemoveDataDisk *bool `pulumi:"noRemoveDataDisk"`
	// Path to a Bash script that automatically runs after a
	// notebook instance fully boots up. The path must be a URL
	// or Cloud Storage path (gs://path-to-file/file-name).
	PostStartupScript *string `pulumi:"postStartupScript"`
	// The name of the Google Cloud project that this VM image belongs to.
	// Format: projects/{project_id}
	Project *string `pulumi:"project"`
	// The proxy endpoint that is used to access the Jupyter notebook.
	ProxyUri *string `pulumi:"proxyUri"`
	// The service account on this instance, giving access to other
	// Google Cloud services. You can use any service account within
	// the same project, but you must have the service account user
	// permission to use the instance. If not specified,
	// the Compute Engine default service account is used.
	ServiceAccount *string `pulumi:"serviceAccount"`
	// The state of this instance.
	State *string `pulumi:"state"`
	// The name of the subnet that this instance is in.
	// Format: projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}
	Subnet *string `pulumi:"subnet"`
	// Instance update time.
	UpdateTime *string `pulumi:"updateTime"`
	// Use a Compute Engine VM image to start the notebook instance.
	// Structure is documented below.
	VmImage *InstanceVmImage `pulumi:"vmImage"`
}

type InstanceState struct {
	// The hardware accelerator used on this instance. If you use accelerators,
	// make sure that your configuration has enough vCPUs and memory to support the
	// machineType you have selected.
	// Structure is documented below.
	AcceleratorConfig InstanceAcceleratorConfigPtrInput
	// The size of the boot disk in GB attached to this instance,
	// up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB.
	// If not specified, this defaults to 100.
	BootDiskSizeGb pulumi.IntPtrInput
	// Possible disk types for notebook instances.
	// Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
	BootDiskType pulumi.StringPtrInput
	// Use a container image to start the notebook instance.
	// Structure is documented below.
	ContainerImage InstanceContainerImagePtrInput
	// Instance creation time
	CreateTime pulumi.StringPtrInput
	// Specify a custom Cloud Storage path where the GPU driver is stored.
	// If not specified, we'll automatically choose from official GPU drivers.
	CustomGpuDriverPath pulumi.StringPtrInput
	// The size of the data disk in GB attached to this instance,
	// up to a maximum of 64000 GB (64 TB).
	// You can choose the size of the data disk based on how big your notebooks and data are.
	// If not specified, this defaults to 100.
	DataDiskSizeGb pulumi.IntPtrInput
	// Possible disk types for notebook instances.
	// Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
	DataDiskType pulumi.StringPtrInput
	// Disk encryption method used on the boot and data disks, defaults to GMEK.
	// Possible values are `DISK_ENCRYPTION_UNSPECIFIED`, `GMEK`, and `CMEK`.
	DiskEncryption pulumi.StringPtrInput
	// Whether the end user authorizes Google Cloud to install GPU driver
	// on this instance. If this field is empty or set to false, the GPU driver
	// won't be installed. Only applicable to instances with GPUs.
	InstallGpuDriver pulumi.BoolPtrInput
	// The list of owners of this instance after creation.
	// Format: alias@example.com.
	// Currently supports one owner only.
	// If not specified, all of the service account users of
	// your VM instance's service account can use the instance.
	InstanceOwners pulumi.StringPtrInput
	// The KMS key used to encrypt the disks, only applicable if diskEncryption is CMEK.
	// Format: projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}
	KmsKey pulumi.StringPtrInput
	// Labels to apply to this instance. These can be later modified by the setLabels method.
	// An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
	Labels pulumi.StringMapInput
	// A reference to the zone where the machine resides.
	Location pulumi.StringPtrInput
	// A reference to a machine type which defines VM kind.
	MachineType pulumi.StringPtrInput
	// Custom metadata to apply to this instance.
	// An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
	Metadata pulumi.StringMapInput
	// The name specified for the Notebook instance.
	Name pulumi.StringPtrInput
	// The name of the VPC that this instance is in.
	// Format: projects/{project_id}/global/networks/{network_id}
	Network pulumi.StringPtrInput
	// the notebook instance will not register with the proxy..
	NoProxyAccess pulumi.BoolPtrInput
	// no public IP will be assigned to this instance.
	NoPublicIp pulumi.BoolPtrInput
	// If true, the data disk will not be auto deleted when deleting the instance.
	NoRemoveDataDisk pulumi.BoolPtrInput
	// Path to a Bash script that automatically runs after a
	// notebook instance fully boots up. The path must be a URL
	// or Cloud Storage path (gs://path-to-file/file-name).
	PostStartupScript pulumi.StringPtrInput
	// The name of the Google Cloud project that this VM image belongs to.
	// Format: projects/{project_id}
	Project pulumi.StringPtrInput
	// The proxy endpoint that is used to access the Jupyter notebook.
	ProxyUri pulumi.StringPtrInput
	// The service account on this instance, giving access to other
	// Google Cloud services. You can use any service account within
	// the same project, but you must have the service account user
	// permission to use the instance. If not specified,
	// the Compute Engine default service account is used.
	ServiceAccount pulumi.StringPtrInput
	// The state of this instance.
	State pulumi.StringPtrInput
	// The name of the subnet that this instance is in.
	// Format: projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}
	Subnet pulumi.StringPtrInput
	// Instance update time.
	UpdateTime pulumi.StringPtrInput
	// Use a Compute Engine VM image to start the notebook instance.
	// Structure is documented below.
	VmImage InstanceVmImagePtrInput
}

func (InstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceState)(nil)).Elem()
}

type instanceArgs struct {
	// The hardware accelerator used on this instance. If you use accelerators,
	// make sure that your configuration has enough vCPUs and memory to support the
	// machineType you have selected.
	// Structure is documented below.
	AcceleratorConfig *InstanceAcceleratorConfig `pulumi:"acceleratorConfig"`
	// The size of the boot disk in GB attached to this instance,
	// up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB.
	// If not specified, this defaults to 100.
	BootDiskSizeGb *int `pulumi:"bootDiskSizeGb"`
	// Possible disk types for notebook instances.
	// Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
	BootDiskType *string `pulumi:"bootDiskType"`
	// Use a container image to start the notebook instance.
	// Structure is documented below.
	ContainerImage *InstanceContainerImage `pulumi:"containerImage"`
	// Instance creation time
	CreateTime *string `pulumi:"createTime"`
	// Specify a custom Cloud Storage path where the GPU driver is stored.
	// If not specified, we'll automatically choose from official GPU drivers.
	CustomGpuDriverPath *string `pulumi:"customGpuDriverPath"`
	// The size of the data disk in GB attached to this instance,
	// up to a maximum of 64000 GB (64 TB).
	// You can choose the size of the data disk based on how big your notebooks and data are.
	// If not specified, this defaults to 100.
	DataDiskSizeGb *int `pulumi:"dataDiskSizeGb"`
	// Possible disk types for notebook instances.
	// Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
	DataDiskType *string `pulumi:"dataDiskType"`
	// Disk encryption method used on the boot and data disks, defaults to GMEK.
	// Possible values are `DISK_ENCRYPTION_UNSPECIFIED`, `GMEK`, and `CMEK`.
	DiskEncryption *string `pulumi:"diskEncryption"`
	// Whether the end user authorizes Google Cloud to install GPU driver
	// on this instance. If this field is empty or set to false, the GPU driver
	// won't be installed. Only applicable to instances with GPUs.
	InstallGpuDriver *bool `pulumi:"installGpuDriver"`
	// The list of owners of this instance after creation.
	// Format: alias@example.com.
	// Currently supports one owner only.
	// If not specified, all of the service account users of
	// your VM instance's service account can use the instance.
	InstanceOwners *string `pulumi:"instanceOwners"`
	// The KMS key used to encrypt the disks, only applicable if diskEncryption is CMEK.
	// Format: projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}
	KmsKey *string `pulumi:"kmsKey"`
	// Labels to apply to this instance. These can be later modified by the setLabels method.
	// An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
	Labels map[string]string `pulumi:"labels"`
	// A reference to the zone where the machine resides.
	Location string `pulumi:"location"`
	// A reference to a machine type which defines VM kind.
	MachineType string `pulumi:"machineType"`
	// Custom metadata to apply to this instance.
	// An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
	Metadata map[string]string `pulumi:"metadata"`
	// The name specified for the Notebook instance.
	Name *string `pulumi:"name"`
	// The name of the VPC that this instance is in.
	// Format: projects/{project_id}/global/networks/{network_id}
	Network *string `pulumi:"network"`
	// the notebook instance will not register with the proxy..
	NoProxyAccess *bool `pulumi:"noProxyAccess"`
	// no public IP will be assigned to this instance.
	NoPublicIp *bool `pulumi:"noPublicIp"`
	// If true, the data disk will not be auto deleted when deleting the instance.
	NoRemoveDataDisk *bool `pulumi:"noRemoveDataDisk"`
	// Path to a Bash script that automatically runs after a
	// notebook instance fully boots up. The path must be a URL
	// or Cloud Storage path (gs://path-to-file/file-name).
	PostStartupScript *string `pulumi:"postStartupScript"`
	// The name of the Google Cloud project that this VM image belongs to.
	// Format: projects/{project_id}
	Project *string `pulumi:"project"`
	// The service account on this instance, giving access to other
	// Google Cloud services. You can use any service account within
	// the same project, but you must have the service account user
	// permission to use the instance. If not specified,
	// the Compute Engine default service account is used.
	ServiceAccount *string `pulumi:"serviceAccount"`
	// The name of the subnet that this instance is in.
	// Format: projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}
	Subnet *string `pulumi:"subnet"`
	// Instance update time.
	UpdateTime *string `pulumi:"updateTime"`
	// Use a Compute Engine VM image to start the notebook instance.
	// Structure is documented below.
	VmImage *InstanceVmImage `pulumi:"vmImage"`
}

// The set of arguments for constructing a Instance resource.
type InstanceArgs struct {
	// The hardware accelerator used on this instance. If you use accelerators,
	// make sure that your configuration has enough vCPUs and memory to support the
	// machineType you have selected.
	// Structure is documented below.
	AcceleratorConfig InstanceAcceleratorConfigPtrInput
	// The size of the boot disk in GB attached to this instance,
	// up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB.
	// If not specified, this defaults to 100.
	BootDiskSizeGb pulumi.IntPtrInput
	// Possible disk types for notebook instances.
	// Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
	BootDiskType pulumi.StringPtrInput
	// Use a container image to start the notebook instance.
	// Structure is documented below.
	ContainerImage InstanceContainerImagePtrInput
	// Instance creation time
	CreateTime pulumi.StringPtrInput
	// Specify a custom Cloud Storage path where the GPU driver is stored.
	// If not specified, we'll automatically choose from official GPU drivers.
	CustomGpuDriverPath pulumi.StringPtrInput
	// The size of the data disk in GB attached to this instance,
	// up to a maximum of 64000 GB (64 TB).
	// You can choose the size of the data disk based on how big your notebooks and data are.
	// If not specified, this defaults to 100.
	DataDiskSizeGb pulumi.IntPtrInput
	// Possible disk types for notebook instances.
	// Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
	DataDiskType pulumi.StringPtrInput
	// Disk encryption method used on the boot and data disks, defaults to GMEK.
	// Possible values are `DISK_ENCRYPTION_UNSPECIFIED`, `GMEK`, and `CMEK`.
	DiskEncryption pulumi.StringPtrInput
	// Whether the end user authorizes Google Cloud to install GPU driver
	// on this instance. If this field is empty or set to false, the GPU driver
	// won't be installed. Only applicable to instances with GPUs.
	InstallGpuDriver pulumi.BoolPtrInput
	// The list of owners of this instance after creation.
	// Format: alias@example.com.
	// Currently supports one owner only.
	// If not specified, all of the service account users of
	// your VM instance's service account can use the instance.
	InstanceOwners pulumi.StringPtrInput
	// The KMS key used to encrypt the disks, only applicable if diskEncryption is CMEK.
	// Format: projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}
	KmsKey pulumi.StringPtrInput
	// Labels to apply to this instance. These can be later modified by the setLabels method.
	// An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
	Labels pulumi.StringMapInput
	// A reference to the zone where the machine resides.
	Location pulumi.StringInput
	// A reference to a machine type which defines VM kind.
	MachineType pulumi.StringInput
	// Custom metadata to apply to this instance.
	// An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
	Metadata pulumi.StringMapInput
	// The name specified for the Notebook instance.
	Name pulumi.StringPtrInput
	// The name of the VPC that this instance is in.
	// Format: projects/{project_id}/global/networks/{network_id}
	Network pulumi.StringPtrInput
	// the notebook instance will not register with the proxy..
	NoProxyAccess pulumi.BoolPtrInput
	// no public IP will be assigned to this instance.
	NoPublicIp pulumi.BoolPtrInput
	// If true, the data disk will not be auto deleted when deleting the instance.
	NoRemoveDataDisk pulumi.BoolPtrInput
	// Path to a Bash script that automatically runs after a
	// notebook instance fully boots up. The path must be a URL
	// or Cloud Storage path (gs://path-to-file/file-name).
	PostStartupScript pulumi.StringPtrInput
	// The name of the Google Cloud project that this VM image belongs to.
	// Format: projects/{project_id}
	Project pulumi.StringPtrInput
	// The service account on this instance, giving access to other
	// Google Cloud services. You can use any service account within
	// the same project, but you must have the service account user
	// permission to use the instance. If not specified,
	// the Compute Engine default service account is used.
	ServiceAccount pulumi.StringPtrInput
	// The name of the subnet that this instance is in.
	// Format: projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}
	Subnet pulumi.StringPtrInput
	// Instance update time.
	UpdateTime pulumi.StringPtrInput
	// Use a Compute Engine VM image to start the notebook instance.
	// Structure is documented below.
	VmImage InstanceVmImagePtrInput
}

func (InstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceArgs)(nil)).Elem()
}
