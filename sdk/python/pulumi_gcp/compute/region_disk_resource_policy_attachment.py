# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['RegionDiskResourcePolicyAttachment']


class RegionDiskResourcePolicyAttachment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disk: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Adds existing resource policies to a disk. You can only add one policy
        which will be applied to this disk for scheduling snapshot creation.

        > **Note:** This resource does not support zonal disks (`compute.Disk`). For zonal disks, please refer to the `compute.DiskResourcePolicyAttachment` resource.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] disk: The name of the regional disk in which the resource policies are attached to.
        :param pulumi.Input[str] name: The resource policy to be attached to the disk for scheduling snapshot
               creation. Do not specify the self link.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: A reference to the region where the disk resides.
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

            if disk is None:
                raise TypeError("Missing required property 'disk'")
            __props__['disk'] = disk
            __props__['name'] = name
            __props__['project'] = project
            __props__['region'] = region
        super(RegionDiskResourcePolicyAttachment, __self__).__init__(
            'gcp:compute/regionDiskResourcePolicyAttachment:RegionDiskResourcePolicyAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            disk: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'RegionDiskResourcePolicyAttachment':
        """
        Get an existing RegionDiskResourcePolicyAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] disk: The name of the regional disk in which the resource policies are attached to.
        :param pulumi.Input[str] name: The resource policy to be attached to the disk for scheduling snapshot
               creation. Do not specify the self link.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: A reference to the region where the disk resides.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["disk"] = disk
        __props__["name"] = name
        __props__["project"] = project
        __props__["region"] = region
        return RegionDiskResourcePolicyAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def disk(self) -> pulumi.Output[str]:
        """
        The name of the regional disk in which the resource policies are attached to.
        """
        return pulumi.get(self, "disk")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource policy to be attached to the disk for scheduling snapshot
        creation. Do not specify the self link.
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
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        A reference to the region where the disk resides.
        """
        return pulumi.get(self, "region")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

