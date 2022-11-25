"""Testing module"""

import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    def test_should_add_two_fractions(self):
        """Scenario 1: Add two fraction with just numerator"""
        self.assertEqual("3", str(Fraction(1).add(Fraction(2))))

    def test_should_add_two_fractional_numbers_with_the_same_denominators(self):
        """Scenario 2: Add two fractional numbers with the same denominators"""
        self.assertEqual("3/5", str(Fraction(1, 5).add(Fraction(2, 5))))

    def test_should_add_two_fractional_numbers_with_the_different_denominators(self):
        """Scenario 3: Add two fractional numbers with the different denominators"""
        self.assertEqual("5/6", str(Fraction(1, 2).add(Fraction(1, 3))))


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
