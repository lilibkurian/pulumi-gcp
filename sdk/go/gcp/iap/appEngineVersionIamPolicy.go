// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package iap

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Three different resources help you manage your IAM policy for Identity-Aware Proxy AppEngineVersion. Each of these resources serves a different use case:
//
// * `iap.AppEngineVersionIamPolicy`: Authoritative. Sets the IAM policy for the appengineversion and replaces any existing policy already attached.
// * `iap.AppEngineVersionIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the appengineversion are preserved.
// * `iap.AppEngineVersionIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the appengineversion are preserved.
//
// > **Note:** `iap.AppEngineVersionIamPolicy` **cannot** be used in conjunction with `iap.AppEngineVersionIamBinding` and `iap.AppEngineVersionIamMember` or they will fight over what your policy should be.
//
// > **Note:** `iap.AppEngineVersionIamBinding` resources **can be** used in conjunction with `iap.AppEngineVersionIamMember` resources **only if** they do not grant privilege to the same role.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_app_engine_version_iam.html.markdown.
type AppEngineVersionIamPolicy struct {
	pulumi.CustomResourceState

	// Id of the App Engine application. Used to find the parent resource to bind the IAM policy to
	AppId pulumi.StringOutput `pulumi:"appId"`
	// (Computed) The etag of the IAM policy.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringOutput `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// Service id of the App Engine application Used to find the parent resource to bind the IAM policy to
	Service pulumi.StringOutput `pulumi:"service"`
	// Version id of the App Engine application Used to find the parent resource to bind the IAM policy to
	VersionId pulumi.StringOutput `pulumi:"versionId"`
}

// NewAppEngineVersionIamPolicy registers a new resource with the given unique name, arguments, and options.
func NewAppEngineVersionIamPolicy(ctx *pulumi.Context,
	name string, args *AppEngineVersionIamPolicyArgs, opts ...pulumi.ResourceOption) (*AppEngineVersionIamPolicy, error) {
	if args == nil || args.AppId == nil {
		return nil, errors.New("missing required argument 'AppId'")
	}
	if args == nil || args.PolicyData == nil {
		return nil, errors.New("missing required argument 'PolicyData'")
	}
	if args == nil || args.Service == nil {
		return nil, errors.New("missing required argument 'Service'")
	}
	if args == nil || args.VersionId == nil {
		return nil, errors.New("missing required argument 'VersionId'")
	}
	if args == nil {
		args = &AppEngineVersionIamPolicyArgs{}
	}
	var resource AppEngineVersionIamPolicy
	err := ctx.RegisterResource("gcp:iap/appEngineVersionIamPolicy:AppEngineVersionIamPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAppEngineVersionIamPolicy gets an existing AppEngineVersionIamPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAppEngineVersionIamPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AppEngineVersionIamPolicyState, opts ...pulumi.ResourceOption) (*AppEngineVersionIamPolicy, error) {
	var resource AppEngineVersionIamPolicy
	err := ctx.ReadResource("gcp:iap/appEngineVersionIamPolicy:AppEngineVersionIamPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AppEngineVersionIamPolicy resources.
type appEngineVersionIamPolicyState struct {
	// Id of the App Engine application. Used to find the parent resource to bind the IAM policy to
	AppId *string `pulumi:"appId"`
	// (Computed) The etag of the IAM policy.
	Etag *string `pulumi:"etag"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData *string `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	// Service id of the App Engine application Used to find the parent resource to bind the IAM policy to
	Service *string `pulumi:"service"`
	// Version id of the App Engine application Used to find the parent resource to bind the IAM policy to
	VersionId *string `pulumi:"versionId"`
}

type AppEngineVersionIamPolicyState struct {
	// Id of the App Engine application. Used to find the parent resource to bind the IAM policy to
	AppId pulumi.StringPtrInput
	// (Computed) The etag of the IAM policy.
	Etag pulumi.StringPtrInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	// Service id of the App Engine application Used to find the parent resource to bind the IAM policy to
	Service pulumi.StringPtrInput
	// Version id of the App Engine application Used to find the parent resource to bind the IAM policy to
	VersionId pulumi.StringPtrInput
}

func (AppEngineVersionIamPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*appEngineVersionIamPolicyState)(nil)).Elem()
}

type appEngineVersionIamPolicyArgs struct {
	// Id of the App Engine application. Used to find the parent resource to bind the IAM policy to
	AppId string `pulumi:"appId"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData string `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	// Service id of the App Engine application Used to find the parent resource to bind the IAM policy to
	Service string `pulumi:"service"`
	// Version id of the App Engine application Used to find the parent resource to bind the IAM policy to
	VersionId string `pulumi:"versionId"`
}

// The set of arguments for constructing a AppEngineVersionIamPolicy resource.
type AppEngineVersionIamPolicyArgs struct {
	// Id of the App Engine application. Used to find the parent resource to bind the IAM policy to
	AppId pulumi.StringInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	// Service id of the App Engine application Used to find the parent resource to bind the IAM policy to
	Service pulumi.StringInput
	// Version id of the App Engine application Used to find the parent resource to bind the IAM policy to
	VersionId pulumi.StringInput
}

func (AppEngineVersionIamPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*appEngineVersionIamPolicyArgs)(nil)).Elem()
}
