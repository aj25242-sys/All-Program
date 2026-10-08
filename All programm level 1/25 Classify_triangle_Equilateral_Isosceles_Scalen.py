# 25. Classify triangle as Equilateral, Isosceles, or Scalene

a = float(input("Enter first side = "))
b = float(input("Enter second side = "))
c = float(input("Enter first side = "))

if a == b and b == c:
    print("Euuilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")