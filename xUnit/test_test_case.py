"""Testing module for TestCase"""
from was_run import WasRun
from test_case import TestCase


class TestCaseTest(TestCase):
    """Test class for TestCase"""

    def test_should_invoke_test_method(self):
        """Scenario 1: test should have been invoked if the test was run"""
        test = WasRun("test_method")
        assert not test.was_run
        test.run()
        assert test.was_run


TestCaseTest("test_should_invoke_testMethod").run()
