# Discount calculator original price - (discount % x price).

price = float(input("Enter Product Price : "))
discount = price * 10/100
final_price = price - discount
print("Final Price of Product is : ", final_price)