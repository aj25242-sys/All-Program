# gender = input("Enter M for Male and F for Female ").lower()

# if gender == "m" or gender == "f":
#     age = int(input("Enter your age "))
#     exp = int(input("Do you have many year of experience? "))
#     salary = int(input("Enter your salary "))
#     if gender == "m":
#         if age > 18:
#             if exp < 2 :
#                 bonus = salary*7/100
#                 print("Your bonous is ", bonus)
#                 print("Net salary after adding bonus ", salary+bonus)
#             elif exp >= 2 and exp < 5 :
#                 bonus = salary*18/100
#                 print("Your bonous is ", bonus)
#                 print("Net salary after adding bonus ", salary+bonus)
#             elif exp >= 5 and exp <= 30:
#                 bonus = salary*30/100
#                 print("Your bonous is ", bonus)
#                 print("Net salary after adding bonus ", salary+bonus)
#             else:
#                 print("You are retired")
#         else:
#              print("No bonus")
#     else:
#         if age > 18:
#             if exp < 2 :
#                 bonus = salary*7/100
#                 print("Your bonous is ", bonus)
#                 print("Net salary after adding bonus ", salary+bonus)
#             elif exp >= 2 and exp < 5 :
#                 bonus = salary*18/100
#                 print("Your bonous is ", bonus)
#                 print("Net salary after adding bonus ", salary+bonus)
#             elif exp >= 5 and exp <= 30:
#                 bonus = salary*30/100
#                 print("Your bonous is ", bonus)
#                 print("Net salary after adding bonus ", salary+bonus)
#             else:
#                 print("You are retired")
        
        
        
#         else:
#             print("No Bonou")
            

        
            
   
# else:
#     print("Invalid Input")


balance = 10000
correct_pin = 1234

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    print("PIN is correct")

    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    else:
        if choice == 2:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= balance:
                balance = balance - amount
                print("Please collect your cash")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance")

        else:
            if choice == 3:
                amount = int(input("Enter deposit amount: "))
                balance = balance + amount
                print("Amount deposited successfully")
                print("Total balance:", balance)

            else:
                print("Invalid choice")

else:
    print("Incorrect PIN")
