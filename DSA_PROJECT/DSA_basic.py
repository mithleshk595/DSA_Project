nums = [10, 20, 30, 40, 50]

target = int(input("Enter number to search: "))

found = False

for num in nums:
    if num == target:
        found = True
        break

if found:
    print("Number found!")
else:
    print("Number not found!")
