# 25. Take marks and print:
# 90 or above → Excellent
# 75–89 → Very Good
# 50–74 → Good
# Below 50 → Need Improvement

marks = int(input("Enter student Marks\t"))
if marks >= 90:
    print("Student is excellent")
elif marks >= 75 or marks <=89:
    print("Very good", marks)
elif marks >=50 or marks <=74:
    print("Good", marks)
else:
    print("Need Improvement", marks)

