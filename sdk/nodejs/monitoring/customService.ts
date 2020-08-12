// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * A Service is a discrete, autonomous, and network-accessible unit,
 * designed to solve an individual concern (Wikipedia). In Cloud Monitoring,
 * a Service acts as the root resource under which operational aspects of
 * the service are accessible
 *
 * To get more information about Service, see:
 *
 * * [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services)
 * * How-to Guides
 *     * [Service Monitoring](https://cloud.google.com/monitoring/service-monitoring)
 *     * [Monitoring API Documentation](https://cloud.google.com/monitoring/api/v3/)
 *
 * ## Example Usage
 */
export class CustomService extends pulumi.CustomResource {
    /**
     * Get an existing CustomService resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CustomServiceState, opts?: pulumi.CustomResourceOptions): CustomService {
        return new CustomService(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:monitoring/customService:CustomService';

    /**
     * Returns true if the given object is an instance of CustomService.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CustomService {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CustomService.__pulumiType;
    }

    /**
     * Name used for UI elements listing this Service.
     */
    public readonly displayName!: pulumi.Output<string | undefined>;
    /**
     * The full resource name for this service. The syntax is: projects/[PROJECT_ID]/services/[SERVICE_ID].
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * An optional service ID to use. If not given, the server will generate a
     * service ID.
     */
    public readonly serviceId!: pulumi.Output<string>;
    /**
     * Configuration for how to query telemetry on a Service.
     * Structure is documented below.
     */
    public readonly telemetry!: pulumi.Output<outputs.monitoring.CustomServiceTelemetry | undefined>;

    /**
     * Create a CustomService resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: CustomServiceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CustomServiceArgs | CustomServiceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as CustomServiceState | undefined;
            inputs["displayName"] = state ? state.displayName : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["serviceId"] = state ? state.serviceId : undefined;
            inputs["telemetry"] = state ? state.telemetry : undefined;
        } else {
            const args = argsOrState as CustomServiceArgs | undefined;
            inputs["displayName"] = args ? args.displayName : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["serviceId"] = args ? args.serviceId : undefined;
            inputs["telemetry"] = args ? args.telemetry : undefined;
            inputs["name"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(CustomService.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CustomService resources.
 */
export interface CustomServiceState {
    /**
     * Name used for UI elements listing this Service.
     */
    readonly displayName?: pulumi.Input<string>;
    /**
     * The full resource name for this service. The syntax is: projects/[PROJECT_ID]/services/[SERVICE_ID].
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * An optional service ID to use. If not given, the server will generate a
     * service ID.
     */
    readonly serviceId?: pulumi.Input<string>;
    /**
     * Configuration for how to query telemetry on a Service.
     * Structure is documented below.
     */
    readonly telemetry?: pulumi.Input<inputs.monitoring.CustomServiceTelemetry>;
}

/**
 * The set of arguments for constructing a CustomService resource.
 */
export interface CustomServiceArgs {
    /**
     * Name used for UI elements listing this Service.
     */
    readonly displayName?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * An optional service ID to use. If not given, the server will generate a
     * service ID.
     */
    readonly serviceId?: pulumi.Input<string>;
    /**
     * Configuration for how to query telemetry on a Service.
     * Structure is documented below.
     */
    readonly telemetry?: pulumi.Input<inputs.monitoring.CustomServiceTelemetry>;
}
