#2. The distance between two cities (in Km)  is input through the keyboard . Write a program to convert and print this distance in meter, feet, inches and centimeter.

distance = float(input("Enter distance between two cities in KM : "))

meter =  distance * 1000
feet = distance * 3280.84
inches = distance * 39370.08
centimeter = distance * 100000

print("KM converted in meter and value is = ", meter)
print("KM converted in feet and value is = ", feet)
print("KM converted in inches and value is = ", inches)
print("KM converted in centimeter and value is = ", centimeter)