# Shopping cart total Take multiple itmes (qty * price), calculate bill + GST.

item = int(input("Please enter Items : "))
qty = int(input("Please enter quntity of items : "))

# Calculate gross total
gross_total = item * qty
print("Gross Total of pruchasing items : ", gross_total)

# Calculate GST
bill = gross_total*18/100
print("GST on purchase Item : ", bill)

# Adding GST and calculate final bill
final_bill = bill + gross_total
print("Final Price of Purchasing Item is = ", final_bill)