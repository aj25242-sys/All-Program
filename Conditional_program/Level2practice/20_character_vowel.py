# 20. Check whether a character is a vowel (using multiple if statements, not nested).

ch = input("Enter a character\t")

if ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
    print("Entered character is vowel")
if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    print("Entered character is vowel")
if ch != "A" and ch != "E" and ch != "I" and ch != "O" and ch != "U" and ch != "a" and ch != "e" and ch != "i" and ch != "o" and ch != "u":
    print("Entered character is not vowel") 