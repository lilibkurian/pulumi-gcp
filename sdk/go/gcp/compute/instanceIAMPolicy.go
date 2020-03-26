// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Three different resources help you manage your IAM policy for Compute Engine Instance. Each of these resources serves a different use case:
//
// * `compute.InstanceIAMPolicy`: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.
// * `compute.InstanceIAMBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.
// * `compute.InstanceIAMMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.
//
// > **Note:** `compute.InstanceIAMPolicy` **cannot** be used in conjunction with `compute.InstanceIAMBinding` and `compute.InstanceIAMMember` or they will fight over what your policy should be.
//
// > **Note:** `compute.InstanceIAMBinding` resources **can be** used in conjunction with `compute.InstanceIAMMember` resources **only if** they do not grant privilege to the same role.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam.html.markdown.
type InstanceIAMPolicy struct {
	pulumi.CustomResourceState

	// (Computed) The etag of the IAM policy.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// Used to find the parent resource to bind the IAM policy to
	InstanceName pulumi.StringOutput `pulumi:"instanceName"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringOutput `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
	// zone is specified, it is taken from the provider configuration.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewInstanceIAMPolicy registers a new resource with the given unique name, arguments, and options.
func NewInstanceIAMPolicy(ctx *pulumi.Context,
	name string, args *InstanceIAMPolicyArgs, opts ...pulumi.ResourceOption) (*InstanceIAMPolicy, error) {
	if args == nil || args.InstanceName == nil {
		return nil, errors.New("missing required argument 'InstanceName'")
	}
	if args == nil || args.PolicyData == nil {
		return nil, errors.New("missing required argument 'PolicyData'")
	}
	if args == nil {
		args = &InstanceIAMPolicyArgs{}
	}
	var resource InstanceIAMPolicy
	err := ctx.RegisterResource("gcp:compute/instanceIAMPolicy:InstanceIAMPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstanceIAMPolicy gets an existing InstanceIAMPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstanceIAMPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceIAMPolicyState, opts ...pulumi.ResourceOption) (*InstanceIAMPolicy, error) {
	var resource InstanceIAMPolicy
	err := ctx.ReadResource("gcp:compute/instanceIAMPolicy:InstanceIAMPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering InstanceIAMPolicy resources.
type instanceIAMPolicyState struct {
	// (Computed) The etag of the IAM policy.
	Etag *string `pulumi:"etag"`
	// Used to find the parent resource to bind the IAM policy to
	InstanceName *string `pulumi:"instanceName"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData *string `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
	// zone is specified, it is taken from the provider configuration.
	Zone *string `pulumi:"zone"`
}

type InstanceIAMPolicyState struct {
	// (Computed) The etag of the IAM policy.
	Etag pulumi.StringPtrInput
	// Used to find the parent resource to bind the IAM policy to
	InstanceName pulumi.StringPtrInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
	// zone is specified, it is taken from the provider configuration.
	Zone pulumi.StringPtrInput
}

func (InstanceIAMPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceIAMPolicyState)(nil)).Elem()
}

type instanceIAMPolicyArgs struct {
	// Used to find the parent resource to bind the IAM policy to
	InstanceName string `pulumi:"instanceName"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData string `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
	// zone is specified, it is taken from the provider configuration.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a InstanceIAMPolicy resource.
type InstanceIAMPolicyArgs struct {
	// Used to find the parent resource to bind the IAM policy to
	InstanceName pulumi.StringInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
	// zone is specified, it is taken from the provider configuration.
	Zone pulumi.StringPtrInput
}

func (InstanceIAMPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceIAMPolicyArgs)(nil)).Elem()
}
