"""Testing module for TestCase"""
from was_run import WasRun
from test_case import TestCase


class TestCaseTest(TestCase):
    """Test class for TestCase"""

    def __init__(self, name):
        self.test = None
        TestCase.__init__(self, name)

    def set_up(self):
        self.test = WasRun("test_method")

    def test_should_invoke_in_order_setup_test_method_and_tear_down(self):
        """Testing test running"""
        self.test.run()
        assert self.test.log == "setUp testMethod tearDown"


TestCaseTest("test_should_invoke_in_order_setup_test_method_and_tear_down").run()
