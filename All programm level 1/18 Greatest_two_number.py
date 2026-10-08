# 18. Check whether a number is the greatest of two numbers

num = int(input("Enter First Number : "))
num1 = int(input("Enter Second Number : "))

if num > num1:
    print(num,"First Number is greatest")
elif num1 > num:
    print(num1,"Second Number is greatest")
else:
    print("Both number are equal")
