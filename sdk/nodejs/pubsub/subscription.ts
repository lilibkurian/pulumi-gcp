// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * A named resource representing the stream of messages from a single,
 * specific topic, to be delivered to the subscribing application.
 *
 * To get more information about Subscription, see:
 *
 * * [API documentation](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions)
 * * How-to Guides
 *     * [Managing Subscriptions](https://cloud.google.com/pubsub/docs/admin#managing_subscriptions)
 *
 * ## Example Usage
 */
export class Subscription extends pulumi.CustomResource {
    /**
     * Get an existing Subscription resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubscriptionState, opts?: pulumi.CustomResourceOptions): Subscription {
        return new Subscription(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:pubsub/subscription:Subscription';

    /**
     * Returns true if the given object is an instance of Subscription.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Subscription {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Subscription.__pulumiType;
    }

    /**
     * This value is the maximum time after a subscriber receives a message
     * before the subscriber should acknowledge the message. After message
     * delivery but before the ack deadline expires and before the message is
     * acknowledged, it is an outstanding message and will not be delivered
     * again during that time (on a best-effort basis).
     * For pull subscriptions, this value is used as the initial value for
     * the ack deadline. To override this value for a given message, call
     * subscriptions.modifyAckDeadline with the corresponding ackId if using
     * pull. The minimum custom deadline you can specify is 10 seconds. The
     * maximum custom deadline you can specify is 600 seconds (10 minutes).
     * If this parameter is 0, a default value of 10 seconds is used.
     * For push delivery, this value is also used to set the request timeout
     * for the call to the push endpoint.
     * If the subscriber never acknowledges the message, the Pub/Sub system
     * will eventually redeliver the message.
     */
    public readonly ackDeadlineSeconds!: pulumi.Output<number>;
    /**
     * A policy that specifies the conditions for dead lettering messages in
     * this subscription. If deadLetterPolicy is not set, dead lettering
     * is disabled.
     * The Cloud Pub/Sub service account associated with this subscriptions's
     * parent project (i.e.,
     * service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have
     * permission to Acknowledge() messages on this subscription.
     * Structure is documented below.
     */
    public readonly deadLetterPolicy!: pulumi.Output<outputs.pubsub.SubscriptionDeadLetterPolicy | undefined>;
    /**
     * If `true`, messages published with the same orderingKey in PubsubMessage will be delivered to
     * the subscribers in the order in which they are received by the Pub/Sub system. Otherwise, they
     * may be delivered in any order.
     */
    public readonly enableMessageOrdering!: pulumi.Output<boolean | undefined>;
    /**
     * A policy that specifies the conditions for this subscription's expiration.
     * A subscription is considered active as long as any connected subscriber
     * is successfully consuming messages from the subscription or is issuing
     * operations on the subscription. If expirationPolicy is not set, a default
     * policy with ttl of 31 days will be used.  If it is set but ttl is "", the
     * resource never expires.  The minimum allowed value for expirationPolicy.ttl
     * is 1 day.
     * Structure is documented below.
     */
    public readonly expirationPolicy!: pulumi.Output<outputs.pubsub.SubscriptionExpirationPolicy>;
    /**
     * The subscription only delivers the messages that match the filter.
     * Pub/Sub automatically acknowledges the messages that don't match the filter. You can filter messages
     * by their attributes. The maximum length of a filter is 256 bytes. After creating the subscription,
     * you can't modify the filter.
     */
    public readonly filter!: pulumi.Output<string | undefined>;
    /**
     * A set of key/value label pairs to assign to this Subscription.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * How long to retain unacknowledged messages in the subscription's
     * backlog, from the moment a message is published. If
     * retainAckedMessages is true, then this also configures the retention
     * of acknowledged messages, and thus configures how far back in time a
     * subscriptions.seek can be done. Defaults to 7 days. Cannot be more
     * than 7 days (`"604800s"`) or less than 10 minutes (`"600s"`).
     * A duration in seconds with up to nine fractional digits, terminated
     * by 's'. Example: `"600.5s"`.
     */
    public readonly messageRetentionDuration!: pulumi.Output<string | undefined>;
    /**
     * Name of the subscription.
     */
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly path!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * If push delivery is used with this subscription, this field is used to
     * configure it. An empty pushConfig signifies that the subscriber will
     * pull and ack messages using API methods.
     * Structure is documented below.
     */
    public readonly pushConfig!: pulumi.Output<outputs.pubsub.SubscriptionPushConfig | undefined>;
    /**
     * Indicates whether to retain acknowledged messages. If `true`, then
     * messages are not expunged from the subscription's backlog, even if
     * they are acknowledged, until they fall out of the
     * messageRetentionDuration window.
     */
    public readonly retainAckedMessages!: pulumi.Output<boolean | undefined>;
    /**
     * A policy that specifies how Pub/Sub retries message delivery for this subscription.
     * If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers.
     * RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message
     * Structure is documented below.
     */
    public readonly retryPolicy!: pulumi.Output<outputs.pubsub.SubscriptionRetryPolicy | undefined>;
    /**
     * A reference to a Topic resource.
     */
    public readonly topic!: pulumi.Output<string>;

    /**
     * Create a Subscription resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SubscriptionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SubscriptionArgs | SubscriptionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SubscriptionState | undefined;
            inputs["ackDeadlineSeconds"] = state ? state.ackDeadlineSeconds : undefined;
            inputs["deadLetterPolicy"] = state ? state.deadLetterPolicy : undefined;
            inputs["enableMessageOrdering"] = state ? state.enableMessageOrdering : undefined;
            inputs["expirationPolicy"] = state ? state.expirationPolicy : undefined;
            inputs["filter"] = state ? state.filter : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["messageRetentionDuration"] = state ? state.messageRetentionDuration : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["path"] = state ? state.path : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["pushConfig"] = state ? state.pushConfig : undefined;
            inputs["retainAckedMessages"] = state ? state.retainAckedMessages : undefined;
            inputs["retryPolicy"] = state ? state.retryPolicy : undefined;
            inputs["topic"] = state ? state.topic : undefined;
        } else {
            const args = argsOrState as SubscriptionArgs | undefined;
            if (!args || args.topic === undefined) {
                throw new Error("Missing required property 'topic'");
            }
            inputs["ackDeadlineSeconds"] = args ? args.ackDeadlineSeconds : undefined;
            inputs["deadLetterPolicy"] = args ? args.deadLetterPolicy : undefined;
            inputs["enableMessageOrdering"] = args ? args.enableMessageOrdering : undefined;
            inputs["expirationPolicy"] = args ? args.expirationPolicy : undefined;
            inputs["filter"] = args ? args.filter : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["messageRetentionDuration"] = args ? args.messageRetentionDuration : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["pushConfig"] = args ? args.pushConfig : undefined;
            inputs["retainAckedMessages"] = args ? args.retainAckedMessages : undefined;
            inputs["retryPolicy"] = args ? args.retryPolicy : undefined;
            inputs["topic"] = args ? args.topic : undefined;
            inputs["path"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Subscription.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Subscription resources.
 */
export interface SubscriptionState {
    /**
     * This value is the maximum time after a subscriber receives a message
     * before the subscriber should acknowledge the message. After message
     * delivery but before the ack deadline expires and before the message is
     * acknowledged, it is an outstanding message and will not be delivered
     * again during that time (on a best-effort basis).
     * For pull subscriptions, this value is used as the initial value for
     * the ack deadline. To override this value for a given message, call
     * subscriptions.modifyAckDeadline with the corresponding ackId if using
     * pull. The minimum custom deadline you can specify is 10 seconds. The
     * maximum custom deadline you can specify is 600 seconds (10 minutes).
     * If this parameter is 0, a default value of 10 seconds is used.
     * For push delivery, this value is also used to set the request timeout
     * for the call to the push endpoint.
     * If the subscriber never acknowledges the message, the Pub/Sub system
     * will eventually redeliver the message.
     */
    readonly ackDeadlineSeconds?: pulumi.Input<number>;
    /**
     * A policy that specifies the conditions for dead lettering messages in
     * this subscription. If deadLetterPolicy is not set, dead lettering
     * is disabled.
     * The Cloud Pub/Sub service account associated with this subscriptions's
     * parent project (i.e.,
     * service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have
     * permission to Acknowledge() messages on this subscription.
     * Structure is documented below.
     */
    readonly deadLetterPolicy?: pulumi.Input<inputs.pubsub.SubscriptionDeadLetterPolicy>;
    /**
     * If `true`, messages published with the same orderingKey in PubsubMessage will be delivered to
     * the subscribers in the order in which they are received by the Pub/Sub system. Otherwise, they
     * may be delivered in any order.
     */
    readonly enableMessageOrdering?: pulumi.Input<boolean>;
    /**
     * A policy that specifies the conditions for this subscription's expiration.
     * A subscription is considered active as long as any connected subscriber
     * is successfully consuming messages from the subscription or is issuing
     * operations on the subscription. If expirationPolicy is not set, a default
     * policy with ttl of 31 days will be used.  If it is set but ttl is "", the
     * resource never expires.  The minimum allowed value for expirationPolicy.ttl
     * is 1 day.
     * Structure is documented below.
     */
    readonly expirationPolicy?: pulumi.Input<inputs.pubsub.SubscriptionExpirationPolicy>;
    /**
     * The subscription only delivers the messages that match the filter.
     * Pub/Sub automatically acknowledges the messages that don't match the filter. You can filter messages
     * by their attributes. The maximum length of a filter is 256 bytes. After creating the subscription,
     * you can't modify the filter.
     */
    readonly filter?: pulumi.Input<string>;
    /**
     * A set of key/value label pairs to assign to this Subscription.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * How long to retain unacknowledged messages in the subscription's
     * backlog, from the moment a message is published. If
     * retainAckedMessages is true, then this also configures the retention
     * of acknowledged messages, and thus configures how far back in time a
     * subscriptions.seek can be done. Defaults to 7 days. Cannot be more
     * than 7 days (`"604800s"`) or less than 10 minutes (`"600s"`).
     * A duration in seconds with up to nine fractional digits, terminated
     * by 's'. Example: `"600.5s"`.
     */
    readonly messageRetentionDuration?: pulumi.Input<string>;
    /**
     * Name of the subscription.
     */
    readonly name?: pulumi.Input<string>;
    readonly path?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * If push delivery is used with this subscription, this field is used to
     * configure it. An empty pushConfig signifies that the subscriber will
     * pull and ack messages using API methods.
     * Structure is documented below.
     */
    readonly pushConfig?: pulumi.Input<inputs.pubsub.SubscriptionPushConfig>;
    /**
     * Indicates whether to retain acknowledged messages. If `true`, then
     * messages are not expunged from the subscription's backlog, even if
     * they are acknowledged, until they fall out of the
     * messageRetentionDuration window.
     */
    readonly retainAckedMessages?: pulumi.Input<boolean>;
    /**
     * A policy that specifies how Pub/Sub retries message delivery for this subscription.
     * If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers.
     * RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message
     * Structure is documented below.
     */
    readonly retryPolicy?: pulumi.Input<inputs.pubsub.SubscriptionRetryPolicy>;
    /**
     * A reference to a Topic resource.
     */
    readonly topic?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Subscription resource.
 */
export interface SubscriptionArgs {
    /**
     * This value is the maximum time after a subscriber receives a message
     * before the subscriber should acknowledge the message. After message
     * delivery but before the ack deadline expires and before the message is
     * acknowledged, it is an outstanding message and will not be delivered
     * again during that time (on a best-effort basis).
     * For pull subscriptions, this value is used as the initial value for
     * the ack deadline. To override this value for a given message, call
     * subscriptions.modifyAckDeadline with the corresponding ackId if using
     * pull. The minimum custom deadline you can specify is 10 seconds. The
     * maximum custom deadline you can specify is 600 seconds (10 minutes).
     * If this parameter is 0, a default value of 10 seconds is used.
     * For push delivery, this value is also used to set the request timeout
     * for the call to the push endpoint.
     * If the subscriber never acknowledges the message, the Pub/Sub system
     * will eventually redeliver the message.
     */
    readonly ackDeadlineSeconds?: pulumi.Input<number>;
    /**
     * A policy that specifies the conditions for dead lettering messages in
     * this subscription. If deadLetterPolicy is not set, dead lettering
     * is disabled.
     * The Cloud Pub/Sub service account associated with this subscriptions's
     * parent project (i.e.,
     * service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have
     * permission to Acknowledge() messages on this subscription.
     * Structure is documented below.
     */
    readonly deadLetterPolicy?: pulumi.Input<inputs.pubsub.SubscriptionDeadLetterPolicy>;
    /**
     * If `true`, messages published with the same orderingKey in PubsubMessage will be delivered to
     * the subscribers in the order in which they are received by the Pub/Sub system. Otherwise, they
     * may be delivered in any order.
     */
    readonly enableMessageOrdering?: pulumi.Input<boolean>;
    /**
     * A policy that specifies the conditions for this subscription's expiration.
     * A subscription is considered active as long as any connected subscriber
     * is successfully consuming messages from the subscription or is issuing
     * operations on the subscription. If expirationPolicy is not set, a default
     * policy with ttl of 31 days will be used.  If it is set but ttl is "", the
     * resource never expires.  The minimum allowed value for expirationPolicy.ttl
     * is 1 day.
     * Structure is documented below.
     */
    readonly expirationPolicy?: pulumi.Input<inputs.pubsub.SubscriptionExpirationPolicy>;
    /**
     * The subscription only delivers the messages that match the filter.
     * Pub/Sub automatically acknowledges the messages that don't match the filter. You can filter messages
     * by their attributes. The maximum length of a filter is 256 bytes. After creating the subscription,
     * you can't modify the filter.
     */
    readonly filter?: pulumi.Input<string>;
    /**
     * A set of key/value label pairs to assign to this Subscription.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * How long to retain unacknowledged messages in the subscription's
     * backlog, from the moment a message is published. If
     * retainAckedMessages is true, then this also configures the retention
     * of acknowledged messages, and thus configures how far back in time a
     * subscriptions.seek can be done. Defaults to 7 days. Cannot be more
     * than 7 days (`"604800s"`) or less than 10 minutes (`"600s"`).
     * A duration in seconds with up to nine fractional digits, terminated
     * by 's'. Example: `"600.5s"`.
     */
    readonly messageRetentionDuration?: pulumi.Input<string>;
    /**
     * Name of the subscription.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * If push delivery is used with this subscription, this field is used to
     * configure it. An empty pushConfig signifies that the subscriber will
     * pull and ack messages using API methods.
     * Structure is documented below.
     */
    readonly pushConfig?: pulumi.Input<inputs.pubsub.SubscriptionPushConfig>;
    /**
     * Indicates whether to retain acknowledged messages. If `true`, then
     * messages are not expunged from the subscription's backlog, even if
     * they are acknowledged, until they fall out of the
     * messageRetentionDuration window.
     */
    readonly retainAckedMessages?: pulumi.Input<boolean>;
    /**
     * A policy that specifies how Pub/Sub retries message delivery for this subscription.
     * If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers.
     * RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message
     * Structure is documented below.
     */
    readonly retryPolicy?: pulumi.Input<inputs.pubsub.SubscriptionRetryPolicy>;
    /**
     * A reference to a Topic resource.
     */
    readonly topic: pulumi.Input<string>;
}
