# -*- coding: utf-8 -*-
"""
Module for testing functions in  pyhpecfm.system.
"""

import os
import vcr
import logging

from unittest import TestCase
from unittest import mock
from nose.plugins.skip import SkipTest

from pyhpecfm import client
from pyhpecfm import system

cfm_ip= os.environ['CFM_IP']
cfm_username= os.environ['CFM_USERNAME']
cfm_password= os.environ['CFM_PASSWORD']


cfm = client.CFMClient(cfm_ip, cfm_username,cfm_password)
#cfm.connect()

#TODO TAKE OUT HARDCODED DATA LATER



logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from vcrpy
vcr_log = logging.getLogger("vcr")
vcr_log.setLevel(logging.INFO)

class TestGetVersions(TestCase):
    """
    Test Case for pyhpecfm.fabric get_switches function
    """


    @vcr.use_cassette(cassette_library_dir='./test_pyhpecfm/fixtures/cassettes')
    def test_get_versions(self):
        """
        Test pyhpeimc.system.get_version function.
        """
        cfm.connect()
        test_version = system.get_versions(cfm)
        my_attributes = ['current', 'supported', 'software']
        self.assertIs(type(test_version), dict)
        for i in test_version.keys():
            self.assertIn(i, my_attributes)

class TestGetAuditLogs(TestCase):
    """
    Test Case for pyhpecfm.fabric get_switches function
    """

    @vcr.use_cassette(cassette_library_dir='./test_pyhpecfm/fixtures/cassettes')
    def test_get_audit_logs(self):
        """
        Test pyhpecfm.system.get_audit_logs function.
        """
        cfm.connect()
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

    @vcr.use_cassette(cassette_library_dir='./test_pyhpecfm/fixtures/cassettes')
    def test_get_backups(self):
        """
        Test pyhpecfm.system.get_backups function.
        """
        cfm.connect()
        my_backups = system.get_backups(cfm)
        my_attributes = ['supported','image_version','url', 'checksum', 'uuid', 'name',
                         'date_created']
        self.assertIs(type(my_backups), list)
        for i in my_backups[0].keys():
            self.assertIn(i, my_attributes)

    @vcr.use_cassette(cassette_library_dir='./test_pyhpecfm/fixtures/cassettes')
    def test_get_specific_backup(self):
        """
        Test pyhpecfm.system.get_backups function.
        """
        cfm.connect()
        my_backups = system.get_backups(cfm)
        my_uuid = my_backups[0]['uuid']
        single_backup = system.get_backups(cfm, my_uuid)
        my_attributes = ['supported','image_version','url', 'checksum', 'uuid', 'name',
                         'date_created']
        self.assertIs(type(single_backup), dict)
        for i in single_backup.keys():
            self.assertIn(i, my_attributes)

class TestCreateBackup(TestCase):
    """
    Test Case for pyhpecfm.system create_backup function
    """

    @vcr.use_cassette(cassette_library_dir='./test_pyhpecfm/fixtures/cassettes')
    def test_create_backups(self):
        """
        Test pyhpecfm.system.create_backup function.
        """
        cfm.connect()
        backup_result = system.create_backup(cfm)
        my_attributes = ['supported','image_version','url', 'checksum', 'uuid', 'name',
                         'date_created']
        self.assertIs(type(backup_result), dict)
        for i in backup_result.keys():
            self.assertIn(i, my_attributes)


class TestGetAuthSources(TestCase):
    """
    Test Cases for pyhpecfm.system get_auth_sources function
    """

    @vcr.use_cassette(cassette_library_dir='./test_pyhpecfm/fixtures/cassettes')
    def test_get_auth_sources(self):
        """
        Test pyhpecfm.system.auth_sources function.
        """
        cfm.connect()
        my_sources = system.get_auth_sources(cfm)
        my_attributes = ['type', 'config', 'uuid', 'name', 'description']
        self.assertIs(type(my_sources), list)
        self.assertIs(type(my_sources[0]), dict)
        for i in my_sources[0].keys():
            self.assertIn(i, my_attributes)

    @vcr.use_cassette(cassette_library_dir='./test_pyhpecfm/fixtures/cassettes')
    def test_get_auth_sources_local(self):
        """
        Test pyhpecfm.system.auth_sources function.
        """
        cfm.connect()
        my_sources = system.get_auth_sources(cfm, params={'type' : 'local'})
        my_attributes = ['type', 'config', 'uuid', 'name', 'description']
        self.assertIs(type(my_sources), list)
        self.assertIs(type(my_sources[0]), dict)
        for i in my_sources[0].keys():
            self.assertIn(i, my_attributes)
        self.assertEqual(my_sources[0]['type'],'local')


class TestGetUsers(TestCase):
    """
    Test Cases for pyhpecfm.system get_users function
    """

    @vcr.use_cassette(cassette_library_dir='./test_pyhpecfm/fixtures/cassettes')
    def test_get_users(self):
        """
        Test pyhpecfm.system.users function.
        """
        cfm.connect()
        my_users = system.get_users(cfm)
        my_attributes = ['username', 'token_lifetime', 'uuid', 'auth_source_uuid', 'auth_source_name', 'distinguished_name', 'role', 'immutable', 'preferences']
        self.assertIs(type(my_users), list)
        self.assertIs(type(my_users[0]), dict)
        for i in my_users[0].keys():
            self.assertIn(i, my_attributes)

    def test_get_admin_user(self):
        """
        Test pyhpecfm.system.users function.
        """
        cfm.connect()
        my_users = system.get_users(cfm, params={"username": "admin"})
        my_attributes = ['username', 'token_lifetime', 'uuid', 'auth_source_uuid', 'auth_source_name', 'distinguished_name', 'role', 'immutable', 'preferences']
        self.assertIs(type(my_users), list)
        self.assertIs(type(my_users[0]), dict)
        for i in my_users[0].keys():
            self.assertIn(i, my_attributes)
        self.assertEqual(my_users[0]['username'], 'admin')


class TestAddLocalUsers(TestCase):
    """
    Test Cases for pyhpecfm.system get_users function
    """

    @vcr.use_cassette(cassette_library_dir='./test_pyhpecfm/fixtures/cassettes')
    def test_add_local_user(self):
        """
        Test pyhpecfm.system.users function.
        """
        cfm.connect()
        system.delete_local_user(cfm, 'test_user')
        my_users = system.add_local_user(cfm, 'test_user', 'Administrator', 'password')
        my_users = system.get_users(cfm, params={"username": "test_user"})
        my_attributes = ['username', 'token_lifetime', 'uuid', 'auth_source_uuid', 'auth_source_name',
                         'distinguished_name', 'role', 'immutable', 'preferences']
        self.assertIs(type(my_users), list)
        self.assertIs(type(my_users[0]), dict)
        for i in my_users[0].keys():
            self.assertIn(i, my_attributes)
        self.assertEqual(my_users[0]['username'], 'test_user')


class TestDeleteLocalUsers(TestCase):
    """
    Test Cases for pyhpecfm.system get_users function
    """

    @vcr.use_cassette(cassette_library_dir='./test_pyhpecfm/fixtures/cassettes')
    def test_delete_local_user(self):
        """
        Test pyhpecfm.system.users function.
        """
        cfm.connect()
        system.delete_local_user(cfm, 'test_user')
        system.add_local_user(cfm, 'test_user', 'Administrator', 'password')
        my_users = system.get_users(cfm, params={"username": "test_user"})
        my_attributes = ['username', 'token_lifetime', 'uuid', 'auth_source_uuid', 'auth_source_name',
                         'distinguished_name', 'role', 'immutable', 'preferences']
        self.assertIs(type(my_users), list)
        self.assertIs(type(my_users[0]), dict)
        for i in my_users[0].keys():
            self.assertIn(i, my_attributes)
        self.assertEqual(my_users[0]['username'], 'test_user')
        x = system.delete_local_user(cfm, 'test_user')
        self.assertIs(x, None)


