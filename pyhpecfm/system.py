#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_version(cfmclient):
    """
    Function takes input cfmclient type object to authenticate against CFM API and queries
    versions API to return the version number of the system represented by the CFCMclient object
    Current supported params are

    :param cfmclient: object of type CFMClient
    :param params: dict of query parameters used to filter request from API
    :return: list of dicts

    >>> client= CFMClient('10.101.0.210', 'admin', 'plexxi')
    >>>get_switches(client)

    """
    path = 'versions'
    # takes input of dict object params and crafts query string from it.
    # looked at requests PreparedRequest but didn't mesh with cfmclient.get method
    # due to the way the URL was split
    return cfmclient.get(path).json().get('result')