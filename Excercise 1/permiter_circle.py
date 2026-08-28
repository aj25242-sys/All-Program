#Calculate area & perimeter of circle, rectangle, triangle, square.
# Area
radius = float(input("Entera Area of circle = "))

circle_area = 3.14 * radius * radius
circle_perimeter = 2 * 3.14 * radius

print("Area of Cirecle = ", circle_area)
print("Perimeter of Circle = ", circle_perimeter)

# Rectangle 
length = float(input("\nEnter length of Rectangle = "))
width = float(input("Enter widht of Rectangle = "))

rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)

print("Area of Rectangle = \t ", rectangle_area)
print("Perimeter of Rectangle = \t", rectangle_perimeter)