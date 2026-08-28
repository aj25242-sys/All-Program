# Age                         Message
# 0 to 5                   You are child
# 6 to 12                  You are Kid
# 13 to 19                 You are Teenager
# 20 to 35                 You are Younger
# 36 to 59                 You are Adult
# 60 to 80                 You are Old
# 81 to 100                You are very old
# age > 0 and < 100        Invaild Age



age = int(input("Enter your age \t"))
        # Programme creating using if and elif

if age < 0 or age > 100:
    print("Invalid Age")
elif age >= 1 and age <= 5:
     print("Child")
elif age > 5 and age <=12:
    print("You are Kid")
elif age > 12 and age <=19:
    print("You are Teenager")
elif age > 19 and age <=35:
    print("You are younger")
elif age > 35 and age <=59:
    print("You are Adult")
elif age > 59 and age <=80:
    print("You are old")
elif age > 80 and age <= 100:
    print("You are very old")



        # Programme creating using if and else
# if age < 0 or age > 100:
#     print("Invalid Age")
# else:
#     if age >= 1 and age <= 5:
#         print("Child")
#     else:
#         if age > 5 and age <=12:
#             print("You are Kid")
#         else:
#             if age > 12 and age <=19:
#                 print("You are Teenager")
#             else:
#                 if age > 19 and age <=35:
#                     print("You are younger")
#                 else:
#                     if age > 35 and age <=59:
#                         print("You are Adult")
#                     else:
#                         if age > 59 and age <=80:
#                             print("You are old")
#                         else:
#                             if age > 80 and age <= 100:
#                                 print("You are very old")




          
        
    
