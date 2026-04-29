class solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        start = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                temp = nums[i]
                nums[i] = nums[start]
                nums[start] = temp
                start += 1

        return nums