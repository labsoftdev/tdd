""" FizzBuzz module"""


class FizzBuzz:
    """FizzBuzz class"""

    def __init__(self, display):
        self.display = display

    def fizzbuzz(self, number):
        """FizzBuzz implementation"""
        result = ""
        if (number % 3) == 0:
            result = "Fizz"
        if (number % 5) == 0:
            result += "Buzz"
        if result == "":
            result = str(number)
        self.display(self._render(result))
        return result

    def iterate(self, start, end):
        """Iterate to provided range of numbers"""
        _it = 0
        for value in range(start, end + 1):
            _it += 1
            self.fizzbuzz(value)
        return _it

    def _render(self, result):
        print(result)
        return result
