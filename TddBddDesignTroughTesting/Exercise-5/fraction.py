"""Fraction module"""


class Fraction:
    """Fraction class"""

    def __init__(self, numerator, denominator=1):
        gdc = self._gcd(numerator, denominator)
        self.numerator = int(numerator / gdc)
        self.denominator = int(denominator / gdc)

    def add(self, other):
        """Performing addition of two fractional numbers"""
        return Fraction(self._get_numerator(other), self._get_denominator(other))

    def __str__(self) -> str:
        ret_val = str(self.numerator)
        if self.denominator != 1:
            if self.numerator < self.denominator:
                ret_val += "/" + str(self.denominator)
            elif self.numerator == self.denominator:
                ret_val = str(int(self.numerator / self.denominator))
            else:
                ret_val = (
                    str(int(self.numerator / self.denominator))
                    + " "
                    + str(self.numerator % self.denominator)
                    + "/"
                    + str(self.denominator)
                )
        return ret_val

    def _get_numerator(self, other):
        return self.numerator * other.denominator + other.numerator * self.denominator

    def _get_denominator(self, other):
        return self.denominator * other.denominator

    def _gcd(self, num, den):
        while num != den:
            if num > den:
                num -= den
            else:
                den -= num
        return num
