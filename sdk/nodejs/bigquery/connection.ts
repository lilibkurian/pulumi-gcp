// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * A connection allows BigQuery connections to external data sources..
 *
 * To get more information about Connection, see:
 *
 * * [API documentation](https://cloud.google.com/bigquery/docs/reference/bigqueryconnection/rest/v1beta1/projects.locations.connections/create)
 * * How-to Guides
 *     * [Cloud SQL federated queries](https://cloud.google.com/bigquery/docs/cloud-sql-federated-queries)
 *
 * > **Warning:** All arguments including `cloud_sql.credential.password` will be stored in the raw
 * state as plain-text. [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
 *
 * ## Example Usage - Bigquery Connection Basic
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * import * as random from "@pulumi/random";
 *
 * const instance = new gcp.sql.DatabaseInstance("instance", {
 *     databaseVersion: "POSTGRES_11",
 *     region: "us-central1",
 *     settings: {
 *         tier: "db-f1-micro",
 *     },
 * });
 * const db = new gcp.sql.Database("db", {instance: instance.name});
 * const pwd = new random.RandomPassword("pwd", {
 *     length: 16,
 *     special: false,
 * });
 * const user = new gcp.sql.User("user", {
 *     instance: instance.name,
 *     password: pwd.result,
 * });
 * const connection = new gcp.bigquery.Connection("connection", {
 *     friendlyName: "👋",
 *     description: "a riveting description",
 *     cloud_sql: {
 *         instanceId: instance.connectionName,
 *         database: db.name,
 *         type: "POSTGRES",
 *         credential: {
 *             username: user.name,
 *             password: user.password,
 *         },
 *     },
 * });
 * ```
 * ## Example Usage - Bigquery Connection Full
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * import * as random from "@pulumi/random";
 *
 * const instance = new gcp.sql.DatabaseInstance("instance", {
 *     databaseVersion: "POSTGRES_11",
 *     region: "us-central1",
 *     settings: {
 *         tier: "db-f1-micro",
 *     },
 * });
 * const db = new gcp.sql.Database("db", {instance: instance.name});
 * const pwd = new random.RandomPassword("pwd", {
 *     length: 16,
 *     special: false,
 * });
 * const user = new gcp.sql.User("user", {
 *     instance: instance.name,
 *     password: pwd.result,
 * });
 * const connection = new gcp.bigquery.Connection("connection", {
 *     connectionId: "my-connection",
 *     location: "US",
 *     friendlyName: "👋",
 *     description: "a riveting description",
 *     cloud_sql: {
 *         instanceId: instance.connectionName,
 *         database: db.name,
 *         type: "POSTGRES",
 *         credential: {
 *             username: user.name,
 *             password: user.password,
 *         },
 *     },
 * });
 * ```
 */
export class Connection extends pulumi.CustomResource {
    /**
     * Get an existing Connection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConnectionState, opts?: pulumi.CustomResourceOptions): Connection {
        return new Connection(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:bigquery/connection:Connection';

    /**
     * Returns true if the given object is an instance of Connection.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Connection {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Connection.__pulumiType;
    }

    /**
     * Cloud SQL properties.  Structure is documented below.
     */
    public readonly cloudSql!: pulumi.Output<outputs.bigquery.ConnectionCloudSql>;
    /**
     * Optional connection id that should be assigned to the created connection.
     */
    public readonly connectionId!: pulumi.Output<string | undefined>;
    /**
     * A descriptive description for the connection
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * A descriptive name for the connection
     */
    public readonly friendlyName!: pulumi.Output<string | undefined>;
    /**
     * True if the connection has credential assigned.
     */
    public /*out*/ readonly hasCredential!: pulumi.Output<boolean>;
    /**
     * The geographic location where the connection should reside.
     * Cloud SQL instance must be in the same location as the connection
     * with following exceptions: Cloud SQL us-central1 maps to BigQuery US, Cloud SQL europe-west1 maps to BigQuery EU.
     * Examples: US, EU, asia-northeast1, us-central1, europe-west1. The default value is US.
     */
    public readonly location!: pulumi.Output<string | undefined>;
    /**
     * The resource name of the connection in the form of:
     * "projects/{project_id}/locations/{location_id}/connections/{connectionId}"
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;

    /**
     * Create a Connection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConnectionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ConnectionArgs | ConnectionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ConnectionState | undefined;
            inputs["cloudSql"] = state ? state.cloudSql : undefined;
            inputs["connectionId"] = state ? state.connectionId : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["friendlyName"] = state ? state.friendlyName : undefined;
            inputs["hasCredential"] = state ? state.hasCredential : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
        } else {
            const args = argsOrState as ConnectionArgs | undefined;
            if (!args || args.cloudSql === undefined) {
                throw new Error("Missing required property 'cloudSql'");
            }
            inputs["cloudSql"] = args ? args.cloudSql : undefined;
            inputs["connectionId"] = args ? args.connectionId : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["friendlyName"] = args ? args.friendlyName : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["hasCredential"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Connection.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Connection resources.
 */
export interface ConnectionState {
    /**
     * Cloud SQL properties.  Structure is documented below.
     */
    readonly cloudSql?: pulumi.Input<inputs.bigquery.ConnectionCloudSql>;
    /**
     * Optional connection id that should be assigned to the created connection.
     */
    readonly connectionId?: pulumi.Input<string>;
    /**
     * A descriptive description for the connection
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A descriptive name for the connection
     */
    readonly friendlyName?: pulumi.Input<string>;
    /**
     * True if the connection has credential assigned.
     */
    readonly hasCredential?: pulumi.Input<boolean>;
    /**
     * The geographic location where the connection should reside.
     * Cloud SQL instance must be in the same location as the connection
     * with following exceptions: Cloud SQL us-central1 maps to BigQuery US, Cloud SQL europe-west1 maps to BigQuery EU.
     * Examples: US, EU, asia-northeast1, us-central1, europe-west1. The default value is US.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * The resource name of the connection in the form of:
     * "projects/{project_id}/locations/{location_id}/connections/{connectionId}"
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Connection resource.
 */
export interface ConnectionArgs {
    /**
     * Cloud SQL properties.  Structure is documented below.
     */
    readonly cloudSql: pulumi.Input<inputs.bigquery.ConnectionCloudSql>;
    /**
     * Optional connection id that should be assigned to the created connection.
     */
    readonly connectionId?: pulumi.Input<string>;
    /**
     * A descriptive description for the connection
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A descriptive name for the connection
     */
    readonly friendlyName?: pulumi.Input<string>;
    /**
     * The geographic location where the connection should reside.
     * Cloud SQL instance must be in the same location as the connection
     * with following exceptions: Cloud SQL us-central1 maps to BigQuery US, Cloud SQL europe-west1 maps to BigQuery EU.
     * Examples: US, EU, asia-northeast1, us-central1, europe-west1. The default value is US.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
}
