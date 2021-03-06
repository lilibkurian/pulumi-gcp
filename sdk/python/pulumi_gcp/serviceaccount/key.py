# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Key']


class Key(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_algorithm: Optional[pulumi.Input[str]] = None,
                 private_key_type: Optional[pulumi.Input[str]] = None,
                 public_key_data: Optional[pulumi.Input[str]] = None,
                 public_key_type: Optional[pulumi.Input[str]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates and manages service account key-pairs, which allow the user to establish identity of a service account outside of GCP. For more information, see [the official documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and [API](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys).

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_algorithm: The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
               Valid values are listed at
               [ServiceAccountPrivateKeyType](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)
               (only used on create)
        :param pulumi.Input[str] private_key_type: The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.
        :param pulumi.Input[str] public_key_data: Public key data to create a service account key for given service account. The expected format for this field is a base64 encoded X509_PEM and it conflicts with `public_key_type` and `private_key_type`.
        :param pulumi.Input[str] public_key_type: The output format of the public key requested. TYPE_X509_PEM_FILE is the default output format.
        :param pulumi.Input[str] service_account_id: The Service account id of the Key Pair. This can be a string in the format
               `{ACCOUNT}` or `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`, where `{ACCOUNT}` is the email address or
               unique id of the service account. If the `{ACCOUNT}` syntax is used, the project will be inferred from the account.
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

            __props__['key_algorithm'] = key_algorithm
            __props__['private_key_type'] = private_key_type
            __props__['public_key_data'] = public_key_data
            __props__['public_key_type'] = public_key_type
            if service_account_id is None:
                raise TypeError("Missing required property 'service_account_id'")
            __props__['service_account_id'] = service_account_id
            __props__['name'] = None
            __props__['private_key'] = None
            __props__['public_key'] = None
            __props__['valid_after'] = None
            __props__['valid_before'] = None
        super(Key, __self__).__init__(
            'gcp:serviceAccount/key:Key',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            key_algorithm: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            private_key_type: Optional[pulumi.Input[str]] = None,
            public_key: Optional[pulumi.Input[str]] = None,
            public_key_data: Optional[pulumi.Input[str]] = None,
            public_key_type: Optional[pulumi.Input[str]] = None,
            service_account_id: Optional[pulumi.Input[str]] = None,
            valid_after: Optional[pulumi.Input[str]] = None,
            valid_before: Optional[pulumi.Input[str]] = None) -> 'Key':
        """
        Get an existing Key resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_algorithm: The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
               Valid values are listed at
               [ServiceAccountPrivateKeyType](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)
               (only used on create)
        :param pulumi.Input[str] name: The name used for this key pair
        :param pulumi.Input[str] private_key: The private key in JSON format, base64 encoded. This is what you normally get as a file when creating
               service account keys through the CLI or web console. This is only populated when creating a new key.
        :param pulumi.Input[str] private_key_type: The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.
        :param pulumi.Input[str] public_key: The public key, base64 encoded
        :param pulumi.Input[str] public_key_data: Public key data to create a service account key for given service account. The expected format for this field is a base64 encoded X509_PEM and it conflicts with `public_key_type` and `private_key_type`.
        :param pulumi.Input[str] public_key_type: The output format of the public key requested. TYPE_X509_PEM_FILE is the default output format.
        :param pulumi.Input[str] service_account_id: The Service account id of the Key Pair. This can be a string in the format
               `{ACCOUNT}` or `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`, where `{ACCOUNT}` is the email address or
               unique id of the service account. If the `{ACCOUNT}` syntax is used, the project will be inferred from the account.
        :param pulumi.Input[str] valid_after: The key can be used after this timestamp. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        :param pulumi.Input[str] valid_before: The key can be used before this timestamp.
               A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["key_algorithm"] = key_algorithm
        __props__["name"] = name
        __props__["private_key"] = private_key
        __props__["private_key_type"] = private_key_type
        __props__["public_key"] = public_key
        __props__["public_key_data"] = public_key_data
        __props__["public_key_type"] = public_key_type
        __props__["service_account_id"] = service_account_id
        __props__["valid_after"] = valid_after
        __props__["valid_before"] = valid_before
        return Key(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> pulumi.Output[Optional[str]]:
        """
        The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
        Valid values are listed at
        [ServiceAccountPrivateKeyType](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)
        (only used on create)
        """
        return pulumi.get(self, "key_algorithm")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name used for this key pair
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[str]:
        """
        The private key in JSON format, base64 encoded. This is what you normally get as a file when creating
        service account keys through the CLI or web console. This is only populated when creating a new key.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="privateKeyType")
    def private_key_type(self) -> pulumi.Output[Optional[str]]:
        """
        The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.
        """
        return pulumi.get(self, "private_key_type")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[str]:
        """
        The public key, base64 encoded
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter(name="publicKeyData")
    def public_key_data(self) -> pulumi.Output[Optional[str]]:
        """
        Public key data to create a service account key for given service account. The expected format for this field is a base64 encoded X509_PEM and it conflicts with `public_key_type` and `private_key_type`.
        """
        return pulumi.get(self, "public_key_data")

    @property
    @pulumi.getter(name="publicKeyType")
    def public_key_type(self) -> pulumi.Output[Optional[str]]:
        """
        The output format of the public key requested. TYPE_X509_PEM_FILE is the default output format.
        """
        return pulumi.get(self, "public_key_type")

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Output[str]:
        """
        The Service account id of the Key Pair. This can be a string in the format
        `{ACCOUNT}` or `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`, where `{ACCOUNT}` is the email address or
        unique id of the service account. If the `{ACCOUNT}` syntax is used, the project will be inferred from the account.
        """
        return pulumi.get(self, "service_account_id")

    @property
    @pulumi.getter(name="validAfter")
    def valid_after(self) -> pulumi.Output[str]:
        """
        The key can be used after this timestamp. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "valid_after")

    @property
    @pulumi.getter(name="validBefore")
    def valid_before(self) -> pulumi.Output[str]:
        """
        The key can be used before this timestamp.
        A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "valid_before")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

