"""TestCase module"""


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
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()
