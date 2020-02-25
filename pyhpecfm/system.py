#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains functions related to working with the system characteristics of the
desired HPE Composable Fabric Manager instance
"""
from pyhpecfm import system


def get_versions(cfmclient):
    """
    Function takes input cfmclient type object to authenticate against CFM API and queries
    versions API to return the version number of the system represented by the CFCMclient object
    Current supported params are

    :param cfmclient: object of type CFMClient
    :return: list of dicts
    """
    path = 'versions'
    response = cfmclient.get(path)
    return response.json().get('result') if response else None


def get_audit_logs(cfmclient):
    """
    Get :List of audit log records currently defined in Composable Fabric.
    :param cfmclient:
    :return: list of Dictionary objects where each dictionary represents a single entry in the
    audit log of the HPE Composable Fabric Manager
    :rtype: list
    """
    path = 'v1/audits'
    response = cfmclient.get(path)
    return response.json().get('result') if response else None


def get_backups(cfmclient, uuid=None):
    """
    Function to get a list of current backups located on the Composable Fabric Manager
    represented by the cfcmclient object.
    :param cfmclient: Composable Fabric Manager connection object of type CFMClient
    :param uuid: str that represents the unique identifier for a specific backup
    :return: single dictionary if UUID. List of dictionaries where each dictionary represents a
    single backup.
    """
    path = 'v1/backups'
    if uuid:
        path += '/{}'.format(uuid)
    response = cfmclient.get(path)
    return response.json().get('result') if response else None


def create_backup(cfmclient):
    """
    Function to initiate a new backup on the Composable Fabric Manager represented by the
    CFCMClient object
    :param cfmclient: Composable Fabric Manager connection object of type CFMClient
    :return: HTTP response
    """
    path = 'v1/backups'
    response = cfmclient.post(path)
    return response.json().get('result') if response else None

def get_auth_sources(cfmclient, params=None):
    """
    Function to query current auth sources from a Composable Fabric Manager represented
    by the CFMClient object
    :param cfmclient: Composable Fabric Manager connection object of type CFMClient
    :return: list of dict where each dict represents a CFM auth source
    """
    path = 'v1/auth/sources'
    response = cfmclient.get(path, params)
    return response.json().get('result')

def get_users(cfmclient, params=None):
    """
        Function to query current local users from a Composable Fabric Manager represented
        by the CFMClient object
        :param cfmclient: Composable Fabric Manager connection object of type CFMClient
        :return: list of dict where each dict represents a CFM auth source
        """
    path = 'v1/users'
    response = cfmclient.get(path, params)
    return response.json().get('result')

def add_local_user(cfmclient, username, role, password, params=None):
    """
    Function to add a single new local user to a Composable Fabric Manager
    represented by the CFMClient Object
    :param cfmclient: Composable Fabric Manager connection object of type CFMClient
    :param username:
    :param role:
    :param password:
    :return:
    """
    local_uuid = system.get_auth_sources(cfmclient, params={'type':'local'})[0]['uuid']
    valid_roles = ['Viewer', 'Operator', 'Administrator']
    data =  {
            "username": username,
            "role": role,
            "auth_source_uuid" : local_uuid,
            "password" : password
                }
    return cfmclient.post('v1/users',params, data)



def delete_local_user(cfmclient, username):
    """
    Function to add a single new local user to a Composable Fabric Manager
    represented by the CFMClient Object
    :param cfmclient: Composable Fabric Manager connection object of type CFMClient
    :param username:
    :return:
    """
    user_uuid = system.get_users(cfmclient, params={"username": username})
    if len(user_uuid) > 0:
        user_uuid= user_uuid[0]['uuid']
    else:
        return ("Username not present")
    path = 'v1/users/{}'.format(user_uuid)
    print (path)
    return cfmclient.delete(path).json().get('result')
