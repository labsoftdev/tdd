"""String calculator module"""


class Calculator:
    """Calculator class that calculate resoult for inputs passed in string format"""

    def add(self, calc):
        """Returns the sum of numbers in the input"""
        ret_val = 0
        if calc != "":
            values = calc.split(", ")
            for value in values:
                ret_val += int(value)
        return ret_val
