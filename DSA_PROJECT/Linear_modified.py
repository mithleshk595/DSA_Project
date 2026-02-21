# def linear_search_all(nums, target):
#     indexes = []

#     for i in range(len(nums)):
#         if nums[i] == target:
#             indexes.append[i]

#     return indexes

# nums = []

# for i in range(5):
#     num = int(input("Enter Number: "))
#     nums.append(num)

# target = int(input("Enter Number to Search: "))

# result = linear_search_all(nums, target)

# if len(result) > 0:
#     print("Enter Found at index(es):", result)

# else:
#     print("Number Not found")


def linear_search_all(nums, target):
    indexes = []

    for i in range(len(nums)):
        if nums[i] == target:
            indexes.append(i)

    return indexes


nums = []

for i in range(5):
    num = int(input("Enter number: "))
    nums.append(num)

target = int(input("Enter number to search: "))

result = linear_search_all(nums, target)

if len(result) > 0:
    print("Number Found at index(es):", result)
else:
    print("Number Not Found")
