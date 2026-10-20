student_name =str(input("enter student name: "));
print("Student name:", student_name)
subject1 =int(input("enter subject_1 :"));
print("Subject 1 marks:", subject1)
subject2 =int(input("enter subject_2 :"));
print("Subject 2 marks:", subject2)
subject3 =int(input("enter subject_3 :"));
print("Subject 3 marks:", subject3)
total = subject1 + subject2 + subject3
print("Total marks:", total)
average = total / 3
print("Average marks:", average)
percentage = (total / 300) * 100
print("Percentage:", percentage, "%")