# unittest module is imported for using functionalities of unittest later in program
import unittest
# import all the functions from calculate
from calculator import *

# setUp() method allows us to define instruction that will be executed before running tests.
def setUpModule():
    print("Starting the testing of program")

# tearDown() method allows us to define instruction that will be executed after running tests.
def tearDownModule():
    print("Stopping the testing of program")

# unittest.TestCase is subclassed to create a testcase
class TestCalculator(unittest.TestCase):

    # an instance of the calculator is created which can be used in all tests
    @classmethod
    def setUpClass(cls):
        print('Setting up the class')
        cls.calc = Calculator()

    # method for testing addition functionality
    def test_addition(self):
        # assertEqual() is called to check for an expected result
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        answer = num1 + num2
        self.assertEqual(self.calc.addition(num1, num2), answer,
                         msg="Addition Test Case --> failed")

    # method for testing subtraction functionality
    def test_subtraction(self):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        answer = num1 - num2
        self.assertEqual(self.calc.subtraction(num1, num2), answer,
                         msg="Subtraction Test Case --> failed")

    # method for testing multiplication functionality
    def test_multiplication(self):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        answer = num1 * num2
        self.assertEqual(self.calc.multiplication(num1, num2), answer,
                         msg="Multiplication Test Case --> failed")

    # method for testing division functionality
    def test_division(self):
        dividend = int(input("Enter dividend: "))
        divisor = int(input("Enter divisor: "))
        answer = 0
        try:
            answer = dividend / divisor
        except Exception as e:
            print("Error:", e)
        self.assertEqual(self.calc.division(dividend, divisor), answer,
                         msg="Division Test Case --> failed")

    # method for testing factorial functionality
    def test_factorial(self):
        num = int(input("Enter number: "))
        fact = 1
        if num < 0:
            fact = None
        else:
            for i in range(1, num+1):
                fact = fact*i
        self.assertEqual(self.calc.factorial(num), fact,
                         msg="Factorial Test Case -> failed")

    # method for testing remainder functionality
    def test_remainder(self):
        dividend = int(input("Enter dividend: "))
        divisor = int(input("Enter divisor: "))
        answer = 0
        try:
            answer = dividend % divisor
        except Exception as e:
            print("Error:", e)
        self.assertEqual(self.calc.remainder(dividend, divisor), answer,
                         msg="Remainder Test Case --> failed")

    # def test_perfect_division(self):
    #     self.assertEqual(self.calc.perfect_division(5, 5), answer, quotient, remainder,
    #                      msg="Perfect Division Test-1: positive number, positive number --> failed")

    # method for testing sin functionality
    def test_sine(self):
        angle_degrees = int(input("Enter angle in degrees: "))
        angle_radian = math.pi * (angle_degrees / 180)
        answer = math.sin(angle_radian)
        self.assertEqual(self.calc.sine(angle_degrees), answer,
                         msg="Sine Test --> failed")

    # method for testing cos functionality
    def test_cosine(self):
        angle_degrees = int(input("Enter angle in degrees: "))
        angle_radian = math.pi * (angle_degrees / 180)
        answer = math.cos(angle_radian)
        self.assertEqual(self.calc.cosine(angle_degrees), answer,
                         msg="Cosine Test --> failed")

    # method for testing tan functionality
    def test_tangent(self):
        angle_degrees = int(input("Enter angle in degrees: "))
        angle_radian = math.pi * (angle_degrees / 180)
        answer = math.tan(angle_radian)
        self.assertEqual(self.calc.tangent(angle_degrees), answer,
                         msg="Tangent Test --> failed")

    # method for testing square root functionality
    def test_square_root(self):
        num = int(input("Enter number: "))
        answer = math.sqrt(num)
        self.assertEqual(self.calc.square_root(num), answer,
                         msg="Square root Test --> failed")

    # method for testing square functionality
    def test_square(self):
        num = int(input("Enter number: "))
        answer = num*num
        self.assertEqual(self.calc.square(num), answer,
                         msg="Square Test --> failed")

    # method for testing cube functionality
    def test_cube(self):
        num = int(input("Enter number: "))
        answer = num * num * num
        self.assertEqual(self.calc.cube(num), answer,
                         msg="Cube Test --> failed")

    # method for testing any power functionality
    def test_any_power(self):
        num = int(input("Enter number: "))
        power = int(input("Enter power: "))
        answer = num**power
        self.assertEqual(self.calc.any_power(num, power), answer,
                         msg="Any Power Test --> failed")

    # method for testing log of base 10 functionalit
    def test_log_of_base_10(self):
        num = int(input("Enter number: "))
        answer = math.log10(num)
        self.assertEqual(self.calc.log_of_base_10(num), answer,
                         msg="Log of base 10 Test --> failed")

    # method for testing log of base 2 functionality
    def test_log_of_base_2(self):
        num = int(input("Enter number: "))
        answer = math.log2(num)
        self.assertEqual(self.calc.log_of_base_2(num), answer,
                         msg="Log of base 2 Test --> failed")


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # verbosity=2 is used to see the 2nd level of information about test cases
