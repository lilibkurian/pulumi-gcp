// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Three different resources help you manage IAM policies on dataproc jobs. Each of these resources serves a different use case:
 *
 * * `gcp.dataproc.JobIAMPolicy`: Authoritative. Sets the IAM policy for the job and replaces any existing policy already attached.
 * * `gcp.dataproc.JobIAMBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the job are preserved.
 * * `gcp.dataproc.JobIAMMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the job are preserved.
 *
 * > **Note:** `gcp.dataproc.JobIAMPolicy` **cannot** be used in conjunction with `gcp.dataproc.JobIAMBinding` and `gcp.dataproc.JobIAMMember` or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the job as `gcp.dataproc.JobIAMPolicy` replaces the entire policy.
 *
 * > **Note:** `gcp.dataproc.JobIAMBinding` resources **can be** used in conjunction with `gcp.dataproc.JobIAMMember` resources **only if** they do not grant privilege to the same role.
 */
export class JobIAMMember extends pulumi.CustomResource {
    /**
     * Get an existing JobIAMMember resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: JobIAMMemberState, opts?: pulumi.CustomResourceOptions): JobIAMMember {
        return new JobIAMMember(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:dataproc/jobIAMMember:JobIAMMember';

    /**
     * Returns true if the given object is an instance of JobIAMMember.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is JobIAMMember {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === JobIAMMember.__pulumiType;
    }

    public readonly condition!: pulumi.Output<outputs.dataproc.JobIAMMemberCondition | undefined>;
    /**
     * (Computed) The etag of the jobs's IAM policy.
     */
    public /*out*/ readonly etag!: pulumi.Output<string>;
    public readonly jobId!: pulumi.Output<string>;
    public readonly member!: pulumi.Output<string>;
    /**
     * The project in which the job belongs. If it
     * is not provided, the provider will use a default.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The region in which the job belongs. If it
     * is not provided, the provider will use a default.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.dataproc.JobIAMBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`.
     */
    public readonly role!: pulumi.Output<string>;

    /**
     * Create a JobIAMMember resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: JobIAMMemberArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: JobIAMMemberArgs | JobIAMMemberState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as JobIAMMemberState | undefined;
            inputs["condition"] = state ? state.condition : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["jobId"] = state ? state.jobId : undefined;
            inputs["member"] = state ? state.member : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["role"] = state ? state.role : undefined;
        } else {
            const args = argsOrState as JobIAMMemberArgs | undefined;
            if (!args || args.jobId === undefined) {
                throw new Error("Missing required property 'jobId'");
            }
            if (!args || args.member === undefined) {
                throw new Error("Missing required property 'member'");
            }
            if (!args || args.role === undefined) {
                throw new Error("Missing required property 'role'");
            }
            inputs["condition"] = args ? args.condition : undefined;
            inputs["jobId"] = args ? args.jobId : undefined;
            inputs["member"] = args ? args.member : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["role"] = args ? args.role : undefined;
            inputs["etag"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(JobIAMMember.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering JobIAMMember resources.
 */
export interface JobIAMMemberState {
    readonly condition?: pulumi.Input<inputs.dataproc.JobIAMMemberCondition>;
    /**
     * (Computed) The etag of the jobs's IAM policy.
     */
    readonly etag?: pulumi.Input<string>;
    readonly jobId?: pulumi.Input<string>;
    readonly member?: pulumi.Input<string>;
    /**
     * The project in which the job belongs. If it
     * is not provided, the provider will use a default.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The region in which the job belongs. If it
     * is not provided, the provider will use a default.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.dataproc.JobIAMBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`.
     */
    readonly role?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a JobIAMMember resource.
 */
export interface JobIAMMemberArgs {
    readonly condition?: pulumi.Input<inputs.dataproc.JobIAMMemberCondition>;
    readonly jobId: pulumi.Input<string>;
    readonly member: pulumi.Input<string>;
    /**
     * The project in which the job belongs. If it
     * is not provided, the provider will use a default.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The region in which the job belongs. If it
     * is not provided, the provider will use a default.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.dataproc.JobIAMBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`.
     */
    readonly role: pulumi.Input<string>;
}
