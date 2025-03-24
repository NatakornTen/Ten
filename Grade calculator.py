print("Enter course ID, credit and grade; or X to terminate")
totalCredit = 0
totalGrade = 0
while(True):
    data = input()
    if(data == "X"):
        break
    Data = data.split()
    credit = int(Data[1])
    if Data[2] == "A":
        grade = 4
    elif Data[2] == "B+":
        grade = 3.5
    elif Data[2] == "B":
        grade = 3
    elif Data[2] == "C+":
        grade = 2.5
    elif Data[2] == "C":
        grade = 2
    elif Data[2] == "D+":
        grade = 1.5
    elif Data[2] == "D":
        grade = 1
    else:
        grade = 0
    totalCredit = totalCredit + credit
    totalGrade = totalGrade + (grade*credit)
GPA = totalGrade/totalCredit
print("GPA = " + str(GPA))