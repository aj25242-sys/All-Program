# 6. Two numbers are input through the keyboard into two location C and D. Write a program to interchange the content of C and D.

a = int(input("Enter first number = "))
b = int(input("Enter second number = "))

print("Before interchange first number is = ", a)
print("Before interchange second number is = ", b)
c = a
a = b
b = c

print("After interchange first number is = ", a)
print("After interchange second number is = ", b)