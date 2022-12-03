"""TestCase module"""
from test_result import TestResult


class TestCase:
    """TestCase class"""

    def __init__(self, name):
        self.name = name

    def set_up(self):
        """Set up given for TestCase"""

    def tear_down(self):
        """Clean after TestCase"""

    def run(self):
        """Run method that is passed in constructor"""
        result = TestResult()
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.tear_down()
        return result
