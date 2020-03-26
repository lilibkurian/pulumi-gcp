# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class StandardAppVersion(pulumi.CustomResource):
    delete_service_on_destroy: pulumi.Output[bool]
    """
    If set to `true`, the service will be deleted if it is the last version.    
    """
    deployment: pulumi.Output[dict]
    """
    Code and application artifacts that make up this version.

      * `files` (`list`)
        * `name` (`str`) - The identifier for this object. Format specified above.
        * `sha1Sum` (`str`)
        * `sourceUrl` (`str`)

      * `zip` (`dict`)
        * `filesCount` (`float`)
        * `sourceUrl` (`str`)
    """
    entrypoint: pulumi.Output[dict]
    """
    The entrypoint for the application.

      * `shell` (`str`)
    """
    env_variables: pulumi.Output[dict]
    """
    Environment variables available to the application.
    """
    handlers: pulumi.Output[list]
    """
    An ordered list of URL-matching patterns that should be applied to incoming requests. The first matching URL handles the
    request and other request handlers are not attempted.

      * `authFailAction` (`str`)
      * `login` (`str`)
      * `redirectHttpResponseCode` (`str`)
      * `script` (`dict`)
        * `scriptPath` (`str`)

      * `securityLevel` (`str`)
      * `staticFiles` (`dict`)
        * `applicationReadable` (`bool`)
        * `expiration` (`str`)
        * `httpHeaders` (`dict`)
        * `mimeType` (`str`)
        * `path` (`str`)
        * `requireMatchingFile` (`bool`)
        * `uploadPathRegex` (`str`)

      * `urlRegex` (`str`)
    """
    instance_class: pulumi.Output[str]
    """
    Instance class that is used to run this version. Valid values are AutomaticScaling F1, F2, F4, F4_1G (Only
    AutomaticScaling is supported at the moment)
    """
    libraries: pulumi.Output[list]
    """
    Configuration for third-party Python runtime libraries that are required by the application.

      * `name` (`str`) - The identifier for this object. Format specified above.
      * `version` (`str`)
    """
    name: pulumi.Output[str]
    """
    The identifier for this object. Format specified above.
    """
    noop_on_destroy: pulumi.Output[bool]
    """
    If set to `true`, the application version will not be deleted.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    runtime: pulumi.Output[str]
    """
    Desired runtime. Example python27.
    """
    runtime_api_version: pulumi.Output[str]
    """
    The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
    https://cloud.google.com/appengine/docs/standard//config/appref
    """
    service: pulumi.Output[str]
    """
    AppEngine service resource
    """
    threadsafe: pulumi.Output[bool]
    """
    Whether multiple requests can be dispatched to this version at once.
    """
    version_id: pulumi.Output[str]
    """
    Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
    numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
    """
    def __init__(__self__, resource_name, opts=None, delete_service_on_destroy=None, deployment=None, entrypoint=None, env_variables=None, handlers=None, instance_class=None, libraries=None, noop_on_destroy=None, project=None, runtime=None, runtime_api_version=None, service=None, threadsafe=None, version_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Standard App Version resource to create a new version of standard GAE Application.
        Currently supporting Zip and File Containers.
        Currently does not support async operation checking.


        To get more information about StandardAppVersion, see:

        * [API documentation](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/appengine/docs/admin-api/deploying-overview)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_standard_app_version.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] delete_service_on_destroy: If set to `true`, the service will be deleted if it is the last version.    
        :param pulumi.Input[dict] deployment: Code and application artifacts that make up this version.
        :param pulumi.Input[dict] entrypoint: The entrypoint for the application.
        :param pulumi.Input[dict] env_variables: Environment variables available to the application.
        :param pulumi.Input[list] handlers: An ordered list of URL-matching patterns that should be applied to incoming requests. The first matching URL handles the
               request and other request handlers are not attempted.
        :param pulumi.Input[str] instance_class: Instance class that is used to run this version. Valid values are AutomaticScaling F1, F2, F4, F4_1G (Only
               AutomaticScaling is supported at the moment)
        :param pulumi.Input[list] libraries: Configuration for third-party Python runtime libraries that are required by the application.
        :param pulumi.Input[bool] noop_on_destroy: If set to `true`, the application version will not be deleted.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] runtime: Desired runtime. Example python27.
        :param pulumi.Input[str] runtime_api_version: The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
               https://cloud.google.com/appengine/docs/standard//config/appref
        :param pulumi.Input[str] service: AppEngine service resource
        :param pulumi.Input[bool] threadsafe: Whether multiple requests can be dispatched to this version at once.
        :param pulumi.Input[str] version_id: Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
               numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".

        The **deployment** object supports the following:

          * `files` (`pulumi.Input[list]`)
            * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
            * `sha1Sum` (`pulumi.Input[str]`)
            * `sourceUrl` (`pulumi.Input[str]`)

          * `zip` (`pulumi.Input[dict]`)
            * `filesCount` (`pulumi.Input[float]`)
            * `sourceUrl` (`pulumi.Input[str]`)

        The **entrypoint** object supports the following:

          * `shell` (`pulumi.Input[str]`)

        The **handlers** object supports the following:

          * `authFailAction` (`pulumi.Input[str]`)
          * `login` (`pulumi.Input[str]`)
          * `redirectHttpResponseCode` (`pulumi.Input[str]`)
          * `script` (`pulumi.Input[dict]`)
            * `scriptPath` (`pulumi.Input[str]`)

          * `securityLevel` (`pulumi.Input[str]`)
          * `staticFiles` (`pulumi.Input[dict]`)
            * `applicationReadable` (`pulumi.Input[bool]`)
            * `expiration` (`pulumi.Input[str]`)
            * `httpHeaders` (`pulumi.Input[dict]`)
            * `mimeType` (`pulumi.Input[str]`)
            * `path` (`pulumi.Input[str]`)
            * `requireMatchingFile` (`pulumi.Input[bool]`)
            * `uploadPathRegex` (`pulumi.Input[str]`)

          * `urlRegex` (`pulumi.Input[str]`)

        The **libraries** object supports the following:

          * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
          * `version` (`pulumi.Input[str]`)
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

            __props__['delete_service_on_destroy'] = delete_service_on_destroy
            __props__['deployment'] = deployment
            __props__['entrypoint'] = entrypoint
            __props__['env_variables'] = env_variables
            __props__['handlers'] = handlers
            __props__['instance_class'] = instance_class
            __props__['libraries'] = libraries
            __props__['noop_on_destroy'] = noop_on_destroy
            __props__['project'] = project
            if runtime is None:
                raise TypeError("Missing required property 'runtime'")
            __props__['runtime'] = runtime
            __props__['runtime_api_version'] = runtime_api_version
            __props__['service'] = service
            __props__['threadsafe'] = threadsafe
            __props__['version_id'] = version_id
            __props__['name'] = None
        super(StandardAppVersion, __self__).__init__(
            'gcp:appengine/standardAppVersion:StandardAppVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, delete_service_on_destroy=None, deployment=None, entrypoint=None, env_variables=None, handlers=None, instance_class=None, libraries=None, name=None, noop_on_destroy=None, project=None, runtime=None, runtime_api_version=None, service=None, threadsafe=None, version_id=None):
        """
        Get an existing StandardAppVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] delete_service_on_destroy: If set to `true`, the service will be deleted if it is the last version.    
        :param pulumi.Input[dict] deployment: Code and application artifacts that make up this version.
        :param pulumi.Input[dict] entrypoint: The entrypoint for the application.
        :param pulumi.Input[dict] env_variables: Environment variables available to the application.
        :param pulumi.Input[list] handlers: An ordered list of URL-matching patterns that should be applied to incoming requests. The first matching URL handles the
               request and other request handlers are not attempted.
        :param pulumi.Input[str] instance_class: Instance class that is used to run this version. Valid values are AutomaticScaling F1, F2, F4, F4_1G (Only
               AutomaticScaling is supported at the moment)
        :param pulumi.Input[list] libraries: Configuration for third-party Python runtime libraries that are required by the application.
        :param pulumi.Input[str] name: The identifier for this object. Format specified above.
        :param pulumi.Input[bool] noop_on_destroy: If set to `true`, the application version will not be deleted.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] runtime: Desired runtime. Example python27.
        :param pulumi.Input[str] runtime_api_version: The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
               https://cloud.google.com/appengine/docs/standard//config/appref
        :param pulumi.Input[str] service: AppEngine service resource
        :param pulumi.Input[bool] threadsafe: Whether multiple requests can be dispatched to this version at once.
        :param pulumi.Input[str] version_id: Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
               numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".

        The **deployment** object supports the following:

          * `files` (`pulumi.Input[list]`)
            * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
            * `sha1Sum` (`pulumi.Input[str]`)
            * `sourceUrl` (`pulumi.Input[str]`)

          * `zip` (`pulumi.Input[dict]`)
            * `filesCount` (`pulumi.Input[float]`)
            * `sourceUrl` (`pulumi.Input[str]`)

        The **entrypoint** object supports the following:

          * `shell` (`pulumi.Input[str]`)

        The **handlers** object supports the following:

          * `authFailAction` (`pulumi.Input[str]`)
          * `login` (`pulumi.Input[str]`)
          * `redirectHttpResponseCode` (`pulumi.Input[str]`)
          * `script` (`pulumi.Input[dict]`)
            * `scriptPath` (`pulumi.Input[str]`)

          * `securityLevel` (`pulumi.Input[str]`)
          * `staticFiles` (`pulumi.Input[dict]`)
            * `applicationReadable` (`pulumi.Input[bool]`)
            * `expiration` (`pulumi.Input[str]`)
            * `httpHeaders` (`pulumi.Input[dict]`)
            * `mimeType` (`pulumi.Input[str]`)
            * `path` (`pulumi.Input[str]`)
            * `requireMatchingFile` (`pulumi.Input[bool]`)
            * `uploadPathRegex` (`pulumi.Input[str]`)

          * `urlRegex` (`pulumi.Input[str]`)

        The **libraries** object supports the following:

          * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
          * `version` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["delete_service_on_destroy"] = delete_service_on_destroy
        __props__["deployment"] = deployment
        __props__["entrypoint"] = entrypoint
        __props__["env_variables"] = env_variables
        __props__["handlers"] = handlers
        __props__["instance_class"] = instance_class
        __props__["libraries"] = libraries
        __props__["name"] = name
        __props__["noop_on_destroy"] = noop_on_destroy
        __props__["project"] = project
        __props__["runtime"] = runtime
        __props__["runtime_api_version"] = runtime_api_version
        __props__["service"] = service
        __props__["threadsafe"] = threadsafe
        __props__["version_id"] = version_id
        return StandardAppVersion(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

