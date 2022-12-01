"""TestCase module"""


class TestCase:
    """TestCase class"""

    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        """Run method that is passed in constructor"""
        self.setUp()
        method = getattr(self, self.name)
        method()
