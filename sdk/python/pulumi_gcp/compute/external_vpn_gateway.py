# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class ExternalVpnGateway(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    An optional description of this resource.
    """
    interfaces: pulumi.Output[list]
    """
    A list of interfaces on this external VPN gateway.
    Structure is documented below.

      * `id` (`float`) - The numberic ID for this interface. Allowed values are based on the redundancy type
        of this external VPN gateway
        * `0 - SINGLE_IP_INTERNALLY_REDUNDANT`
        * `0, 1 - TWO_IPS_REDUNDANCY`
        * `0, 1, 2, 3 - FOUR_IPS_REDUNDANCY`
      * `ip_address` (`str`) - IP address of the interface in the external VPN gateway.
        Only IPv4 is supported. This IP address can be either from
        your on-premise gateway or another Cloud provider’s VPN gateway,
        it cannot be an IP address from Google Compute Engine.
    """
    name: pulumi.Output[str]
    """
    Name of the resource. Provided by the client when the resource is
    created. The name must be 1-63 characters long, and comply with
    RFC1035.  Specifically, the name must be 1-63 characters long and
    match the regular expression `a-z?` which means
    the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last
    character, which cannot be a dash.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    redundancy_type: pulumi.Output[str]
    """
    Indicates the redundancy type of this external VPN gateway
    Possible values are `FOUR_IPS_REDUNDANCY`, `SINGLE_IP_INTERNALLY_REDUNDANT`, and `TWO_IPS_REDUNDANCY`.
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    def __init__(__self__, resource_name, opts=None, description=None, interfaces=None, name=None, project=None, redundancy_type=None, __props__=None, __name__=None, __opts__=None):
        """
        Represents a VPN gateway managed outside of GCP.

        To get more information about ExternalVpnGateway, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/externalVpnGateways)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[list] interfaces: A list of interfaces on this external VPN gateway.
               Structure is documented below.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035.  Specifically, the name must be 1-63 characters long and
               match the regular expression `a-z?` which means
               the first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] redundancy_type: Indicates the redundancy type of this external VPN gateway
               Possible values are `FOUR_IPS_REDUNDANCY`, `SINGLE_IP_INTERNALLY_REDUNDANT`, and `TWO_IPS_REDUNDANCY`.

        The **interfaces** object supports the following:

          * `id` (`pulumi.Input[float]`) - The numberic ID for this interface. Allowed values are based on the redundancy type
            of this external VPN gateway
            * `0 - SINGLE_IP_INTERNALLY_REDUNDANT`
            * `0, 1 - TWO_IPS_REDUNDANCY`
            * `0, 1, 2, 3 - FOUR_IPS_REDUNDANCY`
          * `ip_address` (`pulumi.Input[str]`) - IP address of the interface in the external VPN gateway.
            Only IPv4 is supported. This IP address can be either from
            your on-premise gateway or another Cloud provider’s VPN gateway,
            it cannot be an IP address from Google Compute Engine.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['description'] = description
            __props__['interfaces'] = interfaces
            __props__['name'] = name
            __props__['project'] = project
            __props__['redundancy_type'] = redundancy_type
            __props__['self_link'] = None
        super(ExternalVpnGateway, __self__).__init__(
            'gcp:compute/externalVpnGateway:ExternalVpnGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, interfaces=None, name=None, project=None, redundancy_type=None, self_link=None):
        """
        Get an existing ExternalVpnGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[list] interfaces: A list of interfaces on this external VPN gateway.
               Structure is documented below.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035.  Specifically, the name must be 1-63 characters long and
               match the regular expression `a-z?` which means
               the first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] redundancy_type: Indicates the redundancy type of this external VPN gateway
               Possible values are `FOUR_IPS_REDUNDANCY`, `SINGLE_IP_INTERNALLY_REDUNDANT`, and `TWO_IPS_REDUNDANCY`.
        :param pulumi.Input[str] self_link: The URI of the created resource.

        The **interfaces** object supports the following:

          * `id` (`pulumi.Input[float]`) - The numberic ID for this interface. Allowed values are based on the redundancy type
            of this external VPN gateway
            * `0 - SINGLE_IP_INTERNALLY_REDUNDANT`
            * `0, 1 - TWO_IPS_REDUNDANCY`
            * `0, 1, 2, 3 - FOUR_IPS_REDUNDANCY`
          * `ip_address` (`pulumi.Input[str]`) - IP address of the interface in the external VPN gateway.
            Only IPv4 is supported. This IP address can be either from
            your on-premise gateway or another Cloud provider’s VPN gateway,
            it cannot be an IP address from Google Compute Engine.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["interfaces"] = interfaces
        __props__["name"] = name
        __props__["project"] = project
        __props__["redundancy_type"] = redundancy_type
        __props__["self_link"] = self_link
        return ExternalVpnGateway(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
