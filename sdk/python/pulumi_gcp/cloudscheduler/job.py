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

__all__ = ['Job']


class Job(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_engine_http_target: Optional[pulumi.Input[pulumi.InputType['JobAppEngineHttpTargetArgs']]] = None,
                 attempt_deadline: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 http_target: Optional[pulumi.Input[pulumi.InputType['JobHttpTargetArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 pubsub_target: Optional[pulumi.Input[pulumi.InputType['JobPubsubTargetArgs']]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 retry_config: Optional[pulumi.Input[pulumi.InputType['JobRetryConfigArgs']]] = None,
                 schedule: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A scheduled job that can publish a pubsub message or a http request
        every X interval of time, using crontab format string.

        To use Cloud Scheduler your project must contain an App Engine app
        that is located in one of the supported regions. If your project
        does not have an App Engine app, you must create one.

        To get more information about Job, see:

        * [API documentation](https://cloud.google.com/scheduler/docs/reference/rest/)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/scheduler/)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['JobAppEngineHttpTargetArgs']] app_engine_http_target: App Engine HTTP target.
               If the job providers a App Engine HTTP target the cron will
               send a request to the service instance
               Structure is documented below.
        :param pulumi.Input[str] attempt_deadline: The deadline for job attempts. If the request handler does not respond by this deadline then the request is
               cancelled and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in
               execution logs. Cloud Scheduler will retry the job according to the RetryConfig.
               The allowed duration for this deadline is:
               * For HTTP targets, between 15 seconds and 30 minutes.
               * For App Engine HTTP targets, between 15 seconds and 24 hours.
               A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
        :param pulumi.Input[str] description: A human-readable description for the job.
               This string must not contain more than 500 characters.
        :param pulumi.Input[pulumi.InputType['JobHttpTargetArgs']] http_target: HTTP target.
               If the job providers a http_target the cron will
               send a request to the targeted url
               Structure is documented below.
        :param pulumi.Input[str] name: The name of the job.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['JobPubsubTargetArgs']] pubsub_target: Pub/Sub target
               If the job providers a Pub/Sub target the cron will publish
               a message to the provided topic
               Structure is documented below.
        :param pulumi.Input[str] region: Region where the scheduler job resides. If it is not provided, Terraform will use the provider default.
        :param pulumi.Input[pulumi.InputType['JobRetryConfigArgs']] retry_config: By default, if a job does not complete successfully,
               meaning that an acknowledgement is not received from the handler,
               then it will be retried with exponential backoff according to the settings
               Structure is documented below.
        :param pulumi.Input[str] schedule: Describes the schedule on which the job will be executed.
        :param pulumi.Input[str] time_zone: Specifies the time zone to be used in interpreting schedule.
               The value of this field must be a time zone name from the tz database.
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

            __props__['app_engine_http_target'] = app_engine_http_target
            __props__['attempt_deadline'] = attempt_deadline
            __props__['description'] = description
            __props__['http_target'] = http_target
            __props__['name'] = name
            __props__['project'] = project
            __props__['pubsub_target'] = pubsub_target
            __props__['region'] = region
            __props__['retry_config'] = retry_config
            __props__['schedule'] = schedule
            __props__['time_zone'] = time_zone
        super(Job, __self__).__init__(
            'gcp:cloudscheduler/job:Job',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_engine_http_target: Optional[pulumi.Input[pulumi.InputType['JobAppEngineHttpTargetArgs']]] = None,
            attempt_deadline: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            http_target: Optional[pulumi.Input[pulumi.InputType['JobHttpTargetArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            pubsub_target: Optional[pulumi.Input[pulumi.InputType['JobPubsubTargetArgs']]] = None,
            region: Optional[pulumi.Input[str]] = None,
            retry_config: Optional[pulumi.Input[pulumi.InputType['JobRetryConfigArgs']]] = None,
            schedule: Optional[pulumi.Input[str]] = None,
            time_zone: Optional[pulumi.Input[str]] = None) -> 'Job':
        """
        Get an existing Job resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['JobAppEngineHttpTargetArgs']] app_engine_http_target: App Engine HTTP target.
               If the job providers a App Engine HTTP target the cron will
               send a request to the service instance
               Structure is documented below.
        :param pulumi.Input[str] attempt_deadline: The deadline for job attempts. If the request handler does not respond by this deadline then the request is
               cancelled and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in
               execution logs. Cloud Scheduler will retry the job according to the RetryConfig.
               The allowed duration for this deadline is:
               * For HTTP targets, between 15 seconds and 30 minutes.
               * For App Engine HTTP targets, between 15 seconds and 24 hours.
               A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
        :param pulumi.Input[str] description: A human-readable description for the job.
               This string must not contain more than 500 characters.
        :param pulumi.Input[pulumi.InputType['JobHttpTargetArgs']] http_target: HTTP target.
               If the job providers a http_target the cron will
               send a request to the targeted url
               Structure is documented below.
        :param pulumi.Input[str] name: The name of the job.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['JobPubsubTargetArgs']] pubsub_target: Pub/Sub target
               If the job providers a Pub/Sub target the cron will publish
               a message to the provided topic
               Structure is documented below.
        :param pulumi.Input[str] region: Region where the scheduler job resides. If it is not provided, Terraform will use the provider default.
        :param pulumi.Input[pulumi.InputType['JobRetryConfigArgs']] retry_config: By default, if a job does not complete successfully,
               meaning that an acknowledgement is not received from the handler,
               then it will be retried with exponential backoff according to the settings
               Structure is documented below.
        :param pulumi.Input[str] schedule: Describes the schedule on which the job will be executed.
        :param pulumi.Input[str] time_zone: Specifies the time zone to be used in interpreting schedule.
               The value of this field must be a time zone name from the tz database.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["app_engine_http_target"] = app_engine_http_target
        __props__["attempt_deadline"] = attempt_deadline
        __props__["description"] = description
        __props__["http_target"] = http_target
        __props__["name"] = name
        __props__["project"] = project
        __props__["pubsub_target"] = pubsub_target
        __props__["region"] = region
        __props__["retry_config"] = retry_config
        __props__["schedule"] = schedule
        __props__["time_zone"] = time_zone
        return Job(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appEngineHttpTarget")
    def app_engine_http_target(self) -> pulumi.Output[Optional['outputs.JobAppEngineHttpTarget']]:
        """
        App Engine HTTP target.
        If the job providers a App Engine HTTP target the cron will
        send a request to the service instance
        Structure is documented below.
        """
        return pulumi.get(self, "app_engine_http_target")

    @property
    @pulumi.getter(name="attemptDeadline")
    def attempt_deadline(self) -> pulumi.Output[Optional[str]]:
        """
        The deadline for job attempts. If the request handler does not respond by this deadline then the request is
        cancelled and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in
        execution logs. Cloud Scheduler will retry the job according to the RetryConfig.
        The allowed duration for this deadline is:
        * For HTTP targets, between 15 seconds and 30 minutes.
        * For App Engine HTTP targets, between 15 seconds and 24 hours.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
        """
        return pulumi.get(self, "attempt_deadline")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A human-readable description for the job.
        This string must not contain more than 500 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="httpTarget")
    def http_target(self) -> pulumi.Output[Optional['outputs.JobHttpTarget']]:
        """
        HTTP target.
        If the job providers a http_target the cron will
        send a request to the targeted url
        Structure is documented below.
        """
        return pulumi.get(self, "http_target")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the job.
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
    @pulumi.getter(name="pubsubTarget")
    def pubsub_target(self) -> pulumi.Output[Optional['outputs.JobPubsubTarget']]:
        """
        Pub/Sub target
        If the job providers a Pub/Sub target the cron will publish
        a message to the provided topic
        Structure is documented below.
        """
        return pulumi.get(self, "pubsub_target")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Region where the scheduler job resides. If it is not provided, Terraform will use the provider default.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="retryConfig")
    def retry_config(self) -> pulumi.Output[Optional['outputs.JobRetryConfig']]:
        """
        By default, if a job does not complete successfully,
        meaning that an acknowledgement is not received from the handler,
        then it will be retried with exponential backoff according to the settings
        Structure is documented below.
        """
        return pulumi.get(self, "retry_config")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[str]]:
        """
        Describes the schedule on which the job will be executed.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the time zone to be used in interpreting schedule.
        The value of this field must be a time zone name from the tz database.
        """
        return pulumi.get(self, "time_zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

