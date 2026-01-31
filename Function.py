class solution:
    def smallerNumbersThanCurrent(self, nums): 
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            






