// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package projects

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Allows management of Organization policies for a Google Project. For more information see
// [the official
// documentation](https://cloud.google.com/resource-manager/docs/organization-policy/overview) and
// [API](https://cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy).
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_project_organization_policy.html.markdown.
type OrganizationPolicy struct {
	pulumi.CustomResourceState

	// A boolean policy is a constraint that is either enforced or not. Structure is documented below.
	BooleanPolicy OrganizationPolicyBooleanPolicyPtrOutput `pulumi:"booleanPolicy"`
	// The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
	Constraint pulumi.StringOutput `pulumi:"constraint"`
	// (Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
	ListPolicy OrganizationPolicyListPolicyPtrOutput `pulumi:"listPolicy"`
	// The project id of the project to set the policy for.
	Project pulumi.StringOutput `pulumi:"project"`
	// A restore policy is a constraint to restore the default policy. Structure is documented below.
	RestorePolicy OrganizationPolicyRestorePolicyPtrOutput `pulumi:"restorePolicy"`
	// (Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
	// Version of the Policy. Default version is 0.
	Version pulumi.IntOutput `pulumi:"version"`
}

// NewOrganizationPolicy registers a new resource with the given unique name, arguments, and options.
func NewOrganizationPolicy(ctx *pulumi.Context,
	name string, args *OrganizationPolicyArgs, opts ...pulumi.ResourceOption) (*OrganizationPolicy, error) {
	if args == nil || args.Constraint == nil {
		return nil, errors.New("missing required argument 'Constraint'")
	}
	if args == nil || args.Project == nil {
		return nil, errors.New("missing required argument 'Project'")
	}
	if args == nil {
		args = &OrganizationPolicyArgs{}
	}
	var resource OrganizationPolicy
	err := ctx.RegisterResource("gcp:projects/organizationPolicy:OrganizationPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrganizationPolicy gets an existing OrganizationPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrganizationPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrganizationPolicyState, opts ...pulumi.ResourceOption) (*OrganizationPolicy, error) {
	var resource OrganizationPolicy
	err := ctx.ReadResource("gcp:projects/organizationPolicy:OrganizationPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OrganizationPolicy resources.
type organizationPolicyState struct {
	// A boolean policy is a constraint that is either enforced or not. Structure is documented below.
	BooleanPolicy *OrganizationPolicyBooleanPolicy `pulumi:"booleanPolicy"`
	// The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
	Constraint *string `pulumi:"constraint"`
	// (Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
	Etag *string `pulumi:"etag"`
	// A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
	ListPolicy *OrganizationPolicyListPolicy `pulumi:"listPolicy"`
	// The project id of the project to set the policy for.
	Project *string `pulumi:"project"`
	// A restore policy is a constraint to restore the default policy. Structure is documented below.
	RestorePolicy *OrganizationPolicyRestorePolicy `pulumi:"restorePolicy"`
	// (Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
	UpdateTime *string `pulumi:"updateTime"`
	// Version of the Policy. Default version is 0.
	Version *int `pulumi:"version"`
}

type OrganizationPolicyState struct {
	// A boolean policy is a constraint that is either enforced or not. Structure is documented below.
	BooleanPolicy OrganizationPolicyBooleanPolicyPtrInput
	// The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
	Constraint pulumi.StringPtrInput
	// (Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
	Etag pulumi.StringPtrInput
	// A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
	ListPolicy OrganizationPolicyListPolicyPtrInput
	// The project id of the project to set the policy for.
	Project pulumi.StringPtrInput
	// A restore policy is a constraint to restore the default policy. Structure is documented below.
	RestorePolicy OrganizationPolicyRestorePolicyPtrInput
	// (Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
	UpdateTime pulumi.StringPtrInput
	// Version of the Policy. Default version is 0.
	Version pulumi.IntPtrInput
}

func (OrganizationPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationPolicyState)(nil)).Elem()
}

type organizationPolicyArgs struct {
	// A boolean policy is a constraint that is either enforced or not. Structure is documented below.
	BooleanPolicy *OrganizationPolicyBooleanPolicy `pulumi:"booleanPolicy"`
	// The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
	Constraint string `pulumi:"constraint"`
	// A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
	ListPolicy *OrganizationPolicyListPolicy `pulumi:"listPolicy"`
	// The project id of the project to set the policy for.
	Project string `pulumi:"project"`
	// A restore policy is a constraint to restore the default policy. Structure is documented below.
	RestorePolicy *OrganizationPolicyRestorePolicy `pulumi:"restorePolicy"`
	// Version of the Policy. Default version is 0.
	Version *int `pulumi:"version"`
}

// The set of arguments for constructing a OrganizationPolicy resource.
type OrganizationPolicyArgs struct {
	// A boolean policy is a constraint that is either enforced or not. Structure is documented below.
	BooleanPolicy OrganizationPolicyBooleanPolicyPtrInput
	// The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
	Constraint pulumi.StringInput
	// A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
	ListPolicy OrganizationPolicyListPolicyPtrInput
	// The project id of the project to set the policy for.
	Project pulumi.StringInput
	// A restore policy is a constraint to restore the default policy. Structure is documented below.
	RestorePolicy OrganizationPolicyRestorePolicyPtrInput
	// Version of the Policy. Default version is 0.
	Version pulumi.IntPtrInput
}

func (OrganizationPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationPolicyArgs)(nil)).Elem()
}
