# def binary_search(nums, target):
#     left = 0
#     right = len(nums) - 1

#     while left <= right:
#         mid = (left + right) // 2
    
#     if nums[mid] == target:
#         return mid
    
#     elif nums[mid] < target:
#         left = mid + 1
    
#     else:
#         right = mid -1

#     return -1

# nums = []

# for i in range(5):
#     num = int(input("Enter Number: "))
#     nums.append(num)

# nums.sort() # Importan: list must be sorted

# target = int(input("Enter number to search: "))

# result = binary_search(nums, target)

# if result != -1:
#     print("Number Found at index: ", result)

# else:
#     print("number not found")



def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ---- Main Program ----
nums = []

for i in range(5):
    num = int(input("Enter number: "))
    nums.append(num)

nums.sort()  # Important: List must be sorted

target = int(input("Enter number to search: "))

result = binary_search(nums, target)

if result != -1:
    print("Number Found at index:", result)
else:
    print("Number Not Found")