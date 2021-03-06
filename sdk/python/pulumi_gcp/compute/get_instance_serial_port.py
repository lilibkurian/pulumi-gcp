# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetInstanceSerialPortResult',
    'AwaitableGetInstanceSerialPortResult',
    'get_instance_serial_port',
]

@pulumi.output_type
class GetInstanceSerialPortResult:
    """
    A collection of values returned by getInstanceSerialPort.
    """
    def __init__(__self__, contents=None, id=None, instance=None, port=None, project=None, zone=None):
        if contents and not isinstance(contents, str):
            raise TypeError("Expected argument 'contents' to be a str")
        pulumi.set(__self__, "contents", contents)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance and not isinstance(instance, str):
            raise TypeError("Expected argument 'instance' to be a str")
        pulumi.set(__self__, "instance", instance)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def contents(self) -> str:
        """
        The output of the serial port. Serial port output is available only when the VM instance is running, and logs are limited to the most recent 1 MB of output per port.
        """
        return pulumi.get(self, "contents")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def instance(self) -> str:
        return pulumi.get(self, "instance")

    @property
    @pulumi.getter
    def port(self) -> int:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def zone(self) -> str:
        return pulumi.get(self, "zone")


class AwaitableGetInstanceSerialPortResult(GetInstanceSerialPortResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceSerialPortResult(
            contents=self.contents,
            id=self.id,
            instance=self.instance,
            port=self.port,
            project=self.project,
            zone=self.zone)


def get_instance_serial_port(instance: Optional[str] = None,
                             port: Optional[int] = None,
                             project: Optional[str] = None,
                             zone: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceSerialPortResult:
    """
    Get the serial port output from a Compute Instance. For more information see
    the official [API](https://cloud.google.com/compute/docs/instances/viewing-serial-port-output) documentation.


    :param str instance: The name of the Compute Instance to read output from.
    :param int port: The number of the serial port to read output from. Possible values are 1-4.
    :param str project: The project in which the Compute Instance exists. If it
           is not provided, the provider project is used.
    :param str zone: The zone in which the Compute Instance exists.
           If it is not provided, the provider zone is used.
    """
    __args__ = dict()
    __args__['instance'] = instance
    __args__['port'] = port
    __args__['project'] = project
    __args__['zone'] = zone
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:compute/getInstanceSerialPort:getInstanceSerialPort', __args__, opts=opts, typ=GetInstanceSerialPortResult).value

    return AwaitableGetInstanceSerialPortResult(
        contents=__ret__.contents,
        id=__ret__.id,
        instance=__ret__.instance,
        port=__ret__.port,
        project=__ret__.project,
        zone=__ret__.zone)
