"""Test suite module"""


class TestSuite:
    """TestSuite class"""

    def __init__(self):
        self.tests = []

    def add(self, test):
        """Add new test to test suite"""
        self.tests.append(test)

    def run(self, result):
        """Run all tests in test suite"""
        for test in self.tests:
            test.run(result)
