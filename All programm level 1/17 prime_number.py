# 17. Check whether a number is prime or not

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2,num):
        if i % num == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime Number")