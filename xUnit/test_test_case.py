"""Testing module for TestCase"""
from was_run import WasRun
from test_case import TestCase
from test_result import TestResult
from test_suite import TestSuite


class TestCaseTest(TestCase):
    """Test class for TestCase"""

    def __init__(self, name):
        self.test = None
        TestCase.__init__(self, name)

    def set_up(self):
        self.result = TestResult()
        self.test = WasRun("test_method")

    def test_should_invoke_in_order_setup_test_method_and_tear_down(self):
        """Testing test running"""
        self.test.run(self.result)
        assert self.test.log == "setUp testMethod tearDown"

    def test_should_return_collected_results(self):
        """Testing result of test running"""
        self.test.run(self.result)
        assert self.result.summary() == "1 run, 0 failed"

    def test_should_return_that_one_test_failed(self):
        """Testing test summary format"""
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert result.summary() == "1 run, 1 failed"

    def test_should_return_collected_results_of_failing_test(self):
        """Testing result of test running"""
        self.test = WasRun("failing_test_method")
        self.test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed"

    def test_should_return_summary_of_multiple_tests(self):
        """Testing multiple tests run"""
        suite = TestSuite()
        suite.add(WasRun("failing_test_method"))
        suite.add(self.test)
        suite.run(self.result)
        assert self.result.summary() == "2 run, 1 failed"


suite = TestSuite()
suite.add(TestCaseTest("test_should_invoke_in_order_setup_test_method_and_tear_down"))
suite.add(TestCaseTest("test_should_return_collected_results"))
suite.add(TestCaseTest("test_should_return_that_one_test_failed"))
suite.add(TestCaseTest("test_should_return_collected_results_of_failing_test"))
suite.add(TestCaseTest("test_should_return_summary_of_multiple_tests"))
result = TestResult()
suite.run(result)
print(result.summary())
