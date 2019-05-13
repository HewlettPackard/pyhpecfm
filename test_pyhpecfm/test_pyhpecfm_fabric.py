# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpecfm.fabric module.
"""



from unittest import TestCase
from unittest import mock
from nose.plugins.skip import SkipTest


from pyhpecfm.fabric import *
from pyhpecfm.auth import *
import os

cfm_ip = os.environ['CFM_IP']
cfm_username = os.environ['CFM_USERNAME']
cfm_password = os.environ['CFM_PASSWORD']

client= CFMClient(cfm_ip, cfm_username,cfm_password)

#TODO TAKE OUT HARDCODED DATA LATER


class TestGetSwitches(TestCase):
    """
    Test Case for pyhpecfm.fabric get_switches function
    """

    def test_get_switches(self):
        """
        There will be verbose text here to describe what the test is actually doing
        """
        test_switches = get_switches(client)
        my_attributes = ['segment','fabric_uuid', 'fitting_number', 'ip_gateway', 'hostip_state', 'ip_address_v6', 'uuid', 'ip_mode', 'ip_gateway_v6', 'health', 'mac_address', 'ip_mode_v6', 'serial_number', 'status', 'description', 'ip_address', 'model', 'hw_revision', 'sw_version', 'name', 'ip_mask', 'configuration_number', 'operational_stage', 'ip_mask_v6']
        self.assertIs(type(test_switches), list)
        self.assertIs(type(test_switches[0]), dict)
        for i in test_switches[0].keys():
            self.assertIn(i, my_attributes)

    def test_get_switches_single_param(self):
        """
        There will be verbose text here to describe what the test is actually doing
        """
        test_switches = get_switches(client, params={'ports': True})
        my_attributes = ['ports','segment','fabric_uuid', 'fitting_number', 'ip_gateway',
                         'hostip_state', 'ip_address_v6', 'uuid', 'ip_mode', 'ip_gateway_v6', 'health', 'mac_address', 'ip_mode_v6', 'serial_number', 'status', 'description', 'ip_address', 'model', 'hw_revision', 'sw_version', 'name', 'ip_mask', 'configuration_number', 'operational_stage', 'ip_mask_v6']
        self.assertIs(type(test_switches), list)
        self.assertIs(type(test_switches[0]), dict)
        for i in test_switches[0].keys():
            self.assertIn(i, my_attributes)

    def test_get_switches_multiple_param(self):
        """
        There will be verbose text here to describe what the test is actually doing
        """
        test_switches = get_switches(client, params={'ports': True, 'software': True, 'fabric': True})
        my_attributes = ['ports','segment','fabric_uuid', 'fitting_number', 'ip_gateway',
                         'hostip_state', 'ip_address_v6', 'uuid', 'ip_mode', 'ip_gateway_v6', 'health', 'mac_address', 'ip_mode_v6', 'serial_number', 'status', 'description', 'ip_address', 'model', 'hw_revision', 'sw_version', 'name', 'ip_mask', 'configuration_number', 'operational_stage', 'ip_mask_v6']
        self.assertIs(type(test_switches), list)
        self.assertIs(type(test_switches[0]), dict)
        for i in test_switches[0].keys():
            self.assertIn(i, my_attributes)

class TestGetPorts(TestCase):
    """
    Test case for pyhpecfm.fabric get_ports function
    """
    def test_get_ports(self):
        """
        """
        test_switches = get_switches(client)
        test_switch = test_switches[0]['uuid']
        ports_list = get_ports(client, test_switch)
        my_attributes = ['fec_mode','holddown', 'native_vlan', 'description', 'speed_group',
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
    def test_get_fabric(self):
        """
        General test for get_fabric function
        """
        test_fabric = get_fabrics(client)
        my_attributes = ['description', 'foreign_manager_id', 'foreign_fabric_state', 'name',
                         'is_stable', 'foreign_management_state', 'foreign_manager_url', 'uuid']
        self.assertIs(type(test_fabric), list)
        self.assertIs(type(test_fabric[0]), dict)
        for i in test_fabric[0].keys():
            self.assertIn(i, my_attributes)

    def test_get_specific_fabric(self):
        """
        Test for get_fabrics using specific UUID
        :return:
        """
        all_fabrics = get_fabrics(client)
        my_fabric = all_fabrics[0]['uuid']
        test_fabric = get_fabrics(client, fabric_uuid=my_fabric)
        my_attributes = ['description', 'foreign_manager_id', 'foreign_fabric_state', 'name',
                         'is_stable', 'foreign_management_state', 'foreign_manager_url', 'uuid']
        self.assertIs(type(test_fabric), dict)
        for i in test_fabric.keys():
            self.assertIn(i, my_attributes)




