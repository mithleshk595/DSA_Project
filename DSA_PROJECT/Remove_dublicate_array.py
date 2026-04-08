class solution:
    def removeDublicate(self, nums: list[int]) -> int:
        n = len(nums)

        start = 0
        for i in range(1, n):

            # Unique element
            if nums[i] != nums[start]:
                start += 1
                nums[start] = nums[i]

        return start + 1
    