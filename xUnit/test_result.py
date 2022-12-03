"""Test Result module"""


class TestResult:
    """Result class"""

    def __init__(self):
        self.run_count = 0
        self.error_count = 0

    def test_started(self):
        """Test started"""
        self.run_count += 1

    def test_failed(self):
        """Test failed"""
        self.error_count += 1

    def summary(self):
        """Return test result summary"""
        return f"{self.run_count} run, {self.error_count} failed"
