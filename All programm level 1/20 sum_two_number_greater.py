# 20. Check whether the sum of two numbers is greater than 100

num = int(input("Enter first number :"))
num1 = int(input("Enter Second Number :"))

total = num + num1

if total > 100:
    print("Sum of two number is greater of 100 ",total)
else:
    print("Sum of two number is less than of 100 ", total)