// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Creates a Google Bigtable table inside an instance. For more information see
 * [the official documentation](https://cloud.google.com/bigtable/) and
 * [API](https://cloud.google.com/bigtable/docs/go/reference).
 * 
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const instance = new gcp.bigtable.Instance("instance", {
 *     clusterId: "tf-instance-cluster",
 *     numNodes: 3,
 *     storageType: "HDD",
 *     zone: "us-central1-b",
 * });
 * const table = new gcp.bigtable.Table("table", {
 *     instanceName: instance.name,
 *     splitKeys: [
 *         "a",
 *         "b",
 *         "c",
 *     ],
 * });
 * ```
 */
export class Table extends pulumi.CustomResource {
    /**
     * Get an existing Table resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableState, opts?: pulumi.CustomResourceOptions): Table {
        return new Table(name, <any>state, { ...opts, id: id });
    }

    /**
     * The name of the Bigtable instance.
     */
    public readonly instanceName: pulumi.Output<string>;
    /**
     * The name of the table.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    public readonly project: pulumi.Output<string>;
    /**
     * A list of predefined keys to split the table on.
     */
    public readonly splitKeys: pulumi.Output<string[] | undefined>;

    /**
     * Create a Table resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TableArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TableArgs | TableState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: TableState = argsOrState as TableState | undefined;
            inputs["instanceName"] = state ? state.instanceName : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["splitKeys"] = state ? state.splitKeys : undefined;
        } else {
            const args = argsOrState as TableArgs | undefined;
            if (!args || args.instanceName === undefined) {
                throw new Error("Missing required property 'instanceName'");
            }
            inputs["instanceName"] = args ? args.instanceName : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["splitKeys"] = args ? args.splitKeys : undefined;
        }
        super("gcp:bigtable/table:Table", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Table resources.
 */
export interface TableState {
    /**
     * The name of the Bigtable instance.
     */
    readonly instanceName?: pulumi.Input<string>;
    /**
     * The name of the table.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * A list of predefined keys to split the table on.
     */
    readonly splitKeys?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a Table resource.
 */
export interface TableArgs {
    /**
     * The name of the Bigtable instance.
     */
    readonly instanceName: pulumi.Input<string>;
    /**
     * The name of the table.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * A list of predefined keys to split the table on.
     */
    readonly splitKeys?: pulumi.Input<pulumi.Input<string>[]>;
}
