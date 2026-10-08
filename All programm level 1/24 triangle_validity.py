# 24. Check triangle validity
# Sum of angles must be 180

a = int(input("Enter first angle = "))
b = int(input("Enter second angle = "))
c = int(input("Enter third angle = "))

if a > 0 and b > 0 and c > 0:
    if a + b + c == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")
else:
    print("Invalid Triangle")