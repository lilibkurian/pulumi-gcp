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

__all__ = ['TransferJob']


class TransferJob(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['TransferJobScheduleArgs']]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 transfer_spec: Optional[pulumi.Input[pulumi.InputType['TransferJobTransferSpecArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new Transfer Job in Google Cloud Storage Transfer.

        To get more information about Google Cloud Storage Transfer, see:

        * [Overview](https://cloud.google.com/storage-transfer/docs/overview)
        * [API documentation](https://cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs#TransferJob)
        * How-to Guides
            * [Configuring Access to Data Sources and Sinks](https://cloud.google.com/storage-transfer/docs/configure-access)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Unique description to identify the Transfer Job.
        :param pulumi.Input[str] project: The project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['TransferJobScheduleArgs']] schedule: Schedule specification defining when the Transfer Job should be scheduled to start, end and and what time to run. Structure documented below.
        :param pulumi.Input[str] status: Status of the job. Default: `ENABLED`. **NOTE: The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation.**
        :param pulumi.Input[pulumi.InputType['TransferJobTransferSpecArgs']] transfer_spec: Transfer specification. Structure documented below.
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

            if description is None:
                raise TypeError("Missing required property 'description'")
            __props__['description'] = description
            __props__['project'] = project
            if schedule is None:
                raise TypeError("Missing required property 'schedule'")
            __props__['schedule'] = schedule
            __props__['status'] = status
            if transfer_spec is None:
                raise TypeError("Missing required property 'transfer_spec'")
            __props__['transfer_spec'] = transfer_spec
            __props__['creation_time'] = None
            __props__['deletion_time'] = None
            __props__['last_modification_time'] = None
            __props__['name'] = None
        super(TransferJob, __self__).__init__(
            'gcp:storage/transferJob:TransferJob',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            creation_time: Optional[pulumi.Input[str]] = None,
            deletion_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            last_modification_time: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            schedule: Optional[pulumi.Input[pulumi.InputType['TransferJobScheduleArgs']]] = None,
            status: Optional[pulumi.Input[str]] = None,
            transfer_spec: Optional[pulumi.Input[pulumi.InputType['TransferJobTransferSpecArgs']]] = None) -> 'TransferJob':
        """
        Get an existing TransferJob resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] creation_time: When the Transfer Job was created.
        :param pulumi.Input[str] deletion_time: When the Transfer Job was deleted.
        :param pulumi.Input[str] description: Unique description to identify the Transfer Job.
        :param pulumi.Input[str] last_modification_time: When the Transfer Job was last modified.
        :param pulumi.Input[str] name: The name of the Transfer Job.
        :param pulumi.Input[str] project: The project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['TransferJobScheduleArgs']] schedule: Schedule specification defining when the Transfer Job should be scheduled to start, end and and what time to run. Structure documented below.
        :param pulumi.Input[str] status: Status of the job. Default: `ENABLED`. **NOTE: The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation.**
        :param pulumi.Input[pulumi.InputType['TransferJobTransferSpecArgs']] transfer_spec: Transfer specification. Structure documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["creation_time"] = creation_time
        __props__["deletion_time"] = deletion_time
        __props__["description"] = description
        __props__["last_modification_time"] = last_modification_time
        __props__["name"] = name
        __props__["project"] = project
        __props__["schedule"] = schedule
        __props__["status"] = status
        __props__["transfer_spec"] = transfer_spec
        return TransferJob(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        When the Transfer Job was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="deletionTime")
    def deletion_time(self) -> pulumi.Output[str]:
        """
        When the Transfer Job was deleted.
        """
        return pulumi.get(self, "deletion_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Unique description to identify the Transfer Job.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastModificationTime")
    def last_modification_time(self) -> pulumi.Output[str]:
        """
        When the Transfer Job was last modified.
        """
        return pulumi.get(self, "last_modification_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Transfer Job.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output['outputs.TransferJobSchedule']:
        """
        Schedule specification defining when the Transfer Job should be scheduled to start, end and and what time to run. Structure documented below.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Status of the job. Default: `ENABLED`. **NOTE: The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation.**
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="transferSpec")
    def transfer_spec(self) -> pulumi.Output['outputs.TransferJobTransferSpec']:
        """
        Transfer specification. Structure documented below.
        """
        return pulumi.get(self, "transfer_spec")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

