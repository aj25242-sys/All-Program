#16. Check discount: purchase >= 1000 → 10%

purchase = float(input("Enter Purchase Amount : "))

if purchase >= 1000:
    discount = purchase*10/100
    final_amount = purchase - discount
    print("Discount 10%")
    print("Discount on Purchase item :", discount)
    print("Final Amount is : ", final_amount)
else:
    print("No Discount")
    print("Final Amount :", purchase)
