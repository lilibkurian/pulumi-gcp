// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Three different resources help you manage your IAM policy for BigQuery Table. Each of these resources serves a different use case:
 *
 * * `gcp.bigquery.IamPolicy`: Authoritative. Sets the IAM policy for the table and replaces any existing policy already attached.
 * * `gcp.bigquery.IamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the table are preserved.
 * * `gcp.bigquery.IamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the table are preserved.
 *
 * > **Note:** `gcp.bigquery.IamPolicy` **cannot** be used in conjunction with `gcp.bigquery.IamBinding` and `gcp.bigquery.IamMember` or they will fight over what your policy should be.
 *
 * > **Note:** `gcp.bigquery.IamBinding` resources **can be** used in conjunction with `gcp.bigquery.IamMember` resources **only if** they do not grant privilege to the same role.
 */
export class IamMember extends pulumi.CustomResource {
    /**
     * Get an existing IamMember resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IamMemberState, opts?: pulumi.CustomResourceOptions): IamMember {
        return new IamMember(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:bigquery/iamMember:IamMember';

    /**
     * Returns true if the given object is an instance of IamMember.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IamMember {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IamMember.__pulumiType;
    }

    /**
     * An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
     * Structure is documented below.
     */
    public readonly condition!: pulumi.Output<outputs.bigquery.IamMemberCondition | undefined>;
    public readonly datasetId!: pulumi.Output<string>;
    /**
     * (Computed) The etag of the IAM policy.
     */
    public /*out*/ readonly etag!: pulumi.Output<string>;
    public readonly member!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.bigquery.IamBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`.
     */
    public readonly role!: pulumi.Output<string>;
    public readonly tableId!: pulumi.Output<string>;

    /**
     * Create a IamMember resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IamMemberArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IamMemberArgs | IamMemberState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as IamMemberState | undefined;
            inputs["condition"] = state ? state.condition : undefined;
            inputs["datasetId"] = state ? state.datasetId : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["member"] = state ? state.member : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["role"] = state ? state.role : undefined;
            inputs["tableId"] = state ? state.tableId : undefined;
        } else {
            const args = argsOrState as IamMemberArgs | undefined;
            if (!args || args.datasetId === undefined) {
                throw new Error("Missing required property 'datasetId'");
            }
            if (!args || args.member === undefined) {
                throw new Error("Missing required property 'member'");
            }
            if (!args || args.role === undefined) {
                throw new Error("Missing required property 'role'");
            }
            if (!args || args.tableId === undefined) {
                throw new Error("Missing required property 'tableId'");
            }
            inputs["condition"] = args ? args.condition : undefined;
            inputs["datasetId"] = args ? args.datasetId : undefined;
            inputs["member"] = args ? args.member : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["role"] = args ? args.role : undefined;
            inputs["tableId"] = args ? args.tableId : undefined;
            inputs["etag"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(IamMember.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IamMember resources.
 */
export interface IamMemberState {
    /**
     * An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
     * Structure is documented below.
     */
    readonly condition?: pulumi.Input<inputs.bigquery.IamMemberCondition>;
    readonly datasetId?: pulumi.Input<string>;
    /**
     * (Computed) The etag of the IAM policy.
     */
    readonly etag?: pulumi.Input<string>;
    readonly member?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.bigquery.IamBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`.
     */
    readonly role?: pulumi.Input<string>;
    readonly tableId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IamMember resource.
 */
export interface IamMemberArgs {
    /**
     * An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
     * Structure is documented below.
     */
    readonly condition?: pulumi.Input<inputs.bigquery.IamMemberCondition>;
    readonly datasetId: pulumi.Input<string>;
    readonly member: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.bigquery.IamBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`.
     */
    readonly role: pulumi.Input<string>;
    readonly tableId: pulumi.Input<string>;
}
