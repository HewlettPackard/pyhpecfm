#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains functions related to working with the system characteristics of the
desired HPE Composabale Fabric Manager instance
"""


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
