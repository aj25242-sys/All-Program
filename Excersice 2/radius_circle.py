# Length and breadth of a rectagnle and radius of a circle are input through the keyboard. Write a program to calculate the area & perimeter of the rectagnle, and the area & circumference of the circle Rectangle area = length * breadth, perimeter = 2*(length + breadth) Circle area = 3.14 * radius2, circumference = 2*3.14*radius.

length = int(input("Enter length of a rectagngle of a circle = "))
breadth = int(input("Enter breadth of a rectgnle of a circle = "))
radius = int(input("Enter radius of a circle = "))

area_rectangle = length * breadth
perimeter_rectangle = 2*(length + breadth)

print("Area of rectagle is = ", area_rectangle)
print("Perimeter of a rectangle is = ", perimeter_rectangle)


circle_area = 3.14 * radius * radius
circle_circumference = 2*3.14*radius
print("Area of a circle is = ", circle_area)
print("Circumference of a circle is = ", circle_circumference)