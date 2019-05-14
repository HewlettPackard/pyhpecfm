# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpecfm.system module.
"""



from unittest import TestCase
from unittest import mock
from nose.plugins.skip import SkipTest


from pyhpecfm.system import *
from pyhpecfm.auth import *
import os

cfm_ip= os.environ['CFM_IP']
cfm_username= os.environ['CFM_USERNAME']
cfm_password= os.environ['CFM_PASSWORD']

client= CFMClient(cfm_ip, cfm_username,cfm_password)

#TODO TAKE OUT HARDCODED DATA LATER


class TestGetVersions(TestCase):
    """
    Test Case for pyhpecfm.fabric get_switches function
    """

    def test_get_versions(self):
        """
        There will be verbose text here to describe what the test is actually doing
        """
        test_version = get_version(client)
        my_attributes = ['current', 'supported', 'software']
        self.assertIs(type(test_version), dict)
        for i in test_version.keys():
            self.assertIn(i, my_attributes)

class TestGetAuditLogs(TestCase):
    """
    Test Case for pyhpecfm.fabric get_switches function
    """

    def test_get_audit_logs(self):
        """
        There will be verbose text here to describe what the test is actually doing
        """
        my_logs = get_audit_logs(client)
        my_attributes = ['description', 'record_type', 'log_date', 'uuid', 'stream_id', 'data',
                         'severity']
        self.assertIs(type(my_logs), list)
        for i in my_logs[0].keys():
            self.assertIn(i, my_attributes)







