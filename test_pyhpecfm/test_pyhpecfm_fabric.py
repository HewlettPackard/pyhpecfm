# -*- coding: utf-8 -*-
"""
Module for testing the functions in pyhpecfm.fabric.
"""

import os
import vcr
from unittest import TestCase
from unittest import mock
from nose.plugins.skip import SkipTest

from pyhpecfm import client
from pyhpecfm import fabric

cfm_ip = os.environ['CFM_IP']
cfm_username = os.environ['CFM_USERNAME']
cfm_password = os.environ['CFM_PASSWORD']

cfm = client.CFMClient(cfm_ip, cfm_username,cfm_password)
#cfm.connect()

#TODO TAKE OUT HARDCODED DATA LATER
my_vcr = vcr.VCR(
    serializer='json',
    cassette_library_dir='fixtures/cassettes',
    record_mode='new_episodes',
    match_on=['uri', 'method'],
)

class TestGetSwitches(TestCase):
    """
    Test Case for pyhpecfm.fabric get_switches function
    """

    @vcr.use_cassette(cassette_library_dir='fixtures/cassettes')
    def test_get_switches(self):
        """
        Simple test to return switches. URL has no parameters
        :return:
        """
        cfm.connect()
        test_switches = fabric.get_switches(cfm)
        my_attributes = ['in_default_segment','segment','fabric_uuid', 'fitting_number',
                         'ip_gateway', 'hostip_state', 'ip_address_v6', 'uuid', 'ip_mode', 'ip_gateway_v6', 'health', 'mac_address', 'ip_mode_v6', 'serial_number', 'status', 'description', 'ip_address', 'model', 'hw_revision', 'sw_version', 'name', 'ip_mask', 'configuration_number', 'operational_stage', 'ip_mask_v6']
        self.assertIs(type(test_switches), list)
        self.assertIs(type(test_switches[0]), dict)
        for i in test_switches[0].keys():
            self.assertIn(i, my_attributes)

    @vcr.use_cassette(cassette_library_dir='fixtures/cassettes')
    def test_get_switches_single_param(self):
        """
        Test to return switches. Request is launched with a single parameter of ports.
        """
        cfm.connect()
        test_switches = fabric.get_switches(cfm, params={'ports': True})
        my_attributes = ['in_default_segment','ports','segment','fabric_uuid', 'fitting_number',
                         'ip_gateway',
                         'hostip_state', 'ip_address_v6', 'uuid', 'ip_mode', 'ip_gateway_v6', 'health', 'mac_address', 'ip_mode_v6', 'serial_number', 'status', 'description', 'ip_address', 'model', 'hw_revision', 'sw_version', 'name', 'ip_mask', 'configuration_number', 'operational_stage', 'ip_mask_v6']
        self.assertIs(type(test_switches), list)
        self.assertIs(type(test_switches[0]), dict)
        for i in test_switches[0].keys():
            self.assertIn(i, my_attributes)

    @vcr.use_cassette(cassette_library_dir='fixtures/cassettes')
    def test_get_switches_multiple_param(self):
        """
        Test to return switches. Request is launched with multiple parameters of Ports = True and a specific
        fabric on my CFM system.
        """
        cfm.connect()
        test_switches = fabric.get_switches(cfm)
        cfm_fabric = test_switches[0]['fabric_uuid']
        test_switches = fabric.get_switches(cfm, params={'ports': True, 'fabric' : cfm_fabric})
        my_attributes = ['in_default_segment','ports','segment','fabric_uuid', 'fitting_number',
                         'ip_gateway',
                         'hostip_state', 'ip_address_v6', 'uuid', 'ip_mode', 'ip_gateway_v6', 'health', 'mac_address', 'ip_mode_v6', 'serial_number', 'status', 'description', 'ip_address', 'model', 'hw_revision', 'sw_version', 'name', 'ip_mask', 'configuration_number', 'operational_stage', 'ip_mask_v6']
        self.assertIs(type(test_switches), list)
        self.assertIs(type(test_switches[0]), dict)
        for i in test_switches[0].keys():
            self.assertIn(i, my_attributes)

class TestGetPorts(TestCase):
    """
    Test case for pyhpecfm.fabric get_ports function
    """

    @vcr.use_cassette(cassette_library_dir='fixtures/cassettes')
    def test_get_ports(self):
        """
        """
        cfm.connect()
        test_switches = fabric.get_switches(cfm)
        test_switch = test_switches[0]['uuid']
        ports_list = fabric.get_ports(cfm, test_switch)
        my_attributes = ['downlink_switch_uuid','default_state','fec_mode','holddown',
                         'native_vlan', 'description',
                         'speed_group',
                         'ungrouped_vlans', 'link_state', 'switch_uuid', 'admin_state', 'form_factor',
                         'port_security_enabled', 'vlans', 'speed', 'switch_name', 'fec', 'read_only',
                         'port_label', 'uuid', 'is_uplink', 'vlan_group_uuids', 'name',
                         'permitted_qsfp_modes', 'silkscreen', 'type', 'bridge_loop_detection',
                         'qsfp_mode']
        self.assertIs(type(ports_list), list)
        self.assertIs(type(ports_list[0]), dict)
        for i in ports_list[0].keys():
            self.assertIn(i, my_attributes)



class TestGetFabric(TestCase):
    """
    Test
    case for pyhpecfm.fabric get_fabric function
    """
    @vcr.use_cassette(cassette_library_dir='fixtures/cassettes')
    def test_get_fabric(self):
        """
        General test for get_fabric function
        """
        cfm.connect()
        test_fabric = fabric.get_fabrics(cfm)
        my_attributes = ['health','segmented','description', 'foreign_manager_id',
                         'foreign_fabric_state', 'name',
                         'is_stable', 'foreign_management_state', 'foreign_manager_url', 'uuid']
        self.assertIs(type(test_fabric), list)
        self.assertIs(type(test_fabric[0]), dict)
        for i in test_fabric[0].keys():
            self.assertIn(i, my_attributes)

    @vcr.use_cassette(cassette_library_dir='fixtures/cassettes')
    def test_get_specific_fabric(self):
        """
        Test for get_fabrics using specific UUID
        :return:
        """
        cfm.connect()
        all_fabrics = fabric.get_fabrics(cfm)
        my_fabric = all_fabrics[0]['uuid']
        test_fabric = fabric.get_fabrics(cfm, fabric_uuid=my_fabric)
        my_attributes = ['health','segmented','description', 'foreign_manager_id',
                         'foreign_fabric_state', 'name',
                         'is_stable', 'foreign_management_state', 'foreign_manager_url', 'uuid']
        self.assertIs(type(test_fabric), dict)
        for i in test_fabric.keys():
            self.assertIn(i, my_attributes)


#TODO NEED CREATE IP FABRIC FUNCTION
#TODO NEED DELETE IP FABRIC FUNCTION
class TestGetFabric_IP_Networks(TestCase):
    """
    Test
    case for pyhpecfm.fabric get_fabric function
    """

    @vcr.use_cassette(cassette_library_dir='fixtures/cassettes')
    def test_get_fabric_ip_networks(self):
        """
        General test for pyhpecfm.fabric.get_fabric_ip_networks function
        """
        cfm.connect()
        test_fabric = fabric.get_fabric_ip_networks(cfm)
        my_attributes = ['subnet', 'fabric_uuid', 'name', 'switch_addresses','vlan', 'uuid',
                         'mode', 'description']
        self.assertIs(type(test_fabric), list)
        self.assertIs(type(test_fabric[0]), dict)
        for i in test_fabric[0].keys():
            self.assertIn(i, my_attributes)


#TODO Need Create VLAN Groups function
#TODO NEed Delete VLAN Groups function
class TestGetVLANGroups(TestCase):
    """
    Test
    case for pyhpecfm.fabric get_vlan_groups function
    """

    @vcr.use_cassette(cassette_library_dir='fixtures/cassettes')
    def test_get_vlan_groups(self):
        """
        General test for pyhpecfm.fabric.get_vlan_groups function
        """
        cfm.connect()
        test_vlan_groups = fabric.get_vlan_groups(cfm)
        my_attributes = ['lag_uuids', 'description', 'vlans', 'uuid', 'name']
        self.assertIs(type(test_vlan_groups), list)
        self.assertIs(type(test_vlan_groups[0]), dict)
        for i in test_vlan_groups[0].keys():
            self.assertIn(i, my_attributes)

    @vcr.use_cassette(cassette_library_dir='fixtures/cassettes')
    def test_get_vlan_groups_with_params(self):
        """
        General test for pyhpecfm.fabric.get_vlan_groups function with parameters to select
        a single VLAN group
        """
        cfm.connect()
        params = {'name': 'My_New_VLAN_Group'}
        test_vlan_groups = fabric.get_vlan_groups(cfm, params=params)
        my_attributes = ['lag_uuids', 'description', 'vlans', 'uuid', 'name']
        self.assertIs(type(test_vlan_groups), list)
        self.assertIs(type(test_vlan_groups[0]), dict)
        for i in test_vlan_groups[0].keys():
            self.assertIn(i, my_attributes)


class TestPerformFit(TestCase):
    """
    Test
    case for pyhpecfm.fabric perform_fit function
    """

    @vcr.use_cassette(cassette_library_dir='fixtures/cassettes')
    def test_perform_fit(self):
        """
        General test for pyhpecfm.fabric.perform_fit function
        """
        cfm.connect()
        all_fabrics = fabric.get_fabrics(cfm)
        my_fabric = all_fabrics[0]['uuid']
        fit = fabric.perform_fit(cfm, my_fabric, "Test Fit", "My Test Fit from Python Library")
        self.assertEqual(str(fit), '<Response [200]>')