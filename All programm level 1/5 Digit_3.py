# 5. Check whether a number is 3-digit or not

# num = int(input("Enter a Number  "))

# if 100 <= abs(num) <= 999:
#     print("Number are 3 digit  ", num)
# else:
#     print("Number are not 3 digit  ", num)
num = int(input("Enter a number: "))

if 100 <= abs(num) <= 999:
    print("It is a 3-digit number")
else:
    print("It is not a 3-digit number")