// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Represents a machine learning solution.
 *
 * A model can have multiple versions, each of which is a deployed, trained model
 * ready to receive prediction requests. The model itself is just a container.
 *
 * ## Example Usage
 */
export class EngineModel extends pulumi.CustomResource {
    /**
     * Get an existing EngineModel resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EngineModelState, opts?: pulumi.CustomResourceOptions): EngineModel {
        return new EngineModel(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:ml/engineModel:EngineModel';

    /**
     * Returns true if the given object is an instance of EngineModel.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is EngineModel {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === EngineModel.__pulumiType;
    }

    /**
     * The default version of the model. This version will be used to handle
     * prediction requests that do not specify a version.
     * Structure is documented below.
     */
    public readonly defaultVersion!: pulumi.Output<outputs.ml.EngineModelDefaultVersion | undefined>;
    /**
     * The description specified for the model when it was created.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * One or more labels that you can add, to organize your models.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The name specified for the version when it was created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
     */
    public readonly onlinePredictionConsoleLogging!: pulumi.Output<boolean | undefined>;
    /**
     * If true, online prediction access logs are sent to StackDriver Logging.
     */
    public readonly onlinePredictionLogging!: pulumi.Output<boolean | undefined>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The list of regions where the model is going to be deployed.
     * Currently only one region per model is supported
     */
    public readonly regions!: pulumi.Output<string | undefined>;

    /**
     * Create a EngineModel resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: EngineModelArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: EngineModelArgs | EngineModelState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as EngineModelState | undefined;
            inputs["defaultVersion"] = state ? state.defaultVersion : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["onlinePredictionConsoleLogging"] = state ? state.onlinePredictionConsoleLogging : undefined;
            inputs["onlinePredictionLogging"] = state ? state.onlinePredictionLogging : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["regions"] = state ? state.regions : undefined;
        } else {
            const args = argsOrState as EngineModelArgs | undefined;
            inputs["defaultVersion"] = args ? args.defaultVersion : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["onlinePredictionConsoleLogging"] = args ? args.onlinePredictionConsoleLogging : undefined;
            inputs["onlinePredictionLogging"] = args ? args.onlinePredictionLogging : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["regions"] = args ? args.regions : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(EngineModel.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering EngineModel resources.
 */
export interface EngineModelState {
    /**
     * The default version of the model. This version will be used to handle
     * prediction requests that do not specify a version.
     * Structure is documented below.
     */
    readonly defaultVersion?: pulumi.Input<inputs.ml.EngineModelDefaultVersion>;
    /**
     * The description specified for the model when it was created.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * One or more labels that you can add, to organize your models.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The name specified for the version when it was created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
     */
    readonly onlinePredictionConsoleLogging?: pulumi.Input<boolean>;
    /**
     * If true, online prediction access logs are sent to StackDriver Logging.
     */
    readonly onlinePredictionLogging?: pulumi.Input<boolean>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The list of regions where the model is going to be deployed.
     * Currently only one region per model is supported
     */
    readonly regions?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a EngineModel resource.
 */
export interface EngineModelArgs {
    /**
     * The default version of the model. This version will be used to handle
     * prediction requests that do not specify a version.
     * Structure is documented below.
     */
    readonly defaultVersion?: pulumi.Input<inputs.ml.EngineModelDefaultVersion>;
    /**
     * The description specified for the model when it was created.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * One or more labels that you can add, to organize your models.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The name specified for the version when it was created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
     */
    readonly onlinePredictionConsoleLogging?: pulumi.Input<boolean>;
    /**
     * If true, online prediction access logs are sent to StackDriver Logging.
     */
    readonly onlinePredictionLogging?: pulumi.Input<boolean>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The list of regions where the model is going to be deployed.
     * Currently only one region per model is supported
     */
    readonly regions?: pulumi.Input<string>;
}
