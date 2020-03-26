// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// UrlMaps are used to route requests to a backend service based on rules
// that you define for the host and path of an incoming URL.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_url_map.html.markdown.
type RegionUrlMap struct {
	pulumi.CustomResourceState

	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringOutput `pulumi:"creationTimestamp"`
	// A reference to RegionBackendService resource if none of the hostRules match.
	DefaultService pulumi.StringOutput `pulumi:"defaultService"`
	// An optional description of this resource. Provide this property when you create the resource.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Fingerprint of this resource. This field is used internally during updates of this resource.
	Fingerprint pulumi.StringOutput `pulumi:"fingerprint"`
	// The list of HostRules to use against the URL.
	HostRules RegionUrlMapHostRuleArrayOutput `pulumi:"hostRules"`
	// The unique identifier for the resource.
	MapId pulumi.IntOutput `pulumi:"mapId"`
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name pulumi.StringOutput `pulumi:"name"`
	// The list of named PathMatchers to use against the URL.
	PathMatchers RegionUrlMapPathMatcherArrayOutput `pulumi:"pathMatchers"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The Region in which the url map should reside. If it is not provided, the provider region is used.
	Region pulumi.StringOutput `pulumi:"region"`
	// The URI of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// The list of expected URL mappings. Requests to update this UrlMap will succeed only if all of the test cases pass.
	Tests RegionUrlMapTestArrayOutput `pulumi:"tests"`
}

// NewRegionUrlMap registers a new resource with the given unique name, arguments, and options.
func NewRegionUrlMap(ctx *pulumi.Context,
	name string, args *RegionUrlMapArgs, opts ...pulumi.ResourceOption) (*RegionUrlMap, error) {
	if args == nil || args.DefaultService == nil {
		return nil, errors.New("missing required argument 'DefaultService'")
	}
	if args == nil {
		args = &RegionUrlMapArgs{}
	}
	var resource RegionUrlMap
	err := ctx.RegisterResource("gcp:compute/regionUrlMap:RegionUrlMap", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRegionUrlMap gets an existing RegionUrlMap resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRegionUrlMap(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RegionUrlMapState, opts ...pulumi.ResourceOption) (*RegionUrlMap, error) {
	var resource RegionUrlMap
	err := ctx.ReadResource("gcp:compute/regionUrlMap:RegionUrlMap", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RegionUrlMap resources.
type regionUrlMapState struct {
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp *string `pulumi:"creationTimestamp"`
	// A reference to RegionBackendService resource if none of the hostRules match.
	DefaultService *string `pulumi:"defaultService"`
	// An optional description of this resource. Provide this property when you create the resource.
	Description *string `pulumi:"description"`
	// Fingerprint of this resource. This field is used internally during updates of this resource.
	Fingerprint *string `pulumi:"fingerprint"`
	// The list of HostRules to use against the URL.
	HostRules []RegionUrlMapHostRule `pulumi:"hostRules"`
	// The unique identifier for the resource.
	MapId *int `pulumi:"mapId"`
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name *string `pulumi:"name"`
	// The list of named PathMatchers to use against the URL.
	PathMatchers []RegionUrlMapPathMatcher `pulumi:"pathMatchers"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The Region in which the url map should reside. If it is not provided, the provider region is used.
	Region *string `pulumi:"region"`
	// The URI of the created resource.
	SelfLink *string `pulumi:"selfLink"`
	// The list of expected URL mappings. Requests to update this UrlMap will succeed only if all of the test cases pass.
	Tests []RegionUrlMapTest `pulumi:"tests"`
}

type RegionUrlMapState struct {
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringPtrInput
	// A reference to RegionBackendService resource if none of the hostRules match.
	DefaultService pulumi.StringPtrInput
	// An optional description of this resource. Provide this property when you create the resource.
	Description pulumi.StringPtrInput
	// Fingerprint of this resource. This field is used internally during updates of this resource.
	Fingerprint pulumi.StringPtrInput
	// The list of HostRules to use against the URL.
	HostRules RegionUrlMapHostRuleArrayInput
	// The unique identifier for the resource.
	MapId pulumi.IntPtrInput
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name pulumi.StringPtrInput
	// The list of named PathMatchers to use against the URL.
	PathMatchers RegionUrlMapPathMatcherArrayInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The Region in which the url map should reside. If it is not provided, the provider region is used.
	Region pulumi.StringPtrInput
	// The URI of the created resource.
	SelfLink pulumi.StringPtrInput
	// The list of expected URL mappings. Requests to update this UrlMap will succeed only if all of the test cases pass.
	Tests RegionUrlMapTestArrayInput
}

func (RegionUrlMapState) ElementType() reflect.Type {
	return reflect.TypeOf((*regionUrlMapState)(nil)).Elem()
}

type regionUrlMapArgs struct {
	// A reference to RegionBackendService resource if none of the hostRules match.
	DefaultService string `pulumi:"defaultService"`
	// An optional description of this resource. Provide this property when you create the resource.
	Description *string `pulumi:"description"`
	// The list of HostRules to use against the URL.
	HostRules []RegionUrlMapHostRule `pulumi:"hostRules"`
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name *string `pulumi:"name"`
	// The list of named PathMatchers to use against the URL.
	PathMatchers []RegionUrlMapPathMatcher `pulumi:"pathMatchers"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The Region in which the url map should reside. If it is not provided, the provider region is used.
	Region *string `pulumi:"region"`
	// The list of expected URL mappings. Requests to update this UrlMap will succeed only if all of the test cases pass.
	Tests []RegionUrlMapTest `pulumi:"tests"`
}

// The set of arguments for constructing a RegionUrlMap resource.
type RegionUrlMapArgs struct {
	// A reference to RegionBackendService resource if none of the hostRules match.
	DefaultService pulumi.StringInput
	// An optional description of this resource. Provide this property when you create the resource.
	Description pulumi.StringPtrInput
	// The list of HostRules to use against the URL.
	HostRules RegionUrlMapHostRuleArrayInput
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name pulumi.StringPtrInput
	// The list of named PathMatchers to use against the URL.
	PathMatchers RegionUrlMapPathMatcherArrayInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The Region in which the url map should reside. If it is not provided, the provider region is used.
	Region pulumi.StringPtrInput
	// The list of expected URL mappings. Requests to update this UrlMap will succeed only if all of the test cases pass.
	Tests RegionUrlMapTestArrayInput
}

func (RegionUrlMapArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*regionUrlMapArgs)(nil)).Elem()
}
