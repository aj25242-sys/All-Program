# Salary calculator - Basic salary + HRA + DA - Tax.

basic = int(input("Enter your salary : "))
HRA = basic * 20 / 100
print("Your Home Allowance is = \t", HRA)
DA = basic * 15 /100
print("Your Daily ALlownance is = \t ", DA)

gross_salary = (basic + HRA + DA)
print("Your Gross Salary is = \t", gross_salary)

tax = basic * 9 / 100
print("Your Tax on Gross Gross_salary = \t", tax)

net_salary = gross_salary - tax

print("Your Net salary is after deducation and addition = \t", net_salary)