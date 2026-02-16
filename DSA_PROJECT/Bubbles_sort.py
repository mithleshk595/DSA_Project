mylist = [7, 3, 9, 12, 11, 12]

n = len(mylist)
for i in range(n-1):
    for j in range(n-1-1):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            swapped = True
            if not swapped:
                break
print(mylist)
 
