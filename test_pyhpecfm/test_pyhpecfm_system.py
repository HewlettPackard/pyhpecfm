# -*- coding: utf-8 -*-
"""
Module for testing functions in  pyhpecfm.system.
"""

import os

from unittest import TestCase
from unittest import mock
from nose.plugins.skip import SkipTest

from pyhpecfm import client
from pyhpecfm import system

cfm_ip= os.environ['CFM_IP']
cfm_username= os.environ['CFM_USERNAME']
cfm_password= os.environ['CFM_PASSWORD']

cfm = client.CFMClient(cfm_ip, cfm_username,cfm_password)
cfm.connect()

#TODO TAKE OUT HARDCODED DATA LATER


class TestGetVersions(TestCase):
    """
    Test Case for pyhpecfm.fabric get_switches function
    """

    def test_get_versions(self):
        """
        Test pyhpeimc.system.get_version function.
        """
        test_version = system.get_versions(cfm)
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
        Test pyhpecfm.system.get_audit_logs function.
        """
        my_logs = system.get_audit_logs(cfm)
        my_attributes = ['description', 'record_type', 'log_date', 'uuid',
                         'stream_id', 'data', 'severity']
        self.assertIs(type(my_logs), list)
        for i in my_logs[0].keys():
            self.assertIn(i, my_attributes)


class TestGetBackups(TestCase):
    """
    Test Cases for pyhpecfm.system get_backups function
    """

    def test_get_backups(self):
        """
        Test pyhpecfm.system.get_backups function.
        """
        my_backups = get_backups(client)
        my_attributes = ['url', 'checksum', 'uuid', 'name', 'date_created']
        self.assertIs(type(my_backups), list)
        for i in my_backups[0].keys():
            self.assertIn(i, my_attributes)

    def test_get_specific_backup(self):
        """
        Test pyhpecfm.system.get_backups function.
        """
        my_backups = get_backups(client)
        my_uuid = my_backups[0]['uuid']
        single_backup = get_backups(client, my_uuid)
        my_attributes = ['url', 'checksum', 'uuid', 'name', 'date_created']
        self.assertIs(type(single_backup), dict)
        for i in single_backup.keys():
            self.assertIn(i, my_attributes)

class TestCreateBackup(TestCase):
    """
    Test Case for pyhpecfm.system create_backup function
    """

    def test_get_backups(self):
        """
        Test pyhpecfm.system.create_backup function.
        """
        backup_result = create_backup(client)
        self.assertEqual(200, backup_result.status_code)





