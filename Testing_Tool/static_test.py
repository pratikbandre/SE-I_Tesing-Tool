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
        self.assertEqual(self.calc.addition(5, 5), 10,
                         msg="Addition Test-1 --> positive number, positive number --> failed")
        self.assertEqual(self.calc.addition(-5, 5), 0,
                         msg="Addition Test-2 --> negative number, positive number --> failed")
        self.assertEqual(self.calc.addition(5, -5), 0,
                         msg="Addition Test-3 --> positive number, negative number --> failed")
        self.assertEqual(self.calc.addition(-5, -5), -10,
                         msg="Addition Test-4 --> negative number, negative number --> failed")

    # method for testing subtraction functionality
    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(5, 5), 0,
                         msg="Subtraction Test-1 --> positive number, positive number --> failed")
        self.assertEqual(self.calc.subtraction(-5, 5), -10,
                         msg="Subtraction Test-2 --> negative number, positive number --> failed")
        self.assertEqual(self.calc.subtraction(5, -5), 10,
                         msg="Subtraction Test-3 --> positive number, negative number --> failed")
        self.assertEqual(self.calc.subtraction(-5, -5), 0,
                         msg="Subtraction Test-4 --> negative number, negative number --> failed")

    # method for testing multiplication functionality
    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication(5, 5), 25,
                         msg="Multiplication Test-1 --> positive number, positive number --> failed")
        self.assertEqual(self.calc.multiplication(-5, 5), -25,
                         msg="Multiplication Test-2 --> negative number, positive number --> failed")
        self.assertEqual(self.calc.multiplication(5, -5), -25,
                         msg="Multiplication Test-3 --> positive number, negative number --> failed")
        self.assertEqual(self.calc.multiplication(-5, -5), 25,
                         msg="Multiplication Test-4 --> negative number, negative number --> failed")

    # method for testing division functionality
    def test_division(self):
        self.assertEqual(self.calc.division(5, 5), 1,
                         msg="Division Test-1 --> positive number, positive number --> failed")
        self.assertEqual(self.calc.division(-5, 5), -1,
                         msg="Division Test-2 --> negative number, positive number --> failed")
        self.assertEqual(self.calc.division(5, -5), -1,
                         msg="Division Test-3 --> positive number, negative number --> failed")
        self.assertEqual(self.calc.division(-5, -5), 1,
                         msg="Division Test-4 --> negative number, negative number --> failed")
        self.assertEqual(self.calc.division(5, 0), None,
                         msg="Division Test-5 --> positive number, zero --> failed")

    # method for testing factorial functionality
    def test_factorial(self):
        self.assertEqual(self.calc.factorial(-1), None,
                         msg="Factorial Test-1 --> negative number --> failed")
        self.assertEqual(self.calc.factorial(0), 1,
                         msg="Factorial Test-2 --> for zero --> failed")
        self.assertEqual(self.calc.factorial(1), 1,
                         msg="Factorial Test-3 --> for one --> failed")
        self.assertEqual(self.calc.factorial(5), 120,
                         msg="Factorial Test-4 --> positive number --> failed")

    # method for testing remainder functionality
    def test_remainder(self):
        self.assertEqual(self.calc.remainder(5, 5), 0,
                         msg="Remainder Test-1 --> positive same numbers --> failed")
        self.assertEqual(self.calc.remainder(4, 5), 4,
                         msg="Remainder Test-2 --> positive small number, positive big number --> failed")
        self.assertEqual(self.calc.remainder(5, 4), 1,
                         msg="Remainder Test-3 --> positive big number, positive small number --> failed")
        self.assertEqual(self.calc.remainder(-5, 4), 3,
                         msg="Remainder Test-4 --> negative big number, positive small number --> failed")
        self.assertEqual(self.calc.remainder(5, -4), -3,
                         msg="Remainder Test-5 --> positive big number, negative small number --> failed")
        self.assertEqual(self.calc.remainder(-5, -5), 0,
                         msg="Remainder Test-6 --> negative same numbers --> failed")
        self.assertEqual(self.calc.remainder(5, 0), None,
                         msg="Remainder Test-7 --> number divided by zero --> failed")

    # def test_perfect_division(self):
    #     self.assertEqual(self.calc.perfect_division(5, 5),
    #                      msg="Perfect Division Test-1: positive number, positive number --> failed")
    #     self.assertEqual(self.calc.perfect_division(-5, 5),
    #                      msg="Perfect Division Test-2: negative number, positive number --> failed")
    #     self.assertEqual(self.calc.perfect_division(5, -5),
    #                      msg="Perfect Division Test-3: positive number, negative number --> failed")
    #     self.assertEqual(self.calc.perfect_division(-5, -5),
    #                      msg="Perfect Division Test-4: negative number, negative number --> failed")

    # method for testing sin functionality
    def test_sine(self):
        self.assertEqual(self.calc.sine(0), 0,
                         msg="Sine Test-1 --> 0 degrees angle --> failed")
        self.assertEqual(self.calc.sine(90), 1,
                         msg="Sine Test-2 --> 90 degrees angle --> failed")

    # method for testing cos functionality
    def test_cosine(self):
        self.assertEqual(self.calc.cosine(0), 1,
                         msg="Cosine Test-1 --> 0 degrees angle --> failed")
        self.assertEqual(self.calc.cosine(90), 0,
                         msg="Cosine Test-2 --> 90 degrees angle --> failed")

    # method for testing tan functionality
    def test_tangent(self):
        self.assertEqual(self.calc.tangent(0), 0,
                         msg="Tangent Test-1 --> 0 degrees angle --> failed")
        self.assertEqual(self.calc.tangent(45), 1,
                         msg="Tangent Test-2 --> 45 degrees angle --> failed")

    # method for testing square root functionality
    def test_square_root(self):
        self.assertEqual(self.calc.square_root(4), 2.0,
                         msg="Square root Test-1 --> Perfect square --> failed")
        self.assertEqual(self.calc.square_root(-4), None,
                         msg="Square root Test-2 --> Negative number --> failed")
        self.assertEqual(self.calc.square_root(3), 1.7320508075688772,
                         msg="Square root Test-3 --> Non Perfect square --> failed")

    # method for testing square functionality
    def test_square(self):
        self.assertEqual(self.calc.square(5), 25,
                         msg="Square Test-1 --> Positive number  --> failed")
        self.assertEqual(self.calc.square(-5), 25,
                         msg="Square Test-2 --> Negative number --> failed")

    # method for testing cube functionality
    def test_cube(self):
        self.assertEqual(self.calc.cube(5), 125,
                         msg="Cube Test-1 --> Positive number --> failed")
        self.assertEqual(self.calc.cube(-5), -125,
                         msg="Cube Test-2 --> Negative number --> failed")

    # method for testing any power functionality
    def test_any_power(self):
        self.assertEqual(self.calc.any_power(5, 5), 3125,
                         msg="Any Power Test-1 --> positive number, positive power --> failed")
        self.assertEqual(self.calc.any_power(5, -5), 0.00032,
                         msg="Any Power Test-2 --> positive number, negative power --> failed")
        self.assertEqual(self.calc.any_power(-5, 5), -3125,
                         msg="Any Power Test-3 --> negative number, positive power --> failed")
        self.assertEqual(self.calc.any_power(-5, -5), -0.00032,
                         msg="Any Power Test-4 --> negative number, negative power --> failed")

    # method for testing log of base 10 functionality
    def test_log_of_base_10(self):
        self.assertEqual(self.calc.log_of_base_10(10), 1.0,
                         msg="Log of base 10 Test-1 --> positive number --> failed")
        self.assertEqual(self.calc.log_of_base_10(-10), None,
                         msg="Log of base 10 Test-2 --> negative number --> failed")
        self.assertEqual(self.calc.log_of_base_10(0), None,
                         msg="Log of base 10 Test-3 --> For Zero --> failed")

    # method for testing log of base 2 functionality
    def test_log_of_base_2(self):
        self.assertEqual(self.calc.log_of_base_2(2), 1.0,
                         msg="Log of base 2 Test-1 --> positive number --> failed")
        self.assertEqual(self.calc.log_of_base_2(-2), None,
                         msg="Log of base 2 Test-2 --> negative number --> failed")
        self.assertEqual(self.calc.log_of_base_2(0), None,
                         msg="Log of base 2 Test-3 --> For Zero --> failed")


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # verbosity=2 is used to see the 2nd level of information about test cases

