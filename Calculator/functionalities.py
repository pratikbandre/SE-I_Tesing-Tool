import math


def menu():
    print("Operations")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Factorial")
    print("6. Remainder")
    print("7. Perfect Division")
    print("8. Trigonometric Operations")
    print("9. Exponential Operations")
    print("10. Logarithmic Operations")
    print("0. EXIT")


def trigonometric_menu():
    print("Trigonometric Operations")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")


def exponential_menu():
    print("Exponential Operations")
    print("1. Square root")
    print("2. Square")
    print("3. Cube")
    print("4. Any power")


def logarithmic_menu():
    print("Logarithmic Operations")
    print("1. log of base 10")
    print("2. log of base 2")


def addition(num1, num2):
    return num1+num2


def subtraction(num1, num2):
    return num1-num2


def multiplication(num1, num2):
    return num1*num2


def division(dividend, divisor):
    return dividend / divisor


def factorial(num):
    fact = 1
    if num < 0:
        return ""
    for i in range(1, num+1):
        fact = fact*i
    return fact


def remainder(dividend, divisor):
    return dividend % divisor


def perfect_division(dividend, divisor):
    return dividend/divisor, dividend//divisor, dividend % divisor


def sine(angle_radian):
    return math.sin(angle_radian)


def cosine(angle_radian):
    return math.cos(angle_radian)


def tangent(angle_radian):
    return math.tan(angle_radian)


def square_root(num):
    return num**0.5


def square(num):
    return num**2


def cube(num):
    return num**3


def any_power(num, power):
    return num**power


def log_of_base_10(num):
    return math.log10(num)


def log_of_base_2(num):
    return math.log2(num)