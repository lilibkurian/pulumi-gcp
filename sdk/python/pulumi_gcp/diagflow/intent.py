# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Intent']


class Intent(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 default_response_platforms: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 input_context_names: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 is_fallback: Optional[pulumi.Input[bool]] = None,
                 ml_disabled: Optional[pulumi.Input[bool]] = None,
                 parent_followup_intent_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[float]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reset_contexts: Optional[pulumi.Input[bool]] = None,
                 webhook_state: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Represents a Dialogflow intent. Intents convert a number of user expressions or patterns into an action. An action
        is an extraction of a user command or sentence semantics.

        To get more information about Intent, see:

        * [API documentation](https://cloud.google.com/dialogflow/docs/reference/rest/v2/projects.agent.intents)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/dialogflow/docs/)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The name of the action associated with the intent.
               Note: The action name must not contain whitespaces.
        :param pulumi.Input[List[pulumi.Input[str]]] default_response_platforms: The list of platforms for which the first responses will be copied from the messages in PLATFORM_UNSPECIFIED
               (i.e. default platform).
               Each value may be one of `FACEBOOK`, `SLACK`, `TELEGRAM`, `KIK`, `SKYPE`, `LINE`, `VIBER`, `ACTIONS_ON_GOOGLE`, and `GOOGLE_HANGOUTS`.
        :param pulumi.Input[str] display_name: The name of this intent to be displayed on the console.
        :param pulumi.Input[List[pulumi.Input[str]]] events: The collection of event names that trigger the intent. If the collection of input contexts is not empty, all of
               the contexts must be present in the active user session for an event to trigger this intent. See the
               [events reference](https://cloud.google.com/dialogflow/docs/events-overview) for more details.
        :param pulumi.Input[List[pulumi.Input[str]]] input_context_names: The list of context names required for this intent to be triggered.
               Format: projects/<Project ID>/agent/sessions/-/contexts/<Context ID>.
        :param pulumi.Input[bool] is_fallback: Indicates whether this is a fallback intent.
        :param pulumi.Input[bool] ml_disabled: Indicates whether Machine Learning is disabled for the intent.
               Note: If mlDisabled setting is set to true, then this intent is not taken into account during inference in ML
               ONLY match mode. Also, auto-markup in the UI is turned off.
        :param pulumi.Input[str] parent_followup_intent_name: The unique identifier of the parent intent in the chain of followup intents.
               Format: projects/<Project ID>/agent/intents/<Intent ID>.
        :param pulumi.Input[float] priority: The priority of this intent. Higher numbers represent higher priorities.
               - If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds
               to the Normal priority in the console.
               - If the supplied value is negative, the intent is ignored in runtime detect intent requests.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[bool] reset_contexts: Indicates whether to delete all contexts in the current session when this intent is matched.
        :param pulumi.Input[str] webhook_state: Indicates whether webhooks are enabled for the intent.
               * WEBHOOK_STATE_ENABLED: Webhook is enabled in the agent and in the intent.
               * WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING: Webhook is enabled in the agent and in the intent. Also, each slot
               filling prompt is forwarded to the webhook.
               Possible values are `WEBHOOK_STATE_ENABLED` and `WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING`.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['action'] = action
            __props__['default_response_platforms'] = default_response_platforms
            if display_name is None:
                raise TypeError("Missing required property 'display_name'")
            __props__['display_name'] = display_name
            __props__['events'] = events
            __props__['input_context_names'] = input_context_names
            __props__['is_fallback'] = is_fallback
            __props__['ml_disabled'] = ml_disabled
            __props__['parent_followup_intent_name'] = parent_followup_intent_name
            __props__['priority'] = priority
            __props__['project'] = project
            __props__['reset_contexts'] = reset_contexts
            __props__['webhook_state'] = webhook_state
            __props__['followup_intent_infos'] = None
            __props__['name'] = None
            __props__['root_followup_intent_name'] = None
        super(Intent, __self__).__init__(
            'gcp:diagflow/intent:Intent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[str]] = None,
            default_response_platforms: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            events: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            followup_intent_infos: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['IntentFollowupIntentInfoArgs']]]]] = None,
            input_context_names: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            is_fallback: Optional[pulumi.Input[bool]] = None,
            ml_disabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_followup_intent_name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[float]] = None,
            project: Optional[pulumi.Input[str]] = None,
            reset_contexts: Optional[pulumi.Input[bool]] = None,
            root_followup_intent_name: Optional[pulumi.Input[str]] = None,
            webhook_state: Optional[pulumi.Input[str]] = None) -> 'Intent':
        """
        Get an existing Intent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The name of the action associated with the intent.
               Note: The action name must not contain whitespaces.
        :param pulumi.Input[List[pulumi.Input[str]]] default_response_platforms: The list of platforms for which the first responses will be copied from the messages in PLATFORM_UNSPECIFIED
               (i.e. default platform).
               Each value may be one of `FACEBOOK`, `SLACK`, `TELEGRAM`, `KIK`, `SKYPE`, `LINE`, `VIBER`, `ACTIONS_ON_GOOGLE`, and `GOOGLE_HANGOUTS`.
        :param pulumi.Input[str] display_name: The name of this intent to be displayed on the console.
        :param pulumi.Input[List[pulumi.Input[str]]] events: The collection of event names that trigger the intent. If the collection of input contexts is not empty, all of
               the contexts must be present in the active user session for an event to trigger this intent. See the
               [events reference](https://cloud.google.com/dialogflow/docs/events-overview) for more details.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['IntentFollowupIntentInfoArgs']]]] followup_intent_infos: Information about all followup intents that have this intent as a direct or indirect parent. We populate this field only
               in the output.
        :param pulumi.Input[List[pulumi.Input[str]]] input_context_names: The list of context names required for this intent to be triggered.
               Format: projects/<Project ID>/agent/sessions/-/contexts/<Context ID>.
        :param pulumi.Input[bool] is_fallback: Indicates whether this is a fallback intent.
        :param pulumi.Input[bool] ml_disabled: Indicates whether Machine Learning is disabled for the intent.
               Note: If mlDisabled setting is set to true, then this intent is not taken into account during inference in ML
               ONLY match mode. Also, auto-markup in the UI is turned off.
        :param pulumi.Input[str] name: The unique identifier of this intent. Format: projects/<Project ID>/agent/intents/<Intent ID>.
        :param pulumi.Input[str] parent_followup_intent_name: The unique identifier of the parent intent in the chain of followup intents.
               Format: projects/<Project ID>/agent/intents/<Intent ID>.
        :param pulumi.Input[float] priority: The priority of this intent. Higher numbers represent higher priorities.
               - If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds
               to the Normal priority in the console.
               - If the supplied value is negative, the intent is ignored in runtime detect intent requests.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[bool] reset_contexts: Indicates whether to delete all contexts in the current session when this intent is matched.
        :param pulumi.Input[str] root_followup_intent_name: The unique identifier of the root intent in the chain of followup intents. It identifies the correct followup intents
               chain for this intent. Format: projects/<Project ID>/agent/intents/<Intent ID>.
        :param pulumi.Input[str] webhook_state: Indicates whether webhooks are enabled for the intent.
               * WEBHOOK_STATE_ENABLED: Webhook is enabled in the agent and in the intent.
               * WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING: Webhook is enabled in the agent and in the intent. Also, each slot
               filling prompt is forwarded to the webhook.
               Possible values are `WEBHOOK_STATE_ENABLED` and `WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["action"] = action
        __props__["default_response_platforms"] = default_response_platforms
        __props__["display_name"] = display_name
        __props__["events"] = events
        __props__["followup_intent_infos"] = followup_intent_infos
        __props__["input_context_names"] = input_context_names
        __props__["is_fallback"] = is_fallback
        __props__["ml_disabled"] = ml_disabled
        __props__["name"] = name
        __props__["parent_followup_intent_name"] = parent_followup_intent_name
        __props__["priority"] = priority
        __props__["project"] = project
        __props__["reset_contexts"] = reset_contexts
        __props__["root_followup_intent_name"] = root_followup_intent_name
        __props__["webhook_state"] = webhook_state
        return Intent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        The name of the action associated with the intent.
        Note: The action name must not contain whitespaces.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="defaultResponsePlatforms")
    def default_response_platforms(self) -> pulumi.Output[Optional[List[str]]]:
        """
        The list of platforms for which the first responses will be copied from the messages in PLATFORM_UNSPECIFIED
        (i.e. default platform).
        Each value may be one of `FACEBOOK`, `SLACK`, `TELEGRAM`, `KIK`, `SKYPE`, `LINE`, `VIBER`, `ACTIONS_ON_GOOGLE`, and `GOOGLE_HANGOUTS`.
        """
        return pulumi.get(self, "default_response_platforms")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The name of this intent to be displayed on the console.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def events(self) -> pulumi.Output[Optional[List[str]]]:
        """
        The collection of event names that trigger the intent. If the collection of input contexts is not empty, all of
        the contexts must be present in the active user session for an event to trigger this intent. See the
        [events reference](https://cloud.google.com/dialogflow/docs/events-overview) for more details.
        """
        return pulumi.get(self, "events")

    @property
    @pulumi.getter(name="followupIntentInfos")
    def followup_intent_infos(self) -> pulumi.Output[List['outputs.IntentFollowupIntentInfo']]:
        """
        Information about all followup intents that have this intent as a direct or indirect parent. We populate this field only
        in the output.
        """
        return pulumi.get(self, "followup_intent_infos")

    @property
    @pulumi.getter(name="inputContextNames")
    def input_context_names(self) -> pulumi.Output[Optional[List[str]]]:
        """
        The list of context names required for this intent to be triggered.
        Format: projects/<Project ID>/agent/sessions/-/contexts/<Context ID>.
        """
        return pulumi.get(self, "input_context_names")

    @property
    @pulumi.getter(name="isFallback")
    def is_fallback(self) -> pulumi.Output[bool]:
        """
        Indicates whether this is a fallback intent.
        """
        return pulumi.get(self, "is_fallback")

    @property
    @pulumi.getter(name="mlDisabled")
    def ml_disabled(self) -> pulumi.Output[bool]:
        """
        Indicates whether Machine Learning is disabled for the intent.
        Note: If mlDisabled setting is set to true, then this intent is not taken into account during inference in ML
        ONLY match mode. Also, auto-markup in the UI is turned off.
        """
        return pulumi.get(self, "ml_disabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique identifier of this intent. Format: projects/<Project ID>/agent/intents/<Intent ID>.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentFollowupIntentName")
    def parent_followup_intent_name(self) -> pulumi.Output[str]:
        """
        The unique identifier of the parent intent in the chain of followup intents.
        Format: projects/<Project ID>/agent/intents/<Intent ID>.
        """
        return pulumi.get(self, "parent_followup_intent_name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[float]:
        """
        The priority of this intent. Higher numbers represent higher priorities.
        - If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds
        to the Normal priority in the console.
        - If the supplied value is negative, the intent is ignored in runtime detect intent requests.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="resetContexts")
    def reset_contexts(self) -> pulumi.Output[bool]:
        """
        Indicates whether to delete all contexts in the current session when this intent is matched.
        """
        return pulumi.get(self, "reset_contexts")

    @property
    @pulumi.getter(name="rootFollowupIntentName")
    def root_followup_intent_name(self) -> pulumi.Output[str]:
        """
        The unique identifier of the root intent in the chain of followup intents. It identifies the correct followup intents
        chain for this intent. Format: projects/<Project ID>/agent/intents/<Intent ID>.
        """
        return pulumi.get(self, "root_followup_intent_name")

    @property
    @pulumi.getter(name="webhookState")
    def webhook_state(self) -> pulumi.Output[str]:
        """
        Indicates whether webhooks are enabled for the intent.
        * WEBHOOK_STATE_ENABLED: Webhook is enabled in the agent and in the intent.
        * WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING: Webhook is enabled in the agent and in the intent. Also, each slot
        filling prompt is forwarded to the webhook.
        Possible values are `WEBHOOK_STATE_ENABLED` and `WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING`.
        """
        return pulumi.get(self, "webhook_state")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

