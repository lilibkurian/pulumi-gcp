# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class DatabaseInstance(pulumi.CustomResource):
    connection_name: pulumi.Output[str]
    """
    The connection name of the instance to be used in
    connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
    """
    database_version: pulumi.Output[str]
    """
    The MySQL or PostgreSQL version to
    use. Can be `MYSQL_5_6`, `MYSQL_5_7`, `POSTGRES_9_6` or `POSTGRES_11` (beta) for second-generation
    instances, or `MYSQL_5_5` or `MYSQL_5_6` for first-generation instances.
    See [Second Generation Capabilities](https://cloud.google.com/sql/docs/1st-2nd-gen-differences)
    for more information.
    """
    first_ip_address: pulumi.Output[str]
    ip_addresses: pulumi.Output[list]
    master_instance_name: pulumi.Output[str]
    """
    The name of the instance that will act as
    the master in the replication setup. Note, this requires the master to have
    `binary_log_enabled` set, as well as existing backups.
    """
    name: pulumi.Output[str]
    """
    The name of the instance. If the name is left
    blank, this provider will randomly generate one when the instance is first
    created. This is done because after a name is used, it cannot be reused for
    up to [one week](https://cloud.google.com/sql/docs/delete-instance).
    """
    private_ip_address: pulumi.Output[str]
    """
    The first private (`PRIVATE`) IPv4 address assigned. This provides a convenient way to access an IP of a specific type without
    performing filtering.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs. If it
    is not provided, the provider project is used.
    """
    public_ip_address: pulumi.Output[str]
    """
    The first public (`PRIMARY`) IPv4 address assigned. This provides a convenient way to access an IP of a specific type without
    performing filtering.
    """
    region: pulumi.Output[str]
    """
    The region the instance will sit in. Note, first-generation Cloud SQL instance
    regions do not line up with the Google Compute Engine (GCE) regions, and Cloud SQL is not
    available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
    A valid region must be provided to use this resource. If a region is not provided in the resource definition,
    the provider region will be used instead, but this will be an apply-time error for all first-generation
    instances *and* for second-generation instances if the provider region is not supported with Cloud SQL.
    If you choose not to provide the `region` argument for this resource, make sure you understand this.
    """
    replica_configuration: pulumi.Output[dict]
    """
    The configuration for replication. The
    configuration is detailed below.
    
      * `caCertificate` (`str`)
      * `clientCertificate` (`str`)
      * `clientKey` (`str`)
      * `connectRetryInterval` (`float`)
      * `dumpFilePath` (`str`)
      * `failoverTarget` (`bool`)
      * `masterHeartbeatPeriod` (`float`)
      * `password` (`str`)
      * `sslCipher` (`str`)
      * `username` (`str`)
      * `verifyServerCertificate` (`bool`)
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    server_ca_cert: pulumi.Output[dict]
    service_account_email_address: pulumi.Output[str]
    """
    The service account email address assigned to the
    instance. This property is applicable only to Second Generation instances.
    """
    settings: pulumi.Output[dict]
    """
    The settings to use for the database. The
    configuration is detailed below.
    
      * `activationPolicy` (`str`)
      * `authorizedGaeApplications` (`list`)
      * `availabilityType` (`str`)
      * `backupConfiguration` (`dict`)
    
        * `binaryLogEnabled` (`bool`)
        * `enabled` (`bool`)
        * `location` (`str`)
        * `startTime` (`str`)
    
      * `crashSafeReplication` (`bool`)
      * `databaseFlags` (`list`)
    
        * `name` (`str`) - The name of the instance. If the name is left
          blank, this provider will randomly generate one when the instance is first
          created. This is done because after a name is used, it cannot be reused for
          up to [one week](https://cloud.google.com/sql/docs/delete-instance).
        * `value` (`str`)
    
      * `diskAutoresize` (`bool`)
      * `diskSize` (`float`)
      * `diskType` (`str`)
      * `ip_configuration` (`dict`)
    
        * `authorizedNetworks` (`list`)
    
          * `expiration_time` (`str`)
          * `name` (`str`) - The name of the instance. If the name is left
            blank, this provider will randomly generate one when the instance is first
            created. This is done because after a name is used, it cannot be reused for
            up to [one week](https://cloud.google.com/sql/docs/delete-instance).
          * `value` (`str`)
    
        * `ipv4Enabled` (`bool`)
        * `privateNetwork` (`str`)
        * `requireSsl` (`bool`)
    
      * `locationPreference` (`dict`)
    
        * `followGaeApplication` (`str`)
        * `zone` (`str`)
    
      * `maintenanceWindow` (`dict`)
    
        * `day` (`float`)
        * `hour` (`float`)
        * `updateTrack` (`str`)
    
      * `pricingPlan` (`str`)
      * `replicationType` (`str`)
      * `tier` (`str`)
      * `user_labels` (`dict`)
      * `version` (`float`)
    """
    def __init__(__self__, resource_name, opts=None, database_version=None, master_instance_name=None, name=None, project=None, region=None, replica_configuration=None, settings=None, __props__=None, __name__=None, __opts__=None):
        """
        Creates a new Google SQL Database Instance. For more information, see the [official documentation](https://cloud.google.com/sql/),
        or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/instances).
        
        > **NOTE on `sql.DatabaseInstance`:** - Second-generation instances include a
        default 'root'@'%' user with no password. This user will be deleted by this provider on
        instance creation. You should use `sql.User` to define a custom user with
        a restricted host and strong password.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_version: The MySQL or PostgreSQL version to
               use. Can be `MYSQL_5_6`, `MYSQL_5_7`, `POSTGRES_9_6` or `POSTGRES_11` (beta) for second-generation
               instances, or `MYSQL_5_5` or `MYSQL_5_6` for first-generation instances.
               See [Second Generation Capabilities](https://cloud.google.com/sql/docs/1st-2nd-gen-differences)
               for more information.
        :param pulumi.Input[str] master_instance_name: The name of the instance that will act as
               the master in the replication setup. Note, this requires the master to have
               `binary_log_enabled` set, as well as existing backups.
        :param pulumi.Input[str] name: The name of the instance. If the name is left
               blank, this provider will randomly generate one when the instance is first
               created. This is done because after a name is used, it cannot be reused for
               up to [one week](https://cloud.google.com/sql/docs/delete-instance).
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] region: The region the instance will sit in. Note, first-generation Cloud SQL instance
               regions do not line up with the Google Compute Engine (GCE) regions, and Cloud SQL is not
               available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
               A valid region must be provided to use this resource. If a region is not provided in the resource definition,
               the provider region will be used instead, but this will be an apply-time error for all first-generation
               instances *and* for second-generation instances if the provider region is not supported with Cloud SQL.
               If you choose not to provide the `region` argument for this resource, make sure you understand this.
        :param pulumi.Input[dict] replica_configuration: The configuration for replication. The
               configuration is detailed below.
        :param pulumi.Input[dict] settings: The settings to use for the database. The
               configuration is detailed below.
        
        The **replica_configuration** object supports the following:
        
          * `caCertificate` (`pulumi.Input[str]`)
          * `clientCertificate` (`pulumi.Input[str]`)
          * `clientKey` (`pulumi.Input[str]`)
          * `connectRetryInterval` (`pulumi.Input[float]`)
          * `dumpFilePath` (`pulumi.Input[str]`)
          * `failoverTarget` (`pulumi.Input[bool]`)
          * `masterHeartbeatPeriod` (`pulumi.Input[float]`)
          * `password` (`pulumi.Input[str]`)
          * `sslCipher` (`pulumi.Input[str]`)
          * `username` (`pulumi.Input[str]`)
          * `verifyServerCertificate` (`pulumi.Input[bool]`)
        
        The **settings** object supports the following:
        
          * `activationPolicy` (`pulumi.Input[str]`)
          * `authorizedGaeApplications` (`pulumi.Input[list]`)
          * `availabilityType` (`pulumi.Input[str]`)
          * `backupConfiguration` (`pulumi.Input[dict]`)
        
            * `binaryLogEnabled` (`pulumi.Input[bool]`)
            * `enabled` (`pulumi.Input[bool]`)
            * `location` (`pulumi.Input[str]`)
            * `startTime` (`pulumi.Input[str]`)
        
          * `crashSafeReplication` (`pulumi.Input[bool]`)
          * `databaseFlags` (`pulumi.Input[list]`)
        
            * `name` (`pulumi.Input[str]`) - The name of the instance. If the name is left
              blank, this provider will randomly generate one when the instance is first
              created. This is done because after a name is used, it cannot be reused for
              up to [one week](https://cloud.google.com/sql/docs/delete-instance).
            * `value` (`pulumi.Input[str]`)
        
          * `diskAutoresize` (`pulumi.Input[bool]`)
          * `diskSize` (`pulumi.Input[float]`)
          * `diskType` (`pulumi.Input[str]`)
          * `ip_configuration` (`pulumi.Input[dict]`)
        
            * `authorizedNetworks` (`pulumi.Input[list]`)
        
              * `expiration_time` (`pulumi.Input[str]`)
              * `name` (`pulumi.Input[str]`) - The name of the instance. If the name is left
                blank, this provider will randomly generate one when the instance is first
                created. This is done because after a name is used, it cannot be reused for
                up to [one week](https://cloud.google.com/sql/docs/delete-instance).
              * `value` (`pulumi.Input[str]`)
        
            * `ipv4Enabled` (`pulumi.Input[bool]`)
            * `privateNetwork` (`pulumi.Input[str]`)
            * `requireSsl` (`pulumi.Input[bool]`)
        
          * `locationPreference` (`pulumi.Input[dict]`)
        
            * `followGaeApplication` (`pulumi.Input[str]`)
            * `zone` (`pulumi.Input[str]`)
        
          * `maintenanceWindow` (`pulumi.Input[dict]`)
        
            * `day` (`pulumi.Input[float]`)
            * `hour` (`pulumi.Input[float]`)
            * `updateTrack` (`pulumi.Input[str]`)
        
          * `pricingPlan` (`pulumi.Input[str]`)
          * `replicationType` (`pulumi.Input[str]`)
          * `tier` (`pulumi.Input[str]`)
          * `user_labels` (`pulumi.Input[dict]`)
          * `version` (`pulumi.Input[float]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database_instance.html.markdown.
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

            __props__['database_version'] = database_version
            __props__['master_instance_name'] = master_instance_name
            __props__['name'] = name
            __props__['project'] = project
            __props__['region'] = region
            __props__['replica_configuration'] = replica_configuration
            if settings is None:
                raise TypeError("Missing required property 'settings'")
            __props__['settings'] = settings
            __props__['connection_name'] = None
            __props__['first_ip_address'] = None
            __props__['ip_addresses'] = None
            __props__['private_ip_address'] = None
            __props__['public_ip_address'] = None
            __props__['self_link'] = None
            __props__['server_ca_cert'] = None
            __props__['service_account_email_address'] = None
        super(DatabaseInstance, __self__).__init__(
            'gcp:sql/databaseInstance:DatabaseInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, connection_name=None, database_version=None, first_ip_address=None, ip_addresses=None, master_instance_name=None, name=None, private_ip_address=None, project=None, public_ip_address=None, region=None, replica_configuration=None, self_link=None, server_ca_cert=None, service_account_email_address=None, settings=None):
        """
        Get an existing DatabaseInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_name: The connection name of the instance to be used in
               connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
        :param pulumi.Input[str] database_version: The MySQL or PostgreSQL version to
               use. Can be `MYSQL_5_6`, `MYSQL_5_7`, `POSTGRES_9_6` or `POSTGRES_11` (beta) for second-generation
               instances, or `MYSQL_5_5` or `MYSQL_5_6` for first-generation instances.
               See [Second Generation Capabilities](https://cloud.google.com/sql/docs/1st-2nd-gen-differences)
               for more information.
        :param pulumi.Input[str] master_instance_name: The name of the instance that will act as
               the master in the replication setup. Note, this requires the master to have
               `binary_log_enabled` set, as well as existing backups.
        :param pulumi.Input[str] name: The name of the instance. If the name is left
               blank, this provider will randomly generate one when the instance is first
               created. This is done because after a name is used, it cannot be reused for
               up to [one week](https://cloud.google.com/sql/docs/delete-instance).
        :param pulumi.Input[str] private_ip_address: The first private (`PRIVATE`) IPv4 address assigned. This provides a convenient way to access an IP of a specific type without
               performing filtering.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] public_ip_address: The first public (`PRIMARY`) IPv4 address assigned. This provides a convenient way to access an IP of a specific type without
               performing filtering.
        :param pulumi.Input[str] region: The region the instance will sit in. Note, first-generation Cloud SQL instance
               regions do not line up with the Google Compute Engine (GCE) regions, and Cloud SQL is not
               available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
               A valid region must be provided to use this resource. If a region is not provided in the resource definition,
               the provider region will be used instead, but this will be an apply-time error for all first-generation
               instances *and* for second-generation instances if the provider region is not supported with Cloud SQL.
               If you choose not to provide the `region` argument for this resource, make sure you understand this.
        :param pulumi.Input[dict] replica_configuration: The configuration for replication. The
               configuration is detailed below.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[str] service_account_email_address: The service account email address assigned to the
               instance. This property is applicable only to Second Generation instances.
        :param pulumi.Input[dict] settings: The settings to use for the database. The
               configuration is detailed below.
        
        The **ip_addresses** object supports the following:
        
          * `ip_address` (`pulumi.Input[str]`)
          * `timeToRetire` (`pulumi.Input[str]`)
          * `type` (`pulumi.Input[str]`)
        
        The **replica_configuration** object supports the following:
        
          * `caCertificate` (`pulumi.Input[str]`)
          * `clientCertificate` (`pulumi.Input[str]`)
          * `clientKey` (`pulumi.Input[str]`)
          * `connectRetryInterval` (`pulumi.Input[float]`)
          * `dumpFilePath` (`pulumi.Input[str]`)
          * `failoverTarget` (`pulumi.Input[bool]`)
          * `masterHeartbeatPeriod` (`pulumi.Input[float]`)
          * `password` (`pulumi.Input[str]`)
          * `sslCipher` (`pulumi.Input[str]`)
          * `username` (`pulumi.Input[str]`)
          * `verifyServerCertificate` (`pulumi.Input[bool]`)
        
        The **server_ca_cert** object supports the following:
        
          * `cert` (`pulumi.Input[str]`)
          * `common_name` (`pulumi.Input[str]`)
          * `create_time` (`pulumi.Input[str]`)
          * `expiration_time` (`pulumi.Input[str]`)
          * `sha1_fingerprint` (`pulumi.Input[str]`)
        
        The **settings** object supports the following:
        
          * `activationPolicy` (`pulumi.Input[str]`)
          * `authorizedGaeApplications` (`pulumi.Input[list]`)
          * `availabilityType` (`pulumi.Input[str]`)
          * `backupConfiguration` (`pulumi.Input[dict]`)
        
            * `binaryLogEnabled` (`pulumi.Input[bool]`)
            * `enabled` (`pulumi.Input[bool]`)
            * `location` (`pulumi.Input[str]`)
            * `startTime` (`pulumi.Input[str]`)
        
          * `crashSafeReplication` (`pulumi.Input[bool]`)
          * `databaseFlags` (`pulumi.Input[list]`)
        
            * `name` (`pulumi.Input[str]`) - The name of the instance. If the name is left
              blank, this provider will randomly generate one when the instance is first
              created. This is done because after a name is used, it cannot be reused for
              up to [one week](https://cloud.google.com/sql/docs/delete-instance).
            * `value` (`pulumi.Input[str]`)
        
          * `diskAutoresize` (`pulumi.Input[bool]`)
          * `diskSize` (`pulumi.Input[float]`)
          * `diskType` (`pulumi.Input[str]`)
          * `ip_configuration` (`pulumi.Input[dict]`)
        
            * `authorizedNetworks` (`pulumi.Input[list]`)
        
              * `expiration_time` (`pulumi.Input[str]`)
              * `name` (`pulumi.Input[str]`) - The name of the instance. If the name is left
                blank, this provider will randomly generate one when the instance is first
                created. This is done because after a name is used, it cannot be reused for
                up to [one week](https://cloud.google.com/sql/docs/delete-instance).
              * `value` (`pulumi.Input[str]`)
        
            * `ipv4Enabled` (`pulumi.Input[bool]`)
            * `privateNetwork` (`pulumi.Input[str]`)
            * `requireSsl` (`pulumi.Input[bool]`)
        
          * `locationPreference` (`pulumi.Input[dict]`)
        
            * `followGaeApplication` (`pulumi.Input[str]`)
            * `zone` (`pulumi.Input[str]`)
        
          * `maintenanceWindow` (`pulumi.Input[dict]`)
        
            * `day` (`pulumi.Input[float]`)
            * `hour` (`pulumi.Input[float]`)
            * `updateTrack` (`pulumi.Input[str]`)
        
          * `pricingPlan` (`pulumi.Input[str]`)
          * `replicationType` (`pulumi.Input[str]`)
          * `tier` (`pulumi.Input[str]`)
          * `user_labels` (`pulumi.Input[dict]`)
          * `version` (`pulumi.Input[float]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database_instance.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["connection_name"] = connection_name
        __props__["database_version"] = database_version
        __props__["first_ip_address"] = first_ip_address
        __props__["ip_addresses"] = ip_addresses
        __props__["master_instance_name"] = master_instance_name
        __props__["name"] = name
        __props__["private_ip_address"] = private_ip_address
        __props__["project"] = project
        __props__["public_ip_address"] = public_ip_address
        __props__["region"] = region
        __props__["replica_configuration"] = replica_configuration
        __props__["self_link"] = self_link
        __props__["server_ca_cert"] = server_ca_cert
        __props__["service_account_email_address"] = service_account_email_address
        __props__["settings"] = settings
        return DatabaseInstance(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

