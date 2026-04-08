class solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [nums[0]]

        for i in range(1, n):
            x = result[i-1] + nums[i]
            result.append(x)

        return result 
    
     