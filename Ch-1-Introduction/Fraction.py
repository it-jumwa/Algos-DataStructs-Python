class Fraction:
    def __init__(self, numerator: int, denominator: int):
        commonDivisor = self.gcd(numerator, denominator)
        self.__numerator = int(numerator / commonDivisor)
        self.__denominator = int(denominator / commonDivisor)

    def getNum(self) -> int:
        return self.__numerator

    def getDen(self) -> int:
        return self.__denominator

    def __str__(self) -> str:
        return str(self.__numerator) + "/" + str(self.__denominator)

    def show(self):
        print(self.__numerator, "/", self.__denominator)

    @staticmethod
    def gcd(m: int, n: int) -> int:
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

    def __add__(self, otherFraction: 'Fraction') -> 'Fraction':
        newNumerator = (self.__numerator * otherFraction.getDen() +
                        self.__denominator * otherFraction.getNum())

        newDenominator = self.__denominator * otherFraction.getDen()

        return Fraction(newNumerator, newDenominator)

    def __eq__(self, other: 'Fraction') -> bool:
        firstNum = self.__numerator * other.getDen()
        secondNum = other.getNum() * self.__denominator

        return firstNum == secondNum

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        newNumerator = (self.__numerator * other.getDen()) - (other.getNum() *
                                                              self.__denominator)
        newDenominator = self.__denominator * other.getDen()
        return Fraction(newNumerator, newDenominator)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.__numerator * other.getNum(), self.__denominator
                        * other.getDen())