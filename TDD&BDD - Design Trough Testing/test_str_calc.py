"""Testing module fpr String Calculator"""

import unittest
from str_calc import Calculator


class TestStrCalc(unittest.TestCase):
    """Test class for testing outcomes that StrCalc forms"""

    def test_should_return_zero_for_empty_string(self):
        """Testing scenario 1:"""
        self.assertEqual(0, Calculator().add(""))


unittest.main()
