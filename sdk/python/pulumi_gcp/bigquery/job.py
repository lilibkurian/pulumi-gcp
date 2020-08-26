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
                 copy: Optional[pulumi.Input[pulumi.InputType['JobCopyArgs']]] = None,
                 extract: Optional[pulumi.Input[pulumi.InputType['JobExtractArgs']]] = None,
                 job_id: Optional[pulumi.Input[str]] = None,
                 job_timeout_ms: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 load: Optional[pulumi.Input[pulumi.InputType['JobLoadArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 query: Optional[pulumi.Input[pulumi.InputType['JobQueryArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Jobs are actions that BigQuery runs on your behalf to load data, export data, query data, or copy data.
        Once a BigQuery job is created, it cannot be changed or deleted.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['JobCopyArgs']] copy: Copies a table.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['JobExtractArgs']] extract: Configures an extract job.
               Structure is documented below.
        :param pulumi.Input[str] job_id: The ID of the job. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). The maximum length is 1,024 characters.
        :param pulumi.Input[str] job_timeout_ms: Job timeout in milliseconds. If this time limit is exceeded, BigQuery may attempt to terminate the job.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels associated with this job. You can use these to organize and group your jobs.
        :param pulumi.Input[pulumi.InputType['JobLoadArgs']] load: Configures a load job.
               Structure is documented below.
        :param pulumi.Input[str] location: The geographic location of the job. The default value is US.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['JobQueryArgs']] query: Configures a query job.
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

            __props__['copy'] = copy
            __props__['extract'] = extract
            if job_id is None:
                raise TypeError("Missing required property 'job_id'")
            __props__['job_id'] = job_id
            __props__['job_timeout_ms'] = job_timeout_ms
            __props__['labels'] = labels
            __props__['load'] = load
            __props__['location'] = location
            __props__['project'] = project
            __props__['query'] = query
            __props__['job_type'] = None
            __props__['user_email'] = None
        super(Job, __self__).__init__(
            'gcp:bigquery/job:Job',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            copy: Optional[pulumi.Input[pulumi.InputType['JobCopyArgs']]] = None,
            extract: Optional[pulumi.Input[pulumi.InputType['JobExtractArgs']]] = None,
            job_id: Optional[pulumi.Input[str]] = None,
            job_timeout_ms: Optional[pulumi.Input[str]] = None,
            job_type: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            load: Optional[pulumi.Input[pulumi.InputType['JobLoadArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            query: Optional[pulumi.Input[pulumi.InputType['JobQueryArgs']]] = None,
            user_email: Optional[pulumi.Input[str]] = None) -> 'Job':
        """
        Get an existing Job resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['JobCopyArgs']] copy: Copies a table.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['JobExtractArgs']] extract: Configures an extract job.
               Structure is documented below.
        :param pulumi.Input[str] job_id: The ID of the job. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). The maximum length is 1,024 characters.
        :param pulumi.Input[str] job_timeout_ms: Job timeout in milliseconds. If this time limit is exceeded, BigQuery may attempt to terminate the job.
        :param pulumi.Input[str] job_type: The type of the job.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels associated with this job. You can use these to organize and group your jobs.
        :param pulumi.Input[pulumi.InputType['JobLoadArgs']] load: Configures a load job.
               Structure is documented below.
        :param pulumi.Input[str] location: The geographic location of the job. The default value is US.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['JobQueryArgs']] query: Configures a query job.
               Structure is documented below.
        :param pulumi.Input[str] user_email: Email address of the user who ran the job.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["copy"] = copy
        __props__["extract"] = extract
        __props__["job_id"] = job_id
        __props__["job_timeout_ms"] = job_timeout_ms
        __props__["job_type"] = job_type
        __props__["labels"] = labels
        __props__["load"] = load
        __props__["location"] = location
        __props__["project"] = project
        __props__["query"] = query
        __props__["user_email"] = user_email
        return Job(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def copy(self) -> pulumi.Output[Optional['outputs.JobCopy']]:
        """
        Copies a table.
        Structure is documented below.
        """
        return pulumi.get(self, "copy")

    @property
    @pulumi.getter
    def extract(self) -> pulumi.Output[Optional['outputs.JobExtract']]:
        """
        Configures an extract job.
        Structure is documented below.
        """
        return pulumi.get(self, "extract")

    @property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Output[str]:
        """
        The ID of the job. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). The maximum length is 1,024 characters.
        """
        return pulumi.get(self, "job_id")

    @property
    @pulumi.getter(name="jobTimeoutMs")
    def job_timeout_ms(self) -> pulumi.Output[Optional[str]]:
        """
        Job timeout in milliseconds. If this time limit is exceeded, BigQuery may attempt to terminate the job.
        """
        return pulumi.get(self, "job_timeout_ms")

    @property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Output[str]:
        """
        The type of the job.
        """
        return pulumi.get(self, "job_type")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The labels associated with this job. You can use these to organize and group your jobs.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def load(self) -> pulumi.Output[Optional['outputs.JobLoad']]:
        """
        Configures a load job.
        Structure is documented below.
        """
        return pulumi.get(self, "load")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The geographic location of the job. The default value is US.
        """
        return pulumi.get(self, "location")

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
    def query(self) -> pulumi.Output[Optional['outputs.JobQuery']]:
        """
        Configures a query job.
        Structure is documented below.
        """
        return pulumi.get(self, "query")

    @property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> pulumi.Output[str]:
        """
        Email address of the user who ran the job.
        """
        return pulumi.get(self, "user_email")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

