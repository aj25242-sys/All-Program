# Student grade calucator take marks of 5 subject , find percentage & grade.

sub1 = float(input('Enter marks of subject 1 : '))
sub2 = float(input('Enter marks of subject 2 : '))
sub3 = float(input('Enter marks of subject 3 : '))
sub4 = float(input('Enter marks of subject 4 : '))
sub5 = float(input('Enter marks of subject 5 : '))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

print("Total marks of Subject : ", total)
print("Total percentage of subject : ", percentage)

if percentage >= 90:
    print("Grade A :")
elif percentage >=75:
    print("Grade B : ")
elif percentage >=60:
    print("Grade C : ")
else:
    print("Grade D")