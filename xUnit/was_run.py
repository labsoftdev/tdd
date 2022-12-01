"""Module for test case implementation"""
from test_case import TestCase


class WasRun(TestCase):
    """TestCase class"""

    def __init__(self, name):
        self.log = ""
        TestCase.__init__(self, name)

    def set_up(self):
        self.log += "setUp"

    def test_method(self):
        """test method"""
        self.log += " testMethod"

    def tear_down(self):
        self.log += " tearDown"
