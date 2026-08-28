
# 1. Even or Odd CheckerQuestion: Write a program that asks the user for an integer and prints whether the number is Even or Odd.

# num = int(input("Enter a number\t"))

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# Question: Take an integer input from the user and print its multiplication table from 1 to 10 using a for loop.Hint: Use range(1, 11).

# num = int(input("Enter a number for multiplication\t"))

# for value in range(1,11):
#     print(num,"x",value,"=",value*num)


#Question: Use a loop to print numbers from 10 down to 1, followed by the message "Liftoff!".
# Hint: You can use either a while loop with a decrementor or a for loop with a negative step in range().
# for i in range(10,0,-1):
#     print(i)
# print("liftoff")

#4. The Classic FizzBuzzQuestion: Write a program that iterates through numbers from 1 to 50.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz".
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".
# Hint: Put the combined condition (% 3 == 0 and % 5 == 0) at the very top of your if-elif chain.

# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# 5. List Filtering and SummationQuestion: Given a list of numbers, calculate the sum of all positive even numbers only.pythonnumbers = [12, -4, 7, 0, 8, -11, 3, 6]
#Hint: Check if num > 0 AND num % 2 == 0 inside the loop. 

# number = [12, -4, 7, 0, 8, -11, 3, 6]
# total_sum = 0
# for num in number:
#     if num > 0 and num % 2 == 0:
#      total_sum+=num
#      print("Positive number of sum:", total_sum)
# print("Positive number of sum:", total_sum)

#6. Vowel CounterQuestion: Ask the user to input a string. Count how many vowels (a, e, i, o, u) are in that string using a loop and an if statement.Hint: Convert the string to lowercase first using .lower().

# text = input("Ente a string\t").lower()
# vowel_count = 0
# vowel = "a,e,i,o,u"

# for char in text:
#    if char in vowel:
#       vowel_count+=1
# print("Total Vowels = ", vowel_count)


# 7. Password Validator (while loop focus)Question: Create a program that keeps asking the user to type a password using a while loop. 
# The loop should only terminate when they type the correct master password (e.g., "python123"). 
# Limit the user to a maximum of 3 attempts. 
# If they fail 3 times, print "Locked out".Hint: 
# Maintain an attempts counter variable that increments by 1 on each wrong guess.

correct_password = "Amit@123"
attempt = 0

while attempt < 3 :
   guess = input("Enter password = ")
   if guess == correct_password:
      print("Access Granted!")
      break
   else:
      attempt += 1
      print(f"Incorrect. Attempt remaining:{3-attempt}")
else:
   print("Locked out! Too many attempts")