// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * A domain serving an App Engine application.
 *
 * To get more information about DomainMapping, see:
 *
 * * [API documentation](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/appengine/docs/standard/python/mapping-custom-domains)
 *
 * ## Example Usage
 */
export class DomainMapping extends pulumi.CustomResource {
    /**
     * Get an existing DomainMapping resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainMappingState, opts?: pulumi.CustomResourceOptions): DomainMapping {
        return new DomainMapping(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:appengine/domainMapping:DomainMapping';

    /**
     * Returns true if the given object is an instance of DomainMapping.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DomainMapping {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DomainMapping.__pulumiType;
    }

    /**
     * Relative name of the domain serving the application. Example: example.com.
     */
    public readonly domainName!: pulumi.Output<string>;
    /**
     * Full path to the DomainMapping resource in the API. Example: apps/myapp/domainMapping/example.com.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * Whether the domain creation should override any existing mappings for this domain.
     * By default, overrides are rejected.
     * Default value is `STRICT`.
     * Possible values are `STRICT` and `OVERRIDE`.
     */
    public readonly overrideStrategy!: pulumi.Output<string | undefined>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The resource records required to configure this domain mapping. These records must be added to the domain's DNS
     * configuration in order to serve the application via this domain mapping.
     */
    public /*out*/ readonly resourceRecords!: pulumi.Output<outputs.appengine.DomainMappingResourceRecord[]>;
    /**
     * SSL configuration for this domain. If unconfigured, this domain will not serve with SSL.
     * Structure is documented below.
     */
    public readonly sslSettings!: pulumi.Output<outputs.appengine.DomainMappingSslSettings | undefined>;

    /**
     * Create a DomainMapping resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DomainMappingArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DomainMappingArgs | DomainMappingState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DomainMappingState | undefined;
            inputs["domainName"] = state ? state.domainName : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["overrideStrategy"] = state ? state.overrideStrategy : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["resourceRecords"] = state ? state.resourceRecords : undefined;
            inputs["sslSettings"] = state ? state.sslSettings : undefined;
        } else {
            const args = argsOrState as DomainMappingArgs | undefined;
            if (!args || args.domainName === undefined) {
                throw new Error("Missing required property 'domainName'");
            }
            inputs["domainName"] = args ? args.domainName : undefined;
            inputs["overrideStrategy"] = args ? args.overrideStrategy : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["sslSettings"] = args ? args.sslSettings : undefined;
            inputs["name"] = undefined /*out*/;
            inputs["resourceRecords"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(DomainMapping.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DomainMapping resources.
 */
export interface DomainMappingState {
    /**
     * Relative name of the domain serving the application. Example: example.com.
     */
    readonly domainName?: pulumi.Input<string>;
    /**
     * Full path to the DomainMapping resource in the API. Example: apps/myapp/domainMapping/example.com.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Whether the domain creation should override any existing mappings for this domain.
     * By default, overrides are rejected.
     * Default value is `STRICT`.
     * Possible values are `STRICT` and `OVERRIDE`.
     */
    readonly overrideStrategy?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The resource records required to configure this domain mapping. These records must be added to the domain's DNS
     * configuration in order to serve the application via this domain mapping.
     */
    readonly resourceRecords?: pulumi.Input<pulumi.Input<inputs.appengine.DomainMappingResourceRecord>[]>;
    /**
     * SSL configuration for this domain. If unconfigured, this domain will not serve with SSL.
     * Structure is documented below.
     */
    readonly sslSettings?: pulumi.Input<inputs.appengine.DomainMappingSslSettings>;
}

/**
 * The set of arguments for constructing a DomainMapping resource.
 */
export interface DomainMappingArgs {
    /**
     * Relative name of the domain serving the application. Example: example.com.
     */
    readonly domainName: pulumi.Input<string>;
    /**
     * Whether the domain creation should override any existing mappings for this domain.
     * By default, overrides are rejected.
     * Default value is `STRICT`.
     * Possible values are `STRICT` and `OVERRIDE`.
     */
    readonly overrideStrategy?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * SSL configuration for this domain. If unconfigured, this domain will not serve with SSL.
     * Structure is documented below.
     */
    readonly sslSettings?: pulumi.Input<inputs.appengine.DomainMappingSslSettings>;
}
