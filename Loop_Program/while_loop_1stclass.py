# # First program
# i = 1

# while i <= 5:
#     print("Hello World")
#     i = i+1

# # Second program

# start_value = int(input("Enter starting value\t"))
# end_value = int(input("Enter ending value\t"))

# i = start_value

# while i <=end_value:
#     print(i)
#     i = i+1

# # 3rd program

# start_value = int(input("Enter starting value\t"))
# end_value = int(input("Enter ending value\t"))

# i = start_value
# while i>=end_value:
#     print("Hello world", i)
#     i = i-1

# 4th program

# start_value = int(input("Enter starting value\t"))
# end_value = int(input("Enter ending value\t"))

# i = start_value
# while i >=end_value:
#     print(i, end="-")
#     i = i-1

# # 5th Program

# start_value = int(input("Enter starting value\t"))
# end_value = int(input("Enter ending value\t"))

# i = start_value
# while i >=end_value:
#     if(i==end_value):
#         print(i, end="")
#     else:
#         print(i, end="-")
#     i-=1

# # 5th Program

# start_value = int(input("Enter starting value\t"))
# end_value = int(input("Enter ending value\t"))

# a = start_value
# while a <=end_value:
#     if(a==end_value):
#         print(a, end="")
#     else:
#         print(a, end="-")
#     a+=1

# Table of any number using while loop
num = int(input("Enter a number for table\t"))

i = 1
while i<=10:
    print(num*i)
    i = i+1

# Table of any number using For loop
num = int(input("Enter a number for table\t"))
for value in range(1,11):
    print(num*value)