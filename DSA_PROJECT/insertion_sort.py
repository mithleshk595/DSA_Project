mylist = [64, 34, 24, 12, 22, 11, 90]

n = len(mylist)
for i in range(1, n):
    insert_index = mylist[i]
    current_value = i - 1
    for j in range(i-1, -1, -1):
        mylist[j] > current_value
        mylist[j + 1] = mylist[j]
        insert_index = j
    else:
        break
mylist[insert_index] = current_value
print(mylist)
