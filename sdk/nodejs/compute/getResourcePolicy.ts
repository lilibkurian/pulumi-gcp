// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_resource_policy.html.markdown.
 */
export function getResourcePolicy(args: GetResourcePolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetResourcePolicyResult> & GetResourcePolicyResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetResourcePolicyResult> = pulumi.runtime.invoke("gcp:compute/getResourcePolicy:getResourcePolicy", {
        "name": args.name,
        "project": args.project,
        "region": args.region,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getResourcePolicy.
 */
export interface GetResourcePolicyArgs {
    /**
     * The name of the Resource Policy.
     */
    readonly name: string;
    /**
     * Project from which to list the Resource Policy. Defaults to project declared in the provider.
     */
    readonly project?: string;
    /**
     * Region where the Resource Policy resides.
     */
    readonly region: string;
}

/**
 * A collection of values returned by getResourcePolicy.
 */
export interface GetResourcePolicyResult {
    /**
     * Description of this Resource Policy.
     */
    readonly description: string;
    readonly name: string;
    readonly project?: string;
    readonly region: string;
    /**
     * The URI of the resource.
     */
    readonly selfLink: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
