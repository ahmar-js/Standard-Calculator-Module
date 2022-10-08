# Created by Ahmer Aamir
# Created on 8 oct 2022

import math as mt
from BasicCalculator import BasicCalc


class SecondaryCalc(BasicCalc):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def factorial(self):
        return mt.factorial(self.first), mt.factorial(self.second)

    def power(self):
        return mt.pow(self.first, self.second)

    def log(self):
        return mt.log10(self.first), mt.log10(self.second)

    def ln(self):
        return mt.log(self.first), mt.log(self.second)


num1 = int(input("Please Enter First Number: "))
num2 = int(input("Please Enter Second Number: "))

BCalc = BasicCalc(num1, num2)
SCalc = SecondaryCalc(num1, num2)

print("\n> Sum of ", num1, " and ", num2, " is: ", BCalc.addition())
print("> Subtraction of ", num1, " and ", num2, " is: ", BCalc.subtraction())
print("> Multiplication of ", num1, " and ", num2, " is: ", BCalc.multiplication())
print("> Dvision of ", num1, " and ", num2, " is: ", BCalc.division())

print("\n> Factorial of (", num1, ", ", num2, ") is: ", SCalc.factorial())
print("> (", num1, " pow ", num2, ") is: ", SCalc.power())
print("> Standard Log of (", num1, ", ", num2, ") is: ", SCalc.log())
print("> Natural Log of (", num1, ", ", num2, ") is: ", SCalc.ln())
