class solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []

        for i in candies:
            if (i + extraCandies) >= max(candies):
                result.append(True)
            else:
                result.append(False)

            return result
        