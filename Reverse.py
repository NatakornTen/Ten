x = input()
list = []
for i in x:
    list.append(i)
xR = ""
for i in range(len(x)):
    xR = xR + list[len(x)-i-1]
print(xR)