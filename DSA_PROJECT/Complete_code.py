def first_occurrence(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def last_occurrence(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# ---- Main Program ----
nums = []

for i in range(6):
    num = int(input("Enter number: "))
    nums.append(num)

nums.sort()

target = int(input("Enter number to search: "))

first = first_occurrence(nums, target)
last = last_occurrence(nums, target)

if first == -1:
    print("Total Occurrences: 0")
else:
    total = last - first + 1
    print("Total Occurrences:", total)
    