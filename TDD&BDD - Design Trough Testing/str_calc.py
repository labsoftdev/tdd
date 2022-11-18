"""String calculator module"""

import re


class Calculator:
    """Calculator class that calculate resoult for inputs passed in string format"""

    def get_values(self, values, delimiter):
        """Returns numbers form input string"""
        return filter(None, re.split(delimiter, values))

    def add(self, calc, delimiter=", |\n"):
        """Returns the sum of numbers in the input"""
        ret_val = 0
        if calc != "":
            values = self.get_values(calc, delimiter)
            for value in values:
                ret_val += int(value)
        return ret_val
