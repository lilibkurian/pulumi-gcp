// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package storage

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Creates a new bucket in Google cloud storage service (GCS).
// Once a bucket has been created, its location can't be changed.
// [ACLs](https://cloud.google.com/storage/docs/access-control/lists) can be applied
// using the [`storage.BucketACL`](https://www.terraform.io/docs/providers/google/r/storage_bucket_acl.html) resource.
//
// For more information see
// [the official documentation](https://cloud.google.com/storage/docs/overview)
// and
// [API](https://cloud.google.com/storage/docs/json_api/v1/buckets).
//
// **Note**: If the project id is not set on the resource or in the provider block it will be dynamically
// determined which will require enabling the compute api.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/storage_bucket.html.markdown.
type Bucket struct {
	pulumi.CustomResourceState

	// Enables [Bucket Policy Only](https://cloud.google.com/storage/docs/bucket-policy-only) access to a bucket.
	BucketPolicyOnly pulumi.BoolOutput `pulumi:"bucketPolicyOnly"`
	// The bucket's [Cross-Origin Resource Sharing (CORS)](https://www.w3.org/TR/cors/) configuration. Multiple blocks of this type are permitted. Structure is documented below.
	Cors                  BucketCorArrayOutput `pulumi:"cors"`
	DefaultEventBasedHold pulumi.BoolPtrOutput `pulumi:"defaultEventBasedHold"`
	// The bucket's encryption configuration.
	Encryption BucketEncryptionPtrOutput `pulumi:"encryption"`
	// When deleting a bucket, this
	// boolean option will delete all contained objects. If you try to delete a
	// bucket that contains objects, the provider will fail that run.
	ForceDestroy pulumi.BoolPtrOutput `pulumi:"forceDestroy"`
	// A set of key/value label pairs to assign to the bucket.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// The bucket's [Lifecycle Rules](https://cloud.google.com/storage/docs/lifecycle#configuration) configuration. Multiple blocks of this type are permitted. Structure is documented below.
	LifecycleRules BucketLifecycleRuleArrayOutput `pulumi:"lifecycleRules"`
	// The [GCS location](https://cloud.google.com/storage/docs/bucket-locations)
	Location pulumi.StringPtrOutput `pulumi:"location"`
	// The bucket's [Access & Storage Logs](https://cloud.google.com/storage/docs/access-logs) configuration.
	Logging BucketLoggingPtrOutput `pulumi:"logging"`
	// The name of the bucket.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// Enables [Requester Pays](https://cloud.google.com/storage/docs/requester-pays) on a storage bucket.
	RequesterPays pulumi.BoolPtrOutput `pulumi:"requesterPays"`
	// Configuration of the bucket's data retention policy for how long objects in the bucket should be retained. Structure is documented below.
	RetentionPolicy BucketRetentionPolicyPtrOutput `pulumi:"retentionPolicy"`
	// The URI of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// The target [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects affected by this Lifecycle Rule. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`.
	StorageClass pulumi.StringPtrOutput `pulumi:"storageClass"`
	// The base URL of the bucket, in the format `gs://<bucket-name>`.
	Url pulumi.StringOutput `pulumi:"url"`
	// The bucket's [Versioning](https://cloud.google.com/storage/docs/object-versioning) configuration.
	Versioning BucketVersioningPtrOutput `pulumi:"versioning"`
	// Configuration if the bucket acts as a website. Structure is documented below.
	Website BucketWebsitePtrOutput `pulumi:"website"`
}

// NewBucket registers a new resource with the given unique name, arguments, and options.
func NewBucket(ctx *pulumi.Context,
	name string, args *BucketArgs, opts ...pulumi.ResourceOption) (*Bucket, error) {
	if args == nil {
		args = &BucketArgs{}
	}
	var resource Bucket
	err := ctx.RegisterResource("gcp:storage/bucket:Bucket", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBucket gets an existing Bucket resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBucket(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BucketState, opts ...pulumi.ResourceOption) (*Bucket, error) {
	var resource Bucket
	err := ctx.ReadResource("gcp:storage/bucket:Bucket", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Bucket resources.
type bucketState struct {
	// Enables [Bucket Policy Only](https://cloud.google.com/storage/docs/bucket-policy-only) access to a bucket.
	BucketPolicyOnly *bool `pulumi:"bucketPolicyOnly"`
	// The bucket's [Cross-Origin Resource Sharing (CORS)](https://www.w3.org/TR/cors/) configuration. Multiple blocks of this type are permitted. Structure is documented below.
	Cors                  []BucketCor `pulumi:"cors"`
	DefaultEventBasedHold *bool       `pulumi:"defaultEventBasedHold"`
	// The bucket's encryption configuration.
	Encryption *BucketEncryption `pulumi:"encryption"`
	// When deleting a bucket, this
	// boolean option will delete all contained objects. If you try to delete a
	// bucket that contains objects, the provider will fail that run.
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// A set of key/value label pairs to assign to the bucket.
	Labels map[string]string `pulumi:"labels"`
	// The bucket's [Lifecycle Rules](https://cloud.google.com/storage/docs/lifecycle#configuration) configuration. Multiple blocks of this type are permitted. Structure is documented below.
	LifecycleRules []BucketLifecycleRule `pulumi:"lifecycleRules"`
	// The [GCS location](https://cloud.google.com/storage/docs/bucket-locations)
	Location *string `pulumi:"location"`
	// The bucket's [Access & Storage Logs](https://cloud.google.com/storage/docs/access-logs) configuration.
	Logging *BucketLogging `pulumi:"logging"`
	// The name of the bucket.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// Enables [Requester Pays](https://cloud.google.com/storage/docs/requester-pays) on a storage bucket.
	RequesterPays *bool `pulumi:"requesterPays"`
	// Configuration of the bucket's data retention policy for how long objects in the bucket should be retained. Structure is documented below.
	RetentionPolicy *BucketRetentionPolicy `pulumi:"retentionPolicy"`
	// The URI of the created resource.
	SelfLink *string `pulumi:"selfLink"`
	// The target [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects affected by this Lifecycle Rule. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`.
	StorageClass *string `pulumi:"storageClass"`
	// The base URL of the bucket, in the format `gs://<bucket-name>`.
	Url *string `pulumi:"url"`
	// The bucket's [Versioning](https://cloud.google.com/storage/docs/object-versioning) configuration.
	Versioning *BucketVersioning `pulumi:"versioning"`
	// Configuration if the bucket acts as a website. Structure is documented below.
	Website *BucketWebsite `pulumi:"website"`
}

type BucketState struct {
	// Enables [Bucket Policy Only](https://cloud.google.com/storage/docs/bucket-policy-only) access to a bucket.
	BucketPolicyOnly pulumi.BoolPtrInput
	// The bucket's [Cross-Origin Resource Sharing (CORS)](https://www.w3.org/TR/cors/) configuration. Multiple blocks of this type are permitted. Structure is documented below.
	Cors                  BucketCorArrayInput
	DefaultEventBasedHold pulumi.BoolPtrInput
	// The bucket's encryption configuration.
	Encryption BucketEncryptionPtrInput
	// When deleting a bucket, this
	// boolean option will delete all contained objects. If you try to delete a
	// bucket that contains objects, the provider will fail that run.
	ForceDestroy pulumi.BoolPtrInput
	// A set of key/value label pairs to assign to the bucket.
	Labels pulumi.StringMapInput
	// The bucket's [Lifecycle Rules](https://cloud.google.com/storage/docs/lifecycle#configuration) configuration. Multiple blocks of this type are permitted. Structure is documented below.
	LifecycleRules BucketLifecycleRuleArrayInput
	// The [GCS location](https://cloud.google.com/storage/docs/bucket-locations)
	Location pulumi.StringPtrInput
	// The bucket's [Access & Storage Logs](https://cloud.google.com/storage/docs/access-logs) configuration.
	Logging BucketLoggingPtrInput
	// The name of the bucket.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// Enables [Requester Pays](https://cloud.google.com/storage/docs/requester-pays) on a storage bucket.
	RequesterPays pulumi.BoolPtrInput
	// Configuration of the bucket's data retention policy for how long objects in the bucket should be retained. Structure is documented below.
	RetentionPolicy BucketRetentionPolicyPtrInput
	// The URI of the created resource.
	SelfLink pulumi.StringPtrInput
	// The target [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects affected by this Lifecycle Rule. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`.
	StorageClass pulumi.StringPtrInput
	// The base URL of the bucket, in the format `gs://<bucket-name>`.
	Url pulumi.StringPtrInput
	// The bucket's [Versioning](https://cloud.google.com/storage/docs/object-versioning) configuration.
	Versioning BucketVersioningPtrInput
	// Configuration if the bucket acts as a website. Structure is documented below.
	Website BucketWebsitePtrInput
}

func (BucketState) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketState)(nil)).Elem()
}

type bucketArgs struct {
	// Enables [Bucket Policy Only](https://cloud.google.com/storage/docs/bucket-policy-only) access to a bucket.
	BucketPolicyOnly *bool `pulumi:"bucketPolicyOnly"`
	// The bucket's [Cross-Origin Resource Sharing (CORS)](https://www.w3.org/TR/cors/) configuration. Multiple blocks of this type are permitted. Structure is documented below.
	Cors                  []BucketCor `pulumi:"cors"`
	DefaultEventBasedHold *bool       `pulumi:"defaultEventBasedHold"`
	// The bucket's encryption configuration.
	Encryption *BucketEncryption `pulumi:"encryption"`
	// When deleting a bucket, this
	// boolean option will delete all contained objects. If you try to delete a
	// bucket that contains objects, the provider will fail that run.
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// A set of key/value label pairs to assign to the bucket.
	Labels map[string]string `pulumi:"labels"`
	// The bucket's [Lifecycle Rules](https://cloud.google.com/storage/docs/lifecycle#configuration) configuration. Multiple blocks of this type are permitted. Structure is documented below.
	LifecycleRules []BucketLifecycleRule `pulumi:"lifecycleRules"`
	// The [GCS location](https://cloud.google.com/storage/docs/bucket-locations)
	Location *string `pulumi:"location"`
	// The bucket's [Access & Storage Logs](https://cloud.google.com/storage/docs/access-logs) configuration.
	Logging *BucketLogging `pulumi:"logging"`
	// The name of the bucket.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// Enables [Requester Pays](https://cloud.google.com/storage/docs/requester-pays) on a storage bucket.
	RequesterPays *bool `pulumi:"requesterPays"`
	// Configuration of the bucket's data retention policy for how long objects in the bucket should be retained. Structure is documented below.
	RetentionPolicy *BucketRetentionPolicy `pulumi:"retentionPolicy"`
	// The target [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects affected by this Lifecycle Rule. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`.
	StorageClass *string `pulumi:"storageClass"`
	// The bucket's [Versioning](https://cloud.google.com/storage/docs/object-versioning) configuration.
	Versioning *BucketVersioning `pulumi:"versioning"`
	// Configuration if the bucket acts as a website. Structure is documented below.
	Website *BucketWebsite `pulumi:"website"`
}

// The set of arguments for constructing a Bucket resource.
type BucketArgs struct {
	// Enables [Bucket Policy Only](https://cloud.google.com/storage/docs/bucket-policy-only) access to a bucket.
	BucketPolicyOnly pulumi.BoolPtrInput
	// The bucket's [Cross-Origin Resource Sharing (CORS)](https://www.w3.org/TR/cors/) configuration. Multiple blocks of this type are permitted. Structure is documented below.
	Cors                  BucketCorArrayInput
	DefaultEventBasedHold pulumi.BoolPtrInput
	// The bucket's encryption configuration.
	Encryption BucketEncryptionPtrInput
	// When deleting a bucket, this
	// boolean option will delete all contained objects. If you try to delete a
	// bucket that contains objects, the provider will fail that run.
	ForceDestroy pulumi.BoolPtrInput
	// A set of key/value label pairs to assign to the bucket.
	Labels pulumi.StringMapInput
	// The bucket's [Lifecycle Rules](https://cloud.google.com/storage/docs/lifecycle#configuration) configuration. Multiple blocks of this type are permitted. Structure is documented below.
	LifecycleRules BucketLifecycleRuleArrayInput
	// The [GCS location](https://cloud.google.com/storage/docs/bucket-locations)
	Location pulumi.StringPtrInput
	// The bucket's [Access & Storage Logs](https://cloud.google.com/storage/docs/access-logs) configuration.
	Logging BucketLoggingPtrInput
	// The name of the bucket.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// Enables [Requester Pays](https://cloud.google.com/storage/docs/requester-pays) on a storage bucket.
	RequesterPays pulumi.BoolPtrInput
	// Configuration of the bucket's data retention policy for how long objects in the bucket should be retained. Structure is documented below.
	RetentionPolicy BucketRetentionPolicyPtrInput
	// The target [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects affected by this Lifecycle Rule. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`.
	StorageClass pulumi.StringPtrInput
	// The bucket's [Versioning](https://cloud.google.com/storage/docs/object-versioning) configuration.
	Versioning BucketVersioningPtrInput
	// Configuration if the bucket acts as a website. Structure is documented below.
	Website BucketWebsitePtrInput
}

func (BucketArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketArgs)(nil)).Elem()
}
