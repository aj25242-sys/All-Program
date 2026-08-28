# 11. A cashier has currency note of 10, 50 and 100. If the amount to be withdrawn is input throght the keyboad in hundred, find the total number of currency notes of each denomination.

amount = int(input("Enter the amount = "))

# calculate number of notes
hundred = amount // 100
amount = amount % 100

fifty = amount // 50
amount = amount % 50

ten = amount // 10

print("100 rupees notes =  ", hundred)
print("50 rupee notes = ", fifty)
print("10 rupee notes = ", ten)

