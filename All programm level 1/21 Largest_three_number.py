# 21. Find the largest of three numbers using nested if

# first = int(input("Enter First Number = "))
# second = int(input("Enter second Number = "))
# third = int(input("Enter third Number = "))

# if first > second:
#     print("First number is greater")
# elif second > third:
#     print("Second number is greater")
# elif third > first:
#     print("Third number is greater")
# else:
#     print("Nothing")


# a = int(input("Enter First Number = "))
# b = int(input("Enter second Number = "))
# c = int(input("Enter third Number = "))

# if a > b:
#     if a > c:
#         largest = a
#     else:
#         largest = c
# else:
#     if b > c:
#         largest = b
#     else:
#         largest = c

# print("Largest Number : ", largest) 


# Find the largest of 4 number using nested if 

a = int(input("Enter First Number = "))
b = int(input("Enter second Number = "))
c = int(input("Enter third Number = "))
d = int(input("Enter Fourth Numbre = "))

if a > b:
    if a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
else:
    largest = d

print("Largest Number : ", largest) 


       
