# 3. If the marks obtained a student in five different subject are input through the keyboard find out of the aggregate marks and percentage marks obtained by the student Assume that maximum marks in the subject is 100.

mark1 = int(input("Enter the student marks obtained of Hindi subject = "))
marks2 = int(input("Enter the student marks obtained of English Subject = "))
marks3 = int(input("Enter the studend marks obtained of Math Subject = "))
marks4 = int(input("Enter the studend marks obtained of Science Subject = "))
marks5 = int(input("Enter the studend marks obtained of SST Subject = "))

total_marks = mark1 + marks2 + marks3 + marks4 + marks5
percentage = total_marks / 5

print("Total Marks of student obtained is = ", total_marks)
print("Percentage of student is = ", percentage)