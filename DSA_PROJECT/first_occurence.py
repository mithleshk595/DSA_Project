def first_occurence(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid
            right = mid -1 # left side search continue
        
        elif nums[mid] < target:
            left = mid + 1
        
        else:
            right = mid -1

        return result
    
# --- Main program ---

nums = []

for i in range(6):
    num = int(input("Enter Number: "))
    nums.append(num)

nums.sort()

target = int(input("Enter number to search: "))

index = first_occurence(nums, target)

if index != -1:
    print("First occurence at index: ", index)
else:
    print("Number Not Found!")
    