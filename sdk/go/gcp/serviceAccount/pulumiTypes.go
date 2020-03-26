// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package serviceAccount

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type IAMBindingCondition struct {
	// An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
	Description *string `pulumi:"description"`
	// Textual representation of an expression in Common Expression Language syntax.
	Expression string `pulumi:"expression"`
	// A title for the expression, i.e. a short string describing its purpose.
	Title string `pulumi:"title"`
}

type IAMBindingConditionInput interface {
	pulumi.Input

	ToIAMBindingConditionOutput() IAMBindingConditionOutput
	ToIAMBindingConditionOutputWithContext(context.Context) IAMBindingConditionOutput
}

type IAMBindingConditionArgs struct {
	// An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
	Description pulumi.StringPtrInput `pulumi:"description"`
	// Textual representation of an expression in Common Expression Language syntax.
	Expression pulumi.StringInput `pulumi:"expression"`
	// A title for the expression, i.e. a short string describing its purpose.
	Title pulumi.StringInput `pulumi:"title"`
}

func (IAMBindingConditionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*IAMBindingCondition)(nil)).Elem()
}

func (i IAMBindingConditionArgs) ToIAMBindingConditionOutput() IAMBindingConditionOutput {
	return i.ToIAMBindingConditionOutputWithContext(context.Background())
}

func (i IAMBindingConditionArgs) ToIAMBindingConditionOutputWithContext(ctx context.Context) IAMBindingConditionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IAMBindingConditionOutput)
}

func (i IAMBindingConditionArgs) ToIAMBindingConditionPtrOutput() IAMBindingConditionPtrOutput {
	return i.ToIAMBindingConditionPtrOutputWithContext(context.Background())
}

func (i IAMBindingConditionArgs) ToIAMBindingConditionPtrOutputWithContext(ctx context.Context) IAMBindingConditionPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IAMBindingConditionOutput).ToIAMBindingConditionPtrOutputWithContext(ctx)
}

type IAMBindingConditionPtrInput interface {
	pulumi.Input

	ToIAMBindingConditionPtrOutput() IAMBindingConditionPtrOutput
	ToIAMBindingConditionPtrOutputWithContext(context.Context) IAMBindingConditionPtrOutput
}

type iambindingConditionPtrType IAMBindingConditionArgs

func IAMBindingConditionPtr(v *IAMBindingConditionArgs) IAMBindingConditionPtrInput {
	return (*iambindingConditionPtrType)(v)
}

func (*iambindingConditionPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**IAMBindingCondition)(nil)).Elem()
}

func (i *iambindingConditionPtrType) ToIAMBindingConditionPtrOutput() IAMBindingConditionPtrOutput {
	return i.ToIAMBindingConditionPtrOutputWithContext(context.Background())
}

func (i *iambindingConditionPtrType) ToIAMBindingConditionPtrOutputWithContext(ctx context.Context) IAMBindingConditionPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IAMBindingConditionPtrOutput)
}

type IAMBindingConditionOutput struct{ *pulumi.OutputState }

func (IAMBindingConditionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*IAMBindingCondition)(nil)).Elem()
}

func (o IAMBindingConditionOutput) ToIAMBindingConditionOutput() IAMBindingConditionOutput {
	return o
}

func (o IAMBindingConditionOutput) ToIAMBindingConditionOutputWithContext(ctx context.Context) IAMBindingConditionOutput {
	return o
}

func (o IAMBindingConditionOutput) ToIAMBindingConditionPtrOutput() IAMBindingConditionPtrOutput {
	return o.ToIAMBindingConditionPtrOutputWithContext(context.Background())
}

func (o IAMBindingConditionOutput) ToIAMBindingConditionPtrOutputWithContext(ctx context.Context) IAMBindingConditionPtrOutput {
	return o.ApplyT(func(v IAMBindingCondition) *IAMBindingCondition {
		return &v
	}).(IAMBindingConditionPtrOutput)
}

// An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
func (o IAMBindingConditionOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v IAMBindingCondition) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Textual representation of an expression in Common Expression Language syntax.
func (o IAMBindingConditionOutput) Expression() pulumi.StringOutput {
	return o.ApplyT(func(v IAMBindingCondition) string { return v.Expression }).(pulumi.StringOutput)
}

// A title for the expression, i.e. a short string describing its purpose.
func (o IAMBindingConditionOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v IAMBindingCondition) string { return v.Title }).(pulumi.StringOutput)
}

type IAMBindingConditionPtrOutput struct{ *pulumi.OutputState }

func (IAMBindingConditionPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IAMBindingCondition)(nil)).Elem()
}

func (o IAMBindingConditionPtrOutput) ToIAMBindingConditionPtrOutput() IAMBindingConditionPtrOutput {
	return o
}

func (o IAMBindingConditionPtrOutput) ToIAMBindingConditionPtrOutputWithContext(ctx context.Context) IAMBindingConditionPtrOutput {
	return o
}

func (o IAMBindingConditionPtrOutput) Elem() IAMBindingConditionOutput {
	return o.ApplyT(func(v *IAMBindingCondition) IAMBindingCondition { return *v }).(IAMBindingConditionOutput)
}

// An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
func (o IAMBindingConditionPtrOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v IAMBindingCondition) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Textual representation of an expression in Common Expression Language syntax.
func (o IAMBindingConditionPtrOutput) Expression() pulumi.StringOutput {
	return o.ApplyT(func(v IAMBindingCondition) string { return v.Expression }).(pulumi.StringOutput)
}

// A title for the expression, i.e. a short string describing its purpose.
func (o IAMBindingConditionPtrOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v IAMBindingCondition) string { return v.Title }).(pulumi.StringOutput)
}

type IAMMemberCondition struct {
	// An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
	Description *string `pulumi:"description"`
	// Textual representation of an expression in Common Expression Language syntax.
	Expression string `pulumi:"expression"`
	// A title for the expression, i.e. a short string describing its purpose.
	Title string `pulumi:"title"`
}

type IAMMemberConditionInput interface {
	pulumi.Input

	ToIAMMemberConditionOutput() IAMMemberConditionOutput
	ToIAMMemberConditionOutputWithContext(context.Context) IAMMemberConditionOutput
}

type IAMMemberConditionArgs struct {
	// An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
	Description pulumi.StringPtrInput `pulumi:"description"`
	// Textual representation of an expression in Common Expression Language syntax.
	Expression pulumi.StringInput `pulumi:"expression"`
	// A title for the expression, i.e. a short string describing its purpose.
	Title pulumi.StringInput `pulumi:"title"`
}

func (IAMMemberConditionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*IAMMemberCondition)(nil)).Elem()
}

func (i IAMMemberConditionArgs) ToIAMMemberConditionOutput() IAMMemberConditionOutput {
	return i.ToIAMMemberConditionOutputWithContext(context.Background())
}

func (i IAMMemberConditionArgs) ToIAMMemberConditionOutputWithContext(ctx context.Context) IAMMemberConditionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IAMMemberConditionOutput)
}

func (i IAMMemberConditionArgs) ToIAMMemberConditionPtrOutput() IAMMemberConditionPtrOutput {
	return i.ToIAMMemberConditionPtrOutputWithContext(context.Background())
}

func (i IAMMemberConditionArgs) ToIAMMemberConditionPtrOutputWithContext(ctx context.Context) IAMMemberConditionPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IAMMemberConditionOutput).ToIAMMemberConditionPtrOutputWithContext(ctx)
}

type IAMMemberConditionPtrInput interface {
	pulumi.Input

	ToIAMMemberConditionPtrOutput() IAMMemberConditionPtrOutput
	ToIAMMemberConditionPtrOutputWithContext(context.Context) IAMMemberConditionPtrOutput
}

type iammemberConditionPtrType IAMMemberConditionArgs

func IAMMemberConditionPtr(v *IAMMemberConditionArgs) IAMMemberConditionPtrInput {
	return (*iammemberConditionPtrType)(v)
}

func (*iammemberConditionPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**IAMMemberCondition)(nil)).Elem()
}

func (i *iammemberConditionPtrType) ToIAMMemberConditionPtrOutput() IAMMemberConditionPtrOutput {
	return i.ToIAMMemberConditionPtrOutputWithContext(context.Background())
}

func (i *iammemberConditionPtrType) ToIAMMemberConditionPtrOutputWithContext(ctx context.Context) IAMMemberConditionPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IAMMemberConditionPtrOutput)
}

type IAMMemberConditionOutput struct{ *pulumi.OutputState }

func (IAMMemberConditionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*IAMMemberCondition)(nil)).Elem()
}

func (o IAMMemberConditionOutput) ToIAMMemberConditionOutput() IAMMemberConditionOutput {
	return o
}

func (o IAMMemberConditionOutput) ToIAMMemberConditionOutputWithContext(ctx context.Context) IAMMemberConditionOutput {
	return o
}

func (o IAMMemberConditionOutput) ToIAMMemberConditionPtrOutput() IAMMemberConditionPtrOutput {
	return o.ToIAMMemberConditionPtrOutputWithContext(context.Background())
}

func (o IAMMemberConditionOutput) ToIAMMemberConditionPtrOutputWithContext(ctx context.Context) IAMMemberConditionPtrOutput {
	return o.ApplyT(func(v IAMMemberCondition) *IAMMemberCondition {
		return &v
	}).(IAMMemberConditionPtrOutput)
}

// An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
func (o IAMMemberConditionOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v IAMMemberCondition) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Textual representation of an expression in Common Expression Language syntax.
func (o IAMMemberConditionOutput) Expression() pulumi.StringOutput {
	return o.ApplyT(func(v IAMMemberCondition) string { return v.Expression }).(pulumi.StringOutput)
}

// A title for the expression, i.e. a short string describing its purpose.
func (o IAMMemberConditionOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v IAMMemberCondition) string { return v.Title }).(pulumi.StringOutput)
}

type IAMMemberConditionPtrOutput struct{ *pulumi.OutputState }

func (IAMMemberConditionPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IAMMemberCondition)(nil)).Elem()
}

func (o IAMMemberConditionPtrOutput) ToIAMMemberConditionPtrOutput() IAMMemberConditionPtrOutput {
	return o
}

func (o IAMMemberConditionPtrOutput) ToIAMMemberConditionPtrOutputWithContext(ctx context.Context) IAMMemberConditionPtrOutput {
	return o
}

func (o IAMMemberConditionPtrOutput) Elem() IAMMemberConditionOutput {
	return o.ApplyT(func(v *IAMMemberCondition) IAMMemberCondition { return *v }).(IAMMemberConditionOutput)
}

// An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
func (o IAMMemberConditionPtrOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v IAMMemberCondition) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Textual representation of an expression in Common Expression Language syntax.
func (o IAMMemberConditionPtrOutput) Expression() pulumi.StringOutput {
	return o.ApplyT(func(v IAMMemberCondition) string { return v.Expression }).(pulumi.StringOutput)
}

// A title for the expression, i.e. a short string describing its purpose.
func (o IAMMemberConditionPtrOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v IAMMemberCondition) string { return v.Title }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(IAMBindingConditionOutput{})
	pulumi.RegisterOutputType(IAMBindingConditionPtrOutput{})
	pulumi.RegisterOutputType(IAMMemberConditionOutput{})
	pulumi.RegisterOutputType(IAMMemberConditionPtrOutput{})
}
