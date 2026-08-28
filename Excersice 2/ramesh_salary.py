# 1. Ramesh basic salary is input through the keyboard. His dearner allowance is 40% of basic salary and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary HINT gross salary = basic salary + HRA + DA

basic = int(input("Enter ramesh basic salry : "))

DA = basic * 40/100
HRA = basic * 20/100

gross_salary = basic + DA + HRA 
print("Ramesh daily allownance is = ", DA)
print("Ramesh Rent allowance is = ", HRA)
print("Ramesh basic salary is after adding all benefits = ", gross_salary)