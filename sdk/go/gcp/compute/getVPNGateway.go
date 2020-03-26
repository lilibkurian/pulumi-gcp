// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Get a VPN gateway within GCE from its name.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_compute_vpn_gateway.html.markdown.
func LookupVPNGateway(ctx *pulumi.Context, args *LookupVPNGatewayArgs, opts ...pulumi.InvokeOption) (*LookupVPNGatewayResult, error) {
	var rv LookupVPNGatewayResult
	err := ctx.Invoke("gcp:compute/getVPNGateway:getVPNGateway", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVPNGateway.
type LookupVPNGatewayArgs struct {
	// The name of the VPN gateway.
	Name string `pulumi:"name"`
	// The project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The region in which the resource belongs. If it
	// is not provided, the project region is used.
	Region *string `pulumi:"region"`
}

// A collection of values returned by getVPNGateway.
type LookupVPNGatewayResult struct {
	// Description of this VPN gateway.
	Description string `pulumi:"description"`
	// id is the provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
	// The network of this VPN gateway.
	Network string `pulumi:"network"`
	Project string `pulumi:"project"`
	// Region of this VPN gateway.
	Region string `pulumi:"region"`
	// The URI of the resource.
	SelfLink string `pulumi:"selfLink"`
}
