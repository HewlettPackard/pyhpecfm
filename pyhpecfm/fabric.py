#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains functions related to working with the fabric characteristics of the
desired HPE Composabale Fabric Manager instance
"""
#TODO fabric_ip_neworks functions


# section dealing with fabric functions

def get_fabrics(cfmclient, fabric_uuid=None):
    """
    Get :List of Fabrics currently defined in Composable Fabric .

    :param cfmclient:
    :param fabric_uuid: switch_uuid: UUID of switch from which to fetch port data
    :return: list of Dictionary objects where each dictionary represents a port on a
    Composable Fabric Module
    :rtype: list
    """
    path = 'fabrics'
    if fabric_uuid:
        path = 'fabrics/{}'.format(fabric_uuid)
    return cfmclient.get(path).json().get('result')


def get_fabric_ip_networks(cfmclient, fabric_uuid=None):
    """
    Get :List of Fabrics currently defined in Composable Fabric .

    :param cfmclient:
    :param fabric_uuid: switch_uuid: UUID of switch from which to fetch port data
    :return: list of Dictionary objects where each dictionary represents a port on a
    Composable Fabric Module
    :rtype: list
    """
    path = 'fabric_ip_networks'
    if fabric_uuid:
        path = 'fabric_ip_networks/{}'.format(fabric_uuid)
    return cfmclient.get(path).json().get('result')


# section dealing with switches functions


def get_switches(cfmclient, params=None):
    """
    Function takes input cfmclient type object to authenticate against CFM API and queries
    all currently configured switches from the system and returns a list of dictionaries
    where each item in the list represents a single switch.
    Current supported params are

    :param cfmclient: object of type CFMClient
    :param params: dict of query parameters used to filter request from API
    :return: list of dicts

    >>> client= CFMClient('10.101.0.210', 'admin', 'plexxi')
    >>> get_switches(client, params={'ports': True})
    >>> get_switches(client, params={'ports': True, 'software': True})
    >>> get_switches(client, params={'ports': True, 'software': True, 'fabric': True})
    """
    path = 'switches'
    return cfmclient.get(path, params).json().get('result')





# Section dealing with ports

def get_ports(cfmclient, switch_uuid=None):
    """
    Get Composable Fabric switch ports.
    :param cfmclient: object of type CFMClient
    :param switch_uuid: switch_uuid: UUID of switch from which to fetch port data
    :return: list of Dictionary objects where each dictionary represents a port on a
    Composable Fabric Module
    :rtype: list
    """
    path='ports'
    if switch_uuid:
        path = 'ports?switches={}&type=access'.format(switch_uuid)
        return cfmclient.get(path).json().get('result')
    else:
        return cfmclient.get(path).json().get('result')


def update_ports(cfmclient, port_uuids, field, value):
    """
    Function to update various attributes of composable fabric module ports
    :param cfmclient:
    :param port_uuids: list of str where each string represents a single unique port in a
    composable fabric
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
        cfmclient.patch('ports', data)
