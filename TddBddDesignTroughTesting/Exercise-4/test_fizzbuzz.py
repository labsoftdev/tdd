""" Testing module """

import unittest
from unittest.mock import MagicMock
from fizzbuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):
    """Test class for FizzBuzz"""

    def setUp(self):
        self.display = MagicMock()
        self.fizzbuzz = FizzBuzz(self.display)

    def test_should_return_one(self):
        """Scenario_1:"""
        assert self.fizzbuzz.fizzbuzz(1) == "1"

    def test_should_return_fizz(self):
        """Scenario_2:"""
        assert self.fizzbuzz.fizzbuzz(3) == "Fizz"

    def test_should_return_buzz(self):
        """Scenario_3:"""
        assert self.fizzbuzz.fizzbuzz(5) == "Buzz"

    def test_should_return_fizzbuzz(self):
        """Scenario_4:"""
        assert self.fizzbuzz.fizzbuzz(15) == "FizzBuzz"

    def test_should_iterate_from_one_to_hundred(self):
        """Scenario_5:"""
        iterator = self.fizzbuzz.iterate(1, 100)
        assert iterator == 100

    def test_should_iterate_from_one_to_hundred_and_render_result(self):
        """Scenario_6:"""
        self.fizzbuzz.iterate(1, 100)
        self.display.assert_called_with("Buzz")


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
