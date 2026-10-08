# 26. Determine grade using nested if

marks = int(input("Enter your marks = "))

if marks >= 40:
    if marks >= 90:
        Grade = "A+"
    elif marks >= 75:
        Grade = "B"
    elif marks >= 60:
        Grade = "C"
    else:
        Grade = "D"
    print("Grade ", Grade)

else:
    print("Grade F")
