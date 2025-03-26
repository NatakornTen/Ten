print("Enter your string")
x = input()
listOfAlphabets = []
for i in x:
    listOfAlphabets.append(i)

if len(listOfAlphabets)%2 == 0:
    while(True):
        if len(listOfAlphabets) == 0:
            print("Yes")
            break
        if listOfAlphabets[0] != listOfAlphabets[-1]:
            print("No")
            break
        else:
            listOfAlphabets.pop(0)
            listOfAlphabets.pop(-1)
else:
    while(True):
        if len(listOfAlphabets) == 1:
            print("Yes")
            break
        if listOfAlphabets[0] != listOfAlphabets[-1]:
            print("No")
            break
        else:
            listOfAlphabets.pop(0)
            listOfAlphabets.pop(-1)