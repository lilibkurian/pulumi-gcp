// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package logging

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Logs-based metric can also be used to extract values from logs and create a a distribution
// of the values. The distribution records the statistics of the extracted values along with
// an optional histogram of the values as specified by the bucket options.
//
//
// To get more information about Metric, see:
//
// * [API documentation](https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/create)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/logging/docs/apis)
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_metric.html.markdown.
type Metric struct {
	pulumi.CustomResourceState

	// The bucketOptions are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket
	// boundaries used to create a histogram of the extracted values.
	BucketOptions MetricBucketOptionsPtrOutput `pulumi:"bucketOptions"`
	// A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-filters) which is used to match log
	// entries.
	Filter pulumi.StringOutput `pulumi:"filter"`
	// A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign
	// as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this
	// map. The syntax of the extractor expression is the same as for the valueExtractor field.
	LabelExtractors pulumi.StringMapOutput `pulumi:"labelExtractors"`
	// The metric descriptor associated with the logs-based metric.
	MetricDescriptor MetricMetricDescriptorOutput `pulumi:"metricDescriptor"`
	// The client-assigned metric identifier. Examples - "error_count", "nginx/requests". Metric identifiers are limited to 100
	// characters and can include only the following characters A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The
	// forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// A valueExtractor is required when using a distribution logs-based metric to extract the values to record from a log
	// entry. Two functions are supported for value extraction - EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument
	// are 1. field - The name of the log entry field from which the value is to be extracted. 2. regex - A regular expression
	// using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from
	// the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error
	// to specify a regex that does not include exactly one capture group.
	ValueExtractor pulumi.StringPtrOutput `pulumi:"valueExtractor"`
}

// NewMetric registers a new resource with the given unique name, arguments, and options.
func NewMetric(ctx *pulumi.Context,
	name string, args *MetricArgs, opts ...pulumi.ResourceOption) (*Metric, error) {
	if args == nil || args.Filter == nil {
		return nil, errors.New("missing required argument 'Filter'")
	}
	if args == nil || args.MetricDescriptor == nil {
		return nil, errors.New("missing required argument 'MetricDescriptor'")
	}
	if args == nil {
		args = &MetricArgs{}
	}
	var resource Metric
	err := ctx.RegisterResource("gcp:logging/metric:Metric", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMetric gets an existing Metric resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMetric(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MetricState, opts ...pulumi.ResourceOption) (*Metric, error) {
	var resource Metric
	err := ctx.ReadResource("gcp:logging/metric:Metric", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Metric resources.
type metricState struct {
	// The bucketOptions are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket
	// boundaries used to create a histogram of the extracted values.
	BucketOptions *MetricBucketOptions `pulumi:"bucketOptions"`
	// A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.
	Description *string `pulumi:"description"`
	// An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-filters) which is used to match log
	// entries.
	Filter *string `pulumi:"filter"`
	// A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign
	// as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this
	// map. The syntax of the extractor expression is the same as for the valueExtractor field.
	LabelExtractors map[string]string `pulumi:"labelExtractors"`
	// The metric descriptor associated with the logs-based metric.
	MetricDescriptor *MetricMetricDescriptor `pulumi:"metricDescriptor"`
	// The client-assigned metric identifier. Examples - "error_count", "nginx/requests". Metric identifiers are limited to 100
	// characters and can include only the following characters A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The
	// forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// A valueExtractor is required when using a distribution logs-based metric to extract the values to record from a log
	// entry. Two functions are supported for value extraction - EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument
	// are 1. field - The name of the log entry field from which the value is to be extracted. 2. regex - A regular expression
	// using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from
	// the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error
	// to specify a regex that does not include exactly one capture group.
	ValueExtractor *string `pulumi:"valueExtractor"`
}

type MetricState struct {
	// The bucketOptions are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket
	// boundaries used to create a histogram of the extracted values.
	BucketOptions MetricBucketOptionsPtrInput
	// A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.
	Description pulumi.StringPtrInput
	// An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-filters) which is used to match log
	// entries.
	Filter pulumi.StringPtrInput
	// A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign
	// as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this
	// map. The syntax of the extractor expression is the same as for the valueExtractor field.
	LabelExtractors pulumi.StringMapInput
	// The metric descriptor associated with the logs-based metric.
	MetricDescriptor MetricMetricDescriptorPtrInput
	// The client-assigned metric identifier. Examples - "error_count", "nginx/requests". Metric identifiers are limited to 100
	// characters and can include only the following characters A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The
	// forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// A valueExtractor is required when using a distribution logs-based metric to extract the values to record from a log
	// entry. Two functions are supported for value extraction - EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument
	// are 1. field - The name of the log entry field from which the value is to be extracted. 2. regex - A regular expression
	// using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from
	// the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error
	// to specify a regex that does not include exactly one capture group.
	ValueExtractor pulumi.StringPtrInput
}

func (MetricState) ElementType() reflect.Type {
	return reflect.TypeOf((*metricState)(nil)).Elem()
}

type metricArgs struct {
	// The bucketOptions are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket
	// boundaries used to create a histogram of the extracted values.
	BucketOptions *MetricBucketOptions `pulumi:"bucketOptions"`
	// A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.
	Description *string `pulumi:"description"`
	// An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-filters) which is used to match log
	// entries.
	Filter string `pulumi:"filter"`
	// A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign
	// as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this
	// map. The syntax of the extractor expression is the same as for the valueExtractor field.
	LabelExtractors map[string]string `pulumi:"labelExtractors"`
	// The metric descriptor associated with the logs-based metric.
	MetricDescriptor MetricMetricDescriptor `pulumi:"metricDescriptor"`
	// The client-assigned metric identifier. Examples - "error_count", "nginx/requests". Metric identifiers are limited to 100
	// characters and can include only the following characters A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The
	// forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// A valueExtractor is required when using a distribution logs-based metric to extract the values to record from a log
	// entry. Two functions are supported for value extraction - EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument
	// are 1. field - The name of the log entry field from which the value is to be extracted. 2. regex - A regular expression
	// using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from
	// the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error
	// to specify a regex that does not include exactly one capture group.
	ValueExtractor *string `pulumi:"valueExtractor"`
}

// The set of arguments for constructing a Metric resource.
type MetricArgs struct {
	// The bucketOptions are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket
	// boundaries used to create a histogram of the extracted values.
	BucketOptions MetricBucketOptionsPtrInput
	// A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.
	Description pulumi.StringPtrInput
	// An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-filters) which is used to match log
	// entries.
	Filter pulumi.StringInput
	// A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign
	// as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this
	// map. The syntax of the extractor expression is the same as for the valueExtractor field.
	LabelExtractors pulumi.StringMapInput
	// The metric descriptor associated with the logs-based metric.
	MetricDescriptor MetricMetricDescriptorInput
	// The client-assigned metric identifier. Examples - "error_count", "nginx/requests". Metric identifiers are limited to 100
	// characters and can include only the following characters A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The
	// forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// A valueExtractor is required when using a distribution logs-based metric to extract the values to record from a log
	// entry. Two functions are supported for value extraction - EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument
	// are 1. field - The name of the log entry field from which the value is to be extracted. 2. regex - A regular expression
	// using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from
	// the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error
	// to specify a regex that does not include exactly one capture group.
	ValueExtractor pulumi.StringPtrInput
}

func (MetricArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*metricArgs)(nil)).Elem()
}
