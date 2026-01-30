my_array = [7, 9, 12, 4, 11]
minval = my_array[0]

for i in my_array: 
    if i < minval:
        minval = i
print("Lowest value", minval)