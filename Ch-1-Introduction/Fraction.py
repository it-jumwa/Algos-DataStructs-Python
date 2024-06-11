class Fraction:
    def __init__(self, numerator: float, denominator: float):
        commonDivisor = self.gcd(numerator, denominator)
        self.numerator = numerator / commonDivisor
        self.denominator = denominator / commonDivisor

    def getNum(self) -> float:
        return self.numerator

    def getDen(self) -> float:
        return self.denominator

    def __str__(self) -> str:
        return str(self.numerator) + "/" + str(self.denominator)

    def show(self):
        print(self.numerator, "/", self.denominator)

    @staticmethod
    def gcd(m: float, n: float) -> int:
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

    def __add__(self, otherfraction: 'Fraction') -> 'Fraction':
        newNumerator = (self.numerator * otherfraction.denominator +
                        self.denominator * otherfraction.numerator)

        newDenominator = self.denominator * otherfraction.denominator

        return Fraction(newNumerator, newDenominator)

    def __eq__(self, other) -> bool:
        firstNum = self.numerator * other.denominator
        secondNum = other.numerator * self.denominator

        return firstNum == secondNum
