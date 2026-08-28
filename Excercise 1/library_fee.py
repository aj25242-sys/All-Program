# Library late fee - Days * fine per day.

library = int(input("Enter your library fee : "))
late = int(input("Enter days coming late in library : "))
days = late * 100
final_fee = library + days

print("Your final fees including late fees = ", final_fee)
