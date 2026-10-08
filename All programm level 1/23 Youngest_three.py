# 23. Find the youngest of three people

a = int(input("Enter first member age = "))
b = int(input("Enter Second member age = "))
c = int(input("Enter Third member age = "))

if a < b:
    if a < c:
        print("First Member is Youngest", a)
    else:
        print("THird Member is Youngest", c)
else:
    if b < c:
        print("Second Member is Youngest", b)
    else:
        print("Third Member is Youngest",c)

