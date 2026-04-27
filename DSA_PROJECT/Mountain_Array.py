class solution:
    def peakIndexInMountainArray(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        r = n -2

        ans = n-1



        while l <= r:
            mid = l + (r - l) //2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1

            else:
                r = mid - 1
        return ans
    


