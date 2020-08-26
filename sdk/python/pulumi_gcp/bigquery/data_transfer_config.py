# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['DataTransferConfig']


class DataTransferConfig(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_refresh_window_days: Optional[pulumi.Input[float]] = None,
                 data_source_id: Optional[pulumi.Input[str]] = None,
                 destination_dataset_id: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 params: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[str]] = None,
                 service_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Represents a data transfer configuration. A transfer configuration
        contains all metadata needed to perform a data transfer.

        To get more information about Config, see:

        * [API documentation](https://cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs/create)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/bigquery/docs/reference/datatransfer/rest/)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] data_refresh_window_days: The number of days to look back to automatically refresh the data.
               For example, if dataRefreshWindowDays = 10, then every day BigQuery
               reingests data for [today-10, today-1], rather than ingesting data for
               just [today-1]. Only valid if the data source supports the feature.
               Set the value to 0 to use the default value.
        :param pulumi.Input[str] data_source_id: The data source id. Cannot be changed once the transfer config is created.
        :param pulumi.Input[str] destination_dataset_id: The BigQuery target dataset id.
        :param pulumi.Input[bool] disabled: When set to true, no runs are scheduled for a given transfer.
        :param pulumi.Input[str] display_name: The user specified display name for the transfer config.
        :param pulumi.Input[str] location: The geographic location where the transfer config should reside.
               Examples: US, EU, asia-northeast1. The default value is US.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] params: These parameters are specific to each data source.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] schedule: Data transfer schedule. If the data source does not support a custom
               schedule, this should be empty. If it is empty, the default value for
               the data source will be used. The specified times are in UTC. Examples
               of valid format: 1st,3rd monday of month 15:30, every wed,fri of jan,
               jun 13:15, and first sunday of quarter 00:00. See more explanation
               about the format here:
               https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
               NOTE: the granularity should be at least 8 hours, or less frequent.
        :param pulumi.Input[str] service_account_name: Optional service account name. If this field is set, transfer config will
               be created with this service account credentials. It requires that
               requesting user calling this API has permissions to act as this service account.
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

            __props__['data_refresh_window_days'] = data_refresh_window_days
            if data_source_id is None:
                raise TypeError("Missing required property 'data_source_id'")
            __props__['data_source_id'] = data_source_id
            if destination_dataset_id is None:
                raise TypeError("Missing required property 'destination_dataset_id'")
            __props__['destination_dataset_id'] = destination_dataset_id
            __props__['disabled'] = disabled
            if display_name is None:
                raise TypeError("Missing required property 'display_name'")
            __props__['display_name'] = display_name
            __props__['location'] = location
            if params is None:
                raise TypeError("Missing required property 'params'")
            __props__['params'] = params
            __props__['project'] = project
            __props__['schedule'] = schedule
            __props__['service_account_name'] = service_account_name
            __props__['name'] = None
        super(DataTransferConfig, __self__).__init__(
            'gcp:bigquery/dataTransferConfig:DataTransferConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            data_refresh_window_days: Optional[pulumi.Input[float]] = None,
            data_source_id: Optional[pulumi.Input[str]] = None,
            destination_dataset_id: Optional[pulumi.Input[str]] = None,
            disabled: Optional[pulumi.Input[bool]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            params: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            project: Optional[pulumi.Input[str]] = None,
            schedule: Optional[pulumi.Input[str]] = None,
            service_account_name: Optional[pulumi.Input[str]] = None) -> 'DataTransferConfig':
        """
        Get an existing DataTransferConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] data_refresh_window_days: The number of days to look back to automatically refresh the data.
               For example, if dataRefreshWindowDays = 10, then every day BigQuery
               reingests data for [today-10, today-1], rather than ingesting data for
               just [today-1]. Only valid if the data source supports the feature.
               Set the value to 0 to use the default value.
        :param pulumi.Input[str] data_source_id: The data source id. Cannot be changed once the transfer config is created.
        :param pulumi.Input[str] destination_dataset_id: The BigQuery target dataset id.
        :param pulumi.Input[bool] disabled: When set to true, no runs are scheduled for a given transfer.
        :param pulumi.Input[str] display_name: The user specified display name for the transfer config.
        :param pulumi.Input[str] location: The geographic location where the transfer config should reside.
               Examples: US, EU, asia-northeast1. The default value is US.
        :param pulumi.Input[str] name: The resource name of the transfer config. Transfer config names have the form
               projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
               required. The name is ignored when creating a transfer config.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] params: These parameters are specific to each data source.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] schedule: Data transfer schedule. If the data source does not support a custom
               schedule, this should be empty. If it is empty, the default value for
               the data source will be used. The specified times are in UTC. Examples
               of valid format: 1st,3rd monday of month 15:30, every wed,fri of jan,
               jun 13:15, and first sunday of quarter 00:00. See more explanation
               about the format here:
               https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
               NOTE: the granularity should be at least 8 hours, or less frequent.
        :param pulumi.Input[str] service_account_name: Optional service account name. If this field is set, transfer config will
               be created with this service account credentials. It requires that
               requesting user calling this API has permissions to act as this service account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["data_refresh_window_days"] = data_refresh_window_days
        __props__["data_source_id"] = data_source_id
        __props__["destination_dataset_id"] = destination_dataset_id
        __props__["disabled"] = disabled
        __props__["display_name"] = display_name
        __props__["location"] = location
        __props__["name"] = name
        __props__["params"] = params
        __props__["project"] = project
        __props__["schedule"] = schedule
        __props__["service_account_name"] = service_account_name
        return DataTransferConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataRefreshWindowDays")
    def data_refresh_window_days(self) -> pulumi.Output[Optional[float]]:
        """
        The number of days to look back to automatically refresh the data.
        For example, if dataRefreshWindowDays = 10, then every day BigQuery
        reingests data for [today-10, today-1], rather than ingesting data for
        just [today-1]. Only valid if the data source supports the feature.
        Set the value to 0 to use the default value.
        """
        return pulumi.get(self, "data_refresh_window_days")

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Output[str]:
        """
        The data source id. Cannot be changed once the transfer config is created.
        """
        return pulumi.get(self, "data_source_id")

    @property
    @pulumi.getter(name="destinationDatasetId")
    def destination_dataset_id(self) -> pulumi.Output[str]:
        """
        The BigQuery target dataset id.
        """
        return pulumi.get(self, "destination_dataset_id")

    @property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[bool]]:
        """
        When set to true, no runs are scheduled for a given transfer.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The user specified display name for the transfer config.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The geographic location where the transfer config should reside.
        Examples: US, EU, asia-northeast1. The default value is US.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the transfer config. Transfer config names have the form
        projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
        required. The name is ignored when creating a transfer config.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def params(self) -> pulumi.Output[Mapping[str, str]]:
        """
        These parameters are specific to each data source.
        """
        return pulumi.get(self, "params")

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
    def schedule(self) -> pulumi.Output[Optional[str]]:
        """
        Data transfer schedule. If the data source does not support a custom
        schedule, this should be empty. If it is empty, the default value for
        the data source will be used. The specified times are in UTC. Examples
        of valid format: 1st,3rd monday of month 15:30, every wed,fri of jan,
        jun 13:15, and first sunday of quarter 00:00. See more explanation
        about the format here:
        https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
        NOTE: the granularity should be at least 8 hours, or less frequent.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> pulumi.Output[Optional[str]]:
        """
        Optional service account name. If this field is set, transfer config will
        be created with this service account credentials. It requires that
        requesting user calling this API has permissions to act as this service account.
        """
        return pulumi.get(self, "service_account_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

