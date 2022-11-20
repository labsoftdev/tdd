"""Testing module fpr String Calculator"""

import unittest
from str_calc import Calculator, NegativeNumberException


class TestStrCalc(unittest.TestCase):
    """Test class for testing outcomes that StrCalc forms"""

    def setUp(self):
        self.calc = Calculator(self._display)
        self.result = ""

    def test_should_return_zero_for_empty_string(self):
        """Testing scenario 1:"""
        assert self.calc.add("") == 0

    def test_should_return_value_for_single_number(self):
        """Testing scenario 2:"""
        assert 5 == self.calc.add("5")

    def test_should_return_sum_of_multiple_numbers(self):
        """Testing Scenario 3:"""
        assert 3 == self.calc.add("1, 2")

    def test_should_return_sum_of_multiple_numbers_with_newline_delimiter(self):
        """Testing Scenario 4:"""
        assert 6 == self.calc.add("1\n2, 3")

    def test_should_return_sum_of_multiple_numbers_with_user_defined_delimiter(self):
        """Testing Scenario 5:"""
        assert 3 == self.calc.add("//;\n1;2", "//|;|\n")

    def test_should_generate_an_exception_for_negative_number(
        self,
    ):
        """Testing Scenario 6:"""
        self.assertRaises(NegativeNumberException, self.calc.add, "-1")

    def test_should_generate_an_exception_for_negative_number_with_explanation(
        self,
    ):
        """Testing Scenario 7:"""
        with self.assertRaises(NegativeNumberException) as context:
            self.calc.add("-1")
        assert "Passed negative number!" == str(context.exception)

    def test_should_display_expression_and_result_after_calculationa(
        self,
    ):
        """Test for Scenario_8"""
        self.calc.add("1, 2")
        self.assertEqual("1 + 2 = 3", self.result)

    def _display(self, message):
        self.result = message


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
