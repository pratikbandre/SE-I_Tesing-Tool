# imported for using math functions later in code
import math


class Calculator:
    # function for adding numbers
    def addition(self, num1, num2):
        return num1 + num2

    # function for subtracting numbers
    def subtraction(self, num1, num2):
        return num1 - num2

    # function for multiplying numbers
    def multiplication(self, num1, num2):
        return num1 * num2

    # function for dividing numbers
    def division(self, dividend, divisor):
        if divisor == 0:
            return
        return dividend / divisor

    # function to find factorial of number
    def factorial(self, num):
        fact = 1
        if num < 0:
            return None
        elif num == 0:
            return 1
        for i in range(1, num + 1):
            fact = fact * i
        return fact

    # function to find remainder
    def remainder(self, dividend, divisor):
        if divisor == 0:
            return
        return dividend % divisor

    # def perfect_division(self, dividend, divisor):
    #     return dividend / divisor, dividend // divisor, dividend % divisor

    # function to find sin value of angle
    def sine(self, angle_degrees):
        angle_radian = math.pi * (angle_degrees / 180)
        return math.sin(angle_radian)

    # function to find cos value of angle
    def cosine(self, angle_degrees):
        angle_radian = math.pi * (angle_degrees / 180)
        return math.cos(angle_radian)

    # function to find tan value of angle
    def tangent(self, angle_degrees):
        angle_radian = math.pi * (angle_degrees / 180)
        return math.tan(angle_radian)

    # function to find square root of number
    def square_root(self, num):
        if num < 0:
            return
        return num ** 0.5

    # function to find square of number
    def square(self, num):
        return num ** 2

    # function to find cube of number
    def cube(self, num):
        return num ** 3

    # function to find any number raise to the power any number
    def any_power(self, num, power):
        return num ** power

    # function to find log base 10 of number
    def log_of_base_10(self, num):
        if num <= 0:
            return
        return math.log10(num)

    # function to find log base 2 of number
    def log_of_base_2(self, num):
        if num <= 0:
            return
        return math.log2(num)

