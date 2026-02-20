nums = []

for i in range(5):
    num = int(input("Enter number: "))
    nums.append(num)

print("List:", nums)
print("Max:", max(nums))


# nums = [10, 20, 30, 40, 50]

# target = int(input("Enter number to search: "))

# found = False

# for num in nums:
#     if num == target:
#         found = True
#         break

# if found:
#     print("Number found!")
# else:
#     print("Number not found!")

# nums = [10, 25, 30, 45, 50]

# target = int(input("Enter number to search: "))

# found = False

# for num in nums:
#     if num == target:
#         found = True
#         break

# if found:
#     print("Number Found")
# else:
#     print("Number Not Found")

# nums = []

# # 5 numbers input lena
# for i in range(5):
#     num = int(input("Enter number: "))
#     nums.append(num)

# # Search number input
# target = int(input("Enter number to search: "))

# # Linear Search
# for i in range(len(nums)):
#     if nums[i] == target:
#         print("Number found at index:", i)
#         break
# else:
#     print("Number Not Found")


nums = []
for i in range(10):
    num = int(input("Enter number: "))
    nums.append(num)


# Search number input
target = int(input("Enter number to search: "))

# Linear search 
for i in range(len(nums)):
    if nums[i] == target:
        print("Number found at index: ", i)
        break
else:
    print("number not found")