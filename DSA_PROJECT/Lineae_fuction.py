# def linear_search(nums, targrt):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#         return -1
    
# nums = []

# for i in range(5):
#     num = int(input("Enter Number:"))
#     nums.append(nums)


# target = int(input("Enter Number to search:"))
# result = linear_search(nums, target)

# if result != -1:
#     print("Number Found at index:", result)

# else:
#     print("Number Not Found:")



def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i   # index return karega
    return -1         # agar nahi mila to -1


# ---- Main Program ----
nums = []

for i in range(5):
    num = int(input("Enter number: "))
    nums.append(num)

target = int(input("Enter number to search: "))

result = linear_search(nums, target)

if result != -1:
    print("Number Found at index:", result)
else:
    print("Number Not Found")



