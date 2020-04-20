// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package accesscontextmanager

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// ServicePerimeter describes a set of GCP resources which can freely import
// and export data amongst themselves, but not export outside of the
// ServicePerimeter. If a request with a source within this ServicePerimeter
// has a target outside of the ServicePerimeter, the request will be blocked.
// Otherwise the request is allowed. There are two types of Service Perimeter
// - Regular and Bridge. Regular Service Perimeters cannot overlap, a single
// GCP project can only belong to a single regular Service Perimeter. Service
// Perimeter Bridges can contain only GCP projects as members, a single GCP
// project may belong to multiple Service Perimeter Bridges.
//
//
// To get more information about ServicePerimeter, see:
//
// * [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)
// * How-to Guides
//     * [Service Perimeter Quickstart](https://cloud.google.com/vpc-service-controls/docs/quickstart)
type ServicePerimeter struct {
	pulumi.CustomResourceState

	// Time the AccessPolicy was created in UTC.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Description of the ServicePerimeter and its use. Does not affect behavior.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Resource name for the ServicePerimeter. The short_name component must begin with a letter and only include alphanumeric
	// and '_'. Format: accessPolicies/{policy_id}/servicePerimeters/{short_name}
	Name pulumi.StringOutput `pulumi:"name"`
	// The AccessPolicy this ServicePerimeter lives in. Format: accessPolicies/{policy_id}
	Parent pulumi.StringOutput `pulumi:"parent"`
	// Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains
	// resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter. In
	// addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter
	// bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter
	// (whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by
	// the regular perimeter that resource is in. Perimeter Bridges are typically useful when building more complex topologies
	// with many independent perimeters that need to share some data with a common perimeter, but should not be able to share
	// data among themselves.
	PerimeterType pulumi.StringPtrOutput `pulumi:"perimeterType"`
	// Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter
	// configuration without enforcing actual access restrictions. Only allowed to be set when the 'useExplicitDryRunSpec' flag
	// is set.
	Spec ServicePerimeterSpecPtrOutput `pulumi:"spec"`
	// ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine
	// perimeter content and boundaries.
	Status ServicePerimeterStatusPtrOutput `pulumi:"status"`
	// Human readable title. Must be unique within the Policy.
	Title pulumi.StringOutput `pulumi:"title"`
	// Time the AccessPolicy was updated in UTC.
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
	// Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec
	// is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the
	// implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of
	// the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing
	// them. This testing is done through analyzing the differences between currently enforced and suggested restrictions.
	// useExplicitDryRunSpec must bet set to True if any of the fields in the spec are set to non-default values.
	UseExplicitDryRunSpec pulumi.BoolPtrOutput `pulumi:"useExplicitDryRunSpec"`
}

// NewServicePerimeter registers a new resource with the given unique name, arguments, and options.
func NewServicePerimeter(ctx *pulumi.Context,
	name string, args *ServicePerimeterArgs, opts ...pulumi.ResourceOption) (*ServicePerimeter, error) {
	if args == nil || args.Parent == nil {
		return nil, errors.New("missing required argument 'Parent'")
	}
	if args == nil || args.Title == nil {
		return nil, errors.New("missing required argument 'Title'")
	}
	if args == nil {
		args = &ServicePerimeterArgs{}
	}
	var resource ServicePerimeter
	err := ctx.RegisterResource("gcp:accesscontextmanager/servicePerimeter:ServicePerimeter", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServicePerimeter gets an existing ServicePerimeter resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServicePerimeter(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServicePerimeterState, opts ...pulumi.ResourceOption) (*ServicePerimeter, error) {
	var resource ServicePerimeter
	err := ctx.ReadResource("gcp:accesscontextmanager/servicePerimeter:ServicePerimeter", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServicePerimeter resources.
type servicePerimeterState struct {
	// Time the AccessPolicy was created in UTC.
	CreateTime *string `pulumi:"createTime"`
	// Description of the ServicePerimeter and its use. Does not affect behavior.
	Description *string `pulumi:"description"`
	// Resource name for the ServicePerimeter. The short_name component must begin with a letter and only include alphanumeric
	// and '_'. Format: accessPolicies/{policy_id}/servicePerimeters/{short_name}
	Name *string `pulumi:"name"`
	// The AccessPolicy this ServicePerimeter lives in. Format: accessPolicies/{policy_id}
	Parent *string `pulumi:"parent"`
	// Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains
	// resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter. In
	// addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter
	// bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter
	// (whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by
	// the regular perimeter that resource is in. Perimeter Bridges are typically useful when building more complex topologies
	// with many independent perimeters that need to share some data with a common perimeter, but should not be able to share
	// data among themselves.
	PerimeterType *string `pulumi:"perimeterType"`
	// Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter
	// configuration without enforcing actual access restrictions. Only allowed to be set when the 'useExplicitDryRunSpec' flag
	// is set.
	Spec *ServicePerimeterSpec `pulumi:"spec"`
	// ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine
	// perimeter content and boundaries.
	Status *ServicePerimeterStatus `pulumi:"status"`
	// Human readable title. Must be unique within the Policy.
	Title *string `pulumi:"title"`
	// Time the AccessPolicy was updated in UTC.
	UpdateTime *string `pulumi:"updateTime"`
	// Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec
	// is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the
	// implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of
	// the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing
	// them. This testing is done through analyzing the differences between currently enforced and suggested restrictions.
	// useExplicitDryRunSpec must bet set to True if any of the fields in the spec are set to non-default values.
	UseExplicitDryRunSpec *bool `pulumi:"useExplicitDryRunSpec"`
}

type ServicePerimeterState struct {
	// Time the AccessPolicy was created in UTC.
	CreateTime pulumi.StringPtrInput
	// Description of the ServicePerimeter and its use. Does not affect behavior.
	Description pulumi.StringPtrInput
	// Resource name for the ServicePerimeter. The short_name component must begin with a letter and only include alphanumeric
	// and '_'. Format: accessPolicies/{policy_id}/servicePerimeters/{short_name}
	Name pulumi.StringPtrInput
	// The AccessPolicy this ServicePerimeter lives in. Format: accessPolicies/{policy_id}
	Parent pulumi.StringPtrInput
	// Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains
	// resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter. In
	// addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter
	// bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter
	// (whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by
	// the regular perimeter that resource is in. Perimeter Bridges are typically useful when building more complex topologies
	// with many independent perimeters that need to share some data with a common perimeter, but should not be able to share
	// data among themselves.
	PerimeterType pulumi.StringPtrInput
	// Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter
	// configuration without enforcing actual access restrictions. Only allowed to be set when the 'useExplicitDryRunSpec' flag
	// is set.
	Spec ServicePerimeterSpecPtrInput
	// ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine
	// perimeter content and boundaries.
	Status ServicePerimeterStatusPtrInput
	// Human readable title. Must be unique within the Policy.
	Title pulumi.StringPtrInput
	// Time the AccessPolicy was updated in UTC.
	UpdateTime pulumi.StringPtrInput
	// Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec
	// is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the
	// implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of
	// the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing
	// them. This testing is done through analyzing the differences between currently enforced and suggested restrictions.
	// useExplicitDryRunSpec must bet set to True if any of the fields in the spec are set to non-default values.
	UseExplicitDryRunSpec pulumi.BoolPtrInput
}

func (ServicePerimeterState) ElementType() reflect.Type {
	return reflect.TypeOf((*servicePerimeterState)(nil)).Elem()
}

type servicePerimeterArgs struct {
	// Description of the ServicePerimeter and its use. Does not affect behavior.
	Description *string `pulumi:"description"`
	// Resource name for the ServicePerimeter. The short_name component must begin with a letter and only include alphanumeric
	// and '_'. Format: accessPolicies/{policy_id}/servicePerimeters/{short_name}
	Name *string `pulumi:"name"`
	// The AccessPolicy this ServicePerimeter lives in. Format: accessPolicies/{policy_id}
	Parent string `pulumi:"parent"`
	// Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains
	// resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter. In
	// addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter
	// bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter
	// (whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by
	// the regular perimeter that resource is in. Perimeter Bridges are typically useful when building more complex topologies
	// with many independent perimeters that need to share some data with a common perimeter, but should not be able to share
	// data among themselves.
	PerimeterType *string `pulumi:"perimeterType"`
	// Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter
	// configuration without enforcing actual access restrictions. Only allowed to be set when the 'useExplicitDryRunSpec' flag
	// is set.
	Spec *ServicePerimeterSpec `pulumi:"spec"`
	// ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine
	// perimeter content and boundaries.
	Status *ServicePerimeterStatus `pulumi:"status"`
	// Human readable title. Must be unique within the Policy.
	Title string `pulumi:"title"`
	// Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec
	// is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the
	// implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of
	// the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing
	// them. This testing is done through analyzing the differences between currently enforced and suggested restrictions.
	// useExplicitDryRunSpec must bet set to True if any of the fields in the spec are set to non-default values.
	UseExplicitDryRunSpec *bool `pulumi:"useExplicitDryRunSpec"`
}

// The set of arguments for constructing a ServicePerimeter resource.
type ServicePerimeterArgs struct {
	// Description of the ServicePerimeter and its use. Does not affect behavior.
	Description pulumi.StringPtrInput
	// Resource name for the ServicePerimeter. The short_name component must begin with a letter and only include alphanumeric
	// and '_'. Format: accessPolicies/{policy_id}/servicePerimeters/{short_name}
	Name pulumi.StringPtrInput
	// The AccessPolicy this ServicePerimeter lives in. Format: accessPolicies/{policy_id}
	Parent pulumi.StringInput
	// Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains
	// resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter. In
	// addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter
	// bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter
	// (whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by
	// the regular perimeter that resource is in. Perimeter Bridges are typically useful when building more complex topologies
	// with many independent perimeters that need to share some data with a common perimeter, but should not be able to share
	// data among themselves.
	PerimeterType pulumi.StringPtrInput
	// Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter
	// configuration without enforcing actual access restrictions. Only allowed to be set when the 'useExplicitDryRunSpec' flag
	// is set.
	Spec ServicePerimeterSpecPtrInput
	// ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine
	// perimeter content and boundaries.
	Status ServicePerimeterStatusPtrInput
	// Human readable title. Must be unique within the Policy.
	Title pulumi.StringInput
	// Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec
	// is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the
	// implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of
	// the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing
	// them. This testing is done through analyzing the differences between currently enforced and suggested restrictions.
	// useExplicitDryRunSpec must bet set to True if any of the fields in the spec are set to non-default values.
	UseExplicitDryRunSpec pulumi.BoolPtrInput
}

func (ServicePerimeterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*servicePerimeterArgs)(nil)).Elem()
}
