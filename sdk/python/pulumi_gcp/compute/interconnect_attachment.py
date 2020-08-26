# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['InterconnectAttachment']


class InterconnectAttachment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_enabled: Optional[pulumi.Input[bool]] = None,
                 bandwidth: Optional[pulumi.Input[str]] = None,
                 candidate_subnets: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 edge_availability_domain: Optional[pulumi.Input[str]] = None,
                 interconnect: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 router: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vlan_tag8021q: Optional[pulumi.Input[float]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Represents an InterconnectAttachment (VLAN attachment) resource. For more
        information, see Creating VLAN Attachments.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_enabled: Whether the VLAN attachment is enabled or disabled.  When using
               PARTNER type this will Pre-Activate the interconnect attachment
        :param pulumi.Input[str] bandwidth: Provisioned bandwidth capacity for the interconnect attachment.
               For attachments of type DEDICATED, the user can set the bandwidth.
               For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth.
               Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED,
               Defaults to BPS_10G
               Possible values are `BPS_50M`, `BPS_100M`, `BPS_200M`, `BPS_300M`, `BPS_400M`, `BPS_500M`, `BPS_1G`, `BPS_2G`, `BPS_5G`, `BPS_10G`, `BPS_20G`, and `BPS_50G`.
        :param pulumi.Input[List[pulumi.Input[str]]] candidate_subnets: Up to 16 candidate prefixes that can be used to restrict the allocation
               of cloudRouterIpAddress and customerRouterIpAddress for this attachment.
               All prefixes must be within link-local address space (169.254.0.0/16)
               and must be /29 or shorter (/28, /27, etc). Google will attempt to select
               an unused /29 from the supplied candidate prefix(es). The request will
               fail if all possible /29s are in use on Google's edge. If not supplied,
               Google will randomly select an unused /29 from all of link-local space.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] edge_availability_domain: Desired availability domain for the attachment. Only available for type
               PARTNER, at creation time. For improved reliability, customers should
               configure a pair of attachments with one per availability domain. The
               selected availability domain will be provided to the Partner via the
               pairing key so that the provisioned circuit will lie in the specified
               domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.
        :param pulumi.Input[str] interconnect: URL of the underlying Interconnect object that this attachment's
               traffic will traverse through. Required if type is DEDICATED, must not
               be set if type is PARTNER.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The
               name must be 1-63 characters long, and comply with RFC1035. Specifically, the
               name must be 1-63 characters long and match the regular expression
               `a-z?` which means the first character must be a
               lowercase letter, and all following characters must be a dash, lowercase
               letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where the regional interconnect attachment resides.
        :param pulumi.Input[str] router: URL of the cloud router to be used for dynamic routing. This router must be in
               the same region as this InterconnectAttachment. The InterconnectAttachment will
               automatically connect the Interconnect to the network & region within which the
               Cloud Router is configured.
        :param pulumi.Input[str] type: The type of InterconnectAttachment you wish to create. Defaults to
               DEDICATED.
               Possible values are `DEDICATED`, `PARTNER`, and `PARTNER_PROVIDER`.
        :param pulumi.Input[float] vlan_tag8021q: The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When
               using PARTNER type this will be managed upstream.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['admin_enabled'] = admin_enabled
            __props__['bandwidth'] = bandwidth
            __props__['candidate_subnets'] = candidate_subnets
            __props__['description'] = description
            __props__['edge_availability_domain'] = edge_availability_domain
            __props__['interconnect'] = interconnect
            __props__['name'] = name
            __props__['project'] = project
            __props__['region'] = region
            if router is None:
                raise TypeError("Missing required property 'router'")
            __props__['router'] = router
            __props__['type'] = type
            __props__['vlan_tag8021q'] = vlan_tag8021q
            __props__['cloud_router_ip_address'] = None
            __props__['creation_timestamp'] = None
            __props__['customer_router_ip_address'] = None
            __props__['google_reference_id'] = None
            __props__['pairing_key'] = None
            __props__['partner_asn'] = None
            __props__['private_interconnect_info'] = None
            __props__['self_link'] = None
            __props__['state'] = None
        super(InterconnectAttachment, __self__).__init__(
            'gcp:compute/interconnectAttachment:InterconnectAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_enabled: Optional[pulumi.Input[bool]] = None,
            bandwidth: Optional[pulumi.Input[str]] = None,
            candidate_subnets: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            cloud_router_ip_address: Optional[pulumi.Input[str]] = None,
            creation_timestamp: Optional[pulumi.Input[str]] = None,
            customer_router_ip_address: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            edge_availability_domain: Optional[pulumi.Input[str]] = None,
            google_reference_id: Optional[pulumi.Input[str]] = None,
            interconnect: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            pairing_key: Optional[pulumi.Input[str]] = None,
            partner_asn: Optional[pulumi.Input[str]] = None,
            private_interconnect_info: Optional[pulumi.Input[pulumi.InputType['InterconnectAttachmentPrivateInterconnectInfoArgs']]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            router: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            vlan_tag8021q: Optional[pulumi.Input[float]] = None) -> 'InterconnectAttachment':
        """
        Get an existing InterconnectAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_enabled: Whether the VLAN attachment is enabled or disabled.  When using
               PARTNER type this will Pre-Activate the interconnect attachment
        :param pulumi.Input[str] bandwidth: Provisioned bandwidth capacity for the interconnect attachment.
               For attachments of type DEDICATED, the user can set the bandwidth.
               For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth.
               Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED,
               Defaults to BPS_10G
               Possible values are `BPS_50M`, `BPS_100M`, `BPS_200M`, `BPS_300M`, `BPS_400M`, `BPS_500M`, `BPS_1G`, `BPS_2G`, `BPS_5G`, `BPS_10G`, `BPS_20G`, and `BPS_50G`.
        :param pulumi.Input[List[pulumi.Input[str]]] candidate_subnets: Up to 16 candidate prefixes that can be used to restrict the allocation
               of cloudRouterIpAddress and customerRouterIpAddress for this attachment.
               All prefixes must be within link-local address space (169.254.0.0/16)
               and must be /29 or shorter (/28, /27, etc). Google will attempt to select
               an unused /29 from the supplied candidate prefix(es). The request will
               fail if all possible /29s are in use on Google's edge. If not supplied,
               Google will randomly select an unused /29 from all of link-local space.
        :param pulumi.Input[str] cloud_router_ip_address: IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] customer_router_ip_address: IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] edge_availability_domain: Desired availability domain for the attachment. Only available for type
               PARTNER, at creation time. For improved reliability, customers should
               configure a pair of attachments with one per availability domain. The
               selected availability domain will be provided to the Partner via the
               pairing key so that the provisioned circuit will lie in the specified
               domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.
        :param pulumi.Input[str] google_reference_id: Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity
               issues.
        :param pulumi.Input[str] interconnect: URL of the underlying Interconnect object that this attachment's
               traffic will traverse through. Required if type is DEDICATED, must not
               be set if type is PARTNER.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The
               name must be 1-63 characters long, and comply with RFC1035. Specifically, the
               name must be 1-63 characters long and match the regular expression
               `a-z?` which means the first character must be a
               lowercase letter, and all following characters must be a dash, lowercase
               letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] pairing_key: [Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier of an PARTNER attachment used to
               initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"
        :param pulumi.Input[str] partner_asn: [Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for the router that should be supplied by a
               layer 3 Partner if they configured BGP on behalf of the customer.
        :param pulumi.Input[pulumi.InputType['InterconnectAttachmentPrivateInterconnectInfoArgs']] private_interconnect_info: Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached
               to is of type DEDICATED.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where the regional interconnect attachment resides.
        :param pulumi.Input[str] router: URL of the cloud router to be used for dynamic routing. This router must be in
               the same region as this InterconnectAttachment. The InterconnectAttachment will
               automatically connect the Interconnect to the network & region within which the
               Cloud Router is configured.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[str] state: [Output Only] The current state of this attachment's functionality.
        :param pulumi.Input[str] type: The type of InterconnectAttachment you wish to create. Defaults to
               DEDICATED.
               Possible values are `DEDICATED`, `PARTNER`, and `PARTNER_PROVIDER`.
        :param pulumi.Input[float] vlan_tag8021q: The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When
               using PARTNER type this will be managed upstream.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_enabled"] = admin_enabled
        __props__["bandwidth"] = bandwidth
        __props__["candidate_subnets"] = candidate_subnets
        __props__["cloud_router_ip_address"] = cloud_router_ip_address
        __props__["creation_timestamp"] = creation_timestamp
        __props__["customer_router_ip_address"] = customer_router_ip_address
        __props__["description"] = description
        __props__["edge_availability_domain"] = edge_availability_domain
        __props__["google_reference_id"] = google_reference_id
        __props__["interconnect"] = interconnect
        __props__["name"] = name
        __props__["pairing_key"] = pairing_key
        __props__["partner_asn"] = partner_asn
        __props__["private_interconnect_info"] = private_interconnect_info
        __props__["project"] = project
        __props__["region"] = region
        __props__["router"] = router
        __props__["self_link"] = self_link
        __props__["state"] = state
        __props__["type"] = type
        __props__["vlan_tag8021q"] = vlan_tag8021q
        return InterconnectAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminEnabled")
    def admin_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the VLAN attachment is enabled or disabled.  When using
        PARTNER type this will Pre-Activate the interconnect attachment
        """
        return pulumi.get(self, "admin_enabled")

    @property
    @pulumi.getter
    def bandwidth(self) -> pulumi.Output[str]:
        """
        Provisioned bandwidth capacity for the interconnect attachment.
        For attachments of type DEDICATED, the user can set the bandwidth.
        For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth.
        Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED,
        Defaults to BPS_10G
        Possible values are `BPS_50M`, `BPS_100M`, `BPS_200M`, `BPS_300M`, `BPS_400M`, `BPS_500M`, `BPS_1G`, `BPS_2G`, `BPS_5G`, `BPS_10G`, `BPS_20G`, and `BPS_50G`.
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter(name="candidateSubnets")
    def candidate_subnets(self) -> pulumi.Output[Optional[List[str]]]:
        """
        Up to 16 candidate prefixes that can be used to restrict the allocation
        of cloudRouterIpAddress and customerRouterIpAddress for this attachment.
        All prefixes must be within link-local address space (169.254.0.0/16)
        and must be /29 or shorter (/28, /27, etc). Google will attempt to select
        an unused /29 from the supplied candidate prefix(es). The request will
        fail if all possible /29s are in use on Google's edge. If not supplied,
        Google will randomly select an unused /29 from all of link-local space.
        """
        return pulumi.get(self, "candidate_subnets")

    @property
    @pulumi.getter(name="cloudRouterIpAddress")
    def cloud_router_ip_address(self) -> pulumi.Output[str]:
        """
        IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.
        """
        return pulumi.get(self, "cloud_router_ip_address")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter(name="customerRouterIpAddress")
    def customer_router_ip_address(self) -> pulumi.Output[str]:
        """
        IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.
        """
        return pulumi.get(self, "customer_router_ip_address")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="edgeAvailabilityDomain")
    def edge_availability_domain(self) -> pulumi.Output[str]:
        """
        Desired availability domain for the attachment. Only available for type
        PARTNER, at creation time. For improved reliability, customers should
        configure a pair of attachments with one per availability domain. The
        selected availability domain will be provided to the Partner via the
        pairing key so that the provisioned circuit will lie in the specified
        domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.
        """
        return pulumi.get(self, "edge_availability_domain")

    @property
    @pulumi.getter(name="googleReferenceId")
    def google_reference_id(self) -> pulumi.Output[str]:
        """
        Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity
        issues.
        """
        return pulumi.get(self, "google_reference_id")

    @property
    @pulumi.getter
    def interconnect(self) -> pulumi.Output[Optional[str]]:
        """
        URL of the underlying Interconnect object that this attachment's
        traffic will traverse through. Required if type is DEDICATED, must not
        be set if type is PARTNER.
        """
        return pulumi.get(self, "interconnect")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is created. The
        name must be 1-63 characters long, and comply with RFC1035. Specifically, the
        name must be 1-63 characters long and match the regular expression
        `a-z?` which means the first character must be a
        lowercase letter, and all following characters must be a dash, lowercase
        letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pairingKey")
    def pairing_key(self) -> pulumi.Output[str]:
        """
        [Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier of an PARTNER attachment used to
        initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"
        """
        return pulumi.get(self, "pairing_key")

    @property
    @pulumi.getter(name="partnerAsn")
    def partner_asn(self) -> pulumi.Output[str]:
        """
        [Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for the router that should be supplied by a
        layer 3 Partner if they configured BGP on behalf of the customer.
        """
        return pulumi.get(self, "partner_asn")

    @property
    @pulumi.getter(name="privateInterconnectInfo")
    def private_interconnect_info(self) -> pulumi.Output['outputs.InterconnectAttachmentPrivateInterconnectInfo']:
        """
        Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached
        to is of type DEDICATED.
        """
        return pulumi.get(self, "private_interconnect_info")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Region where the regional interconnect attachment resides.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def router(self) -> pulumi.Output[str]:
        """
        URL of the cloud router to be used for dynamic routing. This router must be in
        the same region as this InterconnectAttachment. The InterconnectAttachment will
        automatically connect the Interconnect to the network & region within which the
        Cloud Router is configured.
        """
        return pulumi.get(self, "router")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        [Output Only] The current state of this attachment's functionality.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of InterconnectAttachment you wish to create. Defaults to
        DEDICATED.
        Possible values are `DEDICATED`, `PARTNER`, and `PARTNER_PROVIDER`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vlanTag8021q")
    def vlan_tag8021q(self) -> pulumi.Output[float]:
        """
        The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When
        using PARTNER type this will be managed upstream.
        """
        return pulumi.get(self, "vlan_tag8021q")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

