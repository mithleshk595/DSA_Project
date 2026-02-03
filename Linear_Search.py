def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
        return -1

arr = [4, 2, 7, 1, 9, 3]
targetVal = 9
result = linearSearch(arr, targetVal)

if result != -1:
    print(f"Value", targetVal, "found at index", result)
else:
    print(f"Value", targetVal, "not found in the array")
    