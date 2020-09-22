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

__all__ = ['GroupMembership']


class GroupMembership(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 member_key: Optional[pulumi.Input[pulumi.InputType['GroupMembershipMemberKeyArgs']]] = None,
                 preferred_member_key: Optional[pulumi.Input[pulumi.InputType['GroupMembershipPreferredMemberKeyArgs']]] = None,
                 roles: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['GroupMembershipRoleArgs']]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A Membership defines a relationship between a Group and an entity belonging to that Group, referred to as a "member".

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group: The name of the Group to create this membership in.
        :param pulumi.Input[pulumi.InputType['GroupMembershipMemberKeyArgs']] member_key: EntityKey of the member.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['GroupMembershipPreferredMemberKeyArgs']] preferred_member_key: EntityKey of the member.
               Structure is documented below.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['GroupMembershipRoleArgs']]]] roles: The MembershipRoles that apply to the Membership.
               Must not contain duplicate MembershipRoles with the same name.
               Structure is documented below.
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

            if group is None:
                raise TypeError("Missing required property 'group'")
            __props__['group'] = group
            __props__['member_key'] = member_key
            __props__['preferred_member_key'] = preferred_member_key
            if roles is None:
                raise TypeError("Missing required property 'roles'")
            __props__['roles'] = roles
            __props__['create_time'] = None
            __props__['name'] = None
            __props__['type'] = None
            __props__['update_time'] = None
        super(GroupMembership, __self__).__init__(
            'gcp:cloudidentity/groupMembership:GroupMembership',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            group: Optional[pulumi.Input[str]] = None,
            member_key: Optional[pulumi.Input[pulumi.InputType['GroupMembershipMemberKeyArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            preferred_member_key: Optional[pulumi.Input[pulumi.InputType['GroupMembershipPreferredMemberKeyArgs']]] = None,
            roles: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['GroupMembershipRoleArgs']]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'GroupMembership':
        """
        Get an existing GroupMembership resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: The time when the Membership was created.
        :param pulumi.Input[str] group: The name of the Group to create this membership in.
        :param pulumi.Input[pulumi.InputType['GroupMembershipMemberKeyArgs']] member_key: EntityKey of the member.
               Structure is documented below.
        :param pulumi.Input[str] name: The name of the MembershipRole. Must be one of OWNER, MANAGER, MEMBER.
               Possible values are `OWNER`, `MANAGER`, and `MEMBER`.
        :param pulumi.Input[pulumi.InputType['GroupMembershipPreferredMemberKeyArgs']] preferred_member_key: EntityKey of the member.
               Structure is documented below.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['GroupMembershipRoleArgs']]]] roles: The MembershipRoles that apply to the Membership.
               Must not contain duplicate MembershipRoles with the same name.
               Structure is documented below.
        :param pulumi.Input[str] type: The type of the membership.
        :param pulumi.Input[str] update_time: The time when the Membership was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["create_time"] = create_time
        __props__["group"] = group
        __props__["member_key"] = member_key
        __props__["name"] = name
        __props__["preferred_member_key"] = preferred_member_key
        __props__["roles"] = roles
        __props__["type"] = type
        __props__["update_time"] = update_time
        return GroupMembership(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the Membership was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def group(self) -> pulumi.Output[str]:
        """
        The name of the Group to create this membership in.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter(name="memberKey")
    def member_key(self) -> pulumi.Output['outputs.GroupMembershipMemberKey']:
        """
        EntityKey of the member.
        Structure is documented below.
        """
        return pulumi.get(self, "member_key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the MembershipRole. Must be one of OWNER, MANAGER, MEMBER.
        Possible values are `OWNER`, `MANAGER`, and `MEMBER`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="preferredMemberKey")
    def preferred_member_key(self) -> pulumi.Output['outputs.GroupMembershipPreferredMemberKey']:
        """
        EntityKey of the member.
        Structure is documented below.
        """
        return pulumi.get(self, "preferred_member_key")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[List['outputs.GroupMembershipRole']]:
        """
        The MembershipRoles that apply to the Membership.
        Must not contain duplicate MembershipRoles with the same name.
        Structure is documented below.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the membership.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time when the Membership was last updated.
        """
        return pulumi.get(self, "update_time")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

