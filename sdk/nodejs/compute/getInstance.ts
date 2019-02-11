// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Get information about a VM instance resource within GCE. For more information see
 * [the official documentation](https://cloud.google.com/compute/docs/instances)
 * and
 * [API](https://cloud.google.com/compute/docs/reference/latest/instances).
 * 
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const appserver = pulumi.output(gcp.compute.getInstance({
 *     name: "primary-application-server",
 *     zone: "us-central1-a",
 * }));
 * ```
 */
export function getInstance(args: GetInstanceArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceResult> {
    return pulumi.runtime.invoke("gcp:compute/getInstance:getInstance", {
        "name": args.name,
        "project": args.project,
        "zone": args.zone,
    }, opts);
}

/**
 * A collection of arguments for invoking getInstance.
 */
export interface GetInstanceArgs {
    /**
     * The name of the instance. One of `name` or `self_link` must be provided.
     */
    readonly name: string;
    /**
     * The ID of the project in which the resource belongs.
     * If `self_link` is provided, this value is ignored.  If neither `self_link`
     * nor `project` are provided, the provider project is used.
     */
    readonly project?: string;
    /**
     * The zone of the instance. If `self_link` is provided, this
     * value is ignored.  If neither `self_link` nor `zone` are provided, the
     * provider zone is used.
     */
    readonly zone?: string;
}

/**
 * A collection of values returned by getInstance.
 */
export interface GetInstanceResult {
    readonly allowStoppingForUpdate: boolean;
    /**
     * List of disks attached to the instance. Structure is documented below.
     */
    readonly attachedDisks: { deviceName: string, diskEncryptionKeyRaw: string, diskEncryptionKeySha256: string, mode: string, source: string }[];
    /**
     * The boot disk for the instance. Sructure is documented below.
     */
    readonly bootDisks: { autoDelete: boolean, deviceName: string, diskEncryptionKeyRaw: string, diskEncryptionKeySha256: string, initializeParams: { image: string, size: number, type: string }[], source: string }[];
    /**
     * Whether sending and receiving of packets with non-matching source or destination IPs is allowed.
     */
    readonly canIpForward: boolean;
    /**
     * The CPU platform used by this instance.
     */
    readonly cpuPlatform: string;
    readonly createTimeout: number;
    /**
     * Whether deletion protection is enabled on this instance.
     */
    readonly deletionProtection: boolean;
    /**
     * A brief description of the resource.
     */
    readonly description: string;
    readonly disks: { autoDelete: boolean, deviceName: string, disk: string, diskEncryptionKeyRaw: string, diskEncryptionKeySha256: string, image: string, scratch: boolean, size: number, type: string }[];
    /**
     * List of the type and count of accelerator cards attached to the instance. Structure is documented below.
     */
    readonly guestAccelerators: { count: number, type: string }[];
    /**
     * The server-assigned unique identifier of this instance.
     */
    readonly instanceId: string;
    /**
     * The unique fingerprint of the labels.
     */
    readonly labelFingerprint: string;
    /**
     * A set of key/value label pairs assigned to the instance.
     */
    readonly labels: {[key: string]: string};
    /**
     * The machine type to create.
     */
    readonly machineType: string;
    /**
     * Metadata key/value pairs made available within the instance.
     */
    readonly metadata: {[key: string]: string};
    /**
     * The unique fingerprint of the metadata.
     */
    readonly metadataFingerprint: string;
    readonly metadataStartupScript: string;
    /**
     * The minimum CPU platform specified for the VM instance.
     */
    readonly minCpuPlatform: string;
    /**
     * The name or self_link of the network attached to this interface.
     */
    readonly networks: { address: string, externalAddress: string, internalAddress: string, name: string, source: string }[];
    /**
     * The networks attached to the instance. Structure is documented below.
     */
    readonly networkInterfaces: { accessConfigs: { assignedNatIp: string, natIp: string, networkTier: string, publicPtrDomainName: string }[], address: string, aliasIpRanges: { ipCidrRange: string, subnetworkRangeName: string }[], name: string, network: string, networkIp: string, subnetwork: string, subnetworkProject: string }[];
    /**
     * The scheduling strategy being used by the instance.
     */
    readonly schedulings: { automaticRestart: boolean, onHostMaintenance: string, preemptible: boolean }[];
    /**
     * The scratch disks attached to the instance. Structure is documented below.
     */
    readonly scratchDisks: { interface: string }[];
    /**
     * The URI of the created resource.
     */
    readonly selfLink: string;
    /**
     * The service account to attach to the instance. Structure is documented below.
     */
    readonly serviceAccounts: { email: string, scopes: string[] }[];
    /**
     * The list of tags attached to the instance.
     */
    readonly tags: string[];
    /**
     * The unique fingerprint of the tags.
     */
    readonly tagsFingerprint: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
