// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package filestore

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type InstanceFileShares struct {
	// File share capacity in GiB. This must be at least 1024 GiB
	// for the standard tier, or 2560 GiB for the premium tier.
	CapacityGb int `pulumi:"capacityGb"`
	// The name of the fileshare (16 characters or less)
	Name             string                              `pulumi:"name"`
	NfsExportOptions []InstanceFileSharesNfsExportOption `pulumi:"nfsExportOptions"`
}

// InstanceFileSharesInput is an input type that accepts InstanceFileSharesArgs and InstanceFileSharesOutput values.
// You can construct a concrete instance of `InstanceFileSharesInput` via:
//
//          InstanceFileSharesArgs{...}
type InstanceFileSharesInput interface {
	pulumi.Input

	ToInstanceFileSharesOutput() InstanceFileSharesOutput
	ToInstanceFileSharesOutputWithContext(context.Context) InstanceFileSharesOutput
}

type InstanceFileSharesArgs struct {
	// File share capacity in GiB. This must be at least 1024 GiB
	// for the standard tier, or 2560 GiB for the premium tier.
	CapacityGb pulumi.IntInput `pulumi:"capacityGb"`
	// The name of the fileshare (16 characters or less)
	Name             pulumi.StringInput                          `pulumi:"name"`
	NfsExportOptions InstanceFileSharesNfsExportOptionArrayInput `pulumi:"nfsExportOptions"`
}

func (InstanceFileSharesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceFileShares)(nil)).Elem()
}

func (i InstanceFileSharesArgs) ToInstanceFileSharesOutput() InstanceFileSharesOutput {
	return i.ToInstanceFileSharesOutputWithContext(context.Background())
}

func (i InstanceFileSharesArgs) ToInstanceFileSharesOutputWithContext(ctx context.Context) InstanceFileSharesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceFileSharesOutput)
}

func (i InstanceFileSharesArgs) ToInstanceFileSharesPtrOutput() InstanceFileSharesPtrOutput {
	return i.ToInstanceFileSharesPtrOutputWithContext(context.Background())
}

func (i InstanceFileSharesArgs) ToInstanceFileSharesPtrOutputWithContext(ctx context.Context) InstanceFileSharesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceFileSharesOutput).ToInstanceFileSharesPtrOutputWithContext(ctx)
}

// InstanceFileSharesPtrInput is an input type that accepts InstanceFileSharesArgs, InstanceFileSharesPtr and InstanceFileSharesPtrOutput values.
// You can construct a concrete instance of `InstanceFileSharesPtrInput` via:
//
//          InstanceFileSharesArgs{...}
//
//  or:
//
//          nil
type InstanceFileSharesPtrInput interface {
	pulumi.Input

	ToInstanceFileSharesPtrOutput() InstanceFileSharesPtrOutput
	ToInstanceFileSharesPtrOutputWithContext(context.Context) InstanceFileSharesPtrOutput
}

type instanceFileSharesPtrType InstanceFileSharesArgs

func InstanceFileSharesPtr(v *InstanceFileSharesArgs) InstanceFileSharesPtrInput {
	return (*instanceFileSharesPtrType)(v)
}

func (*instanceFileSharesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceFileShares)(nil)).Elem()
}

func (i *instanceFileSharesPtrType) ToInstanceFileSharesPtrOutput() InstanceFileSharesPtrOutput {
	return i.ToInstanceFileSharesPtrOutputWithContext(context.Background())
}

func (i *instanceFileSharesPtrType) ToInstanceFileSharesPtrOutputWithContext(ctx context.Context) InstanceFileSharesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceFileSharesPtrOutput)
}

type InstanceFileSharesOutput struct{ *pulumi.OutputState }

func (InstanceFileSharesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceFileShares)(nil)).Elem()
}

func (o InstanceFileSharesOutput) ToInstanceFileSharesOutput() InstanceFileSharesOutput {
	return o
}

func (o InstanceFileSharesOutput) ToInstanceFileSharesOutputWithContext(ctx context.Context) InstanceFileSharesOutput {
	return o
}

func (o InstanceFileSharesOutput) ToInstanceFileSharesPtrOutput() InstanceFileSharesPtrOutput {
	return o.ToInstanceFileSharesPtrOutputWithContext(context.Background())
}

func (o InstanceFileSharesOutput) ToInstanceFileSharesPtrOutputWithContext(ctx context.Context) InstanceFileSharesPtrOutput {
	return o.ApplyT(func(v InstanceFileShares) *InstanceFileShares {
		return &v
	}).(InstanceFileSharesPtrOutput)
}

// File share capacity in GiB. This must be at least 1024 GiB
// for the standard tier, or 2560 GiB for the premium tier.
func (o InstanceFileSharesOutput) CapacityGb() pulumi.IntOutput {
	return o.ApplyT(func(v InstanceFileShares) int { return v.CapacityGb }).(pulumi.IntOutput)
}

// The name of the fileshare (16 characters or less)
func (o InstanceFileSharesOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v InstanceFileShares) string { return v.Name }).(pulumi.StringOutput)
}

func (o InstanceFileSharesOutput) NfsExportOptions() InstanceFileSharesNfsExportOptionArrayOutput {
	return o.ApplyT(func(v InstanceFileShares) []InstanceFileSharesNfsExportOption { return v.NfsExportOptions }).(InstanceFileSharesNfsExportOptionArrayOutput)
}

type InstanceFileSharesPtrOutput struct{ *pulumi.OutputState }

func (InstanceFileSharesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceFileShares)(nil)).Elem()
}

func (o InstanceFileSharesPtrOutput) ToInstanceFileSharesPtrOutput() InstanceFileSharesPtrOutput {
	return o
}

func (o InstanceFileSharesPtrOutput) ToInstanceFileSharesPtrOutputWithContext(ctx context.Context) InstanceFileSharesPtrOutput {
	return o
}

func (o InstanceFileSharesPtrOutput) Elem() InstanceFileSharesOutput {
	return o.ApplyT(func(v *InstanceFileShares) InstanceFileShares { return *v }).(InstanceFileSharesOutput)
}

// File share capacity in GiB. This must be at least 1024 GiB
// for the standard tier, or 2560 GiB for the premium tier.
func (o InstanceFileSharesPtrOutput) CapacityGb() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *InstanceFileShares) *int {
		if v == nil {
			return nil
		}
		return &v.CapacityGb
	}).(pulumi.IntPtrOutput)
}

// The name of the fileshare (16 characters or less)
func (o InstanceFileSharesPtrOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *InstanceFileShares) *string {
		if v == nil {
			return nil
		}
		return &v.Name
	}).(pulumi.StringPtrOutput)
}

func (o InstanceFileSharesPtrOutput) NfsExportOptions() InstanceFileSharesNfsExportOptionArrayOutput {
	return o.ApplyT(func(v *InstanceFileShares) []InstanceFileSharesNfsExportOption {
		if v == nil {
			return nil
		}
		return v.NfsExportOptions
	}).(InstanceFileSharesNfsExportOptionArrayOutput)
}

type InstanceFileSharesNfsExportOption struct {
	// Either READ_ONLY, for allowing only read requests on the exported directory,
	// or READ_WRITE, for allowing both read and write requests. The default is READ_WRITE.
	AccessMode *string `pulumi:"accessMode"`
	// An integer representing the anonymous group id with a default value of 65534.
	// Anon_gid may only be set with squashMode of ROOT_SQUASH. An error will be returned
	// if this field is specified for other squashMode settings.
	AnonGid *int `pulumi:"anonGid"`
	// An integer representing the anonymous user id with a default value of 65534.
	// Anon_uid may only be set with squashMode of ROOT_SQUASH. An error will be returned
	// if this field is specified for other squashMode settings.
	AnonUid *int `pulumi:"anonUid"`
	// List of either IPv4 addresses, or ranges in CIDR notation which may mount the file share.
	// Overlapping IP ranges are not allowed, both within and across NfsExportOptions. An error will be returned.
	// The limit is 64 IP ranges/addresses for each FileShareConfig among all NfsExportOptions.
	IpRanges []string `pulumi:"ipRanges"`
	// Either NO_ROOT_SQUASH, for allowing root access on the exported directory, or ROOT_SQUASH,
	// for not allowing root access. The default is NO_ROOT_SQUASH.
	SquashMode *string `pulumi:"squashMode"`
}

// InstanceFileSharesNfsExportOptionInput is an input type that accepts InstanceFileSharesNfsExportOptionArgs and InstanceFileSharesNfsExportOptionOutput values.
// You can construct a concrete instance of `InstanceFileSharesNfsExportOptionInput` via:
//
//          InstanceFileSharesNfsExportOptionArgs{...}
type InstanceFileSharesNfsExportOptionInput interface {
	pulumi.Input

	ToInstanceFileSharesNfsExportOptionOutput() InstanceFileSharesNfsExportOptionOutput
	ToInstanceFileSharesNfsExportOptionOutputWithContext(context.Context) InstanceFileSharesNfsExportOptionOutput
}

type InstanceFileSharesNfsExportOptionArgs struct {
	// Either READ_ONLY, for allowing only read requests on the exported directory,
	// or READ_WRITE, for allowing both read and write requests. The default is READ_WRITE.
	AccessMode pulumi.StringPtrInput `pulumi:"accessMode"`
	// An integer representing the anonymous group id with a default value of 65534.
	// Anon_gid may only be set with squashMode of ROOT_SQUASH. An error will be returned
	// if this field is specified for other squashMode settings.
	AnonGid pulumi.IntPtrInput `pulumi:"anonGid"`
	// An integer representing the anonymous user id with a default value of 65534.
	// Anon_uid may only be set with squashMode of ROOT_SQUASH. An error will be returned
	// if this field is specified for other squashMode settings.
	AnonUid pulumi.IntPtrInput `pulumi:"anonUid"`
	// List of either IPv4 addresses, or ranges in CIDR notation which may mount the file share.
	// Overlapping IP ranges are not allowed, both within and across NfsExportOptions. An error will be returned.
	// The limit is 64 IP ranges/addresses for each FileShareConfig among all NfsExportOptions.
	IpRanges pulumi.StringArrayInput `pulumi:"ipRanges"`
	// Either NO_ROOT_SQUASH, for allowing root access on the exported directory, or ROOT_SQUASH,
	// for not allowing root access. The default is NO_ROOT_SQUASH.
	SquashMode pulumi.StringPtrInput `pulumi:"squashMode"`
}

func (InstanceFileSharesNfsExportOptionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceFileSharesNfsExportOption)(nil)).Elem()
}

func (i InstanceFileSharesNfsExportOptionArgs) ToInstanceFileSharesNfsExportOptionOutput() InstanceFileSharesNfsExportOptionOutput {
	return i.ToInstanceFileSharesNfsExportOptionOutputWithContext(context.Background())
}

func (i InstanceFileSharesNfsExportOptionArgs) ToInstanceFileSharesNfsExportOptionOutputWithContext(ctx context.Context) InstanceFileSharesNfsExportOptionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceFileSharesNfsExportOptionOutput)
}

// InstanceFileSharesNfsExportOptionArrayInput is an input type that accepts InstanceFileSharesNfsExportOptionArray and InstanceFileSharesNfsExportOptionArrayOutput values.
// You can construct a concrete instance of `InstanceFileSharesNfsExportOptionArrayInput` via:
//
//          InstanceFileSharesNfsExportOptionArray{ InstanceFileSharesNfsExportOptionArgs{...} }
type InstanceFileSharesNfsExportOptionArrayInput interface {
	pulumi.Input

	ToInstanceFileSharesNfsExportOptionArrayOutput() InstanceFileSharesNfsExportOptionArrayOutput
	ToInstanceFileSharesNfsExportOptionArrayOutputWithContext(context.Context) InstanceFileSharesNfsExportOptionArrayOutput
}

type InstanceFileSharesNfsExportOptionArray []InstanceFileSharesNfsExportOptionInput

func (InstanceFileSharesNfsExportOptionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InstanceFileSharesNfsExportOption)(nil)).Elem()
}

func (i InstanceFileSharesNfsExportOptionArray) ToInstanceFileSharesNfsExportOptionArrayOutput() InstanceFileSharesNfsExportOptionArrayOutput {
	return i.ToInstanceFileSharesNfsExportOptionArrayOutputWithContext(context.Background())
}

func (i InstanceFileSharesNfsExportOptionArray) ToInstanceFileSharesNfsExportOptionArrayOutputWithContext(ctx context.Context) InstanceFileSharesNfsExportOptionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceFileSharesNfsExportOptionArrayOutput)
}

type InstanceFileSharesNfsExportOptionOutput struct{ *pulumi.OutputState }

func (InstanceFileSharesNfsExportOptionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceFileSharesNfsExportOption)(nil)).Elem()
}

func (o InstanceFileSharesNfsExportOptionOutput) ToInstanceFileSharesNfsExportOptionOutput() InstanceFileSharesNfsExportOptionOutput {
	return o
}

func (o InstanceFileSharesNfsExportOptionOutput) ToInstanceFileSharesNfsExportOptionOutputWithContext(ctx context.Context) InstanceFileSharesNfsExportOptionOutput {
	return o
}

// Either READ_ONLY, for allowing only read requests on the exported directory,
// or READ_WRITE, for allowing both read and write requests. The default is READ_WRITE.
func (o InstanceFileSharesNfsExportOptionOutput) AccessMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstanceFileSharesNfsExportOption) *string { return v.AccessMode }).(pulumi.StringPtrOutput)
}

// An integer representing the anonymous group id with a default value of 65534.
// Anon_gid may only be set with squashMode of ROOT_SQUASH. An error will be returned
// if this field is specified for other squashMode settings.
func (o InstanceFileSharesNfsExportOptionOutput) AnonGid() pulumi.IntPtrOutput {
	return o.ApplyT(func(v InstanceFileSharesNfsExportOption) *int { return v.AnonGid }).(pulumi.IntPtrOutput)
}

// An integer representing the anonymous user id with a default value of 65534.
// Anon_uid may only be set with squashMode of ROOT_SQUASH. An error will be returned
// if this field is specified for other squashMode settings.
func (o InstanceFileSharesNfsExportOptionOutput) AnonUid() pulumi.IntPtrOutput {
	return o.ApplyT(func(v InstanceFileSharesNfsExportOption) *int { return v.AnonUid }).(pulumi.IntPtrOutput)
}

// List of either IPv4 addresses, or ranges in CIDR notation which may mount the file share.
// Overlapping IP ranges are not allowed, both within and across NfsExportOptions. An error will be returned.
// The limit is 64 IP ranges/addresses for each FileShareConfig among all NfsExportOptions.
func (o InstanceFileSharesNfsExportOptionOutput) IpRanges() pulumi.StringArrayOutput {
	return o.ApplyT(func(v InstanceFileSharesNfsExportOption) []string { return v.IpRanges }).(pulumi.StringArrayOutput)
}

// Either NO_ROOT_SQUASH, for allowing root access on the exported directory, or ROOT_SQUASH,
// for not allowing root access. The default is NO_ROOT_SQUASH.
func (o InstanceFileSharesNfsExportOptionOutput) SquashMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstanceFileSharesNfsExportOption) *string { return v.SquashMode }).(pulumi.StringPtrOutput)
}

type InstanceFileSharesNfsExportOptionArrayOutput struct{ *pulumi.OutputState }

func (InstanceFileSharesNfsExportOptionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InstanceFileSharesNfsExportOption)(nil)).Elem()
}

func (o InstanceFileSharesNfsExportOptionArrayOutput) ToInstanceFileSharesNfsExportOptionArrayOutput() InstanceFileSharesNfsExportOptionArrayOutput {
	return o
}

func (o InstanceFileSharesNfsExportOptionArrayOutput) ToInstanceFileSharesNfsExportOptionArrayOutputWithContext(ctx context.Context) InstanceFileSharesNfsExportOptionArrayOutput {
	return o
}

func (o InstanceFileSharesNfsExportOptionArrayOutput) Index(i pulumi.IntInput) InstanceFileSharesNfsExportOptionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) InstanceFileSharesNfsExportOption {
		return vs[0].([]InstanceFileSharesNfsExportOption)[vs[1].(int)]
	}).(InstanceFileSharesNfsExportOptionOutput)
}

type InstanceNetwork struct {
	// -
	// A list of IPv4 or IPv6 addresses.
	IpAddresses []string `pulumi:"ipAddresses"`
	// IP versions for which the instance has
	// IP addresses assigned.
	Modes []string `pulumi:"modes"`
	// The name of the GCE VPC network to which the
	// instance is connected.
	Network string `pulumi:"network"`
	// A /29 CIDR block that identifies the range of IP
	// addresses reserved for this instance.
	ReservedIpRange *string `pulumi:"reservedIpRange"`
}

// InstanceNetworkInput is an input type that accepts InstanceNetworkArgs and InstanceNetworkOutput values.
// You can construct a concrete instance of `InstanceNetworkInput` via:
//
//          InstanceNetworkArgs{...}
type InstanceNetworkInput interface {
	pulumi.Input

	ToInstanceNetworkOutput() InstanceNetworkOutput
	ToInstanceNetworkOutputWithContext(context.Context) InstanceNetworkOutput
}

type InstanceNetworkArgs struct {
	// -
	// A list of IPv4 or IPv6 addresses.
	IpAddresses pulumi.StringArrayInput `pulumi:"ipAddresses"`
	// IP versions for which the instance has
	// IP addresses assigned.
	Modes pulumi.StringArrayInput `pulumi:"modes"`
	// The name of the GCE VPC network to which the
	// instance is connected.
	Network pulumi.StringInput `pulumi:"network"`
	// A /29 CIDR block that identifies the range of IP
	// addresses reserved for this instance.
	ReservedIpRange pulumi.StringPtrInput `pulumi:"reservedIpRange"`
}

func (InstanceNetworkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceNetwork)(nil)).Elem()
}

func (i InstanceNetworkArgs) ToInstanceNetworkOutput() InstanceNetworkOutput {
	return i.ToInstanceNetworkOutputWithContext(context.Background())
}

func (i InstanceNetworkArgs) ToInstanceNetworkOutputWithContext(ctx context.Context) InstanceNetworkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceNetworkOutput)
}

// InstanceNetworkArrayInput is an input type that accepts InstanceNetworkArray and InstanceNetworkArrayOutput values.
// You can construct a concrete instance of `InstanceNetworkArrayInput` via:
//
//          InstanceNetworkArray{ InstanceNetworkArgs{...} }
type InstanceNetworkArrayInput interface {
	pulumi.Input

	ToInstanceNetworkArrayOutput() InstanceNetworkArrayOutput
	ToInstanceNetworkArrayOutputWithContext(context.Context) InstanceNetworkArrayOutput
}

type InstanceNetworkArray []InstanceNetworkInput

func (InstanceNetworkArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InstanceNetwork)(nil)).Elem()
}

func (i InstanceNetworkArray) ToInstanceNetworkArrayOutput() InstanceNetworkArrayOutput {
	return i.ToInstanceNetworkArrayOutputWithContext(context.Background())
}

func (i InstanceNetworkArray) ToInstanceNetworkArrayOutputWithContext(ctx context.Context) InstanceNetworkArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceNetworkArrayOutput)
}

type InstanceNetworkOutput struct{ *pulumi.OutputState }

func (InstanceNetworkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceNetwork)(nil)).Elem()
}

func (o InstanceNetworkOutput) ToInstanceNetworkOutput() InstanceNetworkOutput {
	return o
}

func (o InstanceNetworkOutput) ToInstanceNetworkOutputWithContext(ctx context.Context) InstanceNetworkOutput {
	return o
}

// -
// A list of IPv4 or IPv6 addresses.
func (o InstanceNetworkOutput) IpAddresses() pulumi.StringArrayOutput {
	return o.ApplyT(func(v InstanceNetwork) []string { return v.IpAddresses }).(pulumi.StringArrayOutput)
}

// IP versions for which the instance has
// IP addresses assigned.
func (o InstanceNetworkOutput) Modes() pulumi.StringArrayOutput {
	return o.ApplyT(func(v InstanceNetwork) []string { return v.Modes }).(pulumi.StringArrayOutput)
}

// The name of the GCE VPC network to which the
// instance is connected.
func (o InstanceNetworkOutput) Network() pulumi.StringOutput {
	return o.ApplyT(func(v InstanceNetwork) string { return v.Network }).(pulumi.StringOutput)
}

// A /29 CIDR block that identifies the range of IP
// addresses reserved for this instance.
func (o InstanceNetworkOutput) ReservedIpRange() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstanceNetwork) *string { return v.ReservedIpRange }).(pulumi.StringPtrOutput)
}

type InstanceNetworkArrayOutput struct{ *pulumi.OutputState }

func (InstanceNetworkArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InstanceNetwork)(nil)).Elem()
}

func (o InstanceNetworkArrayOutput) ToInstanceNetworkArrayOutput() InstanceNetworkArrayOutput {
	return o
}

func (o InstanceNetworkArrayOutput) ToInstanceNetworkArrayOutputWithContext(ctx context.Context) InstanceNetworkArrayOutput {
	return o
}

func (o InstanceNetworkArrayOutput) Index(i pulumi.IntInput) InstanceNetworkOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) InstanceNetwork {
		return vs[0].([]InstanceNetwork)[vs[1].(int)]
	}).(InstanceNetworkOutput)
}

func init() {
	pulumi.RegisterOutputType(InstanceFileSharesOutput{})
	pulumi.RegisterOutputType(InstanceFileSharesPtrOutput{})
	pulumi.RegisterOutputType(InstanceFileSharesNfsExportOptionOutput{})
	pulumi.RegisterOutputType(InstanceFileSharesNfsExportOptionArrayOutput{})
	pulumi.RegisterOutputType(InstanceNetworkOutput{})
	pulumi.RegisterOutputType(InstanceNetworkArrayOutput{})
}
