# 11. Compare two numbers and print the larger one

num1 = int(input("Enter First Number \t"))
num2 = int(input("Enter Second Number \t"))

if num1 == num2:
    print("Both number are same ")
elif num1 >= num2:
    print("First Number is Greater ", num1)
else:
    print("Second Number is Greater ", num2)

