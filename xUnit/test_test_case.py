"""Testing module for TestCase"""
from was_run import WasRun
from test_case import TestCase


class TestCaseTest(TestCase):
    """Test class for TestCase"""

    def setUp(self):
        self.test = WasRun("test_method")

    def test_should_invoke_test_method(self):
        """Scenario 1: test should have been invoked if the test was run"""
        self.test.run()
        assert self.test.was_run

    def test_should_invoke_setup_if_test_was_run(self):
        """Scenario 2: setUp should have been invoked if the test was run"""
        self.test.run()
        assert self.test.was_setup


TestCaseTest("test_should_invoke_test_method").run()
TestCaseTest("test_should_invoke_setup_if_test_was_run").run()
