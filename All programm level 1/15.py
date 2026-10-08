#15. Classify marks into Excellent, Very Good, Good, Poor

marks = float(input("Enter your Marks : "))

if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
else:
    print('Poor')