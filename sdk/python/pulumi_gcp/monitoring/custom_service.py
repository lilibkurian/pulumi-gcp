# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['CustomService']


class CustomService(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 telemetry: Optional[pulumi.Input[pulumi.InputType['CustomServiceTelemetryArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A Service is a discrete, autonomous, and network-accessible unit,
        designed to solve an individual concern (Wikipedia). In Cloud Monitoring,
        a Service acts as the root resource under which operational aspects of
        the service are accessible

        To get more information about Service, see:

        * [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services)
        * How-to Guides
            * [Service Monitoring](https://cloud.google.com/monitoring/service-monitoring)
            * [Monitoring API Documentation](https://cloud.google.com/monitoring/api/v3/)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Name used for UI elements listing this Service.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] service_id: An optional service ID to use. If not given, the server will generate a
               service ID.
        :param pulumi.Input[pulumi.InputType['CustomServiceTelemetryArgs']] telemetry: Configuration for how to query telemetry on a Service.
               Structure is documented below.
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

            __props__['display_name'] = display_name
            __props__['project'] = project
            __props__['service_id'] = service_id
            __props__['telemetry'] = telemetry
            __props__['name'] = None
        super(CustomService, __self__).__init__(
            'gcp:monitoring/customService:CustomService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            service_id: Optional[pulumi.Input[str]] = None,
            telemetry: Optional[pulumi.Input[pulumi.InputType['CustomServiceTelemetryArgs']]] = None) -> 'CustomService':
        """
        Get an existing CustomService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Name used for UI elements listing this Service.
        :param pulumi.Input[str] name: The full resource name for this service. The syntax is: projects/[PROJECT_ID]/services/[SERVICE_ID].
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] service_id: An optional service ID to use. If not given, the server will generate a
               service ID.
        :param pulumi.Input[pulumi.InputType['CustomServiceTelemetryArgs']] telemetry: Configuration for how to query telemetry on a Service.
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["display_name"] = display_name
        __props__["name"] = name
        __props__["project"] = project
        __props__["service_id"] = service_id
        __props__["telemetry"] = telemetry
        return CustomService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name used for UI elements listing this Service.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The full resource name for this service. The syntax is: projects/[PROJECT_ID]/services/[SERVICE_ID].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[str]:
        """
        An optional service ID to use. If not given, the server will generate a
        service ID.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter
    def telemetry(self) -> pulumi.Output[Optional['outputs.CustomServiceTelemetry']]:
        """
        Configuration for how to query telemetry on a Service.
        Structure is documented below.
        """
        return pulumi.get(self, "telemetry")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

