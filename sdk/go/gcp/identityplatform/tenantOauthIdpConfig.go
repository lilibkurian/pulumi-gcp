// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package identityplatform

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// OIDC IdP configuration for a Identity Toolkit project within a tenant.
//
// You must enable the
// [Google Identity Platform](https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity) in
// the marketplace prior to using this resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/identity_platform_tenant_oauth_idp_config.html.markdown.
type TenantOauthIdpConfig struct {
	pulumi.CustomResourceState

	// The client id of an OAuth client.
	ClientId pulumi.StringOutput `pulumi:"clientId"`
	// The client secret of the OAuth client, to enable OIDC code flow.
	ClientSecret pulumi.StringPtrOutput `pulumi:"clientSecret"`
	// Human friendly display name.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// If this config allows users to sign in with the provider.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// For OIDC Idps, the issuer identifier.
	Issuer pulumi.StringOutput `pulumi:"issuer"`
	// The name of the OauthIdpConfig. Must start with 'oidc.'.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The name of the tenant where this OIDC IDP configuration resource exists
	Tenant pulumi.StringOutput `pulumi:"tenant"`
}

// NewTenantOauthIdpConfig registers a new resource with the given unique name, arguments, and options.
func NewTenantOauthIdpConfig(ctx *pulumi.Context,
	name string, args *TenantOauthIdpConfigArgs, opts ...pulumi.ResourceOption) (*TenantOauthIdpConfig, error) {
	if args == nil || args.ClientId == nil {
		return nil, errors.New("missing required argument 'ClientId'")
	}
	if args == nil || args.DisplayName == nil {
		return nil, errors.New("missing required argument 'DisplayName'")
	}
	if args == nil || args.Issuer == nil {
		return nil, errors.New("missing required argument 'Issuer'")
	}
	if args == nil || args.Tenant == nil {
		return nil, errors.New("missing required argument 'Tenant'")
	}
	if args == nil {
		args = &TenantOauthIdpConfigArgs{}
	}
	var resource TenantOauthIdpConfig
	err := ctx.RegisterResource("gcp:identityplatform/tenantOauthIdpConfig:TenantOauthIdpConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTenantOauthIdpConfig gets an existing TenantOauthIdpConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTenantOauthIdpConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TenantOauthIdpConfigState, opts ...pulumi.ResourceOption) (*TenantOauthIdpConfig, error) {
	var resource TenantOauthIdpConfig
	err := ctx.ReadResource("gcp:identityplatform/tenantOauthIdpConfig:TenantOauthIdpConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TenantOauthIdpConfig resources.
type tenantOauthIdpConfigState struct {
	// The client id of an OAuth client.
	ClientId *string `pulumi:"clientId"`
	// The client secret of the OAuth client, to enable OIDC code flow.
	ClientSecret *string `pulumi:"clientSecret"`
	// Human friendly display name.
	DisplayName *string `pulumi:"displayName"`
	// If this config allows users to sign in with the provider.
	Enabled *bool `pulumi:"enabled"`
	// For OIDC Idps, the issuer identifier.
	Issuer *string `pulumi:"issuer"`
	// The name of the OauthIdpConfig. Must start with 'oidc.'.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The name of the tenant where this OIDC IDP configuration resource exists
	Tenant *string `pulumi:"tenant"`
}

type TenantOauthIdpConfigState struct {
	// The client id of an OAuth client.
	ClientId pulumi.StringPtrInput
	// The client secret of the OAuth client, to enable OIDC code flow.
	ClientSecret pulumi.StringPtrInput
	// Human friendly display name.
	DisplayName pulumi.StringPtrInput
	// If this config allows users to sign in with the provider.
	Enabled pulumi.BoolPtrInput
	// For OIDC Idps, the issuer identifier.
	Issuer pulumi.StringPtrInput
	// The name of the OauthIdpConfig. Must start with 'oidc.'.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The name of the tenant where this OIDC IDP configuration resource exists
	Tenant pulumi.StringPtrInput
}

func (TenantOauthIdpConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*tenantOauthIdpConfigState)(nil)).Elem()
}

type tenantOauthIdpConfigArgs struct {
	// The client id of an OAuth client.
	ClientId string `pulumi:"clientId"`
	// The client secret of the OAuth client, to enable OIDC code flow.
	ClientSecret *string `pulumi:"clientSecret"`
	// Human friendly display name.
	DisplayName string `pulumi:"displayName"`
	// If this config allows users to sign in with the provider.
	Enabled *bool `pulumi:"enabled"`
	// For OIDC Idps, the issuer identifier.
	Issuer string `pulumi:"issuer"`
	// The name of the OauthIdpConfig. Must start with 'oidc.'.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The name of the tenant where this OIDC IDP configuration resource exists
	Tenant string `pulumi:"tenant"`
}

// The set of arguments for constructing a TenantOauthIdpConfig resource.
type TenantOauthIdpConfigArgs struct {
	// The client id of an OAuth client.
	ClientId pulumi.StringInput
	// The client secret of the OAuth client, to enable OIDC code flow.
	ClientSecret pulumi.StringPtrInput
	// Human friendly display name.
	DisplayName pulumi.StringInput
	// If this config allows users to sign in with the provider.
	Enabled pulumi.BoolPtrInput
	// For OIDC Idps, the issuer identifier.
	Issuer pulumi.StringInput
	// The name of the OauthIdpConfig. Must start with 'oidc.'.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The name of the tenant where this OIDC IDP configuration resource exists
	Tenant pulumi.StringInput
}

func (TenantOauthIdpConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tenantOauthIdpConfigArgs)(nil)).Elem()
}
