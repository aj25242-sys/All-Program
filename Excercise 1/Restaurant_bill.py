# Restaurant bill - Menu items + Tax + tip.

# menu1 = int(input("Enter menu items \t"))
# tax = menu * 18 / 100
# bill = menu + tax
# print("Your bill is after adding tax \t", bill)
# tip = bill + 200
# print("Your Final bill of this Restaurant is = \t", tip)

item1 = float(input("Enter price of Item 1: "))
item2 = float(input("Enter price of Item 2: "))
item3 = float(input("Enter price of Item 3: "))

tax_rate = float(input("Enter your tax rate = \t"))
tip_rate = float(input("Enter your tip rate = \t"))

food_total = item1 + item2 + item3
tax = (food_total * tax_rate) / 100
print("Tax on items = \t", tax)
tip = (food_total * tip_rate) / 100
print("Tip on items = \t", tip)
final_bill = food_total + tax + tip

print("Your final bill is = \t", final_bill)