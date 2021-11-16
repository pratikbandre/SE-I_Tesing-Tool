from functionalities import *

while True:
    menu()
    choice = int(input("Enter choice: "))
    if choice in range(0, 11):
        if choice == 1:
            num1 = int(input("Enter a 1st number: "))
            num2 = int(input("Enter a 2nd number: "))
            add = addition(num1, num2)
            print("Addition of", num1, "and", num2, "is", add)

        elif choice == 2:
            num1 = int(input("Enter a 1st number: "))
            num2 = int(input("Enter a 2nd number: "))
            sub = subtraction(num1, num2)
            print("Subtraction of", num1, "and", num2, "is", sub)

        elif choice == 3:
            num1 = int(input("Enter a 1st number: "))
            num2 = int(input("Enter a 2nd number: "))
            mul = multiplication(num1, num2)
            print("Multiplication of", num1, "and", num2, "is", mul)

        elif choice == 4:
            dividend = int(input("Enter Dividend: "))
            divisor = int(input("Enter Divisor: "))
            if divisor == 0:
                print("Can not divide number by 0")
            else:
                div = division(dividend, divisor)
                print("Division of", dividend, "and", divisor, "is", div)

        elif choice == 5:
            num = int(input("Enter a number: "))
            fact = 1
            if num < 0:
                print(" Factorial does not exist for negative numbers")
            elif num == 0:
                fact = 1
                print("The factorial of", num, "is", fact)
            else:
                fact = factorial(num)
                print("The factorial of", num, "is", fact)

        elif choice == 6:
            dividend = int(input("Enter Dividend: "))
            divisor = int(input("Enter Divisor: "))
            if divisor == 0:
                print("Can not divide number by 0")
            else:
                rem = remainder(dividend, divisor)
                print("Remainder of", dividend, "and", divisor, "is", rem)

        elif choice == 7:
            dividend = int(input("Enter Dividend: "))
            divisor = int(input("Enter Divisor: "))
            if divisor == 0:
                print("Can not divide number by 0")
            else:
                ans, quotient, rem = perfect_division(dividend, divisor)
                print("Dividend = ", dividend)
                print("Divisor = ", divisor)
                print("Answer = ", ans)
                print("Quotient = ", quotient)
                print("Remainder = ", rem)

        elif choice == 8:
            trigonometric_menu()
            trigonometric_choice = int(input("Enter choice: "))
            angle_degrees = int(input("Enter the Angle in Degrees: "))
            angle_radian = math.pi * (angle_degrees / 180)
            answer = None
            if trigonometric_choice == 1:
                answer = sine(angle_radian)
                print("Sin(", angle_degrees, ") = ", answer)
            elif trigonometric_choice == 2:
                answer = cosine(angle_radian)
                print("Cos(", angle_degrees, ") = ", answer)
            elif trigonometric_choice == 3:
                answer = tangent(angle_radian)
                print("Tan(", angle_degrees, ") = ", answer)

        elif choice == 9:
            exponential_menu()
            exponential_choice = int(input("Enter choice: "))
            num = int(input("Enter number: "))
            if exponential_choice == 1:
                answer = square_root(num)
                print("Square root of", num, "is", answer)
            elif exponential_choice == 2:
                answer = square(num)
                print("Square of", num, "is", answer)
            elif exponential_choice == 3:
                answer = cube(num)
                print("Cube of", num, "is", answer)
            elif exponential_choice == 4:
                power = int(input("Enter power: "))
                answer = any_power(num, power)
                print("Power", power, "of", num, "is", answer)

        elif choice == 10:
            logarithmic_menu()
            logarithmic_choice = int(input("Enter choice: "))
            num = int(input("Enter number: "))
            if logarithmic_choice == 1:
                answer = log_of_base_10(num)
                print("Base 10 log of", num, "is", answer)
            elif logarithmic_choice == 2:
                answer = log_of_base_2(num)
                print("Base 2 log of", num, "is", answer)

        next_calculation = input("Wants to continue? (yes/no): ")
        if next_calculation == "no":
            break
        elif choice == '0':
            break
    else:
        print("Invalid Choice!!!")