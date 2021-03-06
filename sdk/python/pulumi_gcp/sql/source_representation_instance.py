# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['SourceRepresentationInstance']


class SourceRepresentationInstance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_version: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A source representation instance is a Cloud SQL instance that represents
        the source database server to the Cloud SQL replica. It is visible in the
        Cloud Console and appears the same as a regular Cloud SQL instance, but it
        contains no data, requires no configuration or maintenance, and does not
        affect billing. You cannot update the source representation instance.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_version: The MySQL version running on your source database server.
               Possible values are `MYSQL_5_6` and `MYSQL_5_7`.
        :param pulumi.Input[str] host: The externally accessible IPv4 address for the source database server.
        :param pulumi.Input[str] name: The name of the source representation instance. Use any valid Cloud SQL instance name.
        :param pulumi.Input[int] port: The externally accessible port for the source database server.
               Defaults to 3306.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The Region in which the created instance should reside.
               If it is not provided, the provider region is used.
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

            if database_version is None:
                raise TypeError("Missing required property 'database_version'")
            __props__['database_version'] = database_version
            if host is None:
                raise TypeError("Missing required property 'host'")
            __props__['host'] = host
            __props__['name'] = name
            __props__['port'] = port
            __props__['project'] = project
            __props__['region'] = region
        super(SourceRepresentationInstance, __self__).__init__(
            'gcp:sql/sourceRepresentationInstance:SourceRepresentationInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            database_version: Optional[pulumi.Input[str]] = None,
            host: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'SourceRepresentationInstance':
        """
        Get an existing SourceRepresentationInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_version: The MySQL version running on your source database server.
               Possible values are `MYSQL_5_6` and `MYSQL_5_7`.
        :param pulumi.Input[str] host: The externally accessible IPv4 address for the source database server.
        :param pulumi.Input[str] name: The name of the source representation instance. Use any valid Cloud SQL instance name.
        :param pulumi.Input[int] port: The externally accessible port for the source database server.
               Defaults to 3306.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The Region in which the created instance should reside.
               If it is not provided, the provider region is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["database_version"] = database_version
        __props__["host"] = host
        __props__["name"] = name
        __props__["port"] = port
        __props__["project"] = project
        __props__["region"] = region
        return SourceRepresentationInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> pulumi.Output[str]:
        """
        The MySQL version running on your source database server.
        Possible values are `MYSQL_5_6` and `MYSQL_5_7`.
        """
        return pulumi.get(self, "database_version")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[str]:
        """
        The externally accessible IPv4 address for the source database server.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the source representation instance. Use any valid Cloud SQL instance name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[int]]:
        """
        The externally accessible port for the source database server.
        Defaults to 3306.
        """
        return pulumi.get(self, "port")

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
        The Region in which the created instance should reside.
        If it is not provided, the provider region is used.
        """
        return pulumi.get(self, "region")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

