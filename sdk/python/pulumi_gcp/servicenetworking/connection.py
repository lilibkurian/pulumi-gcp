# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Connection']


class Connection(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 reserved_peering_ranges: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a private VPC connection with a GCP service provider. For more information see
        [the official documentation](https://cloud.google.com/vpc/docs/configure-private-services-access#creating-connection)
        and
        [API](https://cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network: Name of VPC network connected with service producers using VPC peering.
        :param pulumi.Input[List[pulumi.Input[str]]] reserved_peering_ranges: Named IP address range(s) of PEERING type reserved for
               this service provider. Note that invoking this method with a different range when connection
               is already established will not reallocate already provisioned service producer subnetworks.
        :param pulumi.Input[str] service: Provider peering service that is managing peering connectivity for a
               service provider organization. For Google services that support this functionality it is
               'servicenetworking.googleapis.com'.
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

            if network is None:
                raise TypeError("Missing required property 'network'")
            __props__['network'] = network
            if reserved_peering_ranges is None:
                raise TypeError("Missing required property 'reserved_peering_ranges'")
            __props__['reserved_peering_ranges'] = reserved_peering_ranges
            if service is None:
                raise TypeError("Missing required property 'service'")
            __props__['service'] = service
            __props__['peering'] = None
        super(Connection, __self__).__init__(
            'gcp:servicenetworking/connection:Connection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            network: Optional[pulumi.Input[str]] = None,
            peering: Optional[pulumi.Input[str]] = None,
            reserved_peering_ranges: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            service: Optional[pulumi.Input[str]] = None) -> 'Connection':
        """
        Get an existing Connection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network: Name of VPC network connected with service producers using VPC peering.
        :param pulumi.Input[List[pulumi.Input[str]]] reserved_peering_ranges: Named IP address range(s) of PEERING type reserved for
               this service provider. Note that invoking this method with a different range when connection
               is already established will not reallocate already provisioned service producer subnetworks.
        :param pulumi.Input[str] service: Provider peering service that is managing peering connectivity for a
               service provider organization. For Google services that support this functionality it is
               'servicenetworking.googleapis.com'.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["network"] = network
        __props__["peering"] = peering
        __props__["reserved_peering_ranges"] = reserved_peering_ranges
        __props__["service"] = service
        return Connection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        Name of VPC network connected with service producers using VPC peering.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def peering(self) -> pulumi.Output[str]:
        return pulumi.get(self, "peering")

    @property
    @pulumi.getter(name="reservedPeeringRanges")
    def reserved_peering_ranges(self) -> pulumi.Output[List[str]]:
        """
        Named IP address range(s) of PEERING type reserved for
        this service provider. Note that invoking this method with a different range when connection
        is already established will not reallocate already provisioned service producer subnetworks.
        """
        return pulumi.get(self, "reserved_peering_ranges")

    @property
    @pulumi.getter
    def service(self) -> pulumi.Output[str]:
        """
        Provider peering service that is managing peering connectivity for a
        service provider organization. For Google services that support this functionality it is
        'servicenetworking.googleapis.com'.
        """
        return pulumi.get(self, "service")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

