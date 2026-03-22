list1 = [1, 2, 3]

list2 = list1 # deep copy


list1[0] = 100
list2[1] = 200

print(list1)
print(list2)
