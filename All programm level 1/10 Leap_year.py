# 10. Check whether the entered year is a leap year

year = int(input("Enter a Year : "))

if year % 4 == 0:
    print("Leap year")
else:
    print("Not an Leap Year")