nums = []

# 5 Number input lena 
for i in range(5):
    num = int(input("Enter number:"))
    nums.append(num)

# Search Number input
target = int(input("Enter Number to search:"))

# linear search
for i in range(len(nums)):
    if nums[i] == target:
        print("Number Found at index:", i)
        break

else:
    print("Number not Found")


# nums = [] 

# # 5 number input lena
# for i in range(5):
#     num = int(input("Enter number:"))
#     nums.append(num)

# # Search number input 
# target = int(input("Enter Number tO search:"))

# # linear Search 
# for i in range(len(nums)):
#     if nums[i] == target:
#         print("Number found at index:", i)
#         break
# else:
#     print("Number Not Found")






