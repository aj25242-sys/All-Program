

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a > 0 and b > 0 and c > 0:
    if a * a + b * b == c * c:
        print("Right-angled triangle")
    elif a * a + c * c == b * b:
        print("Right-angled triangle")
    elif b * b + c * c == a * a:
        print("Right-angled triangle")
    else:
        print("Not a right-angled triangle")
else:
    print("Invalid sides")