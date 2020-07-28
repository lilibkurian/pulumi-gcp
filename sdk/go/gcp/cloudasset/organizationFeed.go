// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudasset

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Describes a Cloud Asset Inventory feed used to to listen to asset updates.
//
// To get more information about OrganizationFeed, see:
//
// * [API documentation](https://cloud.google.com/asset-inventory/docs/reference/rest/)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/asset-inventory/docs)
//
// ## Example Usage
type OrganizationFeed struct {
	pulumi.CustomResourceState

	// A list of the full names of the assets to receive updates. You must specify either or both of
	// assetNames and assetTypes. Only asset updates matching specified assetNames and assetTypes are
	// exported to the feed. For example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1.
	// See https://cloud.google.com/apis/design/resourceNames#fullResourceName for more info.
	AssetNames pulumi.StringArrayOutput `pulumi:"assetNames"`
	// A list of types of the assets to receive updates. You must specify either or both of assetNames
	// and assetTypes. Only asset updates matching specified assetNames and assetTypes are exported to
	// the feed. For example: "compute.googleapis.com/Disk"
	// See https://cloud.google.com/asset-inventory/docs/supported-asset-types for a list of all
	// supported asset types.
	AssetTypes pulumi.StringArrayOutput `pulumi:"assetTypes"`
	// The project whose identity will be used when sending messages to the
	// destination pubsub topic. It also specifies the project for API
	// enablement check, quota, and billing.
	BillingProject pulumi.StringOutput `pulumi:"billingProject"`
	// Asset content type. If not specified, no content but the asset name and type will be returned.
	ContentType pulumi.StringPtrOutput `pulumi:"contentType"`
	// This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
	FeedId pulumi.StringOutput `pulumi:"feedId"`
	// Output configuration for asset feed destination.  Structure is documented below.
	FeedOutputConfig OrganizationFeedFeedOutputConfigOutput `pulumi:"feedOutputConfig"`
	// The format will be organizations/{organization_number}/feeds/{client-assigned_feed_identifier}.
	Name pulumi.StringOutput `pulumi:"name"`
	// The organization this feed should be created in.
	OrgId pulumi.StringOutput `pulumi:"orgId"`
}

// NewOrganizationFeed registers a new resource with the given unique name, arguments, and options.
func NewOrganizationFeed(ctx *pulumi.Context,
	name string, args *OrganizationFeedArgs, opts ...pulumi.ResourceOption) (*OrganizationFeed, error) {
	if args == nil || args.BillingProject == nil {
		return nil, errors.New("missing required argument 'BillingProject'")
	}
	if args == nil || args.FeedId == nil {
		return nil, errors.New("missing required argument 'FeedId'")
	}
	if args == nil || args.FeedOutputConfig == nil {
		return nil, errors.New("missing required argument 'FeedOutputConfig'")
	}
	if args == nil || args.OrgId == nil {
		return nil, errors.New("missing required argument 'OrgId'")
	}
	if args == nil {
		args = &OrganizationFeedArgs{}
	}
	var resource OrganizationFeed
	err := ctx.RegisterResource("gcp:cloudasset/organizationFeed:OrganizationFeed", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrganizationFeed gets an existing OrganizationFeed resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrganizationFeed(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrganizationFeedState, opts ...pulumi.ResourceOption) (*OrganizationFeed, error) {
	var resource OrganizationFeed
	err := ctx.ReadResource("gcp:cloudasset/organizationFeed:OrganizationFeed", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OrganizationFeed resources.
type organizationFeedState struct {
	// A list of the full names of the assets to receive updates. You must specify either or both of
	// assetNames and assetTypes. Only asset updates matching specified assetNames and assetTypes are
	// exported to the feed. For example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1.
	// See https://cloud.google.com/apis/design/resourceNames#fullResourceName for more info.
	AssetNames []string `pulumi:"assetNames"`
	// A list of types of the assets to receive updates. You must specify either or both of assetNames
	// and assetTypes. Only asset updates matching specified assetNames and assetTypes are exported to
	// the feed. For example: "compute.googleapis.com/Disk"
	// See https://cloud.google.com/asset-inventory/docs/supported-asset-types for a list of all
	// supported asset types.
	AssetTypes []string `pulumi:"assetTypes"`
	// The project whose identity will be used when sending messages to the
	// destination pubsub topic. It also specifies the project for API
	// enablement check, quota, and billing.
	BillingProject *string `pulumi:"billingProject"`
	// Asset content type. If not specified, no content but the asset name and type will be returned.
	ContentType *string `pulumi:"contentType"`
	// This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
	FeedId *string `pulumi:"feedId"`
	// Output configuration for asset feed destination.  Structure is documented below.
	FeedOutputConfig *OrganizationFeedFeedOutputConfig `pulumi:"feedOutputConfig"`
	// The format will be organizations/{organization_number}/feeds/{client-assigned_feed_identifier}.
	Name *string `pulumi:"name"`
	// The organization this feed should be created in.
	OrgId *string `pulumi:"orgId"`
}

type OrganizationFeedState struct {
	// A list of the full names of the assets to receive updates. You must specify either or both of
	// assetNames and assetTypes. Only asset updates matching specified assetNames and assetTypes are
	// exported to the feed. For example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1.
	// See https://cloud.google.com/apis/design/resourceNames#fullResourceName for more info.
	AssetNames pulumi.StringArrayInput
	// A list of types of the assets to receive updates. You must specify either or both of assetNames
	// and assetTypes. Only asset updates matching specified assetNames and assetTypes are exported to
	// the feed. For example: "compute.googleapis.com/Disk"
	// See https://cloud.google.com/asset-inventory/docs/supported-asset-types for a list of all
	// supported asset types.
	AssetTypes pulumi.StringArrayInput
	// The project whose identity will be used when sending messages to the
	// destination pubsub topic. It also specifies the project for API
	// enablement check, quota, and billing.
	BillingProject pulumi.StringPtrInput
	// Asset content type. If not specified, no content but the asset name and type will be returned.
	ContentType pulumi.StringPtrInput
	// This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
	FeedId pulumi.StringPtrInput
	// Output configuration for asset feed destination.  Structure is documented below.
	FeedOutputConfig OrganizationFeedFeedOutputConfigPtrInput
	// The format will be organizations/{organization_number}/feeds/{client-assigned_feed_identifier}.
	Name pulumi.StringPtrInput
	// The organization this feed should be created in.
	OrgId pulumi.StringPtrInput
}

func (OrganizationFeedState) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationFeedState)(nil)).Elem()
}

type organizationFeedArgs struct {
	// A list of the full names of the assets to receive updates. You must specify either or both of
	// assetNames and assetTypes. Only asset updates matching specified assetNames and assetTypes are
	// exported to the feed. For example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1.
	// See https://cloud.google.com/apis/design/resourceNames#fullResourceName for more info.
	AssetNames []string `pulumi:"assetNames"`
	// A list of types of the assets to receive updates. You must specify either or both of assetNames
	// and assetTypes. Only asset updates matching specified assetNames and assetTypes are exported to
	// the feed. For example: "compute.googleapis.com/Disk"
	// See https://cloud.google.com/asset-inventory/docs/supported-asset-types for a list of all
	// supported asset types.
	AssetTypes []string `pulumi:"assetTypes"`
	// The project whose identity will be used when sending messages to the
	// destination pubsub topic. It also specifies the project for API
	// enablement check, quota, and billing.
	BillingProject string `pulumi:"billingProject"`
	// Asset content type. If not specified, no content but the asset name and type will be returned.
	ContentType *string `pulumi:"contentType"`
	// This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
	FeedId string `pulumi:"feedId"`
	// Output configuration for asset feed destination.  Structure is documented below.
	FeedOutputConfig OrganizationFeedFeedOutputConfig `pulumi:"feedOutputConfig"`
	// The organization this feed should be created in.
	OrgId string `pulumi:"orgId"`
}

// The set of arguments for constructing a OrganizationFeed resource.
type OrganizationFeedArgs struct {
	// A list of the full names of the assets to receive updates. You must specify either or both of
	// assetNames and assetTypes. Only asset updates matching specified assetNames and assetTypes are
	// exported to the feed. For example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1.
	// See https://cloud.google.com/apis/design/resourceNames#fullResourceName for more info.
	AssetNames pulumi.StringArrayInput
	// A list of types of the assets to receive updates. You must specify either or both of assetNames
	// and assetTypes. Only asset updates matching specified assetNames and assetTypes are exported to
	// the feed. For example: "compute.googleapis.com/Disk"
	// See https://cloud.google.com/asset-inventory/docs/supported-asset-types for a list of all
	// supported asset types.
	AssetTypes pulumi.StringArrayInput
	// The project whose identity will be used when sending messages to the
	// destination pubsub topic. It also specifies the project for API
	// enablement check, quota, and billing.
	BillingProject pulumi.StringInput
	// Asset content type. If not specified, no content but the asset name and type will be returned.
	ContentType pulumi.StringPtrInput
	// This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
	FeedId pulumi.StringInput
	// Output configuration for asset feed destination.  Structure is documented below.
	FeedOutputConfig OrganizationFeedFeedOutputConfigInput
	// The organization this feed should be created in.
	OrgId pulumi.StringInput
}

func (OrganizationFeedArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationFeedArgs)(nil)).Elem()
}
