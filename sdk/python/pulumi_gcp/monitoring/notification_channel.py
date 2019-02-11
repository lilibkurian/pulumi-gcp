# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class NotificationChannel(pulumi.CustomResource):
    description: pulumi.Output[str]
    display_name: pulumi.Output[str]
    enabled: pulumi.Output[bool]
    labels: pulumi.Output[dict]
    name: pulumi.Output[str]
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    type: pulumi.Output[str]
    user_labels: pulumi.Output[dict]
    verification_status: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, description=None, display_name=None, enabled=None, labels=None, project=None, type=None, user_labels=None, __name__=None, __opts__=None):
        """
        A NotificationChannel is a medium through which an alert is delivered
        when a policy violation is detected. Examples of channels include email, SMS,
        and third-party messaging applications. Fields containing sensitive information
        like authentication tokens or contact info are only partially populated on retrieval.
        
        
        To get more information about NotificationChannel, see:
        
        * [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/monitoring/api/v3/)
        
        <div class = "oics-button" style="float: right; margin: 0 0 -15px">
          <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=notification_channel_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
            <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
          </a>
        </div>
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description
        :param pulumi.Input[str] display_name
        :param pulumi.Input[bool] enabled
        :param pulumi.Input[dict] labels
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] type
        :param pulumi.Input[dict] user_labels
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['description'] = description

        if display_name is None:
            raise TypeError('Missing required property display_name')
        __props__['display_name'] = display_name

        __props__['enabled'] = enabled

        __props__['labels'] = labels

        __props__['project'] = project

        if type is None:
            raise TypeError('Missing required property type')
        __props__['type'] = type

        __props__['user_labels'] = user_labels

        __props__['name'] = None
        __props__['verification_status'] = None

        super(NotificationChannel, __self__).__init__(
            'gcp:monitoring/notificationChannel:NotificationChannel',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

