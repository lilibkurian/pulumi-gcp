// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Represents a MachineImage resource. Machine images store all the configuration,
 * metadata, permissions, and data from one or more disks required to create a
 * Virtual machine (VM) instance.
 *
 * To get more information about MachineImage, see:
 *
 * * [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/machineImages)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/compute/docs/machine-images)
 *
 * ## Example Usage - Machine Image Basic
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const vm = new gcp.compute.Instance("vm", {
 *     machineType: "n1-standard-1",
 *     boot_disk: {
 *         initialize_params: {
 *             image: "debian-cloud/debian-9",
 *         },
 *     },
 *     network_interface: [{
 *         network: "default",
 *     }],
 * });
 * const image = new gcp.compute.MachineImage("image", {sourceInstance: vm.selfLink});
 * ```
 */
export class MachineImage extends pulumi.CustomResource {
    /**
     * Get an existing MachineImage resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MachineImageState, opts?: pulumi.CustomResourceOptions): MachineImage {
        return new MachineImage(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:compute/machineImage:MachineImage';

    /**
     * Returns true if the given object is an instance of MachineImage.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MachineImage {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MachineImage.__pulumiType;
    }

    /**
     * A text description of the resource.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Name of the resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The URI of the created resource.
     */
    public /*out*/ readonly selfLink!: pulumi.Output<string>;
    /**
     * The source instance used to create the machine image. You can provide this as a partial or full URL to the resource.
     */
    public readonly sourceInstance!: pulumi.Output<string>;

    /**
     * Create a MachineImage resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MachineImageArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MachineImageArgs | MachineImageState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as MachineImageState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["selfLink"] = state ? state.selfLink : undefined;
            inputs["sourceInstance"] = state ? state.sourceInstance : undefined;
        } else {
            const args = argsOrState as MachineImageArgs | undefined;
            if (!args || args.sourceInstance === undefined) {
                throw new Error("Missing required property 'sourceInstance'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["sourceInstance"] = args ? args.sourceInstance : undefined;
            inputs["selfLink"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(MachineImage.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MachineImage resources.
 */
export interface MachineImageState {
    /**
     * A text description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The URI of the created resource.
     */
    readonly selfLink?: pulumi.Input<string>;
    /**
     * The source instance used to create the machine image. You can provide this as a partial or full URL to the resource.
     */
    readonly sourceInstance?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MachineImage resource.
 */
export interface MachineImageArgs {
    /**
     * A text description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Name of the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The source instance used to create the machine image. You can provide this as a partial or full URL to the resource.
     */
    readonly sourceInstance: pulumi.Input<string>;
}
