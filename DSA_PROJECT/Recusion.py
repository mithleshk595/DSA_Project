# def binary_search_recursive(nums, target, left, right):

#     if left < right:
#         return -1
    
#     mid = (left + right) // 2

#     if nums[mid] == target:
#         return mid
#     elif nums[mid] < target:
#         return binary_search_recursive(nums, target, mid + 1, right)
    
#     else:
#         return binary_search_recursive(nums, target, left, right, mid -1)
    

# nums = []

# for i in range(5):
#     num = int(input("Enter Number: "))
#     nums.append(num)

# nums.sort()

# target = int(input("Enter Number to search: "))

# result = binary_search_recursive(nums, target, 0, len(nums-1))

# if result != 1:
#     print("Number Found at index: ")

# else:
#     print("Number Not Found")


def binary_search_recursive(nums, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


# ---- Main Program ----
nums = []

for i in range(5):
    num = int(input("Enter number: "))
    nums.append(num)

nums.sort()

target = int(input("Enter number to search: "))

result = binary_search_recursive(nums, target, 0, len(nums)-1)

if result != -1:
    print("Number Found at index:", result)
else:
    print("Number Not Found")   