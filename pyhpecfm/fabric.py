# -*- coding: utf-8 -*-
"""
This module contains functions for working with fabric objects
of the HPE Composabale Fabric Manager instance.

For detailed documentation on the HPE Composable Fabric Manager API, please see the API
documentation located in your local CFM instance
"""


####################
# Fabric functions #
####################


def get_fabrics(cfmclient, fabric_uuid=None):
    """
    Get a list of Fabrics currently defined in Composable Fabric.
    :param cfmclient:
    :param fabric_uuid: switch_uuid: UUID of fabric
    :return: list of Dictionary objects where each dictionary represents a port on a
    Composable Fabric Module
    :rtype: list
    """
    path = 'v1/fabrics'
    if fabric_uuid:
        path += '/{}'.format(fabric_uuid)
    return cfmclient.get(path).json().get('result')


def add_fabrics(cfmclient, switch_ip, name, description):
    """
    Function to add a new fabric for management under a specific CFM instance
    :param cfmclient:
    :param switch_ip: IP address of one switch in the fabric
    :param name: Name of the new fabric
    :param description: description of the fabric
    :return:
    """
    path = 'v1/fabrics'
    data = {
        'host': '{}'.format(switch_ip),
        'name': '{}'.format(name),
        'description': '{}'.format(description)
    }
    return cfmclient.post(path, data=data).json().get('result')


def get_fabric_ip_networks(cfmclient, fabric_uuid=None):
    """
    Get a list of IP networks from the Composable Fabric.
    :param cfmclient:
    :param fabric_uuid: UUID of fabric
    :return: list of IP address dict objects
    :rtype: list
    """
    path = 'v1/fabric_ip_networks'
    if fabric_uuid:
        path += '/{}'.format(fabric_uuid)
    return cfmclient.get(path).json().get('result')


def add_ip_fabric(cfmclient, fabric_uuid, name, description, mode, subnet, prefix_length, vlan, switch_uuid,
                  switch_address):
    """
    Function to add new IP fabrics on specified CFM instance
    :param cfmclient:
    :param fabric_uuid: str UUID of the fabric on which this fabric IP network config should be created.Note that a
    fabric IP network config cannot be associated with a different fabric after creation
    :param name: str value Fabric IP Network name (displayed in UI)
    :param description: str value of the description of the new IP Fabric to be created
    :param mode: str value Fabric IP Network mode of operation
    :param subnet: str value The IPv4 subnet for the fabric IP network.
    :param prefix_length: str value the IPv4 subnet mask length for the fabric IP network
    :param vlan: str value enter a VLAN ID for the fabric IP network, which can be between 0 and 4000
    :param switch_uuid: str value UUID of the switch on which you would like to configure the switch address
    :param switch_address: str value A unique IPv4 switch address that is in the subnet for this fabric IP Network.
    :return: dict containing response of request
    """
    path = 'v1/fabric_ip_networks'
    data = {
        "fabric_uuid": '{}'.format(fabric_uuid),
        "subnet": {
            "prefix_length": int("{}".format(prefix_length)),
            "address": "{}".format(subnet)
        },
        "description": "{}".format(description),
        "vlan": int("{}".format(vlan)),
        "name": "{}".format(name),
        "switch_addresses": [
            {
                "switch_uuid": "{}".format(switch_uuid),
                "ip_address": {
                    "prefix_length": int("{}".format(prefix_length)),
                    "address": "{}".format(switch_address)
                }
            }
        ],
        "mode": "{}".format(mode)
    }
    return cfmclient.post(path, data=data).json().get('result')


def delete_fabric_ip_networks(cfmclient, fabric_uuid):
    """
    Delete a specific IP networks from the Composable Fabric.
    :param cfmclient:
    :param fabric_uuid: UUID of fabric
    :return:
    :rtype: list
    """
    path = 'v1/fabric_ip_networks/{}'.format(fabric_uuid)
    return cfmclient.delete(path).json().get('result')

#####################
# Fitting functions #
#####################


def perform_fit(cfmclient, fabric_uuid, name, description):
    """
    Request a full fit across managed Composable Fabrics.
    :param cfmclient: CFM Client object
    :param fabric_uuid: Valid Fabric UUID of an existing fabric
    :param name: Simple name of the fit
    :param description: Longer Description of the fitting request
    :return:
    """
    data = {
        'fabric_uuid': '{}'.format(fabric_uuid),
        'name': '{}'.format(name),
        'description': '{}'.format(description)
    }
    path = 'v1/fits'
    return cfmclient.post(path, data=data)


####################
# Switch functions #
####################


def get_switches(cfmclient, params=None):
    """
    Get a list of Composable Fabric switches
    :param cfmclient: object of type CFMClient
    :param params: dict of query parameters used to filter request from API
    :return: list of dicts
    >>> from pyhpecfm import client
    >>> cfm = client.CFMClient('hpecfm.local', 'admin', 'plexxi')
    >>> cfm.connect()
    >>> get_switches(cfm, params={'ports': True})
    >>> get_switches(cfm, params={'ports': True, 'software': True})
    >>> get_switches(cfm, params={'ports': True, 'software': True, 'fabric': True})
    """
    return cfmclient.get('v1/switches', params).json().get('result')


def create_switch(cfmclient, data, fabric_type=None):
    """
    Create a Composable Fabric switch.
    """
    params = {'type': fabric_type} if fabric_type else None
    return cfmclient.post('v1/switches', params, data).json().get('result')


####################
# Lag functions    #
####################


def get_lags(cfmclient, params=None):
    """
    Get a list of link aggregated objects
    :param cfmclient: object of type CFMClient
    :param params: dict of query parameters used to filter request from API
    :return: list of dicts
    >>> from pyhpecfm import client
    >>> cfm = client.CFMClient('hpecfm.local', 'admin', 'plexxi')
    >>> get_lags(cfm)
    >>> get_lags(cfm, params={'count_only': False})
    >>> get_lags(cfm, params={'count_only': False,'mac_attachments': False ,'mac_learnining':
    True,'ports': True,'port_type': access,'tag': True,'type': provisioned,'vlan_groups': True})
    """
    return cfmclient.get('v1/lags', params).json().get('result')


##################
# Port functions #
##################


def get_ports(cfmclient, switch_uuid=None):
    """
    Get Composable Fabric switch ports.
    :param cfmclient: object of type CFMClient
    :param switch_uuid: switch_uuid: UUID of switch from which to fetch port data
    :return: list of Dictionary objects where each dictionary represents a port on a
    Composable Fabric Module
    :rtype: list
    """
    path = 'v1/ports'
    if switch_uuid:
        path += '?switches={}&type=access'.format(switch_uuid)
    return cfmclient.get(path).json().get('result')


# TODO Write test for this function
def update_ports(cfmclient, port_uuids, field, value):
    """
    Update attributes of composable fabric switch ports
    :param cfmclient:
    :param port_uuids: list of str representing Composable Fabric port UUIDs
    :param field: str specific field which is desired to be modified (case-sensitive)
    :param value: str specific field which sets the new desired value for the field
    :return: dict which contains count, result, and time of the update
    :rtype: dict
    """
    if port_uuids:
        data = [{
            'uuids': port_uuids,
            'patch': [
                {
                    'path': '/{}'.format(field),
                    'value': value,
                    'op': 'replace'
                }
            ]
        }]
        return cfmclient.patch('v1/ports', data)


##################
# VLAN functions #
##################


def get_vlan_groups(cfmclient, params=None):
    """
    Get Composable Fabric vlan groups.
    :param params:
    :param cfmclient: object of type CFMClient
    :return: list of VLAN Group dictionary objects in the Composable Fabric
    :rtype: list
    """
    return cfmclient.get('v1/vlan_groups', params).json().get('result')

# TODO POST VLAN_GROUP FUNCTION

# TODO PUT VLAN GROUP FUNCTION

# TODO DELETE VLAN GROUP FUNCTION
