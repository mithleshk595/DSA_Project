class solution:
    def removeDublicate(self, nums: list[int]) -> int:
        n = len(nums)

        if n<=2:
            return n
        
        start = 0
        for i in range(1, n):

            #Unique Element
            if nums[i] != nums[start-1]:
                start += 1
                nums[start] = nums[i]

        return start + 1
    