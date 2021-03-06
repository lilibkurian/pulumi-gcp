# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'ManagedZoneDnssecConfig',
    'ManagedZoneDnssecConfigDefaultKeySpec',
    'ManagedZoneForwardingConfig',
    'ManagedZoneForwardingConfigTargetNameServer',
    'ManagedZonePeeringConfig',
    'ManagedZonePeeringConfigTargetNetwork',
    'ManagedZonePrivateVisibilityConfig',
    'ManagedZonePrivateVisibilityConfigNetwork',
    'ManagedZoneServiceDirectoryConfig',
    'ManagedZoneServiceDirectoryConfigNamespace',
    'PolicyAlternativeNameServerConfig',
    'PolicyAlternativeNameServerConfigTargetNameServer',
    'PolicyNetwork',
    'GetKeysKeySigningKeyResult',
    'GetKeysKeySigningKeyDigestResult',
    'GetKeysZoneSigningKeyResult',
    'GetKeysZoneSigningKeyDigestResult',
]

@pulumi.output_type
class ManagedZoneDnssecConfig(dict):
    def __init__(__self__, *,
                 default_key_specs: Optional[Sequence['outputs.ManagedZoneDnssecConfigDefaultKeySpec']] = None,
                 kind: Optional[str] = None,
                 non_existence: Optional[str] = None,
                 state: Optional[str] = None):
        """
        :param Sequence['ManagedZoneDnssecConfigDefaultKeySpecArgs'] default_key_specs: Specifies parameters that will be used for generating initial DnsKeys
               for this ManagedZone. If you provide a spec for keySigning or zoneSigning,
               you must also provide one for the other.
               default_key_specs can only be updated when the state is `off`.
               Structure is documented below.
        :param str kind: Identifies what kind of resource this is
        :param str non_existence: Specifies the mechanism used to provide authenticated denial-of-existence responses.
               non_existence can only be updated when the state is `off`.
               Possible values are `nsec` and `nsec3`.
        :param str state: Specifies whether DNSSEC is enabled, and what mode it is in
               Possible values are `off`, `on`, and `transfer`.
        """
        if default_key_specs is not None:
            pulumi.set(__self__, "default_key_specs", default_key_specs)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if non_existence is not None:
            pulumi.set(__self__, "non_existence", non_existence)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="defaultKeySpecs")
    def default_key_specs(self) -> Optional[Sequence['outputs.ManagedZoneDnssecConfigDefaultKeySpec']]:
        """
        Specifies parameters that will be used for generating initial DnsKeys
        for this ManagedZone. If you provide a spec for keySigning or zoneSigning,
        you must also provide one for the other.
        default_key_specs can only be updated when the state is `off`.
        Structure is documented below.
        """
        return pulumi.get(self, "default_key_specs")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Identifies what kind of resource this is
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="nonExistence")
    def non_existence(self) -> Optional[str]:
        """
        Specifies the mechanism used to provide authenticated denial-of-existence responses.
        non_existence can only be updated when the state is `off`.
        Possible values are `nsec` and `nsec3`.
        """
        return pulumi.get(self, "non_existence")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        Specifies whether DNSSEC is enabled, and what mode it is in
        Possible values are `off`, `on`, and `transfer`.
        """
        return pulumi.get(self, "state")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ManagedZoneDnssecConfigDefaultKeySpec(dict):
    def __init__(__self__, *,
                 algorithm: Optional[str] = None,
                 key_length: Optional[int] = None,
                 key_type: Optional[str] = None,
                 kind: Optional[str] = None):
        """
        :param str algorithm: String mnemonic specifying the DNSSEC algorithm of this key
               Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
        :param int key_length: Length of the keys in bits
        :param str key_type: Specifies whether this is a key signing key (KSK) or a zone
               signing key (ZSK). Key signing keys have the Secure Entry
               Point flag set and, when active, will only be used to sign
               resource record sets of type DNSKEY. Zone signing keys do
               not have the Secure Entry Point flag set and will be used
               to sign all other types of resource record sets.
               Possible values are `keySigning` and `zoneSigning`.
        :param str kind: Identifies what kind of resource this is
        """
        if algorithm is not None:
            pulumi.set(__self__, "algorithm", algorithm)
        if key_length is not None:
            pulumi.set(__self__, "key_length", key_length)
        if key_type is not None:
            pulumi.set(__self__, "key_type", key_type)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)

    @property
    @pulumi.getter
    def algorithm(self) -> Optional[str]:
        """
        String mnemonic specifying the DNSSEC algorithm of this key
        Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter(name="keyLength")
    def key_length(self) -> Optional[int]:
        """
        Length of the keys in bits
        """
        return pulumi.get(self, "key_length")

    @property
    @pulumi.getter(name="keyType")
    def key_type(self) -> Optional[str]:
        """
        Specifies whether this is a key signing key (KSK) or a zone
        signing key (ZSK). Key signing keys have the Secure Entry
        Point flag set and, when active, will only be used to sign
        resource record sets of type DNSKEY. Zone signing keys do
        not have the Secure Entry Point flag set and will be used
        to sign all other types of resource record sets.
        Possible values are `keySigning` and `zoneSigning`.
        """
        return pulumi.get(self, "key_type")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Identifies what kind of resource this is
        """
        return pulumi.get(self, "kind")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ManagedZoneForwardingConfig(dict):
    def __init__(__self__, *,
                 target_name_servers: Sequence['outputs.ManagedZoneForwardingConfigTargetNameServer']):
        """
        :param Sequence['ManagedZoneForwardingConfigTargetNameServerArgs'] target_name_servers: List of target name servers to forward to. Cloud DNS will
               select the best available name server if more than
               one target is given.
               Structure is documented below.
        """
        pulumi.set(__self__, "target_name_servers", target_name_servers)

    @property
    @pulumi.getter(name="targetNameServers")
    def target_name_servers(self) -> Sequence['outputs.ManagedZoneForwardingConfigTargetNameServer']:
        """
        List of target name servers to forward to. Cloud DNS will
        select the best available name server if more than
        one target is given.
        Structure is documented below.
        """
        return pulumi.get(self, "target_name_servers")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ManagedZoneForwardingConfigTargetNameServer(dict):
    def __init__(__self__, *,
                 ipv4_address: str,
                 forwarding_path: Optional[str] = None):
        """
        :param str ipv4_address: IPv4 address of a target name server.
        :param str forwarding_path: Forwarding path for this TargetNameServer. If unset or `default` Cloud DNS will make forwarding
               decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
               to the Internet. When set to `private`, Cloud DNS will always send queries through VPC for this target
               Possible values are `default` and `private`.
        """
        pulumi.set(__self__, "ipv4_address", ipv4_address)
        if forwarding_path is not None:
            pulumi.set(__self__, "forwarding_path", forwarding_path)

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> str:
        """
        IPv4 address of a target name server.
        """
        return pulumi.get(self, "ipv4_address")

    @property
    @pulumi.getter(name="forwardingPath")
    def forwarding_path(self) -> Optional[str]:
        """
        Forwarding path for this TargetNameServer. If unset or `default` Cloud DNS will make forwarding
        decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
        to the Internet. When set to `private`, Cloud DNS will always send queries through VPC for this target
        Possible values are `default` and `private`.
        """
        return pulumi.get(self, "forwarding_path")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ManagedZonePeeringConfig(dict):
    def __init__(__self__, *,
                 target_network: 'outputs.ManagedZonePeeringConfigTargetNetwork'):
        """
        :param 'ManagedZonePeeringConfigTargetNetworkArgs' target_network: The network with which to peer.
               Structure is documented below.
        """
        pulumi.set(__self__, "target_network", target_network)

    @property
    @pulumi.getter(name="targetNetwork")
    def target_network(self) -> 'outputs.ManagedZonePeeringConfigTargetNetwork':
        """
        The network with which to peer.
        Structure is documented below.
        """
        return pulumi.get(self, "target_network")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ManagedZonePeeringConfigTargetNetwork(dict):
    def __init__(__self__, *,
                 network_url: str):
        """
        :param str network_url: The id or fully qualified URL of the VPC network to forward queries to.
               This should be formatted like `projects/{project}/global/networks/{network}` or
               `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        pulumi.set(__self__, "network_url", network_url)

    @property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> str:
        """
        The id or fully qualified URL of the VPC network to forward queries to.
        This should be formatted like `projects/{project}/global/networks/{network}` or
        `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        return pulumi.get(self, "network_url")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ManagedZonePrivateVisibilityConfig(dict):
    def __init__(__self__, *,
                 networks: Sequence['outputs.ManagedZonePrivateVisibilityConfigNetwork']):
        """
        :param Sequence['ManagedZonePrivateVisibilityConfigNetworkArgs'] networks: The list of VPC networks that can see this zone. Structure is documented below.
        """
        pulumi.set(__self__, "networks", networks)

    @property
    @pulumi.getter
    def networks(self) -> Sequence['outputs.ManagedZonePrivateVisibilityConfigNetwork']:
        """
        The list of VPC networks that can see this zone. Structure is documented below.
        """
        return pulumi.get(self, "networks")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ManagedZonePrivateVisibilityConfigNetwork(dict):
    def __init__(__self__, *,
                 network_url: str):
        """
        :param str network_url: The id or fully qualified URL of the VPC network to forward queries to.
               This should be formatted like `projects/{project}/global/networks/{network}` or
               `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        pulumi.set(__self__, "network_url", network_url)

    @property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> str:
        """
        The id or fully qualified URL of the VPC network to forward queries to.
        This should be formatted like `projects/{project}/global/networks/{network}` or
        `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        return pulumi.get(self, "network_url")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ManagedZoneServiceDirectoryConfig(dict):
    def __init__(__self__, *,
                 namespace: 'outputs.ManagedZoneServiceDirectoryConfigNamespace'):
        """
        :param 'ManagedZoneServiceDirectoryConfigNamespaceArgs' namespace: The namespace associated with the zone.
               Structure is documented below.
        """
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def namespace(self) -> 'outputs.ManagedZoneServiceDirectoryConfigNamespace':
        """
        The namespace associated with the zone.
        Structure is documented below.
        """
        return pulumi.get(self, "namespace")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ManagedZoneServiceDirectoryConfigNamespace(dict):
    def __init__(__self__, *,
                 namespace_url: str):
        """
        :param str namespace_url: The fully qualified or partial URL of the service directory namespace that should be
               associated with the zone. This should be formatted like
               `https://servicedirectory.googleapis.com/v1/projects/{project}/locations/{location}/namespaces/{namespace_id}`
               or simply `projects/{project}/locations/{location}/namespaces/{namespace_id}`
               Ignored for `public` visibility zones.
        """
        pulumi.set(__self__, "namespace_url", namespace_url)

    @property
    @pulumi.getter(name="namespaceUrl")
    def namespace_url(self) -> str:
        """
        The fully qualified or partial URL of the service directory namespace that should be
        associated with the zone. This should be formatted like
        `https://servicedirectory.googleapis.com/v1/projects/{project}/locations/{location}/namespaces/{namespace_id}`
        or simply `projects/{project}/locations/{location}/namespaces/{namespace_id}`
        Ignored for `public` visibility zones.
        """
        return pulumi.get(self, "namespace_url")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyAlternativeNameServerConfig(dict):
    def __init__(__self__, *,
                 target_name_servers: Sequence['outputs.PolicyAlternativeNameServerConfigTargetNameServer']):
        """
        :param Sequence['PolicyAlternativeNameServerConfigTargetNameServerArgs'] target_name_servers: Sets an alternative name server for the associated networks. When specified,
               all DNS queries are forwarded to a name server that you choose. Names such as .internal
               are not available when an alternative name server is specified.
               Structure is documented below.
        """
        pulumi.set(__self__, "target_name_servers", target_name_servers)

    @property
    @pulumi.getter(name="targetNameServers")
    def target_name_servers(self) -> Sequence['outputs.PolicyAlternativeNameServerConfigTargetNameServer']:
        """
        Sets an alternative name server for the associated networks. When specified,
        all DNS queries are forwarded to a name server that you choose. Names such as .internal
        are not available when an alternative name server is specified.
        Structure is documented below.
        """
        return pulumi.get(self, "target_name_servers")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyAlternativeNameServerConfigTargetNameServer(dict):
    def __init__(__self__, *,
                 ipv4_address: str):
        """
        :param str ipv4_address: IPv4 address to forward to.
        """
        pulumi.set(__self__, "ipv4_address", ipv4_address)

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> str:
        """
        IPv4 address to forward to.
        """
        return pulumi.get(self, "ipv4_address")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyNetwork(dict):
    def __init__(__self__, *,
                 network_url: str):
        """
        :param str network_url: The id or fully qualified URL of the VPC network to forward queries to.
               This should be formatted like `projects/{project}/global/networks/{network}` or
               `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        pulumi.set(__self__, "network_url", network_url)

    @property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> str:
        """
        The id or fully qualified URL of the VPC network to forward queries to.
        This should be formatted like `projects/{project}/global/networks/{network}` or
        `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
        """
        return pulumi.get(self, "network_url")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetKeysKeySigningKeyResult(dict):
    def __init__(__self__, *,
                 algorithm: str,
                 creation_time: str,
                 description: str,
                 digests: Sequence['outputs.GetKeysKeySigningKeyDigestResult'],
                 ds_record: str,
                 id: str,
                 is_active: bool,
                 key_length: int,
                 key_tag: int,
                 public_key: str):
        """
        :param str algorithm: String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
        :param str creation_time: The time that this resource was created in the control plane. This is in RFC3339 text format.
        :param str description: A mutable string of at most 1024 characters associated with this resource for the user's convenience.
        :param Sequence['GetKeysKeySigningKeyDigestArgs'] digests: A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
        :param str ds_record: The DS record based on the KSK record. This is used when [delegating](https://cloud.google.com/dns/docs/dnssec-advanced#subdelegation) DNSSEC-signed subdomains.
        :param str id: Unique identifier for the resource; defined by the server.
        :param bool is_active: Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
        :param int key_length: Length of the key in bits. Specified at creation time then immutable.
        :param int key_tag: The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
        :param str public_key: Base64 encoded public half of this key.
        """
        pulumi.set(__self__, "algorithm", algorithm)
        pulumi.set(__self__, "creation_time", creation_time)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "digests", digests)
        pulumi.set(__self__, "ds_record", ds_record)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "is_active", is_active)
        pulumi.set(__self__, "key_length", key_length)
        pulumi.set(__self__, "key_tag", key_tag)
        pulumi.set(__self__, "public_key", public_key)

    @property
    @pulumi.getter
    def algorithm(self) -> str:
        """
        String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        The time that this resource was created in the control plane. This is in RFC3339 text format.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A mutable string of at most 1024 characters associated with this resource for the user's convenience.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def digests(self) -> Sequence['outputs.GetKeysKeySigningKeyDigestResult']:
        """
        A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
        """
        return pulumi.get(self, "digests")

    @property
    @pulumi.getter(name="dsRecord")
    def ds_record(self) -> str:
        """
        The DS record based on the KSK record. This is used when [delegating](https://cloud.google.com/dns/docs/dnssec-advanced#subdelegation) DNSSEC-signed subdomains.
        """
        return pulumi.get(self, "ds_record")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique identifier for the resource; defined by the server.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isActive")
    def is_active(self) -> bool:
        """
        Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
        """
        return pulumi.get(self, "is_active")

    @property
    @pulumi.getter(name="keyLength")
    def key_length(self) -> int:
        """
        Length of the key in bits. Specified at creation time then immutable.
        """
        return pulumi.get(self, "key_length")

    @property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> int:
        """
        The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
        """
        return pulumi.get(self, "key_tag")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> str:
        """
        Base64 encoded public half of this key.
        """
        return pulumi.get(self, "public_key")


@pulumi.output_type
class GetKeysKeySigningKeyDigestResult(dict):
    def __init__(__self__, *,
                 digest: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str digest: The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
        :param str type: Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
        """
        if digest is not None:
            pulumi.set(__self__, "digest", digest)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def digest(self) -> Optional[str]:
        """
        The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
        """
        return pulumi.get(self, "digest")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetKeysZoneSigningKeyResult(dict):
    def __init__(__self__, *,
                 algorithm: str,
                 creation_time: str,
                 description: str,
                 digests: Sequence['outputs.GetKeysZoneSigningKeyDigestResult'],
                 id: str,
                 is_active: bool,
                 key_length: int,
                 key_tag: int,
                 public_key: str):
        """
        :param str algorithm: String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
        :param str creation_time: The time that this resource was created in the control plane. This is in RFC3339 text format.
        :param str description: A mutable string of at most 1024 characters associated with this resource for the user's convenience.
        :param Sequence['GetKeysZoneSigningKeyDigestArgs'] digests: A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
        :param str id: Unique identifier for the resource; defined by the server.
        :param bool is_active: Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
        :param int key_length: Length of the key in bits. Specified at creation time then immutable.
        :param int key_tag: The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
        :param str public_key: Base64 encoded public half of this key.
        """
        pulumi.set(__self__, "algorithm", algorithm)
        pulumi.set(__self__, "creation_time", creation_time)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "digests", digests)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "is_active", is_active)
        pulumi.set(__self__, "key_length", key_length)
        pulumi.set(__self__, "key_tag", key_tag)
        pulumi.set(__self__, "public_key", public_key)

    @property
    @pulumi.getter
    def algorithm(self) -> str:
        """
        String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        The time that this resource was created in the control plane. This is in RFC3339 text format.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A mutable string of at most 1024 characters associated with this resource for the user's convenience.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def digests(self) -> Sequence['outputs.GetKeysZoneSigningKeyDigestResult']:
        """
        A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
        """
        return pulumi.get(self, "digests")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique identifier for the resource; defined by the server.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isActive")
    def is_active(self) -> bool:
        """
        Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
        """
        return pulumi.get(self, "is_active")

    @property
    @pulumi.getter(name="keyLength")
    def key_length(self) -> int:
        """
        Length of the key in bits. Specified at creation time then immutable.
        """
        return pulumi.get(self, "key_length")

    @property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> int:
        """
        The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
        """
        return pulumi.get(self, "key_tag")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> str:
        """
        Base64 encoded public half of this key.
        """
        return pulumi.get(self, "public_key")


@pulumi.output_type
class GetKeysZoneSigningKeyDigestResult(dict):
    def __init__(__self__, *,
                 digest: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str digest: The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
        :param str type: Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
        """
        if digest is not None:
            pulumi.set(__self__, "digest", digest)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def digest(self) -> Optional[str]:
        """
        The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
        """
        return pulumi.get(self, "digest")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
        """
        return pulumi.get(self, "type")


