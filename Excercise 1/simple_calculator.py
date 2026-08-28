
first = int(input("Enter first Number\t"))
second = int(input("Enter Second Number\t"))
operator = input("Enter any operator for calucating (+ - / *):")


if operator == "+":
    print("Addition of two numbers = ", first + second)
elif operator == "-":
    print("Substraction of two numbers = ", first - second)
elif operator == "*":
    print("Multiple of two numbers = ", first * second)
elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")