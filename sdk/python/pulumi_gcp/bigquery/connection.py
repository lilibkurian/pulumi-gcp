# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Connection(pulumi.CustomResource):
    cloud_sql: pulumi.Output[dict]
    """
    Cloud SQL properties.  Structure is documented below.

      * `credential` (`dict`) - Cloud SQL properties.  Structure is documented below.
        * `password` (`str`) - Password for database.  **Note**: This property is sensitive and will not be displayed in the plan.
        * `username` (`str`) - Username for database.

      * `database` (`str`) - Database name.
      * `instance_id` (`str`) - Cloud SQL instance ID in the form project:location:instance.
      * `type` (`str`) - Type of the Cloud SQL database.
    """
    connection_id: pulumi.Output[str]
    """
    Optional connection id that should be assigned to the created connection.
    """
    description: pulumi.Output[str]
    """
    A descriptive description for the connection
    """
    friendly_name: pulumi.Output[str]
    """
    A descriptive name for the connection
    """
    has_credential: pulumi.Output[bool]
    """
    True if the connection has credential assigned.
    """
    location: pulumi.Output[str]
    """
    The geographic location where the connection should reside.
    Cloud SQL instance must be in the same location as the connection
    with following exceptions: Cloud SQL us-central1 maps to BigQuery US, Cloud SQL europe-west1 maps to BigQuery EU.
    Examples: US, EU, asia-northeast1, us-central1, europe-west1. The default value is US.
    """
    name: pulumi.Output[str]
    """
    The resource name of the connection in the form of:
    "projects/{project_id}/locations/{location_id}/connections/{connectionId}"
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    def __init__(__self__, resource_name, opts=None, cloud_sql=None, connection_id=None, description=None, friendly_name=None, location=None, project=None, __props__=None, __name__=None, __opts__=None):
        """
        A connection allows BigQuery connections to external data sources..

        To get more information about Connection, see:

        * [API documentation](https://cloud.google.com/bigquery/docs/reference/bigqueryconnection/rest/v1beta1/projects.locations.connections/create)
        * How-to Guides
            * [Cloud SQL federated queries](https://cloud.google.com/bigquery/docs/cloud-sql-federated-queries)

        > **Warning:** All arguments including `cloud_sql.credential.password` will be stored in the raw
        state as plain-text. [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

        ## Example Usage - Bigquery Connection Basic


        ```python
        import pulumi
        import pulumi_gcp as gcp
        import pulumi_random as random

        instance = gcp.sql.DatabaseInstance("instance",
            database_version="POSTGRES_11",
            region="us-central1",
            settings={
                "tier": "db-f1-micro",
            })
        db = gcp.sql.Database("db", instance=instance.name)
        pwd = random.RandomPassword("pwd",
            length=16,
            special=False)
        user = gcp.sql.User("user",
            instance=instance.name,
            password=pwd.result)
        connection = gcp.bigquery.Connection("connection",
            friendly_name="👋",
            description="a riveting description",
            cloud_sql={
                "instance_id": instance.connection_name,
                "database": db.name,
                "type": "POSTGRES",
                "credential": {
                    "username": user.name,
                    "password": user.password,
                },
            })
        ```
        ## Example Usage - Bigquery Connection Full


        ```python
        import pulumi
        import pulumi_gcp as gcp
        import pulumi_random as random

        instance = gcp.sql.DatabaseInstance("instance",
            database_version="POSTGRES_11",
            region="us-central1",
            settings={
                "tier": "db-f1-micro",
            })
        db = gcp.sql.Database("db", instance=instance.name)
        pwd = random.RandomPassword("pwd",
            length=16,
            special=False)
        user = gcp.sql.User("user",
            instance=instance.name,
            password=pwd.result)
        connection = gcp.bigquery.Connection("connection",
            connection_id="my-connection",
            location="US",
            friendly_name="👋",
            description="a riveting description",
            cloud_sql={
                "instance_id": instance.connection_name,
                "database": db.name,
                "type": "POSTGRES",
                "credential": {
                    "username": user.name,
                    "password": user.password,
                },
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] cloud_sql: Cloud SQL properties.  Structure is documented below.
        :param pulumi.Input[str] connection_id: Optional connection id that should be assigned to the created connection.
        :param pulumi.Input[str] description: A descriptive description for the connection
        :param pulumi.Input[str] friendly_name: A descriptive name for the connection
        :param pulumi.Input[str] location: The geographic location where the connection should reside.
               Cloud SQL instance must be in the same location as the connection
               with following exceptions: Cloud SQL us-central1 maps to BigQuery US, Cloud SQL europe-west1 maps to BigQuery EU.
               Examples: US, EU, asia-northeast1, us-central1, europe-west1. The default value is US.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.

        The **cloud_sql** object supports the following:

          * `credential` (`pulumi.Input[dict]`) - Cloud SQL properties.  Structure is documented below.
            * `password` (`pulumi.Input[str]`) - Password for database.  **Note**: This property is sensitive and will not be displayed in the plan.
            * `username` (`pulumi.Input[str]`) - Username for database.

          * `database` (`pulumi.Input[str]`) - Database name.
          * `instance_id` (`pulumi.Input[str]`) - Cloud SQL instance ID in the form project:location:instance.
          * `type` (`pulumi.Input[str]`) - Type of the Cloud SQL database.
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

            if cloud_sql is None:
                raise TypeError("Missing required property 'cloud_sql'")
            __props__['cloud_sql'] = cloud_sql
            __props__['connection_id'] = connection_id
            __props__['description'] = description
            __props__['friendly_name'] = friendly_name
            __props__['location'] = location
            __props__['project'] = project
            __props__['has_credential'] = None
            __props__['name'] = None
        super(Connection, __self__).__init__(
            'gcp:bigquery/connection:Connection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, cloud_sql=None, connection_id=None, description=None, friendly_name=None, has_credential=None, location=None, name=None, project=None):
        """
        Get an existing Connection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] cloud_sql: Cloud SQL properties.  Structure is documented below.
        :param pulumi.Input[str] connection_id: Optional connection id that should be assigned to the created connection.
        :param pulumi.Input[str] description: A descriptive description for the connection
        :param pulumi.Input[str] friendly_name: A descriptive name for the connection
        :param pulumi.Input[bool] has_credential: True if the connection has credential assigned.
        :param pulumi.Input[str] location: The geographic location where the connection should reside.
               Cloud SQL instance must be in the same location as the connection
               with following exceptions: Cloud SQL us-central1 maps to BigQuery US, Cloud SQL europe-west1 maps to BigQuery EU.
               Examples: US, EU, asia-northeast1, us-central1, europe-west1. The default value is US.
        :param pulumi.Input[str] name: The resource name of the connection in the form of:
               "projects/{project_id}/locations/{location_id}/connections/{connectionId}"
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.

        The **cloud_sql** object supports the following:

          * `credential` (`pulumi.Input[dict]`) - Cloud SQL properties.  Structure is documented below.
            * `password` (`pulumi.Input[str]`) - Password for database.  **Note**: This property is sensitive and will not be displayed in the plan.
            * `username` (`pulumi.Input[str]`) - Username for database.

          * `database` (`pulumi.Input[str]`) - Database name.
          * `instance_id` (`pulumi.Input[str]`) - Cloud SQL instance ID in the form project:location:instance.
          * `type` (`pulumi.Input[str]`) - Type of the Cloud SQL database.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cloud_sql"] = cloud_sql
        __props__["connection_id"] = connection_id
        __props__["description"] = description
        __props__["friendly_name"] = friendly_name
        __props__["has_credential"] = has_credential
        __props__["location"] = location
        __props__["name"] = name
        __props__["project"] = project
        return Connection(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

