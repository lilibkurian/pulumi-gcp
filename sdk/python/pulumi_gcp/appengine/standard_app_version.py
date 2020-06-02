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
    automatic_scaling: pulumi.Output[dict]
    """
    Automatic scaling is based on request rate, response latencies, and other application metrics.  Structure is documented below.

      * `maxConcurrentRequests` (`float`) - Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance.
        Defaults to a runtime-specific value.
      * `maxIdleInstances` (`float`) - Maximum number of idle instances that should be maintained for this version.
      * `maxPendingLatency` (`str`) - Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".
      * `minIdleInstances` (`float`) - Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service.
      * `minPendingLatency` (`str`) - Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".
      * `standardSchedulerSettings` (`dict`) - Scheduler settings for standard environment.  Structure is documented below.
        * `max_instances` (`float`) - Maximum number of instances to create for this version. Must be in the range [1.0, 200.0].
        * `minInstances` (`float`) - Minimum number of instances to run for this version. Set to zero to disable minInstances configuration.
        * `targetCpuUtilization` (`float`) - Target CPU utilization ratio to maintain when scaling. Should be a value in the range [0.50, 0.95], zero, or a negative value.
        * `targetThroughputUtilization` (`float`) - Target throughput utilization ratio to maintain when scaling. Should be a value in the range [0.50, 0.95], zero, or a negative value.
    """
    basic_scaling: pulumi.Output[dict]
    """
    Basic scaling creates instances when your application receives requests. Each instance will be shut down when the application becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity.  Structure is documented below.

      * `idleTimeout` (`str`) - Duration of time after the last request that an instance must wait before the instance is shut down.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s.
      * `max_instances` (`float`) - Maximum number of instances to create for this version. Must be in the range [1.0, 200.0].
    """
    delete_service_on_destroy: pulumi.Output[bool]
    """
    If set to `true`, the service will be deleted if it is the last version.    
    """
    deployment: pulumi.Output[dict]
    """
    Code and application artifacts that make up this version.  Structure is documented below.

      * `files` (`list`) - Manifest of the files stored in Google Cloud Storage that are included as part of this version.
        All files must be readable using the credentials supplied with this call.  Structure is documented below.
        * `name` (`str`) - Name of the library. Example "django".
        * `sha1Sum` (`str`) - SHA1 checksum of the file
        * `sourceUrl` (`str`) - Source URL

      * `zip` (`dict`) - Zip File  Structure is documented below.
        * `filesCount` (`float`) - files count
        * `sourceUrl` (`str`) - Source URL
    """
    entrypoint: pulumi.Output[dict]
    """
    The entrypoint for the application.  Structure is documented below.

      * `shell` (`str`) - The format should be a shell command that can be fed to bash -c.
    """
    env_variables: pulumi.Output[dict]
    """
    Environment variables available to the application.
    """
    handlers: pulumi.Output[list]
    """
    An ordered list of URL-matching patterns that should be applied to incoming requests.
    The first matching URL handles the request and other request handlers are not attempted.  Structure is documented below.

      * `authFailAction` (`str`) - Actions to take when the user is not logged in.
      * `login` (`str`) - Methods to restrict access to a URL based on login status.
      * `redirectHttpResponseCode` (`str`) - 30x code to use when performing redirects for the secure field.
      * `script` (`dict`) - Executes a script to handle the requests that match this URL pattern.
        Only the auto value is supported for Node.js in the App Engine standard environment, for example "script:" "auto".  Structure is documented below.
        * `scriptPath` (`str`) - Path to the script from the application root directory.

      * `securityLevel` (`str`) - Security (HTTPS) enforcement for this URL.
      * `staticFiles` (`dict`) - Files served directly to the user for a given URL, such as images, CSS stylesheets, or JavaScript source files. Static file handlers describe which files in the application directory are static files, and which URLs serve them.  Structure is documented below.
        * `applicationReadable` (`bool`) - Whether files should also be uploaded as code data. By default, files declared in static file handlers are uploaded as
          static data and are only served to end users; they cannot be read by the application. If enabled, uploads are charged
          against both your code and static data storage resource quotas.
        * `expiration` (`str`) - Time a static file served by this handler should be cached by web proxies and browsers.
          A duration in seconds with up to nine fractional digits, terminated by 's'. Example "3.5s".
        * `httpHeaders` (`dict`) - HTTP headers to use for all responses from these URLs.
          An object containing a list of "key:value" value pairs.".
        * `mimeType` (`str`) - MIME type used to serve all files served by this handler.
          Defaults to file-specific MIME types, which are derived from each file's filename extension.
        * `path` (`str`) - Path to the static files matched by the URL pattern, from the application root directory. The path can refer to text matched in groupings in the URL pattern.
        * `requireMatchingFile` (`bool`) - Whether this handler should match the request if the file referenced by the handler does not exist.
        * `uploadPathRegex` (`str`) - Regular expression that matches the file paths for all files that should be referenced by this handler.

      * `urlRegex` (`str`) - URL prefix. Uses regular expression syntax, which means regexp special characters must be escaped, but should not contain groupings.
        All URLs that begin with this prefix are handled by this handler, using the portion of the URL after the prefix as part of the file path.
    """
    instance_class: pulumi.Output[str]
    """
    Instance class that is used to run this version. Valid values are
    AutomaticScaling: F1, F2, F4, F4_1G
    BasicScaling or ManualScaling: B1, B2, B4, B4_1G, B8
    Defaults to F1 for AutomaticScaling and B2 for ManualScaling and BasicScaling. If no scaling is specified, AutomaticScaling is chosen.
    """
    libraries: pulumi.Output[list]
    """
    Configuration for third-party Python runtime libraries that are required by the application.  Structure is documented below.

      * `name` (`str`) - Name of the library. Example "django".
      * `version` (`str`) - Version of the library to select, or "latest".
    """
    manual_scaling: pulumi.Output[dict]
    """
    A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.  Structure is documented below.

      * `instances` (`float`) - Number of instances to assign to the service at the start.
        **Note:** When managing the number of instances at runtime through the App Engine Admin API or the (now deprecated) Python 2
        Modules API set_num_instances() you must use `lifecycle.ignore_changes = ["manual_scaling"[0].instances]` to prevent drift detection.
    """
    name: pulumi.Output[str]
    """
    Name of the library. Example "django".
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
    The version of the API in the given runtime environment.
    Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref
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
    Relative name of the version within the service. For example, `v1`. Version names can contain only lowercase letters, numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
    """
    def __init__(__self__, resource_name, opts=None, automatic_scaling=None, basic_scaling=None, delete_service_on_destroy=None, deployment=None, entrypoint=None, env_variables=None, handlers=None, instance_class=None, libraries=None, manual_scaling=None, noop_on_destroy=None, project=None, runtime=None, runtime_api_version=None, service=None, threadsafe=None, version_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Standard App Version resource to create a new version of standard GAE Application.
        Learn about the differences between the standard environment and the flexible environment
        at https://cloud.google.com/appengine/docs/the-appengine-environments.
        Currently supporting Zip and File Containers.


        To get more information about StandardAppVersion, see:

        * [API documentation](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/appengine/docs/standard)

        ## Example Usage - App Engine Standard App Version


        ```python
        import pulumi
        import pulumi_gcp as gcp

        bucket = gcp.storage.Bucket("bucket")
        object = gcp.storage.BucketObject("object",
            bucket=bucket.name,
            source=pulumi.FileAsset("./test-fixtures/appengine/hello-world.zip"))
        myapp_v1 = gcp.appengine.StandardAppVersion("myappV1",
            version_id="v1",
            service="myapp",
            runtime="nodejs10",
            entrypoint={
                "shell": "node ./app.js",
            },
            deployment={
                "zip": {
                    "sourceUrl": pulumi.Output.all(bucket.name, object.name).apply(lambda bucketName, objectName: f"https://storage.googleapis.com/{bucket_name}/{object_name}"),
                },
            },
            env_variables={
                "port": "8080",
            },
            automatic_scaling={
                "maxConcurrentRequests": 10,
                "minIdleInstances": 1,
                "maxIdleInstances": 3,
                "minPendingLatency": "1s",
                "maxPendingLatency": "5s",
                "standard_scheduler_settings": {
                    "targetCpuUtilization": 0.5,
                    "targetThroughputUtilization": 0.75,
                    "minInstances": 2,
                    "max_instances": 10,
                },
            },
            delete_service_on_destroy=True)
        myapp_v2 = gcp.appengine.StandardAppVersion("myappV2",
            version_id="v2",
            service="myapp",
            runtime="nodejs10",
            entrypoint={
                "shell": "node ./app.js",
            },
            deployment={
                "zip": {
                    "sourceUrl": pulumi.Output.all(bucket.name, object.name).apply(lambda bucketName, objectName: f"https://storage.googleapis.com/{bucket_name}/{object_name}"),
                },
            },
            env_variables={
                "port": "8080",
            },
            basic_scaling={
                "max_instances": 5,
            },
            noop_on_destroy=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] automatic_scaling: Automatic scaling is based on request rate, response latencies, and other application metrics.  Structure is documented below.
        :param pulumi.Input[dict] basic_scaling: Basic scaling creates instances when your application receives requests. Each instance will be shut down when the application becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity.  Structure is documented below.
        :param pulumi.Input[bool] delete_service_on_destroy: If set to `true`, the service will be deleted if it is the last version.    
        :param pulumi.Input[dict] deployment: Code and application artifacts that make up this version.  Structure is documented below.
        :param pulumi.Input[dict] entrypoint: The entrypoint for the application.  Structure is documented below.
        :param pulumi.Input[dict] env_variables: Environment variables available to the application.
        :param pulumi.Input[list] handlers: An ordered list of URL-matching patterns that should be applied to incoming requests.
               The first matching URL handles the request and other request handlers are not attempted.  Structure is documented below.
        :param pulumi.Input[str] instance_class: Instance class that is used to run this version. Valid values are
               AutomaticScaling: F1, F2, F4, F4_1G
               BasicScaling or ManualScaling: B1, B2, B4, B4_1G, B8
               Defaults to F1 for AutomaticScaling and B2 for ManualScaling and BasicScaling. If no scaling is specified, AutomaticScaling is chosen.
        :param pulumi.Input[list] libraries: Configuration for third-party Python runtime libraries that are required by the application.  Structure is documented below.
        :param pulumi.Input[dict] manual_scaling: A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.  Structure is documented below.
        :param pulumi.Input[bool] noop_on_destroy: If set to `true`, the application version will not be deleted.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] runtime: Desired runtime. Example python27.
        :param pulumi.Input[str] runtime_api_version: The version of the API in the given runtime environment.
               Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref
        :param pulumi.Input[str] service: AppEngine service resource
        :param pulumi.Input[bool] threadsafe: Whether multiple requests can be dispatched to this version at once.
        :param pulumi.Input[str] version_id: Relative name of the version within the service. For example, `v1`. Version names can contain only lowercase letters, numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".

        The **automatic_scaling** object supports the following:

          * `maxConcurrentRequests` (`pulumi.Input[float]`) - Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance.
            Defaults to a runtime-specific value.
          * `maxIdleInstances` (`pulumi.Input[float]`) - Maximum number of idle instances that should be maintained for this version.
          * `maxPendingLatency` (`pulumi.Input[str]`) - Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it.
            A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".
          * `minIdleInstances` (`pulumi.Input[float]`) - Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service.
          * `minPendingLatency` (`pulumi.Input[str]`) - Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it.
            A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".
          * `standardSchedulerSettings` (`pulumi.Input[dict]`) - Scheduler settings for standard environment.  Structure is documented below.
            * `max_instances` (`pulumi.Input[float]`) - Maximum number of instances to create for this version. Must be in the range [1.0, 200.0].
            * `minInstances` (`pulumi.Input[float]`) - Minimum number of instances to run for this version. Set to zero to disable minInstances configuration.
            * `targetCpuUtilization` (`pulumi.Input[float]`) - Target CPU utilization ratio to maintain when scaling. Should be a value in the range [0.50, 0.95], zero, or a negative value.
            * `targetThroughputUtilization` (`pulumi.Input[float]`) - Target throughput utilization ratio to maintain when scaling. Should be a value in the range [0.50, 0.95], zero, or a negative value.

        The **basic_scaling** object supports the following:

          * `idleTimeout` (`pulumi.Input[str]`) - Duration of time after the last request that an instance must wait before the instance is shut down.
            A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s.
          * `max_instances` (`pulumi.Input[float]`) - Maximum number of instances to create for this version. Must be in the range [1.0, 200.0].

        The **deployment** object supports the following:

          * `files` (`pulumi.Input[list]`) - Manifest of the files stored in Google Cloud Storage that are included as part of this version.
            All files must be readable using the credentials supplied with this call.  Structure is documented below.
            * `name` (`pulumi.Input[str]`) - Name of the library. Example "django".
            * `sha1Sum` (`pulumi.Input[str]`) - SHA1 checksum of the file
            * `sourceUrl` (`pulumi.Input[str]`) - Source URL

          * `zip` (`pulumi.Input[dict]`) - Zip File  Structure is documented below.
            * `filesCount` (`pulumi.Input[float]`) - files count
            * `sourceUrl` (`pulumi.Input[str]`) - Source URL

        The **entrypoint** object supports the following:

          * `shell` (`pulumi.Input[str]`) - The format should be a shell command that can be fed to bash -c.

        The **handlers** object supports the following:

          * `authFailAction` (`pulumi.Input[str]`) - Actions to take when the user is not logged in.
          * `login` (`pulumi.Input[str]`) - Methods to restrict access to a URL based on login status.
          * `redirectHttpResponseCode` (`pulumi.Input[str]`) - 30x code to use when performing redirects for the secure field.
          * `script` (`pulumi.Input[dict]`) - Executes a script to handle the requests that match this URL pattern.
            Only the auto value is supported for Node.js in the App Engine standard environment, for example "script:" "auto".  Structure is documented below.
            * `scriptPath` (`pulumi.Input[str]`) - Path to the script from the application root directory.

          * `securityLevel` (`pulumi.Input[str]`) - Security (HTTPS) enforcement for this URL.
          * `staticFiles` (`pulumi.Input[dict]`) - Files served directly to the user for a given URL, such as images, CSS stylesheets, or JavaScript source files. Static file handlers describe which files in the application directory are static files, and which URLs serve them.  Structure is documented below.
            * `applicationReadable` (`pulumi.Input[bool]`) - Whether files should also be uploaded as code data. By default, files declared in static file handlers are uploaded as
              static data and are only served to end users; they cannot be read by the application. If enabled, uploads are charged
              against both your code and static data storage resource quotas.
            * `expiration` (`pulumi.Input[str]`) - Time a static file served by this handler should be cached by web proxies and browsers.
              A duration in seconds with up to nine fractional digits, terminated by 's'. Example "3.5s".
            * `httpHeaders` (`pulumi.Input[dict]`) - HTTP headers to use for all responses from these URLs.
              An object containing a list of "key:value" value pairs.".
            * `mimeType` (`pulumi.Input[str]`) - MIME type used to serve all files served by this handler.
              Defaults to file-specific MIME types, which are derived from each file's filename extension.
            * `path` (`pulumi.Input[str]`) - Path to the static files matched by the URL pattern, from the application root directory. The path can refer to text matched in groupings in the URL pattern.
            * `requireMatchingFile` (`pulumi.Input[bool]`) - Whether this handler should match the request if the file referenced by the handler does not exist.
            * `uploadPathRegex` (`pulumi.Input[str]`) - Regular expression that matches the file paths for all files that should be referenced by this handler.

          * `urlRegex` (`pulumi.Input[str]`) - URL prefix. Uses regular expression syntax, which means regexp special characters must be escaped, but should not contain groupings.
            All URLs that begin with this prefix are handled by this handler, using the portion of the URL after the prefix as part of the file path.

        The **libraries** object supports the following:

          * `name` (`pulumi.Input[str]`) - Name of the library. Example "django".
          * `version` (`pulumi.Input[str]`) - Version of the library to select, or "latest".

        The **manual_scaling** object supports the following:

          * `instances` (`pulumi.Input[float]`) - Number of instances to assign to the service at the start.
            **Note:** When managing the number of instances at runtime through the App Engine Admin API or the (now deprecated) Python 2
            Modules API set_num_instances() you must use `lifecycle.ignore_changes = ["manual_scaling"[0].instances]` to prevent drift detection.
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

            __props__['automatic_scaling'] = automatic_scaling
            __props__['basic_scaling'] = basic_scaling
            __props__['delete_service_on_destroy'] = delete_service_on_destroy
            if deployment is None:
                raise TypeError("Missing required property 'deployment'")
            __props__['deployment'] = deployment
            __props__['entrypoint'] = entrypoint
            __props__['env_variables'] = env_variables
            __props__['handlers'] = handlers
            __props__['instance_class'] = instance_class
            __props__['libraries'] = libraries
            __props__['manual_scaling'] = manual_scaling
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
    def get(resource_name, id, opts=None, automatic_scaling=None, basic_scaling=None, delete_service_on_destroy=None, deployment=None, entrypoint=None, env_variables=None, handlers=None, instance_class=None, libraries=None, manual_scaling=None, name=None, noop_on_destroy=None, project=None, runtime=None, runtime_api_version=None, service=None, threadsafe=None, version_id=None):
        """
        Get an existing StandardAppVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] automatic_scaling: Automatic scaling is based on request rate, response latencies, and other application metrics.  Structure is documented below.
        :param pulumi.Input[dict] basic_scaling: Basic scaling creates instances when your application receives requests. Each instance will be shut down when the application becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity.  Structure is documented below.
        :param pulumi.Input[bool] delete_service_on_destroy: If set to `true`, the service will be deleted if it is the last version.    
        :param pulumi.Input[dict] deployment: Code and application artifacts that make up this version.  Structure is documented below.
        :param pulumi.Input[dict] entrypoint: The entrypoint for the application.  Structure is documented below.
        :param pulumi.Input[dict] env_variables: Environment variables available to the application.
        :param pulumi.Input[list] handlers: An ordered list of URL-matching patterns that should be applied to incoming requests.
               The first matching URL handles the request and other request handlers are not attempted.  Structure is documented below.
        :param pulumi.Input[str] instance_class: Instance class that is used to run this version. Valid values are
               AutomaticScaling: F1, F2, F4, F4_1G
               BasicScaling or ManualScaling: B1, B2, B4, B4_1G, B8
               Defaults to F1 for AutomaticScaling and B2 for ManualScaling and BasicScaling. If no scaling is specified, AutomaticScaling is chosen.
        :param pulumi.Input[list] libraries: Configuration for third-party Python runtime libraries that are required by the application.  Structure is documented below.
        :param pulumi.Input[dict] manual_scaling: A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.  Structure is documented below.
        :param pulumi.Input[str] name: Name of the library. Example "django".
        :param pulumi.Input[bool] noop_on_destroy: If set to `true`, the application version will not be deleted.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] runtime: Desired runtime. Example python27.
        :param pulumi.Input[str] runtime_api_version: The version of the API in the given runtime environment.
               Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref
        :param pulumi.Input[str] service: AppEngine service resource
        :param pulumi.Input[bool] threadsafe: Whether multiple requests can be dispatched to this version at once.
        :param pulumi.Input[str] version_id: Relative name of the version within the service. For example, `v1`. Version names can contain only lowercase letters, numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".

        The **automatic_scaling** object supports the following:

          * `maxConcurrentRequests` (`pulumi.Input[float]`) - Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance.
            Defaults to a runtime-specific value.
          * `maxIdleInstances` (`pulumi.Input[float]`) - Maximum number of idle instances that should be maintained for this version.
          * `maxPendingLatency` (`pulumi.Input[str]`) - Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it.
            A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".
          * `minIdleInstances` (`pulumi.Input[float]`) - Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service.
          * `minPendingLatency` (`pulumi.Input[str]`) - Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it.
            A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".
          * `standardSchedulerSettings` (`pulumi.Input[dict]`) - Scheduler settings for standard environment.  Structure is documented below.
            * `max_instances` (`pulumi.Input[float]`) - Maximum number of instances to create for this version. Must be in the range [1.0, 200.0].
            * `minInstances` (`pulumi.Input[float]`) - Minimum number of instances to run for this version. Set to zero to disable minInstances configuration.
            * `targetCpuUtilization` (`pulumi.Input[float]`) - Target CPU utilization ratio to maintain when scaling. Should be a value in the range [0.50, 0.95], zero, or a negative value.
            * `targetThroughputUtilization` (`pulumi.Input[float]`) - Target throughput utilization ratio to maintain when scaling. Should be a value in the range [0.50, 0.95], zero, or a negative value.

        The **basic_scaling** object supports the following:

          * `idleTimeout` (`pulumi.Input[str]`) - Duration of time after the last request that an instance must wait before the instance is shut down.
            A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s.
          * `max_instances` (`pulumi.Input[float]`) - Maximum number of instances to create for this version. Must be in the range [1.0, 200.0].

        The **deployment** object supports the following:

          * `files` (`pulumi.Input[list]`) - Manifest of the files stored in Google Cloud Storage that are included as part of this version.
            All files must be readable using the credentials supplied with this call.  Structure is documented below.
            * `name` (`pulumi.Input[str]`) - Name of the library. Example "django".
            * `sha1Sum` (`pulumi.Input[str]`) - SHA1 checksum of the file
            * `sourceUrl` (`pulumi.Input[str]`) - Source URL

          * `zip` (`pulumi.Input[dict]`) - Zip File  Structure is documented below.
            * `filesCount` (`pulumi.Input[float]`) - files count
            * `sourceUrl` (`pulumi.Input[str]`) - Source URL

        The **entrypoint** object supports the following:

          * `shell` (`pulumi.Input[str]`) - The format should be a shell command that can be fed to bash -c.

        The **handlers** object supports the following:

          * `authFailAction` (`pulumi.Input[str]`) - Actions to take when the user is not logged in.
          * `login` (`pulumi.Input[str]`) - Methods to restrict access to a URL based on login status.
          * `redirectHttpResponseCode` (`pulumi.Input[str]`) - 30x code to use when performing redirects for the secure field.
          * `script` (`pulumi.Input[dict]`) - Executes a script to handle the requests that match this URL pattern.
            Only the auto value is supported for Node.js in the App Engine standard environment, for example "script:" "auto".  Structure is documented below.
            * `scriptPath` (`pulumi.Input[str]`) - Path to the script from the application root directory.

          * `securityLevel` (`pulumi.Input[str]`) - Security (HTTPS) enforcement for this URL.
          * `staticFiles` (`pulumi.Input[dict]`) - Files served directly to the user for a given URL, such as images, CSS stylesheets, or JavaScript source files. Static file handlers describe which files in the application directory are static files, and which URLs serve them.  Structure is documented below.
            * `applicationReadable` (`pulumi.Input[bool]`) - Whether files should also be uploaded as code data. By default, files declared in static file handlers are uploaded as
              static data and are only served to end users; they cannot be read by the application. If enabled, uploads are charged
              against both your code and static data storage resource quotas.
            * `expiration` (`pulumi.Input[str]`) - Time a static file served by this handler should be cached by web proxies and browsers.
              A duration in seconds with up to nine fractional digits, terminated by 's'. Example "3.5s".
            * `httpHeaders` (`pulumi.Input[dict]`) - HTTP headers to use for all responses from these URLs.
              An object containing a list of "key:value" value pairs.".
            * `mimeType` (`pulumi.Input[str]`) - MIME type used to serve all files served by this handler.
              Defaults to file-specific MIME types, which are derived from each file's filename extension.
            * `path` (`pulumi.Input[str]`) - Path to the static files matched by the URL pattern, from the application root directory. The path can refer to text matched in groupings in the URL pattern.
            * `requireMatchingFile` (`pulumi.Input[bool]`) - Whether this handler should match the request if the file referenced by the handler does not exist.
            * `uploadPathRegex` (`pulumi.Input[str]`) - Regular expression that matches the file paths for all files that should be referenced by this handler.

          * `urlRegex` (`pulumi.Input[str]`) - URL prefix. Uses regular expression syntax, which means regexp special characters must be escaped, but should not contain groupings.
            All URLs that begin with this prefix are handled by this handler, using the portion of the URL after the prefix as part of the file path.

        The **libraries** object supports the following:

          * `name` (`pulumi.Input[str]`) - Name of the library. Example "django".
          * `version` (`pulumi.Input[str]`) - Version of the library to select, or "latest".

        The **manual_scaling** object supports the following:

          * `instances` (`pulumi.Input[float]`) - Number of instances to assign to the service at the start.
            **Note:** When managing the number of instances at runtime through the App Engine Admin API or the (now deprecated) Python 2
            Modules API set_num_instances() you must use `lifecycle.ignore_changes = ["manual_scaling"[0].instances]` to prevent drift detection.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["automatic_scaling"] = automatic_scaling
        __props__["basic_scaling"] = basic_scaling
        __props__["delete_service_on_destroy"] = delete_service_on_destroy
        __props__["deployment"] = deployment
        __props__["entrypoint"] = entrypoint
        __props__["env_variables"] = env_variables
        __props__["handlers"] = handlers
        __props__["instance_class"] = instance_class
        __props__["libraries"] = libraries
        __props__["manual_scaling"] = manual_scaling
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

