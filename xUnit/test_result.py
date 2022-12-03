"""Test Result module"""


class TestResult:
    """Result class"""

    def __init__(self):
        self.run_count = 0
        self.errorCount = 0

    def test_started(self):
        """Test started"""
        self.run_count += 1

    def test_failed(self):
        """Test failed"""
        self.errorCount = self.errorCount + 1

    def summary(self):
        """Return test result summary"""
        return f"{self.run_count} run, {self.errorCount} failed"
