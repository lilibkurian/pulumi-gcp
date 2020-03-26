// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package storage

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The hmacKeys resource represents an HMAC key within Cloud Storage. The resource
// consists of a secret and HMAC key metadata. HMAC keys can be used as credentials
// for service accounts.
//
//
// To get more information about HmacKey, see:
//
// * [API documentation](https://cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/storage/docs/authentication/managing-hmackeys)
//
// > **Warning:** All arguments including the `secret` value will be stored in the raw
// state as plain-text. [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
// On import, the `secret` value will not be retrieved.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/storage_hmac_key.html.markdown.
type HmacKey struct {
	pulumi.CustomResourceState

	// The access ID of the HMAC Key.
	AccessId pulumi.StringOutput `pulumi:"accessId"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// HMAC secret key material.
	Secret pulumi.StringOutput `pulumi:"secret"`
	// The email address of the key's associated service account.
	ServiceAccountEmail pulumi.StringOutput `pulumi:"serviceAccountEmail"`
	// The state of the key. Can be set to one of ACTIVE, INACTIVE.
	State pulumi.StringPtrOutput `pulumi:"state"`
	// 'The creation time of the HMAC key in RFC 3339 format. '
	TimeCreated pulumi.StringOutput `pulumi:"timeCreated"`
	// 'The last modification time of the HMAC key metadata in RFC 3339 format.'
	Updated pulumi.StringOutput `pulumi:"updated"`
}

// NewHmacKey registers a new resource with the given unique name, arguments, and options.
func NewHmacKey(ctx *pulumi.Context,
	name string, args *HmacKeyArgs, opts ...pulumi.ResourceOption) (*HmacKey, error) {
	if args == nil || args.ServiceAccountEmail == nil {
		return nil, errors.New("missing required argument 'ServiceAccountEmail'")
	}
	if args == nil {
		args = &HmacKeyArgs{}
	}
	var resource HmacKey
	err := ctx.RegisterResource("gcp:storage/hmacKey:HmacKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHmacKey gets an existing HmacKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHmacKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HmacKeyState, opts ...pulumi.ResourceOption) (*HmacKey, error) {
	var resource HmacKey
	err := ctx.ReadResource("gcp:storage/hmacKey:HmacKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HmacKey resources.
type hmacKeyState struct {
	// The access ID of the HMAC Key.
	AccessId *string `pulumi:"accessId"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// HMAC secret key material.
	Secret *string `pulumi:"secret"`
	// The email address of the key's associated service account.
	ServiceAccountEmail *string `pulumi:"serviceAccountEmail"`
	// The state of the key. Can be set to one of ACTIVE, INACTIVE.
	State *string `pulumi:"state"`
	// 'The creation time of the HMAC key in RFC 3339 format. '
	TimeCreated *string `pulumi:"timeCreated"`
	// 'The last modification time of the HMAC key metadata in RFC 3339 format.'
	Updated *string `pulumi:"updated"`
}

type HmacKeyState struct {
	// The access ID of the HMAC Key.
	AccessId pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// HMAC secret key material.
	Secret pulumi.StringPtrInput
	// The email address of the key's associated service account.
	ServiceAccountEmail pulumi.StringPtrInput
	// The state of the key. Can be set to one of ACTIVE, INACTIVE.
	State pulumi.StringPtrInput
	// 'The creation time of the HMAC key in RFC 3339 format. '
	TimeCreated pulumi.StringPtrInput
	// 'The last modification time of the HMAC key metadata in RFC 3339 format.'
	Updated pulumi.StringPtrInput
}

func (HmacKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*hmacKeyState)(nil)).Elem()
}

type hmacKeyArgs struct {
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The email address of the key's associated service account.
	ServiceAccountEmail string `pulumi:"serviceAccountEmail"`
	// The state of the key. Can be set to one of ACTIVE, INACTIVE.
	State *string `pulumi:"state"`
}

// The set of arguments for constructing a HmacKey resource.
type HmacKeyArgs struct {
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The email address of the key's associated service account.
	ServiceAccountEmail pulumi.StringInput
	// The state of the key. Can be set to one of ACTIVE, INACTIVE.
	State pulumi.StringPtrInput
}

func (HmacKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hmacKeyArgs)(nil)).Elem()
}
