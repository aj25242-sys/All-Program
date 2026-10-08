# 22. Check uppercase, lowercase, digit, or special symbol

# ch = input("Enter a character = ")

# if ch.isupper():
#     print("Uppercase")
# elif ch.islower():
#     print("Lowercase")
# elif ch.isdigit():
#     print("Digit")
# else:
#     print("Special Symbol") 

ch = input("Enter a character : ")

if ch.isalpha():
    if ch.isupper():
        print("Uppercase")
    else:
        print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")