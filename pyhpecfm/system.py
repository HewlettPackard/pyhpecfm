#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
