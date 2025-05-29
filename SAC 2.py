#Enter the valid total number of students in a single class
student=int(input("Enter the total number of students in the class"))
period=int(input("Enter total number of periods of the class held in a week(between 1 and 5)"))

#Check if the number of periods is between 1 and 5
if period>5:
    print("Invalid, please enter the number between 1 and 5")

#input first student name
student1=input("Enter name for student 1: ")
p10=input("Enter attendance for Alice (P/A) for period 1: ")
p11=input("Enter attendance for Alice (P/A) for period 2: ")
p12=input("Enter attendance for Alice (P/A) for period 3: ")
p13=input("Enter attendance for Alice (P/A) for period 4: ")
p14=input("Enter attendance for Alice (P/A) for period 5: ")
full1=float(p10 + p11 + p12 + p13 + p14)

#input second student name
student2=input("Enter name for student 2: ")
pA=input("Enter attendance for Alice (P/A) for period 1: ")
pB=input("Enter attendance for Alice (P/A) for period 2: ")
pC=input("Enter attendance for Alice (P/A) for period 3: ")
pD=input("Enter attendance for Alice (P/A) for period 4: ")
pE=input("Enter attendance for Alice (P/A) for period 5: ")
full2=float(pA+pB+pC+pD+pE)

#input third student name
student3=int(input("Enter name for student 3: "))
p21=input("Enter attendance for Alice (P/A) for period 1: ")
p22=input("Enter attendance for Alice (P/A) for period 2: ")
p23=input("Enter attendance for Alice (P/A) for period 3: ")
p24=input("Enter attendance for Alice (P/A) for period 4: ")
p25=input("Enter attendance for Alice (P/A) for period 5: ")
full3=float(p21 + p22 + p23 + p24 + p25)

#Print the student's attendance record
print(student1, "receives" ,full1)
print(student2, "receives" ,full2)
print(student3, "receives" ,full3)

if student1 or student2 or student3 >3:
    print("Your attendance is not perfect")
    
