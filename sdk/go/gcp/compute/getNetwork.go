// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Get a network within GCE from its name.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_compute_network.html.markdown.
func LookupNetwork(ctx *pulumi.Context, args *LookupNetworkArgs, opts ...pulumi.InvokeOption) (*LookupNetworkResult, error) {
	var rv LookupNetworkResult
	err := ctx.Invoke("gcp:compute/getNetwork:getNetwork", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNetwork.
type LookupNetworkArgs struct {
	// The name of the network.
	Name string `pulumi:"name"`
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project *string `pulumi:"project"`
}

// A collection of values returned by getNetwork.
type LookupNetworkResult struct {
	// Description of this network.
	Description string `pulumi:"description"`
	// The IP address of the gateway.
	GatewayIpv4 string `pulumi:"gatewayIpv4"`
	// id is the provider-assigned unique ID for this managed resource.
	Id      string  `pulumi:"id"`
	Name    string  `pulumi:"name"`
	Project *string `pulumi:"project"`
	// The URI of the resource.
	SelfLink string `pulumi:"selfLink"`
	// the list of subnetworks which belong to the network
	SubnetworksSelfLinks []string `pulumi:"subnetworksSelfLinks"`
}
