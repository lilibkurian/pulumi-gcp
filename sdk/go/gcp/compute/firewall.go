// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Each network has its own firewall controlling access to and from the
// instances.
//
// All traffic to instances, even from other instances, is blocked by the
// firewall unless firewall rules are created to allow it.
//
// The default network has automatically created firewall rules that are
// shown in default firewall rules. No manually created network has
// automatically created firewall rules except for a default "allow" rule for
// outgoing traffic and a default "deny" for incoming traffic. For all
// networks except the default network, you must create any firewall rules
// you need.
//
//
// To get more information about Firewall, see:
//
// * [API documentation](https://cloud.google.com/compute/docs/reference/v1/firewalls)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/vpc/docs/firewalls)
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_firewall.html.markdown.
type Firewall struct {
	pulumi.CustomResourceState

	// The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
	// permitted connection.
	Allows FirewallAllowArrayOutput `pulumi:"allows"`
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringOutput `pulumi:"creationTimestamp"`
	// The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
	// denied connection.
	Denies FirewallDenyArrayOutput `pulumi:"denies"`
	// An optional description of this resource. Provide this property when you create the resource.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
	// ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
	DestinationRanges pulumi.StringArrayOutput `pulumi:"destinationRanges"`
	// Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
	// to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
	Direction pulumi.StringOutput `pulumi:"direction"`
	// Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
	// the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
	// rule will be enabled.
	Disabled pulumi.BoolPtrOutput `pulumi:"disabled"`
	// This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
	// exported to Stackdriver.
	EnableLogging pulumi.BoolPtrOutput `pulumi:"enableLogging"`
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name pulumi.StringOutput `pulumi:"name"`
	// The name or self_link of the network to attach this firewall to.
	Network pulumi.StringOutput `pulumi:"network"`
	// Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
	// 1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
	// (eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
	// rules having equal priority.
	Priority pulumi.IntPtrOutput `pulumi:"priority"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The URI of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
	// These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
	// are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
	// to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
	// apply. Only IPv4 is supported.
	SourceRanges pulumi.StringArrayOutput `pulumi:"sourceRanges"`
	// If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
	// service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
	// address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
	// time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
	// sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
	// does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
	// as sourceTags or targetTags.
	SourceServiceAccounts pulumi.StringArrayOutput `pulumi:"sourceServiceAccounts"`
	// If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
	// source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
	// associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
	// properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
	// that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
	// firewall to apply.
	SourceTags pulumi.StringArrayOutput `pulumi:"sourceTags"`
	// A list of service accounts indicating sets of instances located in the network that may make network connections as
	// specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
	// targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
	TargetServiceAccounts pulumi.StringArrayOutput `pulumi:"targetServiceAccounts"`
	// A list of instance tags indicating sets of instances located in the network that may make network connections as
	// specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
	// network.
	TargetTags pulumi.StringArrayOutput `pulumi:"targetTags"`
}

// NewFirewall registers a new resource with the given unique name, arguments, and options.
func NewFirewall(ctx *pulumi.Context,
	name string, args *FirewallArgs, opts ...pulumi.ResourceOption) (*Firewall, error) {
	if args == nil || args.Network == nil {
		return nil, errors.New("missing required argument 'Network'")
	}
	if args == nil {
		args = &FirewallArgs{}
	}
	var resource Firewall
	err := ctx.RegisterResource("gcp:compute/firewall:Firewall", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFirewall gets an existing Firewall resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFirewall(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FirewallState, opts ...pulumi.ResourceOption) (*Firewall, error) {
	var resource Firewall
	err := ctx.ReadResource("gcp:compute/firewall:Firewall", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Firewall resources.
type firewallState struct {
	// The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
	// permitted connection.
	Allows []FirewallAllow `pulumi:"allows"`
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp *string `pulumi:"creationTimestamp"`
	// The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
	// denied connection.
	Denies []FirewallDeny `pulumi:"denies"`
	// An optional description of this resource. Provide this property when you create the resource.
	Description *string `pulumi:"description"`
	// If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
	// ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
	DestinationRanges []string `pulumi:"destinationRanges"`
	// Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
	// to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
	Direction *string `pulumi:"direction"`
	// Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
	// the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
	// rule will be enabled.
	Disabled *bool `pulumi:"disabled"`
	// This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
	// exported to Stackdriver.
	EnableLogging *bool `pulumi:"enableLogging"`
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name *string `pulumi:"name"`
	// The name or self_link of the network to attach this firewall to.
	Network *string `pulumi:"network"`
	// Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
	// 1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
	// (eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
	// rules having equal priority.
	Priority *int `pulumi:"priority"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The URI of the created resource.
	SelfLink *string `pulumi:"selfLink"`
	// If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
	// These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
	// are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
	// to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
	// apply. Only IPv4 is supported.
	SourceRanges []string `pulumi:"sourceRanges"`
	// If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
	// service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
	// address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
	// time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
	// sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
	// does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
	// as sourceTags or targetTags.
	SourceServiceAccounts []string `pulumi:"sourceServiceAccounts"`
	// If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
	// source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
	// associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
	// properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
	// that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
	// firewall to apply.
	SourceTags []string `pulumi:"sourceTags"`
	// A list of service accounts indicating sets of instances located in the network that may make network connections as
	// specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
	// targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
	TargetServiceAccounts []string `pulumi:"targetServiceAccounts"`
	// A list of instance tags indicating sets of instances located in the network that may make network connections as
	// specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
	// network.
	TargetTags []string `pulumi:"targetTags"`
}

type FirewallState struct {
	// The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
	// permitted connection.
	Allows FirewallAllowArrayInput
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringPtrInput
	// The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
	// denied connection.
	Denies FirewallDenyArrayInput
	// An optional description of this resource. Provide this property when you create the resource.
	Description pulumi.StringPtrInput
	// If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
	// ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
	DestinationRanges pulumi.StringArrayInput
	// Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
	// to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
	Direction pulumi.StringPtrInput
	// Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
	// the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
	// rule will be enabled.
	Disabled pulumi.BoolPtrInput
	// This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
	// exported to Stackdriver.
	EnableLogging pulumi.BoolPtrInput
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name pulumi.StringPtrInput
	// The name or self_link of the network to attach this firewall to.
	Network pulumi.StringPtrInput
	// Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
	// 1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
	// (eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
	// rules having equal priority.
	Priority pulumi.IntPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The URI of the created resource.
	SelfLink pulumi.StringPtrInput
	// If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
	// These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
	// are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
	// to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
	// apply. Only IPv4 is supported.
	SourceRanges pulumi.StringArrayInput
	// If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
	// service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
	// address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
	// time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
	// sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
	// does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
	// as sourceTags or targetTags.
	SourceServiceAccounts pulumi.StringArrayInput
	// If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
	// source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
	// associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
	// properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
	// that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
	// firewall to apply.
	SourceTags pulumi.StringArrayInput
	// A list of service accounts indicating sets of instances located in the network that may make network connections as
	// specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
	// targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
	TargetServiceAccounts pulumi.StringArrayInput
	// A list of instance tags indicating sets of instances located in the network that may make network connections as
	// specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
	// network.
	TargetTags pulumi.StringArrayInput
}

func (FirewallState) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallState)(nil)).Elem()
}

type firewallArgs struct {
	// The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
	// permitted connection.
	Allows []FirewallAllow `pulumi:"allows"`
	// The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
	// denied connection.
	Denies []FirewallDeny `pulumi:"denies"`
	// An optional description of this resource. Provide this property when you create the resource.
	Description *string `pulumi:"description"`
	// If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
	// ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
	DestinationRanges []string `pulumi:"destinationRanges"`
	// Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
	// to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
	Direction *string `pulumi:"direction"`
	// Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
	// the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
	// rule will be enabled.
	Disabled *bool `pulumi:"disabled"`
	// This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
	// exported to Stackdriver.
	EnableLogging *bool `pulumi:"enableLogging"`
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name *string `pulumi:"name"`
	// The name or self_link of the network to attach this firewall to.
	Network string `pulumi:"network"`
	// Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
	// 1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
	// (eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
	// rules having equal priority.
	Priority *int `pulumi:"priority"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
	// These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
	// are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
	// to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
	// apply. Only IPv4 is supported.
	SourceRanges []string `pulumi:"sourceRanges"`
	// If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
	// service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
	// address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
	// time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
	// sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
	// does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
	// as sourceTags or targetTags.
	SourceServiceAccounts []string `pulumi:"sourceServiceAccounts"`
	// If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
	// source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
	// associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
	// properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
	// that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
	// firewall to apply.
	SourceTags []string `pulumi:"sourceTags"`
	// A list of service accounts indicating sets of instances located in the network that may make network connections as
	// specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
	// targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
	TargetServiceAccounts []string `pulumi:"targetServiceAccounts"`
	// A list of instance tags indicating sets of instances located in the network that may make network connections as
	// specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
	// network.
	TargetTags []string `pulumi:"targetTags"`
}

// The set of arguments for constructing a Firewall resource.
type FirewallArgs struct {
	// The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
	// permitted connection.
	Allows FirewallAllowArrayInput
	// The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
	// denied connection.
	Denies FirewallDenyArrayInput
	// An optional description of this resource. Provide this property when you create the resource.
	Description pulumi.StringPtrInput
	// If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
	// ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
	DestinationRanges pulumi.StringArrayInput
	// Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
	// to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
	Direction pulumi.StringPtrInput
	// Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
	// the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
	// rule will be enabled.
	Disabled pulumi.BoolPtrInput
	// This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
	// exported to Stackdriver.
	EnableLogging pulumi.BoolPtrInput
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name pulumi.StringPtrInput
	// The name or self_link of the network to attach this firewall to.
	Network pulumi.StringInput
	// Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
	// 1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
	// (eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
	// rules having equal priority.
	Priority pulumi.IntPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
	// These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
	// are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
	// to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
	// apply. Only IPv4 is supported.
	SourceRanges pulumi.StringArrayInput
	// If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
	// service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
	// address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
	// time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
	// sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
	// does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
	// as sourceTags or targetTags.
	SourceServiceAccounts pulumi.StringArrayInput
	// If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
	// source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
	// associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
	// properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
	// that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
	// firewall to apply.
	SourceTags pulumi.StringArrayInput
	// A list of service accounts indicating sets of instances located in the network that may make network connections as
	// specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
	// targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
	TargetServiceAccounts pulumi.StringArrayInput
	// A list of instance tags indicating sets of instances located in the network that may make network connections as
	// specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
	// network.
	TargetTags pulumi.StringArrayInput
}

func (FirewallArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallArgs)(nil)).Elem()
}
