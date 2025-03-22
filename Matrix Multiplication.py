print("Matrix Multiplication")
row1 = int(input("Enter number of rows of first Matrix: "))
column1 = int(input("Enter number of columns of first Matrix: "))
row2 = int(input("Enter number of rows of second Matrix: "))
column2 = int(input("Enter number of columns of second Matrix: "))
#Check ว่า 2 เมทริกซ์นี้สามารถนำมาคูณกันได้ไหม
if column1 == row2:
    A = []
    B = []
    print("Enter the first matrix")
    for i in range(row1):
        ra = input()
        rA = []
        for x in ra.split():
            rA.append(int(x))
        if len(rA) != column1:
            print("Invalid input")
            break
        A.append(rA)
    print("Enter the second matrix")
    for i in range(row2):
        rb = input()
        rB = []
        for x in rb.split():
            rB.append(int(x))
        if len(rB) != column2:
            print("Invalid input")
            break
        B.append(rB)
    C = []
    for i in range(column2):
        cb = []
        for j in range(row2):
            cb.append(B[j][i])
        C.append(cb)
    P = []
    for i in range(row1):
        PR = []
        for j in range(column2):
            p = 0
            for k in range(column1):
                p = p + (A[i][k]*C[j][k])
            PR.append(p)
        P.append(PR)
    print("Result: ")
    for i in range(len(P)):
        rp = ""
        for j in range(len(P[i])):
            if j == 0:
                rp = rp + str(P[i][j])
            else:
                rp = rp + " " + str(P[i][j])
        print(rp)
else:
    print("Invalid input")