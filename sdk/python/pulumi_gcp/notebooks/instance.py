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

__all__ = ['Instance']


class Instance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_config: Optional[pulumi.Input[pulumi.InputType['InstanceAcceleratorConfigArgs']]] = None,
                 boot_disk_size_gb: Optional[pulumi.Input[float]] = None,
                 boot_disk_type: Optional[pulumi.Input[str]] = None,
                 container_image: Optional[pulumi.Input[pulumi.InputType['InstanceContainerImageArgs']]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 custom_gpu_driver_path: Optional[pulumi.Input[str]] = None,
                 data_disk_size_gb: Optional[pulumi.Input[float]] = None,
                 data_disk_type: Optional[pulumi.Input[str]] = None,
                 disk_encryption: Optional[pulumi.Input[str]] = None,
                 install_gpu_driver: Optional[pulumi.Input[bool]] = None,
                 instance_owners: Optional[pulumi.Input[str]] = None,
                 kms_key: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 machine_type: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 no_proxy_access: Optional[pulumi.Input[bool]] = None,
                 no_public_ip: Optional[pulumi.Input[bool]] = None,
                 no_remove_data_disk: Optional[pulumi.Input[bool]] = None,
                 post_startup_script: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_account: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 vm_image: Optional[pulumi.Input[pulumi.InputType['InstanceVmImageArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A Cloud AI Platform Notebook instance.

        > **Note:** Due to limitations of the Notebooks Instance API, many fields
        in this resource do not properly detect drift. These fields will also not
        appear in state once imported.

        To get more information about Instance, see:

        * [API documentation](https://cloud.google.com/ai-platform/notebooks/docs/reference/rest)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/ai-platform-notebooks)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['InstanceAcceleratorConfigArgs']] accelerator_config: The hardware accelerator used on this instance. If you use accelerators,
               make sure that your configuration has enough vCPUs and memory to support the
               machineType you have selected.
               Structure is documented below.
        :param pulumi.Input[float] boot_disk_size_gb: The size of the boot disk in GB attached to this instance,
               up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB.
               If not specified, this defaults to 100.
        :param pulumi.Input[str] boot_disk_type: Possible disk types for notebook instances.
               Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
        :param pulumi.Input[pulumi.InputType['InstanceContainerImageArgs']] container_image: Use a container image to start the notebook instance.
               Structure is documented below.
        :param pulumi.Input[str] create_time: Instance creation time
        :param pulumi.Input[str] custom_gpu_driver_path: Specify a custom Cloud Storage path where the GPU driver is stored.
               If not specified, we'll automatically choose from official GPU drivers.
        :param pulumi.Input[float] data_disk_size_gb: The size of the data disk in GB attached to this instance,
               up to a maximum of 64000 GB (64 TB).
               You can choose the size of the data disk based on how big your notebooks and data are.
               If not specified, this defaults to 100.
        :param pulumi.Input[str] data_disk_type: Possible disk types for notebook instances.
               Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
        :param pulumi.Input[str] disk_encryption: Disk encryption method used on the boot and data disks, defaults to GMEK.
               Possible values are `DISK_ENCRYPTION_UNSPECIFIED`, `GMEK`, and `CMEK`.
        :param pulumi.Input[bool] install_gpu_driver: Whether the end user authorizes Google Cloud to install GPU driver
               on this instance. If this field is empty or set to false, the GPU driver
               won't be installed. Only applicable to instances with GPUs.
        :param pulumi.Input[str] instance_owners: The list of owners of this instance after creation.
               Format: alias@example.com.
               Currently supports one owner only.
               If not specified, all of the service account users of
               your VM instance's service account can use the instance.
        :param pulumi.Input[str] kms_key: The KMS key used to encrypt the disks, only applicable if diskEncryption is CMEK.
               Format: projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels to apply to this instance. These can be later modified by the setLabels method.
               An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] location: A reference to the zone where the machine resides.
        :param pulumi.Input[str] machine_type: A reference to a machine type which defines VM kind.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Custom metadata to apply to this instance.
               An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] name: The name specified for the Notebook instance.
        :param pulumi.Input[str] network: The name of the VPC that this instance is in.
               Format: projects/{project_id}/global/networks/{network_id}
        :param pulumi.Input[bool] no_proxy_access: the notebook instance will not register with the proxy..
        :param pulumi.Input[bool] no_public_ip: no public IP will be assigned to this instance.
        :param pulumi.Input[bool] no_remove_data_disk: If true, the data disk will not be auto deleted when deleting the instance.
        :param pulumi.Input[str] post_startup_script: Path to a Bash script that automatically runs after a
               notebook instance fully boots up. The path must be a URL
               or Cloud Storage path (gs://path-to-file/file-name).
        :param pulumi.Input[str] project: The name of the Google Cloud project that this VM image belongs to.
               Format: projects/{project_id}
        :param pulumi.Input[str] service_account: The service account on this instance, giving access to other
               Google Cloud services. You can use any service account within
               the same project, but you must have the service account user
               permission to use the instance. If not specified,
               the Compute Engine default service account is used.
        :param pulumi.Input[str] subnet: The name of the subnet that this instance is in.
               Format: projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}
        :param pulumi.Input[str] update_time: Instance update time.
        :param pulumi.Input[pulumi.InputType['InstanceVmImageArgs']] vm_image: Use a Compute Engine VM image to start the notebook instance.
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

            __props__['accelerator_config'] = accelerator_config
            __props__['boot_disk_size_gb'] = boot_disk_size_gb
            __props__['boot_disk_type'] = boot_disk_type
            __props__['container_image'] = container_image
            __props__['create_time'] = create_time
            __props__['custom_gpu_driver_path'] = custom_gpu_driver_path
            __props__['data_disk_size_gb'] = data_disk_size_gb
            __props__['data_disk_type'] = data_disk_type
            __props__['disk_encryption'] = disk_encryption
            __props__['install_gpu_driver'] = install_gpu_driver
            __props__['instance_owners'] = instance_owners
            __props__['kms_key'] = kms_key
            __props__['labels'] = labels
            if location is None:
                raise TypeError("Missing required property 'location'")
            __props__['location'] = location
            if machine_type is None:
                raise TypeError("Missing required property 'machine_type'")
            __props__['machine_type'] = machine_type
            __props__['metadata'] = metadata
            __props__['name'] = name
            __props__['network'] = network
            __props__['no_proxy_access'] = no_proxy_access
            __props__['no_public_ip'] = no_public_ip
            __props__['no_remove_data_disk'] = no_remove_data_disk
            __props__['post_startup_script'] = post_startup_script
            __props__['project'] = project
            __props__['service_account'] = service_account
            __props__['subnet'] = subnet
            __props__['update_time'] = update_time
            __props__['vm_image'] = vm_image
            __props__['proxy_uri'] = None
            __props__['state'] = None
        super(Instance, __self__).__init__(
            'gcp:notebooks/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accelerator_config: Optional[pulumi.Input[pulumi.InputType['InstanceAcceleratorConfigArgs']]] = None,
            boot_disk_size_gb: Optional[pulumi.Input[float]] = None,
            boot_disk_type: Optional[pulumi.Input[str]] = None,
            container_image: Optional[pulumi.Input[pulumi.InputType['InstanceContainerImageArgs']]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            custom_gpu_driver_path: Optional[pulumi.Input[str]] = None,
            data_disk_size_gb: Optional[pulumi.Input[float]] = None,
            data_disk_type: Optional[pulumi.Input[str]] = None,
            disk_encryption: Optional[pulumi.Input[str]] = None,
            install_gpu_driver: Optional[pulumi.Input[bool]] = None,
            instance_owners: Optional[pulumi.Input[str]] = None,
            kms_key: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            machine_type: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network: Optional[pulumi.Input[str]] = None,
            no_proxy_access: Optional[pulumi.Input[bool]] = None,
            no_public_ip: Optional[pulumi.Input[bool]] = None,
            no_remove_data_disk: Optional[pulumi.Input[bool]] = None,
            post_startup_script: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            proxy_uri: Optional[pulumi.Input[str]] = None,
            service_account: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            subnet: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None,
            vm_image: Optional[pulumi.Input[pulumi.InputType['InstanceVmImageArgs']]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['InstanceAcceleratorConfigArgs']] accelerator_config: The hardware accelerator used on this instance. If you use accelerators,
               make sure that your configuration has enough vCPUs and memory to support the
               machineType you have selected.
               Structure is documented below.
        :param pulumi.Input[float] boot_disk_size_gb: The size of the boot disk in GB attached to this instance,
               up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB.
               If not specified, this defaults to 100.
        :param pulumi.Input[str] boot_disk_type: Possible disk types for notebook instances.
               Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
        :param pulumi.Input[pulumi.InputType['InstanceContainerImageArgs']] container_image: Use a container image to start the notebook instance.
               Structure is documented below.
        :param pulumi.Input[str] create_time: Instance creation time
        :param pulumi.Input[str] custom_gpu_driver_path: Specify a custom Cloud Storage path where the GPU driver is stored.
               If not specified, we'll automatically choose from official GPU drivers.
        :param pulumi.Input[float] data_disk_size_gb: The size of the data disk in GB attached to this instance,
               up to a maximum of 64000 GB (64 TB).
               You can choose the size of the data disk based on how big your notebooks and data are.
               If not specified, this defaults to 100.
        :param pulumi.Input[str] data_disk_type: Possible disk types for notebook instances.
               Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
        :param pulumi.Input[str] disk_encryption: Disk encryption method used on the boot and data disks, defaults to GMEK.
               Possible values are `DISK_ENCRYPTION_UNSPECIFIED`, `GMEK`, and `CMEK`.
        :param pulumi.Input[bool] install_gpu_driver: Whether the end user authorizes Google Cloud to install GPU driver
               on this instance. If this field is empty or set to false, the GPU driver
               won't be installed. Only applicable to instances with GPUs.
        :param pulumi.Input[str] instance_owners: The list of owners of this instance after creation.
               Format: alias@example.com.
               Currently supports one owner only.
               If not specified, all of the service account users of
               your VM instance's service account can use the instance.
        :param pulumi.Input[str] kms_key: The KMS key used to encrypt the disks, only applicable if diskEncryption is CMEK.
               Format: projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels to apply to this instance. These can be later modified by the setLabels method.
               An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] location: A reference to the zone where the machine resides.
        :param pulumi.Input[str] machine_type: A reference to a machine type which defines VM kind.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Custom metadata to apply to this instance.
               An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] name: The name specified for the Notebook instance.
        :param pulumi.Input[str] network: The name of the VPC that this instance is in.
               Format: projects/{project_id}/global/networks/{network_id}
        :param pulumi.Input[bool] no_proxy_access: the notebook instance will not register with the proxy..
        :param pulumi.Input[bool] no_public_ip: no public IP will be assigned to this instance.
        :param pulumi.Input[bool] no_remove_data_disk: If true, the data disk will not be auto deleted when deleting the instance.
        :param pulumi.Input[str] post_startup_script: Path to a Bash script that automatically runs after a
               notebook instance fully boots up. The path must be a URL
               or Cloud Storage path (gs://path-to-file/file-name).
        :param pulumi.Input[str] project: The name of the Google Cloud project that this VM image belongs to.
               Format: projects/{project_id}
        :param pulumi.Input[str] proxy_uri: The proxy endpoint that is used to access the Jupyter notebook.
        :param pulumi.Input[str] service_account: The service account on this instance, giving access to other
               Google Cloud services. You can use any service account within
               the same project, but you must have the service account user
               permission to use the instance. If not specified,
               the Compute Engine default service account is used.
        :param pulumi.Input[str] state: The state of this instance.
        :param pulumi.Input[str] subnet: The name of the subnet that this instance is in.
               Format: projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}
        :param pulumi.Input[str] update_time: Instance update time.
        :param pulumi.Input[pulumi.InputType['InstanceVmImageArgs']] vm_image: Use a Compute Engine VM image to start the notebook instance.
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["accelerator_config"] = accelerator_config
        __props__["boot_disk_size_gb"] = boot_disk_size_gb
        __props__["boot_disk_type"] = boot_disk_type
        __props__["container_image"] = container_image
        __props__["create_time"] = create_time
        __props__["custom_gpu_driver_path"] = custom_gpu_driver_path
        __props__["data_disk_size_gb"] = data_disk_size_gb
        __props__["data_disk_type"] = data_disk_type
        __props__["disk_encryption"] = disk_encryption
        __props__["install_gpu_driver"] = install_gpu_driver
        __props__["instance_owners"] = instance_owners
        __props__["kms_key"] = kms_key
        __props__["labels"] = labels
        __props__["location"] = location
        __props__["machine_type"] = machine_type
        __props__["metadata"] = metadata
        __props__["name"] = name
        __props__["network"] = network
        __props__["no_proxy_access"] = no_proxy_access
        __props__["no_public_ip"] = no_public_ip
        __props__["no_remove_data_disk"] = no_remove_data_disk
        __props__["post_startup_script"] = post_startup_script
        __props__["project"] = project
        __props__["proxy_uri"] = proxy_uri
        __props__["service_account"] = service_account
        __props__["state"] = state
        __props__["subnet"] = subnet
        __props__["update_time"] = update_time
        __props__["vm_image"] = vm_image
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceleratorConfig")
    def accelerator_config(self) -> pulumi.Output[Optional['outputs.InstanceAcceleratorConfig']]:
        """
        The hardware accelerator used on this instance. If you use accelerators,
        make sure that your configuration has enough vCPUs and memory to support the
        machineType you have selected.
        Structure is documented below.
        """
        return pulumi.get(self, "accelerator_config")

    @property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> pulumi.Output[Optional[float]]:
        """
        The size of the boot disk in GB attached to this instance,
        up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB.
        If not specified, this defaults to 100.
        """
        return pulumi.get(self, "boot_disk_size_gb")

    @property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> pulumi.Output[Optional[str]]:
        """
        Possible disk types for notebook instances.
        Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
        """
        return pulumi.get(self, "boot_disk_type")

    @property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> pulumi.Output[Optional['outputs.InstanceContainerImage']]:
        """
        Use a container image to start the notebook instance.
        Structure is documented below.
        """
        return pulumi.get(self, "container_image")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Instance creation time
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="customGpuDriverPath")
    def custom_gpu_driver_path(self) -> pulumi.Output[Optional[str]]:
        """
        Specify a custom Cloud Storage path where the GPU driver is stored.
        If not specified, we'll automatically choose from official GPU drivers.
        """
        return pulumi.get(self, "custom_gpu_driver_path")

    @property
    @pulumi.getter(name="dataDiskSizeGb")
    def data_disk_size_gb(self) -> pulumi.Output[Optional[float]]:
        """
        The size of the data disk in GB attached to this instance,
        up to a maximum of 64000 GB (64 TB).
        You can choose the size of the data disk based on how big your notebooks and data are.
        If not specified, this defaults to 100.
        """
        return pulumi.get(self, "data_disk_size_gb")

    @property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(self) -> pulumi.Output[Optional[str]]:
        """
        Possible disk types for notebook instances.
        Possible values are `DISK_TYPE_UNSPECIFIED`, `PD_STANDARD`, `PD_SSD`, and `PD_BALANCED`.
        """
        return pulumi.get(self, "data_disk_type")

    @property
    @pulumi.getter(name="diskEncryption")
    def disk_encryption(self) -> pulumi.Output[Optional[str]]:
        """
        Disk encryption method used on the boot and data disks, defaults to GMEK.
        Possible values are `DISK_ENCRYPTION_UNSPECIFIED`, `GMEK`, and `CMEK`.
        """
        return pulumi.get(self, "disk_encryption")

    @property
    @pulumi.getter(name="installGpuDriver")
    def install_gpu_driver(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the end user authorizes Google Cloud to install GPU driver
        on this instance. If this field is empty or set to false, the GPU driver
        won't be installed. Only applicable to instances with GPUs.
        """
        return pulumi.get(self, "install_gpu_driver")

    @property
    @pulumi.getter(name="instanceOwners")
    def instance_owners(self) -> pulumi.Output[Optional[str]]:
        """
        The list of owners of this instance after creation.
        Format: alias@example.com.
        Currently supports one owner only.
        If not specified, all of the service account users of
        your VM instance's service account can use the instance.
        """
        return pulumi.get(self, "instance_owners")

    @property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[Optional[str]]:
        """
        The KMS key used to encrypt the disks, only applicable if diskEncryption is CMEK.
        Format: projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}
        """
        return pulumi.get(self, "kms_key")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Labels to apply to this instance. These can be later modified by the setLabels method.
        An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        A reference to the zone where the machine resides.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Output[str]:
        """
        A reference to a machine type which defines VM kind.
        """
        return pulumi.get(self, "machine_type")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Custom metadata to apply to this instance.
        An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name specified for the Notebook instance.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        The name of the VPC that this instance is in.
        Format: projects/{project_id}/global/networks/{network_id}
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="noProxyAccess")
    def no_proxy_access(self) -> pulumi.Output[Optional[bool]]:
        """
        the notebook instance will not register with the proxy..
        """
        return pulumi.get(self, "no_proxy_access")

    @property
    @pulumi.getter(name="noPublicIp")
    def no_public_ip(self) -> pulumi.Output[Optional[bool]]:
        """
        no public IP will be assigned to this instance.
        """
        return pulumi.get(self, "no_public_ip")

    @property
    @pulumi.getter(name="noRemoveDataDisk")
    def no_remove_data_disk(self) -> pulumi.Output[Optional[bool]]:
        """
        If true, the data disk will not be auto deleted when deleting the instance.
        """
        return pulumi.get(self, "no_remove_data_disk")

    @property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> pulumi.Output[Optional[str]]:
        """
        Path to a Bash script that automatically runs after a
        notebook instance fully boots up. The path must be a URL
        or Cloud Storage path (gs://path-to-file/file-name).
        """
        return pulumi.get(self, "post_startup_script")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The name of the Google Cloud project that this VM image belongs to.
        Format: projects/{project_id}
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="proxyUri")
    def proxy_uri(self) -> pulumi.Output[str]:
        """
        The proxy endpoint that is used to access the Jupyter notebook.
        """
        return pulumi.get(self, "proxy_uri")

    @property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[str]:
        """
        The service account on this instance, giving access to other
        Google Cloud services. You can use any service account within
        the same project, but you must have the service account user
        permission to use the instance. If not specified,
        the Compute Engine default service account is used.
        """
        return pulumi.get(self, "service_account")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of this instance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[str]:
        """
        The name of the subnet that this instance is in.
        Format: projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}
        """
        return pulumi.get(self, "subnet")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Instance update time.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> pulumi.Output[Optional['outputs.InstanceVmImage']]:
        """
        Use a Compute Engine VM image to start the notebook instance.
        Structure is documented below.
        """
        return pulumi.get(self, "vm_image")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

