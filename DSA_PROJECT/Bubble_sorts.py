 #Bubble sort
def sortArray(nums):
    n = len(nums)



    for i  in range(n):
        isSwap = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                #swap
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                isswap = True
            if not isSwap:
                break
        return nums

print(sortArray([1, 3, 6, 5, 2, 4]))

