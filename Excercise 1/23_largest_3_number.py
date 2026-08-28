# 23.Take three numbers and find the largest number.

first = int(input("Enter First Number\t"))
second = int(input("Enter Second Number\t"))
third = int(input("Enter Third Number\t"))

if first > second :
    print("First number is largest number or 3 number", first)
elif second > third:
    print("Second Number is largest number of 3 numbers", second)
else:
    print("Third Number is largest number of 3 numbers", third)