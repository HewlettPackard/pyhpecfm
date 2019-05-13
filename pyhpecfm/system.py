#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains functions related to working with the system characteristics of the
desired HPE Composable Fabric Manager instance
"""

#TODO audits functions  events and alarms

def get_version(cfmclient):
    """
    Function takes input cfmclient type object to authenticate against CFM API and queries
    versions API to return the version number of the system represented by the CFCMclient object
    Current supported params are

    :param cfmclient: object of type CFMClient
    :return: list of dicts
    """
    path = 'versions'
    return cfmclient.get(path).json().get('result')


def get_audit_logs(cfmclient):
    """
    Get :List of audit log records currently defined in Composable Fabric.
    :param cfmclient:
    :return: list of Dictionary objects where each dictionary represents a single entry in the
    audit log of the HPE Composable Fabric Manager
    :rtype: list
    """
    path = 'audits'
    return cfmclient.get(path).json().get('result')