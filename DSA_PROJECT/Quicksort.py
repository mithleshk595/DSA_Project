def partition(array, low, high):
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = low - 1
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i +1]
    return i + 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

mylist = [64, 34, 22, 11, 90, 5]
n = len(mylist)
quicksort(mylist, 0, n+-1)
print(mylist)



