myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixArray = myArray.copy()
radixArray = [[], [], [], [], [], [], [], [], [], []]
MaxVal = max(myArray)
exp = 1
while MaxVal // exp > 0:

    while len(myArray) > 0:
        val = myArray.pop(0)
        adixIndex = (val // exp) % 10
        radixArray[adixIndex].append(val)
    
    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop(0)
            myArray.append(val)

        exp *= 10
print("Sorted array:", myArray)




