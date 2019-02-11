// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * A Lien represents an encumbrance on the actions that can be performed on a resource.
 * 
 * 
 * 
 * ## Example Usage - Resource Manager Lien
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const project = new gcp.organizations.Project("project", {
 *     projectId: "staging-project",
 * });
 * const lien = new gcp.resourcemanager.Lien("lien", {
 *     origin: "machine-readable-explanation",
 *     parent: project.number.apply(number => `projects/${number}`),
 *     reason: "This project is an important environment",
 *     restrictions: ["resourcemanager.projects.delete"],
 * });
 * ```
 */
export class Lien extends pulumi.CustomResource {
    /**
     * Get an existing Lien resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LienState, opts?: pulumi.CustomResourceOptions): Lien {
        return new Lien(name, <any>state, { ...opts, id: id });
    }

    public /*out*/ readonly createTime: pulumi.Output<string>;
    public /*out*/ readonly name: pulumi.Output<string>;
    public readonly origin: pulumi.Output<string>;
    public readonly parent: pulumi.Output<string>;
    public readonly reason: pulumi.Output<string>;
    public readonly restrictions: pulumi.Output<string[]>;

    /**
     * Create a Lien resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LienArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LienArgs | LienState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: LienState = argsOrState as LienState | undefined;
            inputs["createTime"] = state ? state.createTime : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["origin"] = state ? state.origin : undefined;
            inputs["parent"] = state ? state.parent : undefined;
            inputs["reason"] = state ? state.reason : undefined;
            inputs["restrictions"] = state ? state.restrictions : undefined;
        } else {
            const args = argsOrState as LienArgs | undefined;
            if (!args || args.origin === undefined) {
                throw new Error("Missing required property 'origin'");
            }
            if (!args || args.parent === undefined) {
                throw new Error("Missing required property 'parent'");
            }
            if (!args || args.reason === undefined) {
                throw new Error("Missing required property 'reason'");
            }
            if (!args || args.restrictions === undefined) {
                throw new Error("Missing required property 'restrictions'");
            }
            inputs["origin"] = args ? args.origin : undefined;
            inputs["parent"] = args ? args.parent : undefined;
            inputs["reason"] = args ? args.reason : undefined;
            inputs["restrictions"] = args ? args.restrictions : undefined;
            inputs["createTime"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
        }
        super("gcp:resourcemanager/lien:Lien", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Lien resources.
 */
export interface LienState {
    readonly createTime?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly origin?: pulumi.Input<string>;
    readonly parent?: pulumi.Input<string>;
    readonly reason?: pulumi.Input<string>;
    readonly restrictions?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a Lien resource.
 */
export interface LienArgs {
    readonly origin: pulumi.Input<string>;
    readonly parent: pulumi.Input<string>;
    readonly reason: pulumi.Input<string>;
    readonly restrictions: pulumi.Input<pulumi.Input<string>[]>;
}
