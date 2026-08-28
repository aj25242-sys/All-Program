# Calculate simple interest.

p = int(input("Enter Principal Amount : "))
r = float(input("Enter Interset Rate : "))
t = float(input("Enter time of Amount Paid : "))

simple_interest = p * r * t / 100
final_amount = p + simple_interest

print("Total amount after interset = ", final_amount)