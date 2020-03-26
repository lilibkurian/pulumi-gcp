# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Attestor(pulumi.CustomResource):
    attestation_authority_note: pulumi.Output[dict]
    """
    A Container Analysis ATTESTATION_AUTHORITY Note, created by the user.

      * `delegationServiceAccountEmail` (`str`)
      * `noteReference` (`str`)
      * `publicKeys` (`list`)
        * `asciiArmoredPgpPublicKey` (`str`)
        * `comment` (`str`)
        * `id` (`str`) - an identifier for the resource with format `projects/{{project}}/attestors/{{name}}`
        * `pkixPublicKey` (`dict`)
          * `publicKeyPem` (`str`)
          * `signatureAlgorithm` (`str`)
    """
    description: pulumi.Output[str]
    """
    A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs.
    """
    name: pulumi.Output[str]
    """
    The resource name.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    def __init__(__self__, resource_name, opts=None, attestation_authority_note=None, description=None, name=None, project=None, __props__=None, __name__=None, __opts__=None):
        """
        An attestor that attests to container image artifacts.


        To get more information about Attestor, see:

        * [API documentation](https://cloud.google.com/binary-authorization/docs/reference/rest/)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/binary-authorization/)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/binary_authorization_attestor.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] attestation_authority_note: A Container Analysis ATTESTATION_AUTHORITY Note, created by the user.
        :param pulumi.Input[str] description: A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs.
        :param pulumi.Input[str] name: The resource name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.

        The **attestation_authority_note** object supports the following:

          * `delegationServiceAccountEmail` (`pulumi.Input[str]`)
          * `noteReference` (`pulumi.Input[str]`)
          * `publicKeys` (`pulumi.Input[list]`)
            * `asciiArmoredPgpPublicKey` (`pulumi.Input[str]`)
            * `comment` (`pulumi.Input[str]`)
            * `id` (`pulumi.Input[str]`) - an identifier for the resource with format `projects/{{project}}/attestors/{{name}}`
            * `pkixPublicKey` (`pulumi.Input[dict]`)
              * `publicKeyPem` (`pulumi.Input[str]`)
              * `signatureAlgorithm` (`pulumi.Input[str]`)
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

            if attestation_authority_note is None:
                raise TypeError("Missing required property 'attestation_authority_note'")
            __props__['attestation_authority_note'] = attestation_authority_note
            __props__['description'] = description
            __props__['name'] = name
            __props__['project'] = project
        super(Attestor, __self__).__init__(
            'gcp:binaryauthorization/attestor:Attestor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, attestation_authority_note=None, description=None, name=None, project=None):
        """
        Get an existing Attestor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] attestation_authority_note: A Container Analysis ATTESTATION_AUTHORITY Note, created by the user.
        :param pulumi.Input[str] description: A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs.
        :param pulumi.Input[str] name: The resource name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.

        The **attestation_authority_note** object supports the following:

          * `delegationServiceAccountEmail` (`pulumi.Input[str]`)
          * `noteReference` (`pulumi.Input[str]`)
          * `publicKeys` (`pulumi.Input[list]`)
            * `asciiArmoredPgpPublicKey` (`pulumi.Input[str]`)
            * `comment` (`pulumi.Input[str]`)
            * `id` (`pulumi.Input[str]`) - an identifier for the resource with format `projects/{{project}}/attestors/{{name}}`
            * `pkixPublicKey` (`pulumi.Input[dict]`)
              * `publicKeyPem` (`pulumi.Input[str]`)
              * `signatureAlgorithm` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["attestation_authority_note"] = attestation_authority_note
        __props__["description"] = description
        __props__["name"] = name
        __props__["project"] = project
        return Attestor(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

