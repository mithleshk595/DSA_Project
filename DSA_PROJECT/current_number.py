class solution:
    def  smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for i in nums:
            c = 0
            for j in nums:
                if j < 1:
                    c += 1
            result.append(c)
        return result
    