// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Get a Compute Region Instance Group within GCE.
// For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroups).
// 
// 
// The most common use of this datasource will be to fetch information about the instances inside regional managed instance groups, for instance:
func LookupRegionInstanceGroup(ctx *pulumi.Context, args *GetRegionInstanceGroupArgs) (*GetRegionInstanceGroupResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["project"] = args.Project
		inputs["region"] = args.Region
		inputs["selfLink"] = args.SelfLink
	}
	outputs, err := ctx.Invoke("gcp:compute/getRegionInstanceGroup:getRegionInstanceGroup", inputs)
	if err != nil {
		return nil, err
	}
	return &GetRegionInstanceGroupResult{
		Instances: outputs["instances"],
		Name: outputs["name"],
		Project: outputs["project"],
		Region: outputs["region"],
		SelfLink: outputs["selfLink"],
		Size: outputs["size"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getRegionInstanceGroup.
type GetRegionInstanceGroupArgs struct {
	// The name of the instance group.  One of `name` or `self_link` must be provided.
	Name interface{}
	// The ID of the project in which the resource belongs.
	// If `self_link` is provided, this value is ignored.  If neither `self_link`
	// nor `project` are provided, the provider project is used.
	Project interface{}
	// The region in which the resource belongs.  If `self_link`
	// is provided, this value is ignored.  If neither `self_link` nor `region` are
	// provided, the provider region is used.
	Region interface{}
	// The link to the instance group.  One of `name` or `self_link` must be provided.
	SelfLink interface{}
}

// A collection of values returned by getRegionInstanceGroup.
type GetRegionInstanceGroupResult struct {
	// List of instances in the group, as a list of resources, each containing:
	Instances interface{}
	// String port name
	Name interface{}
	Project interface{}
	Region interface{}
	SelfLink interface{}
	// The number of instances in the group.
	Size interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
