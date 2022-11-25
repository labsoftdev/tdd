"""Fraction module"""


class Fraction:
    """Fraction class"""

    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        """Performing addition of two fractional numbers"""
        num = self.numerator + other.numerator
        den = self.denominator
        return Fraction(num, den)

    def __str__(self) -> str:
        return str(self.numerator)
