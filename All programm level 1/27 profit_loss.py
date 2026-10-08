# 27. Determine Profit or Loss

cost_price = int(input("Enter cost price of item : "))
selling_price = int(input("Enter selling price of item : "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit : ", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss : ", loss)
else:
    print("No profit No loss")