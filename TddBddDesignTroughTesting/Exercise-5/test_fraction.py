"""Testing module"""

import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    def test_should_add_two_fractions(self):
        """Scenario 1: Add two fraction with just numerator"""
        self.assertEqual("3", str(Fraction(1).add(Fraction(2))))


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
