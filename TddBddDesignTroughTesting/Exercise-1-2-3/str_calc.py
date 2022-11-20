"""String calculator module"""

import re


class Calculator:
    """Calculator class that calculate resoult for inputs passed in string format"""

    def __init__(self, display):
        self.display = display

    def get_values(self, values, delimiter):
        """Returns numbers form input string"""
        return filter(None, re.split(delimiter, values))

    def add(self, calc, delimiter=", |\n"):
        """Returns the sum of numbers in the input"""
        ret_val = 0
        if calc != "":
            values = self.get_values(calc, delimiter)
            for value in values:
                if int(value) < 0:
                    raise NegativeNumberException("Passed negative number!")
                ret_val += int(value)
        self.display(self.display_result(self.get_values(calc, delimiter), ret_val))
        return ret_val

    def display_result(self, values, result):
        """Print and return expression and result of calculation"""
        message = ""
        for value in values:
            if message:
                message += " + "
            message += value
        message += " = " + str(result)
        print(message)
        return message


class NegativeNumberException(Exception):
    """Rise exception if the negative number was passed"""
