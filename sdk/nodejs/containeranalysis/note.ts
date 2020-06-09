// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * A Container Analysis note is a high-level piece of metadata that
 * describes a type of analysis that can be done for a resource.
 *
 *
 * To get more information about Note, see:
 *
 * * [API documentation](https://cloud.google.com/container-analysis/api/reference/rest/)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/container-analysis/)
 *     * [Creating Attestations (Occurrences)](https://cloud.google.com/binary-authorization/docs/making-attestations)
 *
 * ## Example Usage - Container Analysis Note Basic
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const note = new gcp.containeranalysis.Note("note", {
 *     attestationAuthority: {
 *         hint: {
 *             humanReadableName: "Attestor Note",
 *         },
 *     },
 * });
 * ```
 * ## Example Usage - Container Analysis Note Attestation Full
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const note = new gcp.containeranalysis.Note("note", {
 *     attestationAuthority: {
 *         hint: {
 *             humanReadableName: "Attestor Note",
 *         },
 *     },
 *     expirationTime: "2120-10-02T15:01:23.045123456Z",
 *     longDescription: "a longer description of test note",
 *     relatedUrls: [
 *         {
 *             label: "foo",
 *             url: "some.url",
 *         },
 *         {
 *             url: "google.com",
 *         },
 *     ],
 *     shortDescription: "test note",
 * });
 * ```
 */
export class Note extends pulumi.CustomResource {
    /**
     * Get an existing Note resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NoteState, opts?: pulumi.CustomResourceOptions): Note {
        return new Note(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:containeranalysis/note:Note';

    /**
     * Returns true if the given object is an instance of Note.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Note {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Note.__pulumiType;
    }

    /**
     * Note kind that represents a logical attestation "role" or "authority".
     * For example, an organization might have one AttestationAuthority for
     * "QA" and one for "build". This Note is intended to act strictly as a
     * grouping mechanism for the attached Occurrences (Attestations). This
     * grouping mechanism also provides a security boundary, since IAM ACLs
     * gate the ability for a principle to attach an Occurrence to a given
     * Note. It also provides a single point of lookup to find all attached
     * Attestation Occurrences, even if they don't all live in the same
     * project.  Structure is documented below.
     */
    public readonly attestationAuthority!: pulumi.Output<outputs.containeranalysis.NoteAttestationAuthority>;
    /**
     * The time this note was created.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * Time of expiration for this note. Leave empty if note does not expire.
     */
    public readonly expirationTime!: pulumi.Output<string | undefined>;
    /**
     * The type of analysis this note describes
     */
    public /*out*/ readonly kind!: pulumi.Output<string>;
    /**
     * A detailed description of the note
     */
    public readonly longDescription!: pulumi.Output<string | undefined>;
    /**
     * The name of the note.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * Names of other notes related to this note.
     */
    public readonly relatedNoteNames!: pulumi.Output<string[] | undefined>;
    /**
     * URLs associated with this note and related metadata.  Structure is documented below.
     */
    public readonly relatedUrls!: pulumi.Output<outputs.containeranalysis.NoteRelatedUrl[] | undefined>;
    /**
     * A one sentence description of the note.
     */
    public readonly shortDescription!: pulumi.Output<string | undefined>;
    /**
     * The time this note was last updated.
     */
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a Note resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NoteArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NoteArgs | NoteState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as NoteState | undefined;
            inputs["attestationAuthority"] = state ? state.attestationAuthority : undefined;
            inputs["createTime"] = state ? state.createTime : undefined;
            inputs["expirationTime"] = state ? state.expirationTime : undefined;
            inputs["kind"] = state ? state.kind : undefined;
            inputs["longDescription"] = state ? state.longDescription : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["relatedNoteNames"] = state ? state.relatedNoteNames : undefined;
            inputs["relatedUrls"] = state ? state.relatedUrls : undefined;
            inputs["shortDescription"] = state ? state.shortDescription : undefined;
            inputs["updateTime"] = state ? state.updateTime : undefined;
        } else {
            const args = argsOrState as NoteArgs | undefined;
            if (!args || args.attestationAuthority === undefined) {
                throw new Error("Missing required property 'attestationAuthority'");
            }
            inputs["attestationAuthority"] = args ? args.attestationAuthority : undefined;
            inputs["expirationTime"] = args ? args.expirationTime : undefined;
            inputs["longDescription"] = args ? args.longDescription : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["relatedNoteNames"] = args ? args.relatedNoteNames : undefined;
            inputs["relatedUrls"] = args ? args.relatedUrls : undefined;
            inputs["shortDescription"] = args ? args.shortDescription : undefined;
            inputs["createTime"] = undefined /*out*/;
            inputs["kind"] = undefined /*out*/;
            inputs["updateTime"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Note.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Note resources.
 */
export interface NoteState {
    /**
     * Note kind that represents a logical attestation "role" or "authority".
     * For example, an organization might have one AttestationAuthority for
     * "QA" and one for "build". This Note is intended to act strictly as a
     * grouping mechanism for the attached Occurrences (Attestations). This
     * grouping mechanism also provides a security boundary, since IAM ACLs
     * gate the ability for a principle to attach an Occurrence to a given
     * Note. It also provides a single point of lookup to find all attached
     * Attestation Occurrences, even if they don't all live in the same
     * project.  Structure is documented below.
     */
    readonly attestationAuthority?: pulumi.Input<inputs.containeranalysis.NoteAttestationAuthority>;
    /**
     * The time this note was created.
     */
    readonly createTime?: pulumi.Input<string>;
    /**
     * Time of expiration for this note. Leave empty if note does not expire.
     */
    readonly expirationTime?: pulumi.Input<string>;
    /**
     * The type of analysis this note describes
     */
    readonly kind?: pulumi.Input<string>;
    /**
     * A detailed description of the note
     */
    readonly longDescription?: pulumi.Input<string>;
    /**
     * The name of the note.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Names of other notes related to this note.
     */
    readonly relatedNoteNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * URLs associated with this note and related metadata.  Structure is documented below.
     */
    readonly relatedUrls?: pulumi.Input<pulumi.Input<inputs.containeranalysis.NoteRelatedUrl>[]>;
    /**
     * A one sentence description of the note.
     */
    readonly shortDescription?: pulumi.Input<string>;
    /**
     * The time this note was last updated.
     */
    readonly updateTime?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Note resource.
 */
export interface NoteArgs {
    /**
     * Note kind that represents a logical attestation "role" or "authority".
     * For example, an organization might have one AttestationAuthority for
     * "QA" and one for "build". This Note is intended to act strictly as a
     * grouping mechanism for the attached Occurrences (Attestations). This
     * grouping mechanism also provides a security boundary, since IAM ACLs
     * gate the ability for a principle to attach an Occurrence to a given
     * Note. It also provides a single point of lookup to find all attached
     * Attestation Occurrences, even if they don't all live in the same
     * project.  Structure is documented below.
     */
    readonly attestationAuthority: pulumi.Input<inputs.containeranalysis.NoteAttestationAuthority>;
    /**
     * Time of expiration for this note. Leave empty if note does not expire.
     */
    readonly expirationTime?: pulumi.Input<string>;
    /**
     * A detailed description of the note
     */
    readonly longDescription?: pulumi.Input<string>;
    /**
     * The name of the note.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Names of other notes related to this note.
     */
    readonly relatedNoteNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * URLs associated with this note and related metadata.  Structure is documented below.
     */
    readonly relatedUrls?: pulumi.Input<pulumi.Input<inputs.containeranalysis.NoteRelatedUrl>[]>;
    /**
     * A one sentence description of the note.
     */
    readonly shortDescription?: pulumi.Input<string>;
}
