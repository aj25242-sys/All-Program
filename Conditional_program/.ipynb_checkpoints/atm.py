
# cardtype = input("Enter card between Debit or Credit ").lower()
# balance = 30000

# if cardtype == "debit" or cardtype == "credit":
#     cardNumber = input("Enter card Number ")
#     if cardNumber == "1234":
#         cardName = input("Enter the name on card ").lower()
#         if cardName == "amit":
#             amount = int(input("Enter amount you want to withdreaw "))
#             if amount <= balance:
#                 balance = balance - amount
#                 print("Please collect your cash")
#                 print("Remaining balance:", balance)
#             else:
#                 print("infuccient balance ")
#         else:
#             print("Invalid Card name")


        
#     else:
#         print("Invalid card number")
# else:
#     print("Invalid card")


# balance = 10000
# Correct_Pin = 1234

# pin = int(input("Enter your PIN  "))

# if pin == Correct_Pin:
#     print("PIN is correct ")

#     print("1. Check Balance ")
#     print("2. Withdraw Money ")
#     print("3. Deposit Money ")

#     choice = int(input("Enter your choice  "))
#     if choice == 1:
#         print("Your amount is ", balance)
#     else:
#         if choice == 2:
#             amount = int(input("Enter amount you want to withdraw  "))

#         if amount <= balance:
#             balance = balance - amount 
#             print("Pleae collect your cash ")
#             print("Remaining Balance: ", balance)
#         else:
#             print("Infuccient Balance")

#         else:
#          amount = int(input("Enter amount you want to deposit "))
#         balance = amount+balance
#         print("Amount deposit Successfully")
#         print("Total amount : ", balance)
#     else:
#         print("Invalid choice")

balance = 10000
correct_pin = 1234

# PIN के लिए 3 Attempts
attempt = 1

while attempt <= 3:

    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        print("\nLogin Successful!")

        # ATM Menu
        while True:
            print("\n----- ATM MENU -----")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Your Balance is:", balance)

            else:
                if choice == 2:
                    amount = int(input("Enter withdrawal amount: "))

                    if amount <= balance:
                        balance = balance - amount
                        print("Please collect your cash")
                        print("Remaining Balance:", balance)
                    else:
                        print("Insufficient Balance")

                else:
                    if choice == 3:
                        amount = int(input("Enter deposit amount: "))

                        if amount > 0:
                            balance = balance + amount
                            print("Amount deposited successfully")
                            print("Total Balance:", balance)
                        else:
                            print("Invalid amount")

                    else:
                        if choice == 4:
                            print("Thank you for using ATM!")
                            break

                        else:
                            print("Invalid Choice")

        break

    else:
        print("Incorrect PIN")
        print("Attempts remaining:", 3 - attempt)
        attempt = attempt + 1

if attempt > 3:
    print("\nYour card is blocked!")
    print("Please contact your bank.")