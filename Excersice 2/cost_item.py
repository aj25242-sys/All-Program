# 12. If the total selling price of 15 items and the total profit earned on them is input through the keyboad. Write a program to find the cost of one item.

selling_price = int(input("Enter selling Price of 15 items = "))
profit = int(input("Enter profit of 15 items = "))

cost_price = selling_price - profit

one_item_cost = cost_price / 15

print("Cost of one item is = ", one_item_cost)
