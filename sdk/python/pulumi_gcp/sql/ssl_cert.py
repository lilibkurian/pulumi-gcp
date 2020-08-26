# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['SslCert']


class SslCert(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 common_name: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new Google SQL SSL Cert on a Google SQL Instance. For more information, see the [official documentation](https://cloud.google.com/sql/), or the [JSON API](https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/sslCerts).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] common_name: The common name to be used in the certificate to identify the
               client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. Changing this
               forces a new resource to be created.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
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

            if common_name is None:
                raise TypeError("Missing required property 'common_name'")
            __props__['common_name'] = common_name
            if instance is None:
                raise TypeError("Missing required property 'instance'")
            __props__['instance'] = instance
            __props__['project'] = project
            __props__['cert'] = None
            __props__['cert_serial_number'] = None
            __props__['create_time'] = None
            __props__['expiration_time'] = None
            __props__['private_key'] = None
            __props__['server_ca_cert'] = None
            __props__['sha1_fingerprint'] = None
        super(SslCert, __self__).__init__(
            'gcp:sql/sslCert:SslCert',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cert: Optional[pulumi.Input[str]] = None,
            cert_serial_number: Optional[pulumi.Input[str]] = None,
            common_name: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            expiration_time: Optional[pulumi.Input[str]] = None,
            instance: Optional[pulumi.Input[str]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            server_ca_cert: Optional[pulumi.Input[str]] = None,
            sha1_fingerprint: Optional[pulumi.Input[str]] = None) -> 'SslCert':
        """
        Get an existing SslCert resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cert: The actual certificate data for this client certificate.
        :param pulumi.Input[str] cert_serial_number: The serial number extracted from the certificate data.
        :param pulumi.Input[str] common_name: The common name to be used in the certificate to identify the
               client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.
        :param pulumi.Input[str] create_time: The time when the certificate was created in RFC 3339 format,
               for example 2012-11-15T16:19:00.094Z.
        :param pulumi.Input[str] expiration_time: The time when the certificate expires in RFC 3339 format,
               for example 2012-11-15T16:19:00.094Z.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. Changing this
               forces a new resource to be created.
        :param pulumi.Input[str] private_key: The private key associated with the client certificate.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] server_ca_cert: The CA cert of the server this client cert was generated from.
        :param pulumi.Input[str] sha1_fingerprint: The SHA1 Fingerprint of the certificate.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cert"] = cert
        __props__["cert_serial_number"] = cert_serial_number
        __props__["common_name"] = common_name
        __props__["create_time"] = create_time
        __props__["expiration_time"] = expiration_time
        __props__["instance"] = instance
        __props__["private_key"] = private_key
        __props__["project"] = project
        __props__["server_ca_cert"] = server_ca_cert
        __props__["sha1_fingerprint"] = sha1_fingerprint
        return SslCert(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cert(self) -> pulumi.Output[str]:
        """
        The actual certificate data for this client certificate.
        """
        return pulumi.get(self, "cert")

    @property
    @pulumi.getter(name="certSerialNumber")
    def cert_serial_number(self) -> pulumi.Output[str]:
        """
        The serial number extracted from the certificate data.
        """
        return pulumi.get(self, "cert_serial_number")

    @property
    @pulumi.getter(name="commonName")
    def common_name(self) -> pulumi.Output[str]:
        """
        The common name to be used in the certificate to identify the
        client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "common_name")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the certificate was created in RFC 3339 format,
        for example 2012-11-15T16:19:00.094Z.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[str]:
        """
        The time when the certificate expires in RFC 3339 format,
        for example 2012-11-15T16:19:00.094Z.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Output[str]:
        """
        The name of the Cloud SQL instance. Changing this
        forces a new resource to be created.
        """
        return pulumi.get(self, "instance")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[str]:
        """
        The private key associated with the client certificate.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="serverCaCert")
    def server_ca_cert(self) -> pulumi.Output[str]:
        """
        The CA cert of the server this client cert was generated from.
        """
        return pulumi.get(self, "server_ca_cert")

    @property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> pulumi.Output[str]:
        """
        The SHA1 Fingerprint of the certificate.
        """
        return pulumi.get(self, "sha1_fingerprint")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

