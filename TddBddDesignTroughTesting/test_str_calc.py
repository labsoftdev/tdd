"""Testing module fpr String Calculator"""

import unittest
from str_calc import Calculator


class TestStrCalc(unittest.TestCase):
    """Test class for testing outcomes that StrCalc forms"""

    def test_should_return_zero_for_empty_string(self):
        """Testing scenario 1:"""
        assert Calculator().add("") == 0

    def test_should_return_value_for_single_number(self):
        """Testing scenario 2:"""
        assert 5 == Calculator().add("5")

    def test_should_return_sum_of_multiple_numbers(self):
        """Testing Scenario 3:"""
        assert 3 == Calculator().add("1, 2")

    def test_should_return_sum_of_multiple_numbers_with_newline_delimiter(self):
        """Testing Scenario 4:"""
        assert 6 == Calculator().add("1\n2, 3")

    def test_should_return_sum_of_multiple_numbers_with_user_defined_delimiter(self):
        """Testing Scenario 5:"""
        assert 3 == Calculator().add("//;\n1;2", "//|;|\n")


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
