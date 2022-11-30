"""TestCase module"""


class TestCase:
    """TestCase class"""

    def __init__(self, name):
        self.name = name

    def run(self):
        """Run method that is passed in constructor"""
        method = getattr(self, self.name)
        method()
