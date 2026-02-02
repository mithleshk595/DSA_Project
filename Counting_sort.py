def countingSort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] + 1

    arr [:] = []
    for num, freq in enumerate(count):
        arr.extend([num] * freq)


    return arr
unsortedArr = [4, 2, 2, 8, 3, 3, 1, 6, 5, 3, 6]
sorteArr = countingSort(unsortedArr)
print("sorted array is:", sorteArr)























