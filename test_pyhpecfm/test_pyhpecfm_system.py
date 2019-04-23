# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyawair.objects module.
"""



from unittest import TestCase
from unittest import mock
from nose.plugins.skip import SkipTest


from pyhpecfm.system import *
from secrets import *

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