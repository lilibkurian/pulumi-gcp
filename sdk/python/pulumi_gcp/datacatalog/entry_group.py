# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['EntryGroup']


class EntryGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 entry_group_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        An EntryGroup resource represents a logical grouping of zero or more Data Catalog Entry resources.

        To get more information about EntryGroup, see:

        * [API documentation](https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/data-catalog/docs)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Entry group description, which can consist of several sentences or paragraphs that describe entry group contents.
        :param pulumi.Input[str] display_name: A short name to identify the entry group, for example, "analytics data - jan 2011".
        :param pulumi.Input[str] entry_group_id: The id of the entry group to create. The id must begin with a letter or underscore,
               contain only English letters, numbers and underscores, and be at most 64 characters.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: EntryGroup location region.
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

            __props__['description'] = description
            __props__['display_name'] = display_name
            if entry_group_id is None:
                raise TypeError("Missing required property 'entry_group_id'")
            __props__['entry_group_id'] = entry_group_id
            __props__['project'] = project
            __props__['region'] = region
            __props__['name'] = None
        super(EntryGroup, __self__).__init__(
            'gcp:datacatalog/entryGroup:EntryGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            entry_group_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'EntryGroup':
        """
        Get an existing EntryGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Entry group description, which can consist of several sentences or paragraphs that describe entry group contents.
        :param pulumi.Input[str] display_name: A short name to identify the entry group, for example, "analytics data - jan 2011".
        :param pulumi.Input[str] entry_group_id: The id of the entry group to create. The id must begin with a letter or underscore,
               contain only English letters, numbers and underscores, and be at most 64 characters.
        :param pulumi.Input[str] name: The resource name of the entry group in URL format. Example:
               projects/{project}/locations/{location}/entryGroups/{entryGroupId}
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: EntryGroup location region.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["display_name"] = display_name
        __props__["entry_group_id"] = entry_group_id
        __props__["name"] = name
        __props__["project"] = project
        __props__["region"] = region
        return EntryGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Entry group description, which can consist of several sentences or paragraphs that describe entry group contents.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        A short name to identify the entry group, for example, "analytics data - jan 2011".
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="entryGroupId")
    def entry_group_id(self) -> pulumi.Output[str]:
        """
        The id of the entry group to create. The id must begin with a letter or underscore,
        contain only English letters, numbers and underscores, and be at most 64 characters.
        """
        return pulumi.get(self, "entry_group_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the entry group in URL format. Example:
        projects/{project}/locations/{location}/entryGroups/{entryGroupId}
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
        EntryGroup location region.
        """
        return pulumi.get(self, "region")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

