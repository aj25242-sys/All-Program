# 19. Check whether a character is an alphabet.

ch = input("Enter a character\t").lower()

if ch >= "A".lower() and ch <= "Z".lower():
    print("Character is a alphabet")
else:
    print("Character is not a alphabet")
print(ch)