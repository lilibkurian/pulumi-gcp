# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Brand(pulumi.CustomResource):
    application_title: pulumi.Output[str]
    """
    Application name displayed on OAuth consent screen.
    """
    name: pulumi.Output[str]
    """
    Output only. Identifier of the brand, in the format 'projects/{project_number}/brands/{brand_id}'. NOTE: The brand
    identification corresponds to the project number as only one brand per project can be created.
    """
    org_internal_only: pulumi.Output[bool]
    """
    Whether the brand is only intended for usage inside the GSuite organization only.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    support_email: pulumi.Output[str]
    """
    Support email displayed on the OAuth consent screen. Can be either a
    user or group email. When a user email is specified, the caller must
    be the user with the associated email address. When a group email is
    specified, the caller can be either a user or a service account which
    is an owner of the specified group in Cloud Identity.
    """
    def __init__(__self__, resource_name, opts=None, application_title=None, project=None, support_email=None, __props__=None, __name__=None, __opts__=None):
        """
        OAuth brand data. Only "Organization Internal" brands can be created
        programatically via API. To convert it into an external brands
        please use the GCP Console.


        > **Note:** Brands can be created only once for a Google Cloud Platform
        project and cannot be deleted. Destroying a provider-managed Brand
        will remove it from state but *will not delete the resource on the server.*

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_title: Application name displayed on OAuth consent screen.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] support_email: Support email displayed on the OAuth consent screen. Can be either a
               user or group email. When a user email is specified, the caller must
               be the user with the associated email address. When a group email is
               specified, the caller can be either a user or a service account which
               is an owner of the specified group in Cloud Identity.
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

            if application_title is None:
                raise TypeError("Missing required property 'application_title'")
            __props__['application_title'] = application_title
            __props__['project'] = project
            if support_email is None:
                raise TypeError("Missing required property 'support_email'")
            __props__['support_email'] = support_email
            __props__['name'] = None
            __props__['org_internal_only'] = None
        super(Brand, __self__).__init__(
            'gcp:iap/brand:Brand',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, application_title=None, name=None, org_internal_only=None, project=None, support_email=None):
        """
        Get an existing Brand resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_title: Application name displayed on OAuth consent screen.
        :param pulumi.Input[str] name: Output only. Identifier of the brand, in the format 'projects/{project_number}/brands/{brand_id}'. NOTE: The brand
               identification corresponds to the project number as only one brand per project can be created.
        :param pulumi.Input[bool] org_internal_only: Whether the brand is only intended for usage inside the GSuite organization only.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] support_email: Support email displayed on the OAuth consent screen. Can be either a
               user or group email. When a user email is specified, the caller must
               be the user with the associated email address. When a group email is
               specified, the caller can be either a user or a service account which
               is an owner of the specified group in Cloud Identity.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["application_title"] = application_title
        __props__["name"] = name
        __props__["org_internal_only"] = org_internal_only
        __props__["project"] = project
        __props__["support_email"] = support_email
        return Brand(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
