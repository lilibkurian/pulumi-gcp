// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type GetTestablePermissionsPermission struct {
	// Whether the corresponding API has been enabled for the resource.
	ApiDisabled bool `pulumi:"apiDisabled"`
	// The level of support for custom roles. Can be one of `"NOT_SUPPORTED"`, `"SUPPORTED"`, `"TESTING"`. Default is `"SUPPORTED"`
	CustomSupportLevel string `pulumi:"customSupportLevel"`
	// Name of the permission.
	Name string `pulumi:"name"`
	// Release stage of the permission.
	Stage string `pulumi:"stage"`
	// Human readable title of the permission.
	Title string `pulumi:"title"`
}

// GetTestablePermissionsPermissionInput is an input type that accepts GetTestablePermissionsPermissionArgs and GetTestablePermissionsPermissionOutput values.
// You can construct a concrete instance of `GetTestablePermissionsPermissionInput` via:
//
//          GetTestablePermissionsPermissionArgs{...}
type GetTestablePermissionsPermissionInput interface {
	pulumi.Input

	ToGetTestablePermissionsPermissionOutput() GetTestablePermissionsPermissionOutput
	ToGetTestablePermissionsPermissionOutputWithContext(context.Context) GetTestablePermissionsPermissionOutput
}

type GetTestablePermissionsPermissionArgs struct {
	// Whether the corresponding API has been enabled for the resource.
	ApiDisabled pulumi.BoolInput `pulumi:"apiDisabled"`
	// The level of support for custom roles. Can be one of `"NOT_SUPPORTED"`, `"SUPPORTED"`, `"TESTING"`. Default is `"SUPPORTED"`
	CustomSupportLevel pulumi.StringInput `pulumi:"customSupportLevel"`
	// Name of the permission.
	Name pulumi.StringInput `pulumi:"name"`
	// Release stage of the permission.
	Stage pulumi.StringInput `pulumi:"stage"`
	// Human readable title of the permission.
	Title pulumi.StringInput `pulumi:"title"`
}

func (GetTestablePermissionsPermissionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTestablePermissionsPermission)(nil)).Elem()
}

func (i GetTestablePermissionsPermissionArgs) ToGetTestablePermissionsPermissionOutput() GetTestablePermissionsPermissionOutput {
	return i.ToGetTestablePermissionsPermissionOutputWithContext(context.Background())
}

func (i GetTestablePermissionsPermissionArgs) ToGetTestablePermissionsPermissionOutputWithContext(ctx context.Context) GetTestablePermissionsPermissionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetTestablePermissionsPermissionOutput)
}

// GetTestablePermissionsPermissionArrayInput is an input type that accepts GetTestablePermissionsPermissionArray and GetTestablePermissionsPermissionArrayOutput values.
// You can construct a concrete instance of `GetTestablePermissionsPermissionArrayInput` via:
//
//          GetTestablePermissionsPermissionArray{ GetTestablePermissionsPermissionArgs{...} }
type GetTestablePermissionsPermissionArrayInput interface {
	pulumi.Input

	ToGetTestablePermissionsPermissionArrayOutput() GetTestablePermissionsPermissionArrayOutput
	ToGetTestablePermissionsPermissionArrayOutputWithContext(context.Context) GetTestablePermissionsPermissionArrayOutput
}

type GetTestablePermissionsPermissionArray []GetTestablePermissionsPermissionInput

func (GetTestablePermissionsPermissionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetTestablePermissionsPermission)(nil)).Elem()
}

func (i GetTestablePermissionsPermissionArray) ToGetTestablePermissionsPermissionArrayOutput() GetTestablePermissionsPermissionArrayOutput {
	return i.ToGetTestablePermissionsPermissionArrayOutputWithContext(context.Background())
}

func (i GetTestablePermissionsPermissionArray) ToGetTestablePermissionsPermissionArrayOutputWithContext(ctx context.Context) GetTestablePermissionsPermissionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetTestablePermissionsPermissionArrayOutput)
}

type GetTestablePermissionsPermissionOutput struct{ *pulumi.OutputState }

func (GetTestablePermissionsPermissionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTestablePermissionsPermission)(nil)).Elem()
}

func (o GetTestablePermissionsPermissionOutput) ToGetTestablePermissionsPermissionOutput() GetTestablePermissionsPermissionOutput {
	return o
}

func (o GetTestablePermissionsPermissionOutput) ToGetTestablePermissionsPermissionOutputWithContext(ctx context.Context) GetTestablePermissionsPermissionOutput {
	return o
}

// Whether the corresponding API has been enabled for the resource.
func (o GetTestablePermissionsPermissionOutput) ApiDisabled() pulumi.BoolOutput {
	return o.ApplyT(func(v GetTestablePermissionsPermission) bool { return v.ApiDisabled }).(pulumi.BoolOutput)
}

// The level of support for custom roles. Can be one of `"NOT_SUPPORTED"`, `"SUPPORTED"`, `"TESTING"`. Default is `"SUPPORTED"`
func (o GetTestablePermissionsPermissionOutput) CustomSupportLevel() pulumi.StringOutput {
	return o.ApplyT(func(v GetTestablePermissionsPermission) string { return v.CustomSupportLevel }).(pulumi.StringOutput)
}

// Name of the permission.
func (o GetTestablePermissionsPermissionOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetTestablePermissionsPermission) string { return v.Name }).(pulumi.StringOutput)
}

// Release stage of the permission.
func (o GetTestablePermissionsPermissionOutput) Stage() pulumi.StringOutput {
	return o.ApplyT(func(v GetTestablePermissionsPermission) string { return v.Stage }).(pulumi.StringOutput)
}

// Human readable title of the permission.
func (o GetTestablePermissionsPermissionOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v GetTestablePermissionsPermission) string { return v.Title }).(pulumi.StringOutput)
}

type GetTestablePermissionsPermissionArrayOutput struct{ *pulumi.OutputState }

func (GetTestablePermissionsPermissionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetTestablePermissionsPermission)(nil)).Elem()
}

func (o GetTestablePermissionsPermissionArrayOutput) ToGetTestablePermissionsPermissionArrayOutput() GetTestablePermissionsPermissionArrayOutput {
	return o
}

func (o GetTestablePermissionsPermissionArrayOutput) ToGetTestablePermissionsPermissionArrayOutputWithContext(ctx context.Context) GetTestablePermissionsPermissionArrayOutput {
	return o
}

func (o GetTestablePermissionsPermissionArrayOutput) Index(i pulumi.IntInput) GetTestablePermissionsPermissionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetTestablePermissionsPermission {
		return vs[0].([]GetTestablePermissionsPermission)[vs[1].(int)]
	}).(GetTestablePermissionsPermissionOutput)
}

func init() {
	pulumi.RegisterOutputType(GetTestablePermissionsPermissionOutput{})
	pulumi.RegisterOutputType(GetTestablePermissionsPermissionArrayOutput{})
}
