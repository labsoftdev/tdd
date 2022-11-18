"""String calculator module"""


class Calculator:
    """Calculator class that calculate resoult for inputs passed in string format"""

    def add(self, calc):
        """Returns the sum of numbers in the input"""
        if calc == "":
            return 0

        return int(calc)
