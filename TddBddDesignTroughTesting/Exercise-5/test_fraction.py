"""Testing module"""

import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test class for Fraction"""

    def test_should_add_two_fractions(self):
        """Scenario 1: Add two fraction with just numerator"""
        self.assertEqual("3", str(Fraction(1).add(Fraction(2))))

    def test_should_add_two_fractional_numbers_with_the_same_denominators(self):
        """Scenario 2: Add two fractional numbers with the same denominators"""
        self.assertEqual("3/5", str(Fraction(1, 5).add(Fraction(2, 5))))

    def test_should_add_two_fractional_numbers_with_the_different_denominators(self):
        """Scenario 3: Add two fractional numbers with the different denominators"""
        self.assertEqual("5/6", str(Fraction(1, 2).add(Fraction(1, 3))))

    def test_should_add_two_fractional_numbers_with_whole_number(
        self,
    ):
        """Scenario 4: Add two fractional numbers with whole number"""
        self.assertEqual(str(Fraction(1, 3).add(Fraction(3, 4))), "1 1/12")

    def test_should_add_two_fractional_numbers_with_whole_number2(
        self,
    ):
        """Scenario 4: Add two fractional numbers with whole number"""
        self.assertEqual(str(Fraction(1, 3).add(Fraction(2, 3))), "1")


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
