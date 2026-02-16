mylist = [64, 34, 25, 12, 22, 11, 90]
n = len(mylist)

for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if mylist[j] < mylist[min_idx]:
            min_idx = j
            mylist[i], mylist[min_idx] = mylist[min_idx], mylist[i]
print(mylist)
