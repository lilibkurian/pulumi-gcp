// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Allows management of Organization policies for a Google Organization. For more information see
 * [the official
 * documentation](https://cloud.google.com/resource-manager/docs/organization-policy/overview) and
 * [API](https://cloud.google.com/resource-manager/reference/rest/v1/organizations/setOrgPolicy).
 * 
 * ## Example Usage
 * 
 * To set policy with a [boolean constraint](https://cloud.google.com/resource-manager/docs/organization-policy/quickstart-boolean-constraints):
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const serialPortPolicy = new gcp.organizations.Policy("serial_port_policy", {
 *     booleanPolicy: {
 *         enforced: true,
 *     },
 *     constraint: "compute.disableSerialPortAccess",
 *     orgId: "123456789",
 * });
 * ```
 * 
 * 
 * To set a policy with a [list contraint](https://cloud.google.com/resource-manager/docs/organization-policy/quickstart-list-constraints):
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const servicesPolicy = new gcp.organizations.Policy("services_policy", {
 *     constraint: "serviceuser.services",
 *     listPolicy: {
 *         allow: {
 *             all: true,
 *         },
 *     },
 *     orgId: "123456789",
 * });
 * ```
 * 
 * Or to deny some services, use the following instead:
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const servicesPolicy = new gcp.organizations.Policy("services_policy", {
 *     constraint: "serviceuser.services",
 *     listPolicy: {
 *         deny: {
 *             values: ["cloudresourcemanager.googleapis.com"],
 *         },
 *         suggestedValues: "compute.googleapis.com",
 *     },
 *     orgId: "123456789",
 * });
 * ```
 * 
 * To restore the default organization policy, use the following instead:
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const servicesPolicy = new gcp.organizations.Policy("services_policy", {
 *     constraint: "serviceuser.services",
 *     orgId: "123456789",
 *     restorePolicy: {
 *         default: true,
 *     },
 * });
 * ```
 */
export class Policy extends pulumi.CustomResource {
    /**
     * Get an existing Policy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState, opts?: pulumi.CustomResourceOptions): Policy {
        return new Policy(name, <any>state, { ...opts, id: id });
    }

    /**
     * A boolean policy is a constraint that is either enforced or not. Structure is documented below. 
     */
    public readonly booleanPolicy: pulumi.Output<{ enforced: boolean } | undefined>;
    /**
     * The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
     */
    public readonly constraint: pulumi.Output<string>;
    /**
     * (Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. 
     */
    public /*out*/ readonly etag: pulumi.Output<string>;
    /**
     * A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
     */
    public readonly listPolicy: pulumi.Output<{ allow?: { all?: boolean, values?: string[] }, deny?: { all?: boolean, values?: string[] }, suggestedValue: string } | undefined>;
    /**
     * The numeric ID of the organization to set the policy for.
     */
    public readonly orgId: pulumi.Output<string>;
    /**
     * A restore policy is a constraint to restore the default policy. Structure is documented below. 
     */
    public readonly restorePolicy: pulumi.Output<{ default: boolean } | undefined>;
    /**
     * (Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
     */
    public /*out*/ readonly updateTime: pulumi.Output<string>;
    /**
     * Version of the Policy. Default version is 0.
     */
    public readonly version: pulumi.Output<number>;

    /**
     * Create a Policy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PolicyArgs | PolicyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: PolicyState = argsOrState as PolicyState | undefined;
            inputs["booleanPolicy"] = state ? state.booleanPolicy : undefined;
            inputs["constraint"] = state ? state.constraint : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["listPolicy"] = state ? state.listPolicy : undefined;
            inputs["orgId"] = state ? state.orgId : undefined;
            inputs["restorePolicy"] = state ? state.restorePolicy : undefined;
            inputs["updateTime"] = state ? state.updateTime : undefined;
            inputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as PolicyArgs | undefined;
            if (!args || args.constraint === undefined) {
                throw new Error("Missing required property 'constraint'");
            }
            if (!args || args.orgId === undefined) {
                throw new Error("Missing required property 'orgId'");
            }
            inputs["booleanPolicy"] = args ? args.booleanPolicy : undefined;
            inputs["constraint"] = args ? args.constraint : undefined;
            inputs["listPolicy"] = args ? args.listPolicy : undefined;
            inputs["orgId"] = args ? args.orgId : undefined;
            inputs["restorePolicy"] = args ? args.restorePolicy : undefined;
            inputs["version"] = args ? args.version : undefined;
            inputs["etag"] = undefined /*out*/;
            inputs["updateTime"] = undefined /*out*/;
        }
        super("gcp:organizations/policy:Policy", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Policy resources.
 */
export interface PolicyState {
    /**
     * A boolean policy is a constraint that is either enforced or not. Structure is documented below. 
     */
    readonly booleanPolicy?: pulumi.Input<{ enforced: pulumi.Input<boolean> }>;
    /**
     * The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
     */
    readonly constraint?: pulumi.Input<string>;
    /**
     * (Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. 
     */
    readonly etag?: pulumi.Input<string>;
    /**
     * A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
     */
    readonly listPolicy?: pulumi.Input<{ allow?: pulumi.Input<{ all?: pulumi.Input<boolean>, values?: pulumi.Input<pulumi.Input<string>[]> }>, deny?: pulumi.Input<{ all?: pulumi.Input<boolean>, values?: pulumi.Input<pulumi.Input<string>[]> }>, suggestedValue?: pulumi.Input<string> }>;
    /**
     * The numeric ID of the organization to set the policy for.
     */
    readonly orgId?: pulumi.Input<string>;
    /**
     * A restore policy is a constraint to restore the default policy. Structure is documented below. 
     */
    readonly restorePolicy?: pulumi.Input<{ default: pulumi.Input<boolean> }>;
    /**
     * (Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
     */
    readonly updateTime?: pulumi.Input<string>;
    /**
     * Version of the Policy. Default version is 0.
     */
    readonly version?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Policy resource.
 */
export interface PolicyArgs {
    /**
     * A boolean policy is a constraint that is either enforced or not. Structure is documented below. 
     */
    readonly booleanPolicy?: pulumi.Input<{ enforced: pulumi.Input<boolean> }>;
    /**
     * The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
     */
    readonly constraint: pulumi.Input<string>;
    /**
     * A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
     */
    readonly listPolicy?: pulumi.Input<{ allow?: pulumi.Input<{ all?: pulumi.Input<boolean>, values?: pulumi.Input<pulumi.Input<string>[]> }>, deny?: pulumi.Input<{ all?: pulumi.Input<boolean>, values?: pulumi.Input<pulumi.Input<string>[]> }>, suggestedValue?: pulumi.Input<string> }>;
    /**
     * The numeric ID of the organization to set the policy for.
     */
    readonly orgId: pulumi.Input<string>;
    /**
     * A restore policy is a constraint to restore the default policy. Structure is documented below. 
     */
    readonly restorePolicy?: pulumi.Input<{ default: pulumi.Input<boolean> }>;
    /**
     * Version of the Policy. Default version is 0.
     */
    readonly version?: pulumi.Input<number>;
}
