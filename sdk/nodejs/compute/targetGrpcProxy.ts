// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Represents a Target gRPC Proxy resource. A target gRPC proxy is a component
 * of load balancers intended for load balancing gRPC traffic. Global forwarding
 * rules reference a target gRPC proxy. The Target gRPC Proxy references
 * a URL map which specifies how traffic routes to gRPC backend services.
 *
 * To get more information about TargetGrpcProxy, see:
 *
 * * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/targetGrpcProxies)
 * * How-to Guides
 *     * [Using Target gRPC Proxies](https://cloud.google.com/traffic-director/docs/proxyless-overview)
 *
 * ## Example Usage
 */
export class TargetGrpcProxy extends pulumi.CustomResource {
    /**
     * Get an existing TargetGrpcProxy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TargetGrpcProxyState, opts?: pulumi.CustomResourceOptions): TargetGrpcProxy {
        return new TargetGrpcProxy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:compute/targetGrpcProxy:TargetGrpcProxy';

    /**
     * Returns true if the given object is an instance of TargetGrpcProxy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TargetGrpcProxy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TargetGrpcProxy.__pulumiType;
    }

    /**
     * Creation timestamp in RFC3339 text format.
     */
    public /*out*/ readonly creationTimestamp!: pulumi.Output<string>;
    /**
     * An optional description of this resource.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
     * This field will be ignored when inserting a TargetGrpcProxy. An up-to-date fingerprint must be provided in order to
     * patch/update the TargetGrpcProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest
     * fingerprint, make a get() request to retrieve the TargetGrpcProxy. A base64-encoded string.
     */
    public /*out*/ readonly fingerprint!: pulumi.Output<string>;
    /**
     * Name of the resource. Provided by the client when the resource
     * is created. The name must be 1-63 characters long, and comply
     * with RFC1035. Specifically, the name must be 1-63 characters long
     * and match the regular expression a-z? which
     * means the first character must be a lowercase letter, and all
     * following characters must be a dash, lowercase letter, or digit,
     * except the last character, which cannot be a dash.
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
     * Server-defined URL with id for the resource.
     */
    public /*out*/ readonly selfLinkWithId!: pulumi.Output<string>;
    /**
     * URL to the UrlMap resource that defines the mapping from URL to
     * the BackendService. The protocol field in the BackendService
     * must be set to GRPC.
     */
    public readonly urlMap!: pulumi.Output<string | undefined>;
    /**
     * If true, indicates that the BackendServices referenced by
     * the urlMap may be accessed by gRPC applications without using
     * a sidecar proxy. This will enable configuration checks on urlMap
     * and its referenced BackendServices to not allow unsupported features.
     * A gRPC application must use "xds:///" scheme in the target URI
     * of the service it is connecting to. If false, indicates that the
     * BackendServices referenced by the urlMap will be accessed by gRPC
     * applications via a sidecar proxy. In this case, a gRPC application
     * must not use "xds:///" scheme in the target URI of the service
     * it is connecting to
     */
    public readonly validateForProxyless!: pulumi.Output<boolean | undefined>;

    /**
     * Create a TargetGrpcProxy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: TargetGrpcProxyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TargetGrpcProxyArgs | TargetGrpcProxyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as TargetGrpcProxyState | undefined;
            inputs["creationTimestamp"] = state ? state.creationTimestamp : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["fingerprint"] = state ? state.fingerprint : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["selfLink"] = state ? state.selfLink : undefined;
            inputs["selfLinkWithId"] = state ? state.selfLinkWithId : undefined;
            inputs["urlMap"] = state ? state.urlMap : undefined;
            inputs["validateForProxyless"] = state ? state.validateForProxyless : undefined;
        } else {
            const args = argsOrState as TargetGrpcProxyArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["urlMap"] = args ? args.urlMap : undefined;
            inputs["validateForProxyless"] = args ? args.validateForProxyless : undefined;
            inputs["creationTimestamp"] = undefined /*out*/;
            inputs["fingerprint"] = undefined /*out*/;
            inputs["selfLink"] = undefined /*out*/;
            inputs["selfLinkWithId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(TargetGrpcProxy.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TargetGrpcProxy resources.
 */
export interface TargetGrpcProxyState {
    /**
     * Creation timestamp in RFC3339 text format.
     */
    readonly creationTimestamp?: pulumi.Input<string>;
    /**
     * An optional description of this resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
     * This field will be ignored when inserting a TargetGrpcProxy. An up-to-date fingerprint must be provided in order to
     * patch/update the TargetGrpcProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest
     * fingerprint, make a get() request to retrieve the TargetGrpcProxy. A base64-encoded string.
     */
    readonly fingerprint?: pulumi.Input<string>;
    /**
     * Name of the resource. Provided by the client when the resource
     * is created. The name must be 1-63 characters long, and comply
     * with RFC1035. Specifically, the name must be 1-63 characters long
     * and match the regular expression a-z? which
     * means the first character must be a lowercase letter, and all
     * following characters must be a dash, lowercase letter, or digit,
     * except the last character, which cannot be a dash.
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
     * Server-defined URL with id for the resource.
     */
    readonly selfLinkWithId?: pulumi.Input<string>;
    /**
     * URL to the UrlMap resource that defines the mapping from URL to
     * the BackendService. The protocol field in the BackendService
     * must be set to GRPC.
     */
    readonly urlMap?: pulumi.Input<string>;
    /**
     * If true, indicates that the BackendServices referenced by
     * the urlMap may be accessed by gRPC applications without using
     * a sidecar proxy. This will enable configuration checks on urlMap
     * and its referenced BackendServices to not allow unsupported features.
     * A gRPC application must use "xds:///" scheme in the target URI
     * of the service it is connecting to. If false, indicates that the
     * BackendServices referenced by the urlMap will be accessed by gRPC
     * applications via a sidecar proxy. In this case, a gRPC application
     * must not use "xds:///" scheme in the target URI of the service
     * it is connecting to
     */
    readonly validateForProxyless?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a TargetGrpcProxy resource.
 */
export interface TargetGrpcProxyArgs {
    /**
     * An optional description of this resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Name of the resource. Provided by the client when the resource
     * is created. The name must be 1-63 characters long, and comply
     * with RFC1035. Specifically, the name must be 1-63 characters long
     * and match the regular expression a-z? which
     * means the first character must be a lowercase letter, and all
     * following characters must be a dash, lowercase letter, or digit,
     * except the last character, which cannot be a dash.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * URL to the UrlMap resource that defines the mapping from URL to
     * the BackendService. The protocol field in the BackendService
     * must be set to GRPC.
     */
    readonly urlMap?: pulumi.Input<string>;
    /**
     * If true, indicates that the BackendServices referenced by
     * the urlMap may be accessed by gRPC applications without using
     * a sidecar proxy. This will enable configuration checks on urlMap
     * and its referenced BackendServices to not allow unsupported features.
     * A gRPC application must use "xds:///" scheme in the target URI
     * of the service it is connecting to. If false, indicates that the
     * BackendServices referenced by the urlMap will be accessed by gRPC
     * applications via a sidecar proxy. In this case, a gRPC application
     * must not use "xds:///" scheme in the target URI of the service
     * it is connecting to
     */
    readonly validateForProxyless?: pulumi.Input<boolean>;
}
