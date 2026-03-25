class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        curr_sum = 0
        
        for i in nums:
            curr_sum+=1
            if curr_sum<ans:
                ans = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        
        return ans
