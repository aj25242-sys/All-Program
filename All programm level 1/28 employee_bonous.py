# 28. Check Employee Bonus
# Example:
# Experience >= 5 years → 10% bonus
# Experience >= 3 years → 5% bonus
# Otherwise → No bonus

salary = int(input("Enter your salary = "))
experience = int(input("Enter your experience in year = "))

if experience >= 5:
    bonous = salary * 10 / 100
    Net_salary = salary + bonous
    print("Bonus is ", bonous)
    print("Your salary is after adding bonous = ",Net_salary)
elif experience >= 3:
    bonous = salary * 5 / 100
    Net_salary = salary + bonous
    print("Bonous is ", bonous)
    print("Your salary is after adding bonous = ", Net_salary)

else:
    print("No Bonous", salary)