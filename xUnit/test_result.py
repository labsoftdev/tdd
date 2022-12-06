"""Test Result module"""


class TestResult:
    """Result class"""

    def __init__(self):
        self.run_count = 0
        self.error_count = 0
        self.failed = []

    def test_started(self):
        """Test started"""
        self.run_count += 1

    def test_failed(self):
        """Test failed"""
        self.error_count += 1
        self.failed.append(self.run_count)

    def summary(self):
        """Return test result summary"""
        return f"{self.run_count} run, {self.error_count} failed"

    def failed_tests(self):
        """Return which tests failed"""
        return f"tests failed with index {self.failed}"
