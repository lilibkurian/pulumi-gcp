// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func GetTestablePermissions(ctx *pulumi.Context, args *GetTestablePermissionsArgs, opts ...pulumi.InvokeOption) (*GetTestablePermissionsResult, error) {
	var rv GetTestablePermissionsResult
	err := ctx.Invoke("gcp:iam/getTestablePermissions:getTestablePermissions", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTestablePermissions.
type GetTestablePermissionsArgs struct {
	CustomSupportLevel *string  `pulumi:"customSupportLevel"`
	FullResourceName   string   `pulumi:"fullResourceName"`
	Stages             []string `pulumi:"stages"`
}

// A collection of values returned by getTestablePermissions.
type GetTestablePermissionsResult struct {
	CustomSupportLevel *string `pulumi:"customSupportLevel"`
	FullResourceName   string  `pulumi:"fullResourceName"`
	// The provider-assigned unique ID for this managed resource.
	Id          string                             `pulumi:"id"`
	Permissions []GetTestablePermissionsPermission `pulumi:"permissions"`
	Stages      []string                           `pulumi:"stages"`
}
