

age = int(input("Enter your age \t"))

if age >= 18:
    print("You can vote")
    if age > 70:
        print("Senior citizen")
else:
    print("Can not vote")