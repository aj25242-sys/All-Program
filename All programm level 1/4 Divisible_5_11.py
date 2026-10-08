# 4. Check whether a number is divisible by both 5 and 11
num = int(input("Enter a Number  "))

if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by both 5 and 11  ",num)
else:
    print("Number is not divisible by both 5 and 11  ", num)