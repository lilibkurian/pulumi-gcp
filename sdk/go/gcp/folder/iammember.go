// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package folder

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Allows creation and management of a single member for a single binding within
// the IAM policy for an existing Google Cloud Platform folder.
//
// > **Note:** This resource _must not_ be used in conjunction with
//    `folder.IAMPolicy` or they will fight over what your policy
//    should be. Similarly, roles controlled by `folder.IAMBinding`
//    should not be assigned to using `folder.IAMMember`.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_folder_iam_member.html.markdown.
type IAMMember struct {
	pulumi.CustomResourceState

	Condition IAMMemberConditionPtrOutput `pulumi:"condition"`
	// (Computed) The etag of the folder's IAM policy.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.
	Folder pulumi.StringOutput `pulumi:"folder"`
	// The identity that will be granted the privilege in the `role`. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
	// This field can have one of the following values:
	// * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
	// * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
	// * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
	// * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
	Member pulumi.StringOutput `pulumi:"member"`
	// The role that should be applied. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role pulumi.StringOutput `pulumi:"role"`
}

// NewIAMMember registers a new resource with the given unique name, arguments, and options.
func NewIAMMember(ctx *pulumi.Context,
	name string, args *IAMMemberArgs, opts ...pulumi.ResourceOption) (*IAMMember, error) {
	if args == nil || args.Folder == nil {
		return nil, errors.New("missing required argument 'Folder'")
	}
	if args == nil || args.Member == nil {
		return nil, errors.New("missing required argument 'Member'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	if args == nil {
		args = &IAMMemberArgs{}
	}
	var resource IAMMember
	err := ctx.RegisterResource("gcp:folder/iAMMember:IAMMember", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIAMMember gets an existing IAMMember resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIAMMember(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IAMMemberState, opts ...pulumi.ResourceOption) (*IAMMember, error) {
	var resource IAMMember
	err := ctx.ReadResource("gcp:folder/iAMMember:IAMMember", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IAMMember resources.
type iammemberState struct {
	Condition *IAMMemberCondition `pulumi:"condition"`
	// (Computed) The etag of the folder's IAM policy.
	Etag *string `pulumi:"etag"`
	// The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.
	Folder *string `pulumi:"folder"`
	// The identity that will be granted the privilege in the `role`. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
	// This field can have one of the following values:
	// * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
	// * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
	// * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
	// * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
	Member *string `pulumi:"member"`
	// The role that should be applied. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role *string `pulumi:"role"`
}

type IAMMemberState struct {
	Condition IAMMemberConditionPtrInput
	// (Computed) The etag of the folder's IAM policy.
	Etag pulumi.StringPtrInput
	// The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.
	Folder pulumi.StringPtrInput
	// The identity that will be granted the privilege in the `role`. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
	// This field can have one of the following values:
	// * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
	// * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
	// * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
	// * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
	Member pulumi.StringPtrInput
	// The role that should be applied. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role pulumi.StringPtrInput
}

func (IAMMemberState) ElementType() reflect.Type {
	return reflect.TypeOf((*iammemberState)(nil)).Elem()
}

type iammemberArgs struct {
	Condition *IAMMemberCondition `pulumi:"condition"`
	// The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.
	Folder string `pulumi:"folder"`
	// The identity that will be granted the privilege in the `role`. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
	// This field can have one of the following values:
	// * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
	// * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
	// * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
	// * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
	Member string `pulumi:"member"`
	// The role that should be applied. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role string `pulumi:"role"`
}

// The set of arguments for constructing a IAMMember resource.
type IAMMemberArgs struct {
	Condition IAMMemberConditionPtrInput
	// The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.
	Folder pulumi.StringInput
	// The identity that will be granted the privilege in the `role`. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
	// This field can have one of the following values:
	// * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
	// * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
	// * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
	// * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
	Member pulumi.StringInput
	// The role that should be applied. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role pulumi.StringInput
}

func (IAMMemberArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*iammemberArgs)(nil)).Elem()
}
