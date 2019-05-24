# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class PublicIPAddress(Resource):
    """Public IP address resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param sku: The public IP address SKU.
    :type sku: ~azure.mgmt.network.v2018_02_01.models.PublicIPAddressSku
    :param public_ip_allocation_method: The public IP allocation method.
     Possible values are: 'Static' and 'Dynamic'. Possible values include:
     'Static', 'Dynamic'
    :type public_ip_allocation_method: str or
     ~azure.mgmt.network.v2018_02_01.models.IPAllocationMethod
    :param public_ip_address_version: The public IP address version. Possible
     values are: 'IPv4' and 'IPv6'. Possible values include: 'IPv4', 'IPv6'
    :type public_ip_address_version: str or
     ~azure.mgmt.network.v2018_02_01.models.IPVersion
    :ivar ip_configuration: The IP configuration associated with the public IP
     address.
    :vartype ip_configuration:
     ~azure.mgmt.network.v2018_02_01.models.IPConfiguration
    :param dns_settings: The FQDN of the DNS record associated with the public
     IP address.
    :type dns_settings:
     ~azure.mgmt.network.v2018_02_01.models.PublicIPAddressDnsSettings
    :param ip_tags: The list of tags associated with the public IP address.
    :type ip_tags: list[~azure.mgmt.network.v2018_02_01.models.IpTag]
    :param ip_address: The IP address associated with the public IP address
     resource.
    :type ip_address: str
    :param idle_timeout_in_minutes: The idle timeout of the public IP address.
    :type idle_timeout_in_minutes: int
    :param resource_guid: The resource GUID property of the public IP
     resource.
    :type resource_guid: str
    :param provisioning_state: The provisioning state of the PublicIP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    :param zones: A list of availability zones denoting the IP allocated for
     the resource needs to come from.
    :type zones: list[str]
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'ip_configuration': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'PublicIPAddressSku'},
        'public_ip_allocation_method': {'key': 'properties.publicIPAllocationMethod', 'type': 'str'},
        'public_ip_address_version': {'key': 'properties.publicIPAddressVersion', 'type': 'str'},
        'ip_configuration': {'key': 'properties.ipConfiguration', 'type': 'IPConfiguration'},
        'dns_settings': {'key': 'properties.dnsSettings', 'type': 'PublicIPAddressDnsSettings'},
        'ip_tags': {'key': 'properties.ipTags', 'type': '[IpTag]'},
        'ip_address': {'key': 'properties.ipAddress', 'type': 'str'},
        'idle_timeout_in_minutes': {'key': 'properties.idleTimeoutInMinutes', 'type': 'int'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'zones': {'key': 'zones', 'type': '[str]'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, sku=None, public_ip_allocation_method=None, public_ip_address_version=None, dns_settings=None, ip_tags=None, ip_address: str=None, idle_timeout_in_minutes: int=None, resource_guid: str=None, provisioning_state: str=None, etag: str=None, zones=None, **kwargs) -> None:
        super(PublicIPAddress, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.sku = sku
        self.public_ip_allocation_method = public_ip_allocation_method
        self.public_ip_address_version = public_ip_address_version
        self.ip_configuration = None
        self.dns_settings = dns_settings
        self.ip_tags = ip_tags
        self.ip_address = ip_address
        self.idle_timeout_in_minutes = idle_timeout_in_minutes
        self.resource_guid = resource_guid
        self.provisioning_state = provisioning_state
        self.etag = etag
        self.zones = zones