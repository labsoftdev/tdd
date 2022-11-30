"""Module for test case implementation"""
from test_case import TestCase


class WasRun(TestCase):
    """TestCase class"""

    def __init__(self, name):
        self.was_run = False
        TestCase.__init__(self, name)

    def test_method(self):
        """test method"""
        self.was_run = True
