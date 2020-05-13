// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * A consumer override is applied to the consumer on its own authority to limit its own quota usage.
 * Consumer overrides cannot be used to grant more quota than would be allowed by admin overrides,
 * producer overrides, or the default limit of the service.
 * 
 * To get more information about ConsumerQuotaOverride, see:
 * 
 * * How-to Guides
 *     * [Getting Started](https://cloud.google.com/service-usage/docs/getting-started)
 *     * [REST API documentation](https://cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides)
 * 
 * ## Example Usage - Consumer Quota Override
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const myProject = new gcp.organizations.Project("myProject", {
 *     projectId: "quota",
 *     orgId: "123456789",
 * });
 * const override = new gcp.serviceusage.ConsumerQuotaOverride("override", {
 *     project: myProject.projectId,
 *     service: "servicemanagement.googleapis.com",
 *     metric: `servicemanagement.googleapis.com%2Fdefault_requests`,
 *     limit: `%2Fmin%2Fproject`,
 *     overrideValue: "95",
 *     force: true,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_usage_consumer_quota_override.html.markdown.
 */
export class ConsumerQuotaOverride extends pulumi.CustomResource {
    /**
     * Get an existing ConsumerQuotaOverride resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConsumerQuotaOverrideState, opts?: pulumi.CustomResourceOptions): ConsumerQuotaOverride {
        return new ConsumerQuotaOverride(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:serviceusage/consumerQuotaOverride:ConsumerQuotaOverride';

    /**
     * Returns true if the given object is an instance of ConsumerQuotaOverride.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConsumerQuotaOverride {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConsumerQuotaOverride.__pulumiType;
    }

    /**
     * If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
     */
    public readonly dimensions!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * If the new quota would decrease the existing quota by more than 10%, the request is rejected.
     * If `force` is `true`, that safety check is ignored.
     */
    public readonly force!: pulumi.Output<boolean | undefined>;
    /**
     * The limit on the metric, e.g. `/project/region`.
     */
    public readonly limit!: pulumi.Output<string>;
    /**
     * The metric that should be limited, e.g. `compute.googleapis.com/cpus`.
     */
    public readonly metric!: pulumi.Output<string>;
    /**
     * The server-generated name of the quota override.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
     */
    public readonly overrideValue!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The service that the metrics belong to, e.g. `compute.googleapis.com`.
     */
    public readonly service!: pulumi.Output<string>;

    /**
     * Create a ConsumerQuotaOverride resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConsumerQuotaOverrideArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ConsumerQuotaOverrideArgs | ConsumerQuotaOverrideState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ConsumerQuotaOverrideState | undefined;
            inputs["dimensions"] = state ? state.dimensions : undefined;
            inputs["force"] = state ? state.force : undefined;
            inputs["limit"] = state ? state.limit : undefined;
            inputs["metric"] = state ? state.metric : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["overrideValue"] = state ? state.overrideValue : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["service"] = state ? state.service : undefined;
        } else {
            const args = argsOrState as ConsumerQuotaOverrideArgs | undefined;
            if (!args || args.limit === undefined) {
                throw new Error("Missing required property 'limit'");
            }
            if (!args || args.metric === undefined) {
                throw new Error("Missing required property 'metric'");
            }
            if (!args || args.overrideValue === undefined) {
                throw new Error("Missing required property 'overrideValue'");
            }
            if (!args || args.service === undefined) {
                throw new Error("Missing required property 'service'");
            }
            inputs["dimensions"] = args ? args.dimensions : undefined;
            inputs["force"] = args ? args.force : undefined;
            inputs["limit"] = args ? args.limit : undefined;
            inputs["metric"] = args ? args.metric : undefined;
            inputs["overrideValue"] = args ? args.overrideValue : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["service"] = args ? args.service : undefined;
            inputs["name"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ConsumerQuotaOverride.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ConsumerQuotaOverride resources.
 */
export interface ConsumerQuotaOverrideState {
    /**
     * If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
     */
    readonly dimensions?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * If the new quota would decrease the existing quota by more than 10%, the request is rejected.
     * If `force` is `true`, that safety check is ignored.
     */
    readonly force?: pulumi.Input<boolean>;
    /**
     * The limit on the metric, e.g. `/project/region`.
     */
    readonly limit?: pulumi.Input<string>;
    /**
     * The metric that should be limited, e.g. `compute.googleapis.com/cpus`.
     */
    readonly metric?: pulumi.Input<string>;
    /**
     * The server-generated name of the quota override.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
     */
    readonly overrideValue?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The service that the metrics belong to, e.g. `compute.googleapis.com`.
     */
    readonly service?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ConsumerQuotaOverride resource.
 */
export interface ConsumerQuotaOverrideArgs {
    /**
     * If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
     */
    readonly dimensions?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * If the new quota would decrease the existing quota by more than 10%, the request is rejected.
     * If `force` is `true`, that safety check is ignored.
     */
    readonly force?: pulumi.Input<boolean>;
    /**
     * The limit on the metric, e.g. `/project/region`.
     */
    readonly limit: pulumi.Input<string>;
    /**
     * The metric that should be limited, e.g. `compute.googleapis.com/cpus`.
     */
    readonly metric: pulumi.Input<string>;
    /**
     * The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
     */
    readonly overrideValue: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The service that the metrics belong to, e.g. `compute.googleapis.com`.
     */
    readonly service: pulumi.Input<string>;
}